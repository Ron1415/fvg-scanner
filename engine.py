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
    pre_v = [v for v in V[:i] if v > 0]
    rvol = V[i] / (sum(pre_v) / len(pre_v)) if pre_v and sum(pre_v) > 0 else 1.0
    return dict(sweep_idx=s, fvg_idx=i, mss_idx=m, swept=swept, extreme=low, swing=sh, mss=mss, fvg_a=fvg_a,
                fvg_b=fvg_b, ce=ce, eq=eq, ote_a=ote_a, ote_mid=ote_mid, ote_b=ote_b, overlap=overlap,
                entry=entry, stop=stop, t1=t1, t2=t2, rr1=(t1 - entry) / risk, rr2=(t2 - entry) / risk,
                status=status, rvol=rvol, atr=atr)


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
        s["fvg_lo"], s["fvg_hi"] = sorted([s["fvg_a"], s["fvg_b"]])
        s["ote_lo"], s["ote_hi"] = sorted([s["ote_a"], s["ote_b"]])
        s["sweep_min"], s["fvg_min"] = rth[s["sweep_idx"]].min, rth[s["fvg_idx"]].min
    return out


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
    pts["time"] = w["time"] if C.OR_END <= now_min <= C.SIM["plan_window_end"] else 0
    far = s["swing"] - s["entry"] if long else s["entry"] - s["swing"]
    dist = price - s["entry"] if long else s["entry"] - price
    prox = 1.0 if dist <= 0 else max(0.0, 1 - dist / far) if far > 0 else 0.0
    pts["prox"] = w["prox"] * prox
    s.update(pts=pts, notes=notes, proximity=prox, dist_pct=abs(price - s["entry"]) / price * 100)
    mx = max(w["sweep_pd"], w["sweep_other"]) + w["mss"] + w["zone"] + w["ote"] + w["rr"] + w["bias"] + w["vol"] + w["time"] + w["prox"]
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
    s["filter_reasons"], s["qualified"] = r, not r
    return r


def setup_key(session: str, ticker: str, s: dict) -> str:
    return f"{session}|{ticker}|{s['side']}|{hhmm(s['sweep_min'])}"   # one record per sweep
