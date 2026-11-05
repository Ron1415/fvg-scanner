"""Draws annotated 1-minute charts of sample backtest trades so the rules can be checked by eye.

  python charts_1m.py              # 12 sample trades from the backtest -> site/charts/ (GitHub Pages)
  python charts_1m.py --n 20       # more trades

Each chart shows the candles, VWAP, the opening-range high, the broken swing high (break of structure),
the swing low, the trendline, the FVG, the entry, the v2 stop, the 4R target, the runner magnet, and the
fill and exit. The trades are re-run from the 1-minute bars with the same code as the backtest.
"""
from __future__ import annotations

import argparse
import datetime as dt
import html
import random
from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle
import numpy as np
import pandas as pd

import config_1m as K
import fvg1m as F

ROOT = Path(__file__).resolve().parent
OUT = ROOT / "site" / "charts"
RUN = "Stop below the FVG, 4R (v2)"     # the version recommended for paper trading


def pick(df: pd.DataFrame, n: int, seed: int = 7) -> pd.DataFrame:
    """A spread of outcomes: winners, losers and breakevens, from both test periods."""
    rnd = random.Random(seed)
    groups = [df[df["r_plan"] > 0.5], df[df["exit"].str.contains("Stop|Lower low", regex=True)],
              df[df["exit"].str.contains("Breakeven")]]
    out = []
    for g in groups:
        idx = list(g.index)
        rnd.shuffle(idx)
        out += idx[:max(1, n // 3)]
    return df.loc[out]


def bars_for(ticker: str, date: str, fetch=None) -> list:
    import data as D
    d = dt.date.fromisoformat(date)
    fetch = fetch or (lambda t, a, b: D.alpaca_bars(t, a, b, "1Min", rth_only=True))
    return fetch(ticker, d - dt.timedelta(days=7), d)


def rerun(trade: pd.Series, bars: list, run: str) -> tuple[list, dict | None]:
    """Re-runs the walk for the trade's day and returns (day bars, the matching trade with geometry)."""
    by = {}
    for b in bars:
        if K.OPEN <= b.min < 960:
            by.setdefault(b.date, []).append(b)
    days = sorted(by)
    if trade["date"] not in by:
        return [], None
    di = days.index(trade["date"])
    span = [b for x in days[max(0, di - K.MAGNET_DAYS):di + 1] for b in by[x]]
    day = by[trade["date"]]
    for t in F.run_day(day, span, F.bars_15m(span), bool(trade.get("f_daily_up", True)), F.settings(K.RUNS[run])):
        if t["fill_time"] == trade["fill_time"]:
            return day, t
    return day, None


def draw(day: list, t: dict, ticker: str, path: Path) -> None:
    n = len(day)
    a = min(x for x in (t["g_tl_a"], t["g_p1"], t["g_l0"]) if x is not None and x == x)
    a = max(0, int(a) - 15)
    exit_i = next((i for i, b in enumerate(day) if F.hm(b.min) == t["exit_time"]), int(t["g_fill"]) + 30)
    z = min(n, max(int(t["g_fill"]) + 40, min(exit_i + 15, int(t["g_fill"]) + 120)))   # at most 2 hours after the fill
    seg = day[a:z]
    x = np.arange(a, z)
    fig, ax = plt.subplots(figsize=(13, 6.5), dpi=110)
    for i, b in zip(x, seg):
        up = b.c >= b.o
        col = "#1a9e6a" if up else "#d64545"
        ax.vlines(i, b.l, b.h, color=col, linewidth=0.8)
        ax.add_patch(Rectangle((i - 0.35, min(b.o, b.c)), 0.7, max(abs(b.c - b.o), 1e-6), color=col))
    # VWAP and opening-range high
    pv = np.cumsum([(b.h + b.l + b.c) / 3 * max(b.v, 1) for b in day]); vv = np.cumsum([max(b.v, 1) for b in day])
    ax.plot(x, (pv / vv)[a:z], color="#7c3aed", linewidth=1.2, label="VWAP")
    orh = max(b.h for b in day if b.min < K.OR_END)
    ax.axhline(orh, color="#e07b00", linewidth=0.9, linestyle=":", label=f"Opening-range high {orh:.2f}")
    # break of structure: the broken swing high from its pivot to the break bar
    p1, bos = int(t["g_p1"]), int(t["g_bos"])
    ax.hlines(day[p1].h, p1, bos, color="#0e9aa7", linewidth=1.6, label="Broken swing high (BOS)")
    ax.annotate("BOS", (bos, day[p1].h), xytext=(bos + 1, day[p1].h), color="#0e9aa7", fontsize=9, fontweight="bold")
    # swing low
    l0 = int(t["g_l0"])
    ax.scatter([l0], [day[l0].l], marker="^", color="#0e9aa7", s=50, zorder=5)
    ax.hlines(t["swing_low"], l0, min(exit_i, z - 1), color="#64748b", linewidth=1, linestyle="--", label=f"Swing low {t['swing_low']:.2f} (v3 exit level)")
    # trendline from its first anchor to the fill
    if t["g_tl_a"] is not None and t["g_tl_a"] == t["g_tl_a"]:
        ta, tp, ts = int(t["g_tl_a"]), float(t["g_tl_px"]), float(t["g_tl_slope"])
        xs = np.array([ta, int(t["g_fill"]) + 2])
        ax.plot(xs, tp + ts * (xs - ta), color="#f59e0b", linewidth=2, label=f"Trendline ({t['tl_touches']} touches)")
    # FVG box (from the gap to the fill), midpoint
    g = int(t["g_gap"])
    ax.add_patch(Rectangle((g - 1, t["gap_lo"]), int(t["g_fill"]) - g + 2, t["gap_hi"] - t["gap_lo"],
                           facecolor="#2f6fde", alpha=0.18, edgecolor="#2f6fde", label="FVG"))
    # trade levels
    f0, f1 = int(t["g_fill"]), min(exit_i, z - 1)
    for y, col, lab in ((t["entry"], "#2f6fde", f"Entry {t['entry']:.2f} (FVG midpoint, Fib {t['fib_ret'] * 100:.0f}%)"),
                        (t["stop"], "#d64545", f"Stop {t['stop']:.2f} ({t['risk_pct']:.2f}%)"),
                        (t["t1"], "#1a9e6a", f"4R target {t['t1']:.2f}")):
        ax.hlines(y, f0, f1, color=col, linewidth=1.4, label=lab)
    if t.get("magnet") and t["magnet"] == t["magnet"] and t["magnet"] < max(b.h for b in seg) * 1.01:
        ax.hlines(t["magnet"], f0, f1, color="#0e7490", linewidth=1, linestyle="-.", label=f"15-min magnet {t['magnet']:.2f}")
    ax.scatter([f0], [t["entry"]], marker="o", s=70, color="#2f6fde", zorder=6)
    if exit_i < z:
        ax.scatter([exit_i], [day[min(exit_i, n - 1)].c], marker="X", s=80, color="black", zorder=6)
        ax.annotate(f"Exit: {t['exit']}", (exit_i, day[min(exit_i, n - 1)].c), xytext=(4, -14), textcoords="offset points", fontsize=8)
    else:
        ax.annotate(f"Exit at {t['exit_time']} (off the chart): {t['exit']}", (z - 1, seg[-1].c), xytext=(-220, 12),
                    textcoords="offset points", fontsize=8)
    ticks = list(range(a, z, 15))
    ax.set_xticks(ticks, [F.hm(day[i].min) for i in ticks])
    lo = min(min(b.l for b in seg), t["stop"]); hi = max(max(b.h for b in seg), t["t1"] if t["t1"] < max(b.h for b in seg) * 1.01 else 0)
    ax.set_ylim(lo - (hi - lo) * 0.04, hi + (hi - lo) * 0.04)
    ax.set_xlim(a - 1, z)
    ax.set_title(f"{ticker} {t['date']}  ·  fill {t['fill_time']}  ·  {t['exit']}  ·  {t['r_plan']:+.2f}R after costs", fontsize=11)
    ax.grid(alpha=0.15)
    ax.legend(loc="upper left", fontsize=7.5, framealpha=0.9)
    fig.tight_layout()
    fig.savefig(path)
    plt.close(fig)


def main(n: int = 12, fetch=None, trades: pd.DataFrame | None = None, run: str = RUN) -> list[Path]:
    df = trades if trades is not None else pd.read_csv(ROOT / "backtest_1m" / "trades.csv.gz")
    df = df[df["run"] == run]
    OUT.mkdir(parents=True, exist_ok=True)
    made, rows = [], []
    for _, tr in pick(df, n).iterrows():
        day, t = rerun(tr, bars_for(tr["ticker"], tr["date"], fetch), run)
        if t is None:
            continue
        name = f"{tr['ticker']}_{tr['date']}_{t['fill_time'].replace(':', '')}.png"
        draw(day, t, tr["ticker"], OUT / name)
        made.append(OUT / name)
        rows.append(f"<h3>{html.escape(tr['ticker'])} {t['date']} · {t['exit']} · {t['r_plan']:+.2f}R</h3>"
                    f"<img src='{name}' style='max-width:100%'>")
    (OUT / "index.html").write_text("<!doctype html><meta charset='utf-8'><meta name='viewport' content='width=device-width'>"
                                    "<title>FVG 1-minute trade charts</title><body style='font-family:sans-serif;max-width:1500px;margin:auto;padding:16px'>"
                                    f"<h1>FVG 1-minute trade charts ({html.escape(run)})</h1>" + "".join(rows))
    return made


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("--n", type=int, default=12)
    main(ap.parse_args().n)
