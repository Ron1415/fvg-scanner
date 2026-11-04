"""1-minute FVG model ("super power"): long only, up-trend days only.

  python fvg1m.py --backtest 125     # replay the last 125 trading days on 1-minute bars and write review_1m.md
  python fvg1m.py --review           # rebuild review_1m.md from backtest_1m/trades.csv.gz

Rules are in config_1m.py. The walk is strictly bar by bar: every decision at bar i uses only bars
up to i, and an order planned at the close of bar i can only fill from bar i + 1 on.
Needs Alpaca keys for months of 1-minute history (Yahoo keeps about 7 days).
"""
from __future__ import annotations

import argparse
import bisect
import datetime as dt
import gzip
import json
import logging
import os
from concurrent.futures import ProcessPoolExecutor
from pathlib import Path
from zoneinfo import ZoneInfo

import numpy as np
import pandas as pd

import config_1m as K
from engine import Bar

NY = ZoneInfo("America/New_York")
ROOT = Path(__file__).resolve().parent
log = logging.getLogger("fvg1m")


# ----------------------------------------------------------------- helpers
def daily_up(closes: list[float]) -> bool:
    """Prior close above a 20-day average that is higher than 5 days ago."""
    if len(closes) < 26:
        return False
    sma = lambda end: sum(closes[end - 20:end]) / 20
    return closes[-1] > sma(len(closes)) > sma(len(closes) - 5)


def bars_15m(bars: list) -> list:
    """Aggregates 1-minute bars into 15-minute bars (regular session, aligned to 9:30)."""
    out, cur, key = [], None, None
    for b in bars:
        k = (b.date, (b.min - K.OPEN) // 15)
        if k != key:
            if cur:
                out.append(cur)
            key, cur = k, [b.ts, b.date, K.OPEN + k[1] * 15, b.o, b.h, b.l, b.c, b.v]
        else:
            cur[4], cur[5], cur[6], cur[7] = max(cur[4], b.h), min(cur[5], b.l), b.c, cur[7] + b.v
    if cur:
        out.append(cur)
    return [Bar(*x) for x in out]


def magnets(b15: list, hist: list, fill_ts: int, price: float) -> list[float]:
    """Untouched 15-minute FVGs above `price` (bullish or bearish gaps), as of `fill_ts`.
    A gap counts once its third 15-minute bar has closed, and stays a magnet until a later
    1-minute high reaches its lower edge. Returns the lower edges, nearest first."""
    hts = [b.ts for b in hist]
    hh = np.array([b.h for b in hist]) if hist else np.array([])
    out = []
    for j in range(1, len(b15) - 1):
        done = b15[j + 1].ts + 15 * 60
        if done > fill_ts:
            break
        a, c = b15[j - 1], b15[j + 1]
        if c.l > a.h:
            lo = a.h                      # bullish gap a.h .. c.l
        elif c.h < a.l:
            lo = c.h                      # bearish gap c.h .. a.l
        else:
            continue
        if lo <= price:
            continue
        i0, i1 = bisect.bisect_left(hts, done), bisect.bisect_left(hts, fill_ts)
        if i1 > i0 and hh[i0:i1].max() >= lo:
            continue                      # already touched
        out.append(lo)
    return sorted(out)


def trendline(H, C, piv, l0, atr):
    """Falling line through two confirmed pivot highs before the swing low l0 (lower highs).
    Valid if no close from the first anchor to l0 is more than TL_TOL_ATR above it.
    Most touches wins, then the most recent. Returns (a, slope, touches) or None."""
    tol = K.TL_TOL_ATR * atr
    cands = [p for p in piv if p < l0][-8:]
    best = None
    for x, a in enumerate(cands):
        for b in cands[x + 1:]:
            if b - a < 3 or not H[a] > H[b]:
                continue
            sl = (H[b] - H[a]) / (b - a)
            if any(C[j] > H[a] + sl * (j - a) + tol for j in range(a, l0 + 1)):
                continue
            touches = sum(1 for p in cands if p >= a and abs(H[p] - (H[a] + sl * (p - a))) <= tol)
            key = (touches, b, a)
            if best is None or key > best[0]:
                best = (key, a, sl, touches)
    return None if best is None else best[1:]


# ----------------------------------------------------------------- trade management
def manage(t: dict, bars: list, mode: str) -> tuple[float, str, int]:
    """Bars after the fill bar. mode: plan (half at 4R, rest to the 15-minute magnet or the close),
    full4r (everything at 4R), eod (half at 4R, rest held to the close). Breakeven once a 1-minute
    close is above the recent high. When a bar touches both the stop and a target, the stop wins.
    Returns (R before costs, exit reason, exit minute)."""
    e, risk, t1 = t["entry"], t["entry"] - t["stop"], t["t1"]
    runner = t["magnet"] if mode == "plan" else None
    part = 1.0 if mode == "full4r" else K.PARTIAL_AT_TARGET
    stop, done, r, hit = t["stop"], 0.0, 0.0, False
    R = lambda px: (px - e) / risk
    for b in bars:
        if b.min >= K.EOD_EXIT:
            return r + (1 - done) * R(b.c), ("4R then close" if hit else "Close"), b.min
        if b.l <= stop:
            return r + (1 - done) * R(stop), ("4R then breakeven" if hit else "Breakeven" if stop >= e else "Stop"), b.min
        if not hit and b.h >= t1:
            hit, r, done = True, part * R(t1), part
            if done >= 1:
                return r, "4R", b.min
        if hit and runner and b.h >= runner:
            return r + (1 - done) * R(runner), "4R then magnet", b.min
        if b.c > t["recent_high"] or hit:
            stop = max(stop, e)        # breakeven from the next bar
    last = bars[-1] if bars else None
    return (r + (1 - done) * R(last.c) if last else 0.0), "End of data", (last.min if last else None)


# ----------------------------------------------------------------- the walk
def run_day(day: list, hist: list, b15: list, up: bool, rules: dict) -> list[dict]:
    """day: today's 1-minute regular-session bars; hist: 1-minute bars of the prior MAGNET_DAYS
    sessions plus today (for the magnet check); b15: 15-minute bars of the same span."""
    n = len(day)
    if n < 30:
        return []
    H = [b.h for b in day]; L = [b.l for b in day]; C = [b.c for b in day]; O = [b.o for b in day]
    k = K.PIVOT_K
    # session VWAP and 14-bar average range, each using bars up to and including i
    pv = np.cumsum([(b.h + b.l + b.c) / 3 * max(b.v, 1) for b in day]); vv = np.cumsum([max(b.v, 1) for b in day])
    vwap = pv / vv
    rng = np.array([b.h - b.l for b in day])
    atr = np.array([rng[max(0, i - 13):i + 1].mean() for i in range(n)])
    is_ph = [k <= p < n - k and all(H[j] < H[p] for j in range(p - k, p + k + 1) if j != p) for p in range(n)]
    orh = max((b.h for b in day if b.min < K.OR_END), default=None)
    trades, piv, used = [], [], set()
    setup = order = pos = None
    or_broken = False
    for i in range(n):
        b = day[i]
        if i - k >= 0 and is_ph[i - k]:
            piv.append(i - k)                         # pivot high confirmed at the close of bar i
        if orh is not None and b.min >= K.OR_END and C[i] > orh:
            or_broken = True
        # 1. a working order fills on this bar?
        if order is not None:
            if L[i] <= order["entry"] and b.min < K.ENTRY_END:
                fill = min(order["entry"], O[i])
                if fill > order["stop"]:
                    t = {**order, "entry": fill, "fill_min": b.min, "fill_i": i}
                    t["t1"] = fill + K.TARGET_R * (fill - t["stop"])
                    mg = [m for m in magnets(b15, hist, b.ts, fill) if m > t["t1"]]
                    allm = magnets(b15, hist, b.ts, fill)
                    t["magnet"] = mg[0] if mg else None
                    t["magnet_before_t1"] = bool(allm and allm[0] < t["t1"])
                    if L[i] <= t["stop"]:             # the fill bar itself can only stop out
                        res = {m: (-1.0, "Stop", b.min) for m in ("plan", "full4r", "eod")}
                    else:
                        res = {m: manage(t, day[i + 1:], m) for m in ("plan", "full4r", "eod")}
                    cost = 2 * K.COST_PCT_PER_SIDE / 100 * fill / (fill - t["stop"])
                    t.update(r_plan=res["plan"][0] - cost, exit=res["plan"][1], exit_min=res["plan"][2],
                             r_full4r=res["full4r"][0] - cost, r_eod=res["eod"][0] - cost, cost_r=cost)
                    trades.append(t)
                    pos = t
                order = setup = None
            else:
                order = None
        if pos is not None:
            if b.min >= (pos["exit_min"] or 0):
                pos = None
            continue
        if len(trades) >= K.MAX_TRADES_PER_DAY or b.min >= K.ENTRY_END:
            setup = None
            continue
        # 2. break of structure: first close above the last lower high
        if setup is None and len(piv) >= 2:
            p0, p1 = piv[-2], piv[-1]
            if p1 not in used and H[p0] > H[p1] and C[i] > H[p1] and all(C[j] <= H[p1] for j in range(p1 + 1, i)):
                used.add(p1)
                l0 = min(range(p1, i + 1), key=lambda j: (L[j], -j))
                setup = {"bos_i": i, "bos_min": b.min, "l0": l0, "low": L[l0], "broken_high": H[p1],
                         "tl": trendline(H, C, piv, l0, atr[i])}
        if setup is None:
            continue
        # 3. keep the setup alive?
        if L[i] < setup["low"] or i - setup["bos_i"] > K.MAX_WAIT_BARS:
            setup = None
            continue
        # 4. plan an order for the next bar: the FVG midpoint
        l0, hi = setup["l0"], max(H[setup["l0"]:i + 1])
        leg = hi - setup["low"]
        if leg <= 0:
            continue
        best = None
        for j in range(l0 + 1, i):
            if L[j + 1] > H[j - 1] and L[j + 1] - H[j - 1] >= K.MIN_GAP_PCT / 100 * C[i]:
                ce = (L[j + 1] + H[j - 1]) / 2
                if j + 2 <= i and min(L[j + 2:i + 1]) <= ce:
                    continue                          # midpoint already traded: not a fresh gap
                ret = (hi - ce) / leg
                key = (not (K.FIB_ZONE[0] <= ret <= K.FIB_ZONE[1]), abs(ret - 0.559))
                if best is None or key < best[0]:
                    best = (key, j, ce, ret)
        if best is None:
            continue
        _, j, ce, ret = best
        gap_lo, gap_hi = H[j - 1], L[j + 1]
        stop = min(gap_lo - K.STOP_ATR * atr[i], ce * (1 - K.MIN_RISK_PCT / 100))
        tl, line = setup["tl"], None
        if tl:
            a, sl, _t = tl
            broke = any(C[x] > H[a] + sl * (x - a) for x in range(setup["l0"] + 1, i + 1))
            line = H[a] + sl * (i + 1 - a) if broke else None
        pad = K.TL_PAD_ATR * atr[i]
        flags = {"daily_up": up, "vwap": ce > vwap[i], "orb": or_broken,
                 "fib": K.FIB_ZONE[0] <= ret <= K.FIB_ZONE[1],
                 "trendline": line is not None and gap_lo - pad <= line <= gap_hi + pad}
        if all(flags[r] for r, on in rules.items() if on) and day[min(i + 1, n - 1)].min >= K.ENTRY_START:
            order = {"date": b.date, "bos_time": hm(setup["bos_min"]), "entry": ce, "stop": stop,
                     "gap_lo": gap_lo, "gap_hi": gap_hi, "swing_low": setup["low"], "recent_high": hi, "fib_ret": ret,
                     "tl_touches": tl[2] if tl else 0, "vwap": float(vwap[i]), **{f"f_{r}": v for r, v in flags.items()}}
    for t in trades:
        t["risk_pct"] = (t["entry"] - t["stop"]) / t["entry"] * 100
        t["fill_time"], t["exit_time"] = hm(t.pop("fill_min")), hm(t.pop("exit_min"))
        t.pop("fill_i", None)
    return trades


def hm(m) -> str:
    return "" if m is None else f"{int(m) // 60:02d}:{int(m) % 60:02d}"


def run_ticker(ticker: str, bars: list, closes: list, dates: set, runs: dict) -> list[dict]:
    """All runs for one symbol. bars: 1-minute regular-session bars; closes: [(date, close)] daily."""
    by = {}
    for b in bars:
        if K.OPEN <= b.min < 960:
            by.setdefault(b.date, []).append(b)
    days = sorted(by)
    out = []
    for di, d in enumerate(days):
        if di < K.MAGNET_DAYS or (dates and d not in dates):
            continue
        span = [b for x in days[di - K.MAGNET_DAYS:di + 1] for b in by[x]]
        b15 = bars_15m(span)
        up = daily_up([c for x, c in closes if x < d])
        for name, off in runs.items():
            rules = {**K.RULES, **off}
            for t in run_day(by[d], span, b15, up, rules):
                out.append({"run": name, "ticker": ticker, **t})
    return out


# ----------------------------------------------------------------- backtest
def _worker(args):
    t, start, end, closes, dates = args
    import data as D
    try:
        bars = D.alpaca_bars(t, start, end, "1Min", rth_only=True) if D.alpaca_enabled() else \
            D.yahoo_intraday([t], "7d", "1m").get(t, [])
    except Exception as e:
        log.warning("%s: no 1-minute bars (%s)", t, e)
        return []
    return run_ticker(t, bars, closes, dates, K.RUNS)


def backtest(days: int) -> None:
    import data as D
    import scanner as S
    u = S.universe()
    tickers = [t for t in u["tickers"] if "=F" not in t and t not in K.EXCLUDE]
    spy = D.yahoo_daily(["SPY"], "2y")["SPY"]
    today = dt.datetime.now(NY).strftime("%Y-%m-%d")
    sessions = [d for d in spy.index if d < today][-days:]
    start = dt.date.fromisoformat(sessions[0]) - dt.timedelta(days=7)
    end = dt.date.fromisoformat(sessions[-1])
    daily = D.yahoo_daily(tickers, "2y")
    closes = {t: list(zip(df.index, df["Close"].astype(float))) for t, df in daily.items()}
    jobs = [(t, start, end, closes.get(t, []), set(sessions)) for t in tickers]
    os.environ["ALPACA_SLEEP"] = str(0.35 * (os.cpu_count() or 2))
    rows = []
    with ProcessPoolExecutor(max_workers=os.cpu_count() or 2) as ex:
        for r in ex.map(_worker, jobs, chunksize=1):
            rows += r
    out = ROOT / "backtest_1m"
    out.mkdir(exist_ok=True)
    df = pd.DataFrame(rows)
    with gzip.open(out / "trades.csv.gz", "wt") as f:
        df.to_csv(f, index=False)
    meta = {"run_at": dt.datetime.now(NY).strftime("%Y-%m-%d %H:%M ET"), "sessions": [sessions[0], sessions[-1]],
            "days": days, "symbols": len(tickers), "trades": len(df),
            "source": "Alpaca 1-minute (SIP)" if D.alpaca_enabled() else "Yahoo 1-minute (about 7 days only)",
            "rules": K.RULES}
    (out / "meta.json").write_text(json.dumps(meta, indent=1))
    review()


# ----------------------------------------------------------------- review
def stats(r: pd.Series) -> dict:
    r = r.dropna().to_numpy(float)
    if not len(r):
        return {"n": 0}
    eq = np.cumsum(r)
    half = len(r) // 2
    loss = -r[r < 0].sum()
    return {"n": len(r), "win": (r > 0).mean(), "avg": r.mean(), "pf": r[r > 0].sum() / loss if loss else None,
            "total": r.sum(), "dd": float((eq - np.maximum.accumulate(np.maximum(eq, 0))).min()),
            "h1": r[:half].mean() if half else None, "h2": r[half:].mean() if len(r) - half else None,
            "big": (r >= K.TARGET_R * K.PARTIAL_AT_TARGET).mean()}


def _fmt(v, pct=False):
    if v is None or (isinstance(v, float) and np.isnan(v)):
        return ""
    return f"{v * 100:.1f}%" if pct else f"{v:.2f}"


def table(rows: list[tuple[str, dict]]) -> str:
    h = "| Group | Trades | Win rate | Avg R | Profit factor | Total R | Max DD R | 1st half avg R | 2nd half avg R |\n|---|---|---|---|---|---|---|---|---|\n"
    for name, s in rows:
        if not s.get("n"):
            h += f"| {name} | 0 | | | | | | | |\n"
            continue
        h += (f"| {name} | {s['n']} | {_fmt(s['win'], True)} | {_fmt(s['avg'])} | {_fmt(s['pf'])} | {_fmt(s['total'])} | "
              f"{_fmt(s['dd'])} | {_fmt(s['h1'])} | {_fmt(s['h2'])} |\n")
    return h


def review() -> str:
    p = ROOT / "backtest_1m" / "trades.csv.gz"
    meta = json.loads((ROOT / "backtest_1m" / "meta.json").read_text()) if (ROOT / "backtest_1m" / "meta.json").exists() else {}
    df = pd.read_csv(p) if p.exists() and p.stat().st_size > 30 else pd.DataFrame(columns=["run"])
    if len(df):
        df = df.sort_values(["date", "fill_time"])
    md = [f"# 1-minute FVG model review: {dt.datetime.now(NY).strftime('%Y-%m-%d %H:%M ET')}\n",
          f"Data: {meta.get('source', '?')}, {meta.get('sessions', ['?', '?'])[0]} to {meta.get('sessions', ['?', '?'])[-1]}, "
          f"{meta.get('symbols', '?')} symbols. Long only. Results in R, net of {K.COST_PCT_PER_SIDE}% per side.\n\n"]
    md.append("## 1. Each rule switched off in turn (current plan: half at 4R, rest to the 15-minute magnet)\n\n")
    md.append(table([(r, stats(df.loc[df["run"] == r, "r_plan"])) for r in K.RUNS]))
    core = df[df["run"] == "core"] if len(df) else df
    if len(core):
        md.append("\n## 2. Core model: exit methods\n\n")
        md.append(table([("Half at 4R, rest to the 15-minute magnet (plan)", stats(core["r_plan"])),
                         ("Everything at 4R", stats(core["r_full4r"])),
                         ("Half at 4R, rest held to the close", stats(core["r_eod"]))]))
        tmin = core["fill_time"].str.slice(0, 2).astype(int) * 60 + core["fill_time"].str.slice(3, 5).astype(int)
        md.append("\n## 3. Core model: by entry time, risk size, room to the first magnet\n\n")
        md.append(table([("Filled 9:45-10:30", stats(core.loc[tmin < 630, "r_plan"])),
                         ("Filled 10:30-12:00", stats(core.loc[(tmin >= 630) & (tmin < 720), "r_plan"])),
                         ("Filled 12:00-15:00", stats(core.loc[tmin >= 720, "r_plan"])),
                         ("Risk 0.20-0.35% of price", stats(core.loc[core["risk_pct"] < 0.35, "r_plan"])),
                         ("Risk 0.35%+ of price", stats(core.loc[core["risk_pct"] >= 0.35, "r_plan"])),
                         ("A 15-minute magnet sits before 4R", stats(core.loc[core["magnet_before_t1"].astype(str) == "True", "r_plan"])),
                         ("Clear path to 4R", stats(core.loc[core["magnet_before_t1"].astype(str) != "True", "r_plan"])),
                         ("Trendline with 3+ touches", stats(core.loc[core["tl_touches"] >= 3, "r_plan"]))]))
        md.append("\n## 4. Core model: exits and costs\n\n")
        md.append("| Exit | Trades |\n|---|---|\n" + "".join(f"| {k} | {v} |\n" for k, v in core["exit"].value_counts().items()))
        md.append(f"\nAverage cost per trade: {core['cost_r'].mean():.2f}R. Trades reaching 4R: "
                  f"{core['exit'].str.startswith('4R').mean() * 100:.1f}%. Median risk: {core['risk_pct'].median():.2f}% of price.\n")
        top = core.groupby("ticker")["r_plan"].agg(["count", "mean", "sum"]).sort_values("sum", ascending=False)
        md.append("\n## 5. Core model by symbol (top and bottom 8 by total R)\n\n| Symbol | Trades | Avg R | Total R |\n|---|---|---|---|\n")
        for t, r in pd.concat([top.head(8), top.tail(8)]).drop_duplicates().iterrows():
            md.append(f"| {t} | {int(r['count'])} | {r['mean']:.2f} | {r['sum']:.2f} |\n")
    md.append("\nHow to read this: a rule earns its place when switching it off (section 1) lowers the average R in BOTH "
              "halves. Fewer than about 100 core trades is too small a sample to trust.\n")
    text = "".join(md)
    (ROOT / "review_1m.md").write_text(text)
    return text


def main() -> None:
    logging.basicConfig(level=logging.INFO, format="%(asctime)s %(levelname)s %(message)s")
    ap = argparse.ArgumentParser()
    ap.add_argument("--backtest", type=int, metavar="DAYS")
    ap.add_argument("--review", action="store_true")
    a = ap.parse_args()
    if a.backtest:
        backtest(a.backtest)
    elif a.review:
        print(review())


if __name__ == "__main__":
    main()
