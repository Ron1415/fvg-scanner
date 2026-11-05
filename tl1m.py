"""Trendline-break 1-minute FVG model: a bar-by-bar port of the TradingView indicator
FVG_1m_Trendlines.pine (long and short), with a 6-month backtest, a failure analysis and trade charts.

  python tl1m.py --backtest 125     # replay 125 sessions of 1-minute bars -> backtest_tl1m/, review_tl1m.md
  python tl1m.py --review           # rebuild review_tl1m.md
  python tl1m.py --charts 24        # charts of sample losers and winners -> site/tl_charts/

The short side runs the long engine on a mirrored chart (prices multiplied by -1, highs and lows
swapped), so both sides follow exactly the same rules. Settings: config_tl1m.py.
"""
from __future__ import annotations

import argparse
import datetime as dt
import gzip
import html
import json
import logging
import os
from concurrent.futures import ProcessPoolExecutor
from pathlib import Path
from zoneinfo import ZoneInfo

import numpy as np
import pandas as pd

import config_tl1m as K

NY = ZoneInfo("America/New_York")
ROOT = Path(__file__).resolve().parent
OUT = ROOT / "backtest_tl1m"
log = logging.getLogger("tl1m")


def hm(m) -> str:
    return "" if m is None else f"{int(m) // 60:02d}:{int(m) % 60:02d}"


def settings(over: dict | None = None) -> dict:
    over = over or {}
    return {"rules": {r: over.get(r, on) for r, on in K.RULES.items()}, "stop": over.get("stop", "fvg"),
            "target_r": over.get("target_r", K.TARGET_R)}


def daily_trend(closes: list[float]) -> int:
    """+1 up (prior close above a rising 20-day average), -1 down, 0 neither."""
    if len(closes) < 26:
        return 0
    sma = lambda end: sum(closes[end - 20:end]) / 20
    a, b, c = closes[-1], sma(len(closes)), sma(len(closes) - 5)
    return 1 if a > b > c else -1 if a < b < c else 0


# ----------------------------------------------------------------- one side, one day
def run_side(O, H, L, C, V, M, d: int, cfg: dict, or_hit: list[bool], trend_ok: bool) -> tuple[list, list]:
    """The long engine on (possibly mirrored) arrays. d = 1 long, -1 short (only used to un-mirror
    prices in the output). or_hit[i]: the opening range was broken in this direction by bar i.
    Returns (trades, blocked setups)."""
    n, k = len(C), K.PIVOT_K
    rules, tgt_r = cfg["rules"], cfg["target_r"]
    rng = np.array(H) - np.array(L)
    atr = np.array([rng[max(0, i - 13):i + 1].mean() for i in range(n)])
    is_ph = [k <= p < n - k and all(H[j] < H[p] for j in range(p - k, p + k + 1) if j != p) for p in range(n)]
    real = lambda x: None if x is None else d * x
    # trendline state
    piv, active, la, lpx, lsl, lt, last_break, break_bar, above = [], False, 0, 0.0, 0.0, 0, -1, -10 ** 9, 0
    gaps = []        # dicts: top, bot, mid, born, live, hl, ext
    # trade state
    st, pend, last_mid, last_why, blocked_mid = 0, None, None, "", None
    setup, tr = None, None
    trades, blocked = [], []
    for i in range(n):
        # ---- 1. trendline: break first, then a new swing point rebuilds the line
        broke = False
        if active:
            lv = lpx + lsl * (i - la)
            above = above + 1 if C[i] > lv + K.BREAK_MARGIN_ATR * atr[i] else 0
            if above >= K.CONFIRM_CLOSES:
                broke, above, active = True, 0, False
                last_break = break_bar = i
                piv = []
                brk_line = (la, lpx, lsl, lt, C[i] - lv)
        p = i - k
        if not broke and p >= 0 and is_ph[p] and p > last_break:
            piv = (piv + [p])[-K.MAX_PIVOTS:]
            tol, best = K.TOL_ATR * atr[i], None
            for x in range(len(piv) - 1):
                a, ha = piv[x], H[piv[x]]
                for y in range(x + 1, len(piv)):
                    b, hb = piv[y], H[piv[y]]
                    if hb < ha and b - a >= K.MIN_GAP_BARS and i - a < 400:
                        sl = (hb - ha) / (b - a)
                        if all(C[j] <= ha + sl * (j - a) + tol for j in range(a, i + 1)):
                            tc = sum(1 for z in piv[x:] if abs(H[z] - (ha + sl * (z - a))) <= tol)
                            if tc >= K.MIN_TOUCH and (best is None or (tc, b, -a) > best[0]):
                                best = ((tc, b, -a), a, ha, sl, tc)
            if best:
                _, la, lpx, lsl, lt = best
                active, above = True, 0
        # ---- 2. FVGs
        if i >= 2 and L[i] > H[i - 2] and L[i] - H[i - 2] >= K.MIN_GAP_PCT / 100 * abs(C[i]):
            born = i - 1
            gaps.append({"top": L[i], "bot": H[i - 2], "mid": (L[i] + H[i - 2]) / 2, "born": born, "live": True,
                         "hl": born >= break_bar and born - break_bar <= K.HL_AFTER, "ext": L[i]})
        if broke:
            for g in gaps:
                if g["live"] and not g["hl"] and g["born"] >= i - K.HL_BEFORE:
                    g["hl"] = True
        for g in gaps:
            if g["live"] and i - g["born"] > K.MAX_EXT_BARS:
                g["live"] = False
            elif g["live"] and i > g["born"] + 1:
                g["ext"] = min(g["ext"], L[i])
                if L[i] <= g["bot"]:
                    g["live"] = False
        # ---- 3. trade
        if st == 2:
            px, why = None, None
            t = tr
            if M[i] >= K.EOD_EXIT:
                px, why = C[i], "close"
            elif cfg["stop"] == "close2" and t["stp"] is None:
                t["below"] = t["below"] + 1 if C[i] < t["leg_low"] else 0
                if t["below"] >= 2:
                    px, why = C[i], "lower low confirmed"
            if px is None and t["stp"] is not None and L[i] <= t["stp"]:
                px, why = min(t["stp"], O[i]), ("breakeven" if t["stp"] >= t["ent"] else "stop")
            if px is None:
                t["mfe"] = max(t["mfe"], (H[i] - t["ent"]) / t["risk"])
                t["mae"] = max(t["mae"], (t["ent"] - L[i]) / t["risk"])
                if not t["half"] and H[i] >= t["tgt"]:
                    t["half"], t["banked"] = True, K.PARTIAL * tgt_r
                if cfg["stop"] == "close2":
                    t["above"] = t["above"] + 1 if C[i] > t["rec_hi"] else 0
                    if t["above"] >= 2 or t["half"]:
                        t["stp"] = t["ent"] if t["stp"] is None else max(t["stp"], t["ent"])
                elif C[i] > t["rec_hi"] or t["half"]:
                    t["stp"] = max(t["stp"], t["ent"])
            else:
                t["mae"] = max(t["mae"], (t["ent"] - min(L[i], px)) / t["risk"])
                if why.startswith(("stop", "breakeven", "lower")) and t["half"]:
                    why = "4R then " + why
                elif why == "close" and t["half"]:
                    why = "4R then close"
                rest = 1 - (K.PARTIAL if t["half"] else 0)
                t.update(r_gross=(px - t["ent"]) / t["risk"] * rest + t["banked"], exit=why, exit_i=i,
                         exit_px=px, market_share=rest)
                trades.append(t)
                st, tr = 0, None
        elif st == 1 and pend is not None:
            if L[i] <= pend["mid"] - K.TICK and M[i] < K.LAST_FILL:
                ent = min(pend["mid"], O[i])
                stp0 = pend["stop"]
                risk = ent - stp0
                tr = {**pend["info"], "ent": ent, "risk": risk, "stp": None if cfg["stop"] == "close2" else stp0,
                      "stop_ref": stp0, "tgt": ent + tgt_r * risk, "rec_hi": pend["hi"], "half": False, "banked": 0.0,
                      "fill_i": i, "mfe": 0.0, "mae": 0.0, "below": 0, "above": 0, "leg_low": setup["leg_low"]}
                st = 2
                if cfg["stop"] == "close2":
                    tr["below"] = 1 if C[i] < tr["leg_low"] else 0
                elif L[i] <= stp0:                    # the fill bar itself can only stop out
                    tr.update(r_gross=-1.0, exit="stop on the fill bar", exit_i=i, exit_px=stp0, market_share=1.0, mae=1.0)
                    trades.append(tr)
                    st, tr = 0, None
            pend = None
        elif st == 1 and last_mid is not None and last_mid != blocked_mid and L[i] <= last_mid - K.TICK and last_why:
            blocked_mid = last_mid
            blocked.append({"i": i, "why": last_why})
        if broke and st != 2:
            ll = min(range(la, i + 1), key=lambda j: (L[j], -j))
            setup = {"brk": i, "la": la, "lpx": lpx, "lsl": lsl, "touches": lt, "break_dist": brk_line[4],
                     "leg_low": L[ll], "leg_low_i": ll}
            st, last_mid, last_why = 1, None, ""
        if st == 1:
            if L[i] < setup["leg_low"] or i - setup["brk"] > K.MAX_WAIT_BARS or M[i] >= K.LAST_FILL:
                st, setup = 0, None
                continue
            hi = max(H[setup["leg_low_i"]:i + 1])
            leg = hi - setup["leg_low"]
            best = None
            if leg > 0:
                for g in gaps:
                    if g["hl"] and g["live"] and g["born"] >= setup["brk"] - K.HL_BEFORE and i > g["born"] + 1 and g["ext"] > g["mid"]:
                        r = (hi - g["mid"]) / leg
                        sc = (0 if K.FIB_ZONE[0] <= r <= K.FIB_ZONE[1] else 1000) + abs(r - 0.559)
                        if best is None or sc < best[0]:
                            best = (sc, g, r)
            last_mid, last_why = (best[1]["mid"] if best else None), ""
            if best:
                _, g, r = best
                line_next = setup["lpx"] + setup["lsl"] * (i + 1 - setup["la"])
                pad = K.TL_PAD_ATR * atr[i]
                f = {"vwap": g["mid"] > V[i], "orb": or_hit[i], "daily": trend_ok, "fib": K.FIB_ZONE[0] <= r <= K.FIB_ZONE[1],
                     "trendline": g["bot"] - pad <= line_next <= g["top"] + pad}
                timing = K.FIRST_FILL - 1 <= M[i] < K.LAST_FILL - 1
                fails = [x for x, on in rules.items() if on and not f[x]] + ([] if timing else ["time"])
                last_why = ", ".join(fails)
                if not fails:
                    base = setup["leg_low"] if cfg["stop"] in ("swing", "close2") else g["bot"]
                    buf = 0.0 if cfg["stop"] == "close2" else K.STOP_ATR * atr[i]
                    stop = min(base - buf, g["mid"] - K.MIN_RISK_PCT / 100 * abs(g["mid"]))
                    pend = {"mid": g["mid"], "stop": stop, "hi": hi, "info": {
                        "brk_i": setup["brk"], "la": setup["la"], "lpx": real(setup["lpx"]), "lsl": d * setup["lsl"],
                        "tl_touches": setup["touches"], "tl_slope_atr": -setup["lsl"] / atr[i] if atr[i] else None,
                        "tl_len": setup["brk"] - setup["la"], "break_dist_atr": setup["break_dist"] / atr[i] if atr[i] else None,
                        "break_body_atr": abs(C[setup["brk"]] - O[setup["brk"]]) / atr[i] if atr[i] else None,
                        "leg_low_i": setup["leg_low_i"], "leg_low_px": real(setup["leg_low"]), "recent_high_px": real(hi),
                        "leg_atr": leg / atr[i] if atr[i] else None, "gap_born": g["born"], "gap_top": real(g["top"]),
                        "gap_bot": real(g["bot"]), "gap_atr": (g["top"] - g["bot"]) / atr[i] if atr[i] else None,
                        "gap_pct": (g["top"] - g["bot"]) / abs(g["mid"]) * 100, "fib_ret": r,
                        "vwap_dist_atr": (g["mid"] - V[i]) / atr[i] if atr[i] else None, "plan_i": i,
                        **{f"f_{x}": v for x, v in f.items()}}}
    if st == 2 and tr is not None:                 # still open at the end of the data
        rest = 1 - (K.PARTIAL if tr["half"] else 0)
        tr.update(r_gross=(C[-1] - tr["ent"]) / tr["risk"] * rest + tr["banked"], exit="end of data", exit_i=n - 1,
                  exit_px=C[-1], market_share=rest)
        trades.append(tr)
    return trades, blocked


def run_day(day: list, cfg: dict, trend: int) -> list[dict]:
    """Both sides for one session of 1-minute regular-hours bars."""
    if len(day) < 40:
        return []
    O = [b.o for b in day]; H = [b.h for b in day]; L = [b.l for b in day]; C = [b.c for b in day]
    M = [b.min for b in day]
    pv = np.cumsum([(b.h + b.l + b.c) / 3 * max(b.v, 1) for b in day]); vv = np.cumsum([max(b.v, 1) for b in day])
    V = list(pv / vv)
    orh = max((b.h for b in day if b.min < K.OR_END), default=None)
    orl = min((b.l for b in day if b.min < K.OR_END), default=None)
    up = dn = False
    or_up, or_dn = [], []
    for b in day:
        if orh is not None and b.min >= K.OR_END:
            up, dn = up or b.c > orh, dn or b.c < orl
        or_up.append(up); or_dn.append(dn)
    out = []
    for d, arrs, orh_hit, tok in ((1, (O, H, L, C, V), or_up, trend == 1),
                                  (-1, ([-x for x in O], [-x for x in L], [-x for x in H], [-x for x in C], [-x for x in V]), or_dn, trend == -1)):
        trades, blocked = run_side(*arrs, M, d, cfg, orh_hit, tok)
        for t in trades:
            ent_real, cost_std = d * t["ent"], 2 * K.COST_PCT_PER_SIDE / 100 * abs(t["ent"]) / t["risk"]
            t.update(side="LONG" if d == 1 else "SHORT", date=day[0].date, fill_time=hm(M[t["fill_i"]]),
                     exit_time=hm(M[t["exit_i"]]), entry=ent_real, stop=d * t["stop_ref"], target=d * t["tgt"],
                     risk_pct=t["risk"] / abs(t["ent"]) * 100, r_std=t["r_gross"] - cost_std,
                     r_real=t["r_gross"] - t["market_share"] * K.SLIP_PER_SHARE / t["risk"],
                     bars_break_to_fill=t["fill_i"] - t["brk_i"], bars_in_trade=t["exit_i"] - t["fill_i"],
                     fill_min=M[t["fill_i"]])
            for x in ("ent", "risk", "stp", "tgt", "rec_hi", "banked", "below", "above", "leg_low", "stop_ref", "exit_px"):
                t.pop(x, None)
            out.append({"kind": "trade", **t})
        for b in blocked:
            out.append({"kind": "blocked", "side": "LONG" if d == 1 else "SHORT", "date": day[0].date,
                        "time": hm(M[b["i"]]), "why": b["why"]})
    return out


def run_ticker(ticker: str, bars: list, closes: list, dates: set, runs: dict) -> list[dict]:
    by = {}
    for b in bars:
        if 570 <= b.min < 960:
            by.setdefault(b.date, []).append(b)
    out = []
    for dte in sorted(by):
        if dates and dte not in dates:
            continue
        trend = daily_trend([c for x, c in closes if x < dte])
        for name, over in runs.items():
            for r in run_day(by[dte], settings(over), trend):
                out.append({"run": name, "ticker": ticker, **r})
    return out


# ----------------------------------------------------------------- backtest
def _fetch(t, start, end):
    import data as D
    if D.alpaca_enabled():
        return D.alpaca_bars(t, start, end, "1Min", rth_only=True)
    return D.yahoo_intraday([t], "7d", "1m").get(t, [])


def _worker(args):
    t, start, end, closes, dates = args
    try:
        bars = _fetch(t, start, end)
    except Exception as e:
        log.warning("%s: no 1-minute bars (%s)", t, e)
        return []
    return run_ticker(t, bars, closes, dates, K.RUNS)


def backtest(days: int) -> None:
    import config as C0
    import data as D
    import scanner as S
    u = S.universe()
    tickers = [t for t in u["tickers"] if "=F" not in t and (t not in C0.ETF_CANDIDATES or t in K.ALLOW_ETFS)]
    spy = D.yahoo_daily(["SPY"], "2y")["SPY"]
    today = dt.datetime.now(NY).strftime("%Y-%m-%d")
    sessions = [x for x in spy.index if x < today][-days:]
    start = dt.date.fromisoformat(sessions[0]) - dt.timedelta(days=7)
    end = dt.date.fromisoformat(sessions[-1])
    daily = D.yahoo_daily(tickers, "2y")
    closes = {t: list(zip(df.index, df["Close"].astype(float))) for t, df in daily.items()}
    os.environ["ALPACA_SLEEP"] = str(0.35 * (os.cpu_count() or 2))
    rows = []
    with ProcessPoolExecutor(max_workers=os.cpu_count() or 2) as ex:
        for r in ex.map(_worker, [(t, start, end, closes.get(t, []), set(sessions)) for t in tickers], chunksize=1):
            rows += r
    OUT.mkdir(exist_ok=True)
    df = pd.DataFrame(rows)
    with gzip.open(OUT / "trades.csv.gz", "wt") as f:
        df.to_csv(f, index=False)
    (OUT / "meta.json").write_text(json.dumps({
        "run_at": dt.datetime.now(NY).strftime("%Y-%m-%d %H:%M ET"), "sessions": [sessions[0], sessions[-1]],
        "fetch": [str(start), str(end)], "symbols": len(tickers), "rows": len(df),
        "source": "Alpaca 1-minute (SIP)" if D.alpaca_enabled() else "Yahoo 1-minute (about 7 days only)"}, indent=1))
    review()


# ----------------------------------------------------------------- review
def stats(d: pd.DataFrame, col: str = "r_real") -> dict:
    if not len(d):
        return {"n": 0}
    r = d[col].to_numpy(float)
    a, b = d.loc[d["date"] < K.SPLIT_DATE, col], d.loc[d["date"] >= K.SPLIT_DATE, col]
    loss = -r[r < 0].sum()
    eq = np.cumsum(r)
    return {"n": len(r), "win": (r > 0).mean(), "avg": r.mean(), "std": d["r_std"].mean(), "pf": r[r > 0].sum() / loss if loss else None,
            "total": r.sum(), "dd": float((eq - np.maximum.accumulate(np.maximum(eq, 0))).min()),
            "d1": a.mean() if len(a) else None, "n1": len(a), "d2": b.mean() if len(b) else None, "n2": len(b)}


def _f(v, pct=False):
    if v is None or (isinstance(v, float) and np.isnan(v)):
        return ""
    return f"{v * 100:.1f}%" if pct else f"{v:.2f}"


def table(rows) -> str:
    h = ("| Group | Trades | Win rate | Avg R (realistic cost) | Avg R (standard cost) | Profit factor | Total R | Max DD R | "
         "Design avg R (to Aug) | Confirm avg R (Sep on) |\n|---|---|---|---|---|---|---|---|---|---|\n")
    for name, s in rows:
        if not s.get("n"):
            h += f"| {name} | 0 | | | | | | | | |\n"
            continue
        h += (f"| {name} | {s['n']} | {_f(s['win'], True)} | {_f(s['avg'])} | {_f(s['std'])} | {_f(s['pf'])} | {_f(s['total'])} | "
              f"{_f(s['dd'])} | {_f(s['d1'])} (n={s['n1']}) | {_f(s['d2'])} (n={s['n2']}) |\n")
    return h


FEATURES = [  # (column, label) for the failure analysis
    ("risk_pct", "Stop distance, % of price"), ("gap_atr", "FVG height, x ATR"), ("fib_ret", "Retracement of the FVG midpoint"),
    ("tl_touches", "Trendline touches"), ("tl_slope_atr", "Trendline steepness, ATR per bar"), ("tl_len", "Trendline length, bars"),
    ("break_body_atr", "Break candle body, x ATR"), ("break_dist_atr", "Break close beyond the line, x ATR"),
    ("leg_atr", "Size of the new move, x ATR"), ("bars_break_to_fill", "Bars from break to fill"),
    ("vwap_dist_atr", "Entry distance from VWAP, x ATR"), ("fill_min", "Fill time (minutes after midnight)"),
]


def review() -> str:
    p = OUT / "trades.csv.gz"
    meta = json.loads((OUT / "meta.json").read_text()) if (OUT / "meta.json").exists() else {}
    df = pd.read_csv(p) if p.exists() and p.stat().st_size > 30 else pd.DataFrame(columns=["run", "kind", "date"])
    tr = df[df["kind"] == "trade"].sort_values(["date", "fill_time"]) if len(df) else df
    bl = df[df["kind"] == "blocked"] if len(df) else df
    md = [f"# Trendline-break 1-minute model review: {dt.datetime.now(NY).strftime('%Y-%m-%d %H:%M ET')}\n\n",
          f"Data: {meta.get('source', '?')}, {meta.get('sessions', ['?', '?'])[0]} to {meta.get('sessions', ['?', '?'])[-1]}, "
          f"{meta.get('symbols', '?')} symbols (stocks plus {', '.join(K.ALLOW_ETFS)}). Same rules as FVG_1m_Trendlines.pine. "
          f"Rules on: {', '.join(r for r, on in K.RULES.items() if on)}. Realistic cost = limit orders free, ${K.SLIP_PER_SHARE}/share "
          f"on market exits; standard cost = {K.COST_PCT_PER_SIDE}% per side.\n\n"]
    md.append("## 1. Runs (each changes one thing from the core)\n\n")
    rows = []
    for r in K.RUNS:
        x = tr[tr["run"] == r]
        rows += [(f"{r} · both sides", stats(x)), (f"{r} · long", stats(x[x["side"] == "LONG"])), (f"{r} · short", stats(x[x["side"] == "SHORT"]))]
    md.append(table(rows))
    core = tr[tr["run"] == "core"].copy()
    if len(core):
        md.append("\n## 2. How the core trades end\n\n| Exit | Trades | Avg R |\n|---|---|---|\n")
        for k_, g in core.groupby("exit"):
            md.append(f"| {k_} | {len(g)} | {g['r_real'].mean():.2f} |\n")
        lo = core[core["r_real"] < -0.2]            # real losses (breakevens excluded)
        cats = {"Stopped on the fill bar": lo["exit"].str.contains("fill bar"),
                "Stopped within 5 bars of the fill": (lo["bars_in_trade"] <= 5) & ~lo["exit"].str.contains("fill bar"),
                "Was +1R or better first, then stopped": lo["mfe"] >= 1,
                "Never better than +0.5R": lo["mfe"] < 0.5}
        md.append(f"\n## 3. The losing trades ({len(lo)} of {len(core)}; breakevens excluded)\n\n| Pattern | Losers | Share |\n|---|---|---|\n")
        for name, m in cats.items():
            md.append(f"| {name} | {int(m.sum())} | {m.mean() * 100:.0f}% |\n")
        md.append(f"\nAverage best point reached by losers: {lo['mfe'].mean():.2f}R. "
                  f"Winners: {(core['r_real'] > 0).sum()}, of which {core['exit'].str.startswith('4R').sum()} reached 4R.\n")
        md.append("\n## 4. What separates winners from losers (core, realistic cost; quartiles of each measure)\n\n"
                  "| Measure | Quartile range | Trades | Win rate | Avg R | Design avg R | Confirm avg R |\n|---|---|---|---|---|---|---|\n")
        for col, lab in FEATURES:
            v = pd.to_numeric(core[col], errors="coerce")
            if v.notna().sum() < 20:
                continue
            try:
                q = pd.qcut(v, 4, duplicates="drop")
            except ValueError:
                continue
            for b, g in core.groupby(q, observed=True):
                s = stats(g)
                md.append(f"| {lab} | {b} | {s['n']} | {_f(s['win'], True)} | {_f(s['avg'])} | {_f(s['d1'])} | {_f(s['d2'])} |\n")
        # fixed candidate rules for stricter entries; judged on design AND confirm periods
        cands = {
            "Trendline with 3+ touches": core["tl_touches"] >= 3,
            "FVG at least 0.5 ATR tall": core["gap_atr"] >= 0.5,
            "Midpoint at 50-61.8% exactly": core["fib_ret"].between(0.5, 0.618),
            "Break candle body at least 1 ATR": core["break_body_atr"] >= 1,
            "Break close at least 0.25 ATR beyond the line": core["break_dist_atr"] >= 0.25,
            "Fill within 10 bars of the break": core["bars_break_to_fill"] <= 10,
            "Stop at least 0.30% of price": core["risk_pct"] >= 0.30,
            "New move at least 3 ATR": core["leg_atr"] >= 3,
            "Entry within 2 ATR of VWAP": core["vwap_dist_atr"].abs() <= 2,
            "Fill before 13:00": core["fill_min"] < 780,
            "Trendline not steeper than 0.5 ATR per bar": core["tl_slope_atr"].abs() <= 0.5,
        }
        base = stats(core)
        md.append(f"\n## 5. Candidate stricter entries (core baseline: design {_f(base['d1'])}R, confirm {_f(base['d2'])}R)\n\n"
                  "A rule is worth adopting only if it beats the baseline in BOTH periods with a reasonable number of trades.\n\n"
                  "| Rule | Trades kept | Win rate | Avg R | Design avg R | Confirm avg R | Beats baseline in both? |\n|---|---|---|---|---|---|---|\n")
        for name, m in cands.items():
            s = stats(core[m.fillna(False)])
            ok = s.get("n", 0) >= 40 and (s.get("d1") or -9) > (base["d1"] or 0) and (s.get("d2") or -9) > (base["d2"] or 0)
            md.append(f"| {name} | {s.get('n', 0)} | {_f(s.get('win'), True)} | {_f(s.get('avg'))} | {_f(s.get('d1'))} | {_f(s.get('d2'))} | {'yes' if ok else 'no'} |\n")
        md.append("\n## 6. By symbol (core, top and bottom 8 by total R)\n\n| Symbol | Trades | Avg R | Total R |\n|---|---|---|---|\n")
        top = core.groupby("ticker")["r_real"].agg(["count", "mean", "sum"]).sort_values("sum", ascending=False)
        for t, r in pd.concat([top.head(8), top.tail(8)]).drop_duplicates().iterrows():
            md.append(f"| {t} | {int(r['count'])} | {r['mean']:.2f} | {r['sum']:.2f} |\n")
    cb = bl[bl["run"] == "core"] if len(bl) else bl
    if len(cb):
        md.append("\n## 7. Core setups reached but not taken, by blocking rule\n\n| Rule | Setups |\n|---|---|\n")
        for rule in ("vwap", "orb", "daily", "fib", "trendline", "time"):
            md.append(f"| {rule} | {int(cb['why'].fillna('').str.contains(rule).sum())} |\n")
    md.append("\nCharts of sample losers and winners: site/tl_charts/ (GitHub Pages: /tl_charts/).\n")
    text = "".join(md)
    (ROOT / "review_tl1m.md").write_text(text)
    return text


# ----------------------------------------------------------------- charts
def charts(n: int = K.CHARTS) -> list[Path]:
    import matplotlib
    matplotlib.use("Agg")
    import matplotlib.pyplot as plt
    from matplotlib.patches import Rectangle
    meta = json.loads((OUT / "meta.json").read_text())
    df = pd.read_csv(OUT / "trades.csv.gz")
    core = df[(df["kind"] == "trade") & (df["run"] == "core")]
    rnd = np.random.default_rng(11)
    lo, wi = core[core["r_real"] < 0], core[core["r_real"] > 0.5]
    pick = pd.concat([lo.iloc[rnd.permutation(len(lo))[:max(1, 2 * n // 3)]], wi.iloc[rnd.permutation(len(wi))[:max(1, n // 3)]]])
    dest = ROOT / "site" / "tl_charts"
    dest.mkdir(parents=True, exist_ok=True)
    s0, s1 = (dt.date.fromisoformat(x) for x in meta["fetch"])
    cache, made, cards = {}, [], []
    for _, t in pick.iterrows():
        if t["ticker"] not in cache:
            cache[t["ticker"]] = _fetch(t["ticker"], s0, s1)
        day = [b for b in cache[t["ticker"]] if b.date == t["date"] and 570 <= b.min < 960]
        if not day:
            continue
        fi, ei = int(t["fill_i"]), int(t["exit_i"])
        a = max(0, int(t["la"]) - 10)
        z = min(len(day), max(fi + 30, min(ei + 10, fi + 120)))
        fig, ax = plt.subplots(figsize=(13, 6.5), dpi=105)
        for i in range(a, z):
            b = day[i]
            col = "#1a9e6a" if b.c >= b.o else "#d64545"
            ax.vlines(i, b.l, b.h, color=col, linewidth=0.8)
            ax.add_patch(Rectangle((i - 0.35, min(b.o, b.c)), 0.7, max(abs(b.c - b.o), 1e-6), color=col))
        pv = np.cumsum([(b.h + b.l + b.c) / 3 * max(b.v, 1) for b in day]); vv = np.cumsum([max(b.v, 1) for b in day])
        ax.plot(range(a, z), (pv / vv)[a:z], color="#7c3aed", linewidth=1, label="VWAP")
        la, lpx, lsl, bi = int(t["la"]), float(t["lpx"]), float(t["lsl"]), int(t["brk_i"])
        side_col = "#2f6fde" if t["side"] == "LONG" else "#e8590c"
        ax.plot([la, bi], [lpx, lpx + lsl * (bi - la)], color=side_col, linewidth=2, label=f"Trendline ({int(t['tl_touches'])} touches)")
        ax.plot([bi, fi], [lpx + lsl * (bi - la), lpx + lsl * (fi - la)], color=side_col, linewidth=1.5, linestyle=":", label="Broken line, extended")
        ax.scatter([bi], [day[bi].c], marker="^" if t["side"] == "LONG" else "v", color=side_col, s=60, zorder=5)
        gb = int(t["gap_born"])
        ax.add_patch(Rectangle((gb, min(t["gap_bot"], t["gap_top"])), fi - gb + 1, abs(t["gap_top"] - t["gap_bot"]),
                               facecolor=side_col, alpha=0.2, edgecolor=side_col, label="Setup FVG"))
        lo_px, hi_px = float(t["leg_low_px"]), float(t["recent_high_px"])
        z50, z618 = hi_px - 0.5 * (hi_px - lo_px), hi_px - 0.618 * (hi_px - lo_px)
        ax.add_patch(Rectangle((int(t["leg_low_i"]), min(z50, z618)), fi - int(t["leg_low_i"]) + 1, abs(z50 - z618),
                               facecolor="#c58a00", alpha=0.15, edgecolor="#c58a00", label="50-61.8% zone"))
        e1 = min(ei, z - 1)
        for y, c, lab in ((t["entry"], side_col, f"Entry {t['entry']:.2f}"), (t["stop"], "#d64545", f"Stop {t['stop']:.2f} ({t['risk_pct']:.2f}%)"),
                          (t["target"], "#1a9e6a", f"4R {t['target']:.2f}")):
            ax.hlines(y, fi, e1, color=c, linewidth=1.4, label=lab)
        ax.scatter([fi], [t["entry"]], color=side_col, s=60, zorder=6)
        if ei < z:
            ax.scatter([ei], [day[ei].c], marker="X", color="black", s=70, zorder=6)
        ys = [b.l for b in day[a:z]] + [b.h for b in day[a:z]] + [t["stop"]]
        if abs(t["target"] - t["entry"]) < 3 * (max(ys) - min(ys)):
            ys.append(t["target"])
        pad = (max(ys) - min(ys)) * 0.05
        ax.set_ylim(min(ys) - pad, max(ys) + pad)
        ax.set_xlim(a - 1, z)
        ticks = list(range(a, z, 15))
        ax.set_xticks(ticks, [hm(day[i].min) for i in ticks])
        ax.set_title(f"{t['ticker']} {t['date']} {t['side']} · fill {t['fill_time']} · {t['exit']} · {t['r_real']:+.2f}R · best {t['mfe']:.1f}R", fontsize=11)
        ax.legend(loc="best", fontsize=7.5, framealpha=0.9)
        ax.grid(alpha=0.15)
        fig.tight_layout()
        name = f"{t['ticker']}_{t['date']}_{t['side']}_{t['fill_time'].replace(':', '')}.png"
        fig.savefig(dest / name)
        plt.close(fig)
        made.append(dest / name)
        facts = (f"touches {int(t['tl_touches'])} · FVG {t['gap_atr']:.2f} ATR · retracement {t['fib_ret'] * 100:.0f}% · "
                 f"break body {t['break_body_atr']:.2f} ATR · {int(t['bars_break_to_fill'])} bars to fill · stop {t['risk_pct']:.2f}% · "
                 f"VWAP distance {t['vwap_dist_atr']:.1f} ATR")
        cards.append(f"<h3>{html.escape(t['ticker'])} {t['date']} {t['side']} · {html.escape(str(t['exit']))} · {t['r_real']:+.2f}R</h3>"
                     f"<p>{facts}</p><img src='{name}' style='max-width:100%'>")
    (dest / "index.html").write_text("<!doctype html><meta charset='utf-8'><meta name='viewport' content='width=device-width'>"
                                     "<title>Trendline-break trade charts</title><body style='font-family:sans-serif;max-width:1500px;margin:auto;padding:16px'>"
                                     "<h1>Trendline-break model: sample losers and winners (core run)</h1>" + "".join(cards))
    return made


def main() -> None:
    logging.basicConfig(level=logging.INFO, format="%(asctime)s %(levelname)s %(message)s")
    ap = argparse.ArgumentParser()
    ap.add_argument("--backtest", type=int, metavar="DAYS")
    ap.add_argument("--review", action="store_true")
    ap.add_argument("--charts", type=int, metavar="N")
    a = ap.parse_args()
    if a.backtest:
        backtest(a.backtest)
    if a.review:
        print(review())
    if a.charts:
        charts(a.charts)


if __name__ == "__main__":
    main()
