"""FVG setup engine: session levels, liquidity sweep -> market structure shift ->
displacement FVG -> OTE, plus the Setup Score and plan filters.

Ported line for line from the Google Apps Script version so results match.
Shorts reuse the long detector on negated prices.
"""
from __future__ import annotations

import json
from collections import namedtuple
from pathlib import Path

import config as C

ROOT = Path(__file__).resolve().parent
Bar = namedtuple("Bar", "ts date min o h l c v")


# ----------------------------------------------------------------- effective settings
def settings() -> dict:
    """config.py values with tuning.json overrides applied."""
    s = {"weights": dict(C.WEIGHTS), "filters": dict(C.FILTERS), "version": 1}
    p = ROOT / "tuning.json"
    if p.exists():
        t = json.loads(p.read_text() or "{}")
        s["weights"].update(t.get("weights", {}))
        s["filters"].update(t.get("filters", {}))
        s["version"] = t.get("version", 1)
    return s


def is_future(t: str) -> bool:
    return t in C.FUTURES


def asset_type(t: str) -> str:
    return "Future" if is_future(t) else "ETF" if t in C.ETF_CANDIDATES else "Stock"


def mult_of(t: str) -> float:
    return C.FUTURES[t][1] if is_future(t) else 1


def hhmm(m: int) -> str:
    return f"{m // 60:02d}{m % 60:02d}"


def hm(m) -> str:
    return "" if m is None else f"{int(m) // 60:02d}:{int(m) % 60:02d}"


# ----------------------------------------------------------------- levels
def _hi(bars):
    return max(b.h for b in bars) if bars else None


def _lo(bars):
    return min(b.l for b in bars) if bars else None


def is_rth(b) -> bool:
    return C.RTH_OPEN <= b.min < C.RTH_CLOSE


def levels_for(bars: list, today: str, prev: str, fut: bool) -> dict:
    """PDH/PDL = prior 9:30-4:00; PMH/PML = pre-market 4:00-9:30 (futures: overnight since
    the prior 4:00 PM); ORH/ORL = 9:30-10:00 ET."""
    prev_r = [b for b in bars if b.date == prev and is_rth(b)]
    prev_end = prev_r[-1].ts if prev_r else 0
    if fut:
        pre = [b for b in bars if b.ts > prev_end and (b.date < today or b.min < C.RTH_OPEN)
               and not (b.date == today and is_rth(b))]
    else:
        pre = [b for b in bars if b.date == today and C.PRE_START <= b.min < C.RTH_OPEN]
    orng = [b for b in bars if b.date == today and is_rth(b) and b.min < C.OR_END]
    return {"PDH": _hi(prev_r), "PDL": _lo(prev_r), "PMH": _hi(pre), "PML": _lo(pre),
            "ORH": _hi(orng), "ORL": _lo(orng)}


def rth_dates(bars: list) -> list[str]:
    return sorted({b.date for b in bars if is_rth(b)})


def htf_bias(closes: list[float]) -> str:
    n = len(closes)
    if n < 26:
        return "Neutral"
    sma = lambda i: sum(closes[i - 19:i + 1]) / 20
    c, s_now, s_prev = closes[-1], sma(n - 1), sma(n - 6)
    if c > s_now > s_prev:
        return "Bullish"
    if c < s_now < s_prev:
        return "Bearish"
    return "Neutral"


# ----------------------------------------------------------------- detection
def _pivot_highs(H, end, k=2):
    out = []
    for p in range(k, end):
        if p + k >= len(H):
            break
        hp = H[p]
        if all(H[j] < hp for j in range(p - k, p + k + 1) if j != p):
            out.append(p)
    return out


def trendline(H, C_, s, n, atr, piv, tol=None, max_piv=8):
    """Counter-trend line of the leg INTO the sweep (longs: a falling line across lower highs;
    shorts reuse it on negated prices). Ron's "liquidity inflection level" (Nov 4, 2026): price
    respected the line, broke it, and may retest it from the other side.
    A line through two pivot highs a < b (H[a] > H[b], 3+ bars apart) is valid when no close from
    a to the sweep is more than `tol` above it. Most touches wins (pivots within tol), then the most
    recent. Returns None if there is no valid line or it has not been broken by a close yet."""
    tol = 0.1 * atr if tol is None else tol
    cands = [p for p in piv if p < s][-max_piv:]
    best = None
    for ai, a in enumerate(cands):
        for b in cands[ai + 1:]:
            if b - a < 3 or not H[a] > H[b]:
                continue
            slope = (H[b] - H[a]) / (b - a)
            y = lambda j: H[a] + slope * (j - a)
            if any(C_[j] > y(j) + tol for j in range(a, s + 1)):
                continue
            touches = sum(1 for p in cands if p >= a and abs(H[p] - y(p)) <= tol)
            key = (touches, b, a)
            if best is None or key > best[0]:
                best = (key, a, b, slope)
    if best is None:
        return None
    (touches, _, _), a, b, slope = best
    y = lambda j: H[a] + slope * (j - a)
    brk = next((j for j in range(s + 1, n) if C_[j] > y(j)), None)
    if brk is None:
        return None
    # the line "fails" if, after the break, a close lands back below it by more than 0.25 ATR
    failed = any(C_[j] < y(j) - 0.25 * atr for j in range(brk + 1, n))
    return {"tl_a_idx": a, "tl_b_idx": b, "tl_slope": slope, "tl_a_price": H[a], "tl_touches": touches,
            "tl_brk_idx": brk, "tl_failed": failed, "tl_next": y(n)}


def detect_long(H, L, C_, V, liq: dict, extra: dict, ote=C.OTE, stop_buf=C.STOP_ATR_BUFFER):
    n = len(L)
    if n < 6:
        return None
    s = min(range(n), key=lambda i: (L[i], i))
    low = L[s]
    swept = [k for k, v in liq.items() if v is not None and low < v]
    piv = [p for p in _pivot_highs(H, s) if p < s]
    if piv:
        mss = H[piv[-1]]
    elif s >= 2:
        mss = max(H[:s])
    else:
        return None
    m = next((j for j in range(s + 1, n) if C_[j] > mss), None)
    if m is None:
        return None
    best = None
    for i in range(max(s + 1, 1), min(m + 1, n - 1)):
        if i - 1 >= s and H[i - 1] < L[i + 1]:
            size = L[i + 1] - H[i - 1]
            if best is None or size > best[1]:
                best = (i, size)
    if best is None:
        return None
    i = best[0]
    fvg_a, fvg_b = H[i - 1], L[i + 1]
    ce = (fvg_a + fvg_b) / 2
    sh = max(H[s:])
    rng = sh - low
    if rng <= 0:
        return None
    eq = low + 0.5 * rng
    ote_a, ote_mid, ote_b = sh - ote[0] * rng, sh - ote[1] * rng, sh - ote[2] * rng
    ov_lo, ov_hi = max(fvg_a, ote_b), min(fvg_b, ote_a)
    overlap = ov_lo <= ov_hi
    entry = (ov_lo + ov_hi) / 2 if overlap else ce
    last = H[-20:], L[-20:]
    atr = sum(h - l for h, l in zip(*last)) / len(last[0])
    stop = low - stop_buf * atr
    risk = entry - stop
    if risk <= 0:
        return None
    t1 = sh
    beyond = sorted(v for v in extra.values() if v is not None and v > sh)
    t2 = beyond[0] if beyond else max(entry + 2 * risk, t1 + 0.5 * risk)
    touched, invalid = None, False
    for j in range(i + 2, n):
        if touched is None and L[j] <= entry:
            touched = j
        if C_[j] < fvg_a or L[j] <= stop:
            invalid = True
    hit = touched is not None and any(H[j] >= t1 for j in range(touched, n))
    status = "Invalidated" if invalid else "Target hit" if hit else "Entry reached" if touched is not None else "Pending"
    tl = trendline(H, C_, s, n, atr, piv) if atr > 0 else None
    pre_v = [v for v in V[:i] if v > 0]
    rvol = V[i] / (sum(pre_v) / len(pre_v)) if pre_v and sum(pre_v) > 0 else 1.0
    return dict(sweep_idx=s, fvg_idx=i, mss_idx=m, swept=swept, extreme=low, swing=sh, mss=mss, fvg_a=fvg_a,
                fvg_b=fvg_b, ce=ce, eq=eq, ote_a=ote_a, ote_mid=ote_mid, ote_b=ote_b, overlap=overlap,
                entry=entry, stop=stop, t1=t1, t2=t2, rr1=(t1 - entry) / risk, rr2=(t2 - entry) / risk,
                status=status, rvol=rvol, atr=atr, tl=tl)


PRICE_KEYS = ["extreme", "swing", "mss", "fvg_a", "fvg_b", "ce", "eq", "ote_a", "ote_mid", "ote_b",
              "entry", "stop", "t1", "t2"]


def find_setups(rth: list, lv: dict) -> list[dict]:
    """rth: closed regular-session bars of one day (oldest first)."""
    H = [b.h for b in rth]; L = [b.l for b in rth]; Cl = [b.c for b in rth]; V = [b.v for b in rth]
    neg = lambda v: None if v is None else -v
    out = []
    lg = detect_long(H, L, Cl, V, {"PDL": lv["PDL"], "PML": lv["PML"], "ORL": lv["ORL"]},
                     {"ORH": lv["ORH"], "PMH": lv["PMH"], "PDH": lv["PDH"]})
    if lg:
        lg["side"] = "LONG"; out.append(lg)
    sh = detect_long([-x for x in L], [-x for x in H], [-x for x in Cl], V,
                     {"PDH": neg(lv["PDH"]), "PMH": neg(lv["PMH"]), "ORH": neg(lv["ORH"])},
                     {"ORL": neg(lv["ORL"]), "PML": neg(lv["PML"]), "PDL": neg(lv["PDL"])})
    if sh:
        for k in PRICE_KEYS:
            sh[k] = -sh[k]
        sh["side"] = "SHORT"; out.append(sh)
    for s in out:
        _trendline_fields(s, rth)
        s["fvg_lo"], s["fvg_hi"] = sorted([s["fvg_a"], s["fvg_b"]])
        s["ote_lo"], s["ote_hi"] = sorted([s["ote_a"], s["ote_b"]])
        s["sweep_min"], s["fvg_min"] = rth[s["sweep_idx"]].min, rth[s["fvg_idx"]].min
    return out


TL_ZONE_ATR = 0.25   # trendline counts as confluence within 0.25 ATR of the entry zone


def _trendline_fields(s: dict, rth: list) -> None:
    """Adds tl_* fields in real prices and session minutes (shorts were found on negated prices).
    tl_conf: the line has been broken, has not failed, and its projected level at the next bar sits
    inside the entry zone (FVG near edge down to the entry) +/- TL_ZONE_ATR x ATR, i.e. a pullback
    into the FVG would also retest the broken line."""
    tl, sgn = s.pop("tl", None), (1 if s["side"] == "LONG" else -1)
    blank = {"tl_found": False, "tl_conf": False, "tl_touches": 0, "tl_next": None, "tl_a_min": None,
             "tl_a_price": None, "tl_slope_min": None, "tl_dist_atr": None, "tl_failed": None}
    if not tl:
        s.update(blank)
        return
    a, b = tl["tl_a_idx"], tl["tl_b_idx"]
    per_bar = (rth[b].min - rth[a].min) / (b - a) if b > a else 5
    nxt = sgn * tl["tl_next"]
    lo, hi = (min(s["entry"], s["fvg_a"]), s["fvg_b"]) if sgn > 0 else (s["fvg_b"], max(s["entry"], s["fvg_a"]))
    pad = TL_ZONE_ATR * s["atr"]
    s.update(tl_found=True, tl_touches=tl["tl_touches"], tl_next=nxt, tl_a_min=rth[a].min,
             tl_a_price=sgn * tl["tl_a_price"], tl_slope_min=sgn * tl["tl_slope"] / (per_bar or 5),
             tl_failed=tl["tl_failed"], tl_brk_min=rth[tl["tl_brk_idx"]].min,
             tl_dist_atr=sgn * (s["entry"] - nxt) / s["atr"] if s["atr"] else None,
             tl_conf=(not tl["tl_failed"]) and lo - pad <= nxt <= hi + pad)


def tl_at(row: dict, minute) -> float | None:
    """Trendline price at a session minute (None if the setup has no line)."""
    try:
        a_min, a_px, sl = float(row["tl_a_min"]), float(row["tl_a_price"]), float(row["tl_slope_min"])
    except (KeyError, TypeError, ValueError):
        return None
    if any(v != v for v in (a_min, a_px, sl)):   # NaN from CSV
        return None
    return a_px + sl * (float(minute) - a_min)


def apply_live(s: dict, price: float) -> None:
    long = s["side"] == "LONG"
    if (price <= s["stop"]) if long else (price >= s["stop"]):
        s["status"] = "Invalidated"
    elif s["status"] == "Pending" and ((price <= s["entry"]) if long else (price >= s["entry"])):
        s["status"] = "Entry reached"


# ----------------------------------------------------------------- scoring and filters
def score(s: dict, price: float, bias: str, now_min: int, cfg: dict) -> int:
    w, long = cfg["weights"], s["side"] == "LONG"
    pts, notes = {}, []
    pd_key = "PDL" if long else "PDH"
    if pd_key in s["swept"]:
        pts["sweep"] = w["sweep_pd"]; notes.append("Swept " + pd_key)
    elif s["swept"]:
        pts["sweep"] = w["sweep_other"]; notes.append("Swept " + "/".join(s["swept"]))
    else:
        pts["sweep"] = 0; notes.append("No key level swept")
    pts["mss"] = w["mss"]; notes.append("MSS confirmed")
    s["in_zone"] = s["ce"] < s["eq"] if long else s["ce"] > s["eq"]
    pts["zone"] = w["zone"] if s["in_zone"] else 0
    if s["in_zone"]:
        notes.append("FVG in " + ("discount" if long else "premium"))
    pts["ote"] = w["ote"] if s["overlap"] else 0
    if s["overlap"]:
        notes.append("FVG overlaps OTE")
    pts["rr"] = w["rr"] if s["rr1"] >= 2 else w["rr"] / 2 if s["rr1"] >= 1.5 else 0
    notes.append(f"R:R {s['rr1']:.1f} to T1")
    s["bias_aligned"] = (bias == "Bullish" and long) or (bias == "Bearish" and not long)
    if s["bias_aligned"]:
        pts["bias"] = w["bias"]; notes.append("HTF " + bias.lower())
    elif bias == "Neutral":
        pts["bias"] = w["bias_neutral"]; notes.append("HTF neutral")
    else:
        pts["bias"] = 0; notes.append(f"Against HTF ({bias.lower()})")
    pts["vol"] = w["vol"] if s["rvol"] >= 1.5 else 0
    if pts["vol"]:
        notes.append(f"Displacement vol {s['rvol']:.1f}x")
    pts["tl"] = w.get("tl", 0) if s.get("tl_conf") else 0
    if s.get("tl_conf"):
        notes.append(f"Trendline retest confluence ({s['tl_touches']} touches)")
    pts["time"] = w["time"] if C.OR_END <= now_min <= C.SIM["plan_window_end"] else 0
    far = s["swing"] - s["entry"] if long else s["entry"] - s["swing"]
    dist = price - s["entry"] if long else s["entry"] - price
    prox = 1.0 if dist <= 0 else max(0.0, 1 - dist / far) if far > 0 else 0.0
    pts["prox"] = w["prox"] * prox
    s.update(pts=pts, notes=notes, proximity=prox, dist_pct=abs(price - s["entry"]) / price * 100)
    mx = max(w["sweep_pd"], w["sweep_other"]) + w["mss"] + w["zone"] + w["ote"] + w["rr"] + w["bias"] + w["vol"] + w["time"] + w["prox"] + w.get("tl", 0)
    s["score"] = min(100, round(100 * sum(pts.values()) / mx)) if mx > 0 else 0
    return s["score"]


def qualify(s: dict, cfg: dict) -> list[str]:
    f, r = cfg["filters"], []
    if f["require_ote"] and not s["overlap"]:
        r.append("FVG does not overlap OTE")
    if s["rr1"] < f["min_rr_t1"]:
        r.append(f"T1 under {f['min_rr_t1']}R")
    if s["rr2"] < f["min_rr_t2"]:
        r.append(f"T2 under {f['min_rr_t2']}R")
    if s.get("score", 0) < f["min_score"]:
        r.append(f"Score under {f['min_score']}")
    s["base_qualified"] = not r
    s["guards"] = {}
    sr = C.SHORT_RULES
    if s["side"] == "SHORT" and sr["enabled"]:
        risk_pct = abs(s["entry"] - s["stop"]) / s["entry"] * 100 if s["entry"] else 0
        g = {"bias": s.get("bias") == "Bearish" or not sr["require_bearish_bias"],
             "sweep": "PDH" in s["swept"] or len(s["swept"]) >= 2 or not sr["require_strong_sweep"],
             "rr": s["rr2"] >= sr["min_rr_t2"], "risk": risk_pct >= sr["min_risk_pct"],
             "time": s.get("snap_min", 0) >= sr["not_before"] or s.get("session_name", "NY") != "NY",
             "etf": not (sr["no_leveraged_etfs"] and s.get("ticker") in C.LEVERAGED_ETFS)}
        s["guards"] = g
        names = {"bias": "short needs a bearish daily trend", "sweep": "short needs a PDH or 2+ level sweep",
                 "rr": f"short T2 under {sr['min_rr_t2']}R", "risk": f"short risk under {sr['min_risk_pct']}% of price",
                 "time": "short before 10:30", "etf": "no shorts on leveraged ETFs"}
        r += [names[k] for k, ok in g.items() if not ok]
    s["filter_reasons"], s["qualified"] = r, not r
    return r


def setup_key(session: str, ticker: str, s: dict) -> str:
    return f"{session}|{ticker}|{s['side']}|{hhmm(s['sweep_min'])}"   # one record per sweep
