"""Checks the 1-minute FVG model on hand-built charts. Run: python test_fvg1m.py"""
from __future__ import annotations

import datetime as dt
from zoneinfo import ZoneInfo

import config_1m as K
import fvg1m as F
from engine import Bar

NY = ZoneInfo("America/New_York")


def check(name, cond):
    print(("PASS " if cond else "FAIL ") + name)
    assert cond, name


def path(*legs):
    """legs: (target close, number of 1-minute bars) moved to in straight lines."""
    out, c = [], legs[0][0]
    for tgt, n in legs[1:]:
        for k in range(1, n + 1):
            out.append(c + (tgt - c) * k / n)
        c = tgt
    return [legs[0][0]] + out


def make_day(date, closes):
    """1-minute bars from closes; open = prior close; small wicks so swing highs are strict."""
    d0 = dt.datetime.fromisoformat(date + "T09:30").replace(tzinfo=NY)
    out = []
    for i, c in enumerate(closes):
        o = closes[i - 1] if i else c
        t = d0 + dt.timedelta(minutes=i)
        h = c + .02 if c > o else o + .005      # up bars: wick above the close; down bars: tiny wick
        l = o - .005 if c > o else c - .02
        out.append(Bar(int(t.timestamp()), date, 570 + i, o, h, l, c, 1000))
    return out


def winner_closes(after):
    """Opening range ~100-100.4, rally above it, pullback with three lower highs (a gently falling
    trendline), break of structure with a 1-minute FVG, pullback to the FVG midpoint on the line."""
    c = path((100.2, 0), (100.4, 4), (100.0, 4), (100.4, 4), (100.2, 3),       # opening range (15 bars)
             (101.6, 14),                                                    # rally above the range
             (101.2, 4), (101.45, 4), (101.15, 4), (101.40, 4), (101.10, 4), (101.35, 4), (100.85, 6),  # lower highs
             (101.0, 2), (101.05, 1), (101.45, 1), (101.55, 1), (101.75, 3),  # break of structure + FVG
             (101.5, 3), (101.2, 2))                                         # pullback into the gap
    return c + after


def test_core_trade():
    up = path((101.2, 0), (101.6, 5), (102.6, 20), (102.8, 30))[1:]
    day = make_day("2026-10-29", winner_closes(up) + [102.8] * 300)
    tr = F.run_day(day, day, F.bars_15m(day), True, dict(K.RULES))
    check("core model takes exactly one trade", len(tr) == 1)
    t = tr[0]
    for f in ("daily_up", "vwap", "orb", "fib", "trendline"):
        check(f"rule passes: {f}", t[f"f_{f}"])
    check("entry at the FVG midpoint", t["gap_lo"] < t["entry"] < t["gap_hi"] and abs(t["entry"] - (t["gap_lo"] + t["gap_hi"]) / 2) < 0.03)
    check("stop below the gap, at least 0.20% of price", t["stop"] < t["gap_lo"] and t["risk_pct"] >= 0.2 - 1e-9)
    check("first target is 4R", abs(t["t1"] - (t["entry"] + 4 * (t["entry"] - t["stop"]))) < 1e-9)
    check("winner: half at 4R, runner to the close (no magnet above)", t["exit"] == "4R then close" and t["r_plan"] > 2)
    check("full exit at 4R is about +4R less costs", abs(t["r_full4r"] - (4 - t["cost_r"])) < 1e-9)
    # nothing without the daily up-trend
    check("no trade when the daily trend is not up", not F.run_day(day, day, F.bars_15m(day), False, dict(K.RULES)))


def test_loser_and_breakeven():
    down = path((101.2, 0), (100.9, 4), (100.5, 10))[1:]
    day = make_day("2026-10-29", winner_closes(down) + [100.5] * 300)
    t = F.run_day(day, day, F.bars_15m(day), True, dict(K.RULES))[0]
    check("loser stops out at about -1R", t["exit"] == "Stop" and -1.4 < t["r_plan"] < -1)
    be = path((101.2, 0), (101.85, 4), (101.0, 6))[1:]    # closes above the recent high, then fails
    day = make_day("2026-10-29", winner_closes(be) + [101.0] * 300)
    t = F.run_day(day, day, F.bars_15m(day), True, dict(K.RULES))[0]
    check("stop moves to breakeven after a close above the recent high", t["exit"] == "Breakeven" and abs(t["r_plan"] + t["cost_r"]) < 1e-9)


def test_no_lookahead_and_magnet():
    up = path((101.2, 0), (101.6, 5), (102.6, 20), (104.8, 30))[1:]
    day = make_day("2026-10-29", winner_closes(up) + [104.8] * 300)
    full = F.run_day(day, day, F.bars_15m(day), True, dict(K.RULES))[0]
    cut = [b for b in day if b.min <= 570 + len(winner_closes([]))]
    part = F.run_day(cut, cut, F.bars_15m(cut), True, dict(K.RULES))
    check("same entry whether or not later bars exist", part and abs(part[0]["entry"] - full["entry"]) < 1e-9)
    # a prior-day 15-minute bearish gap above 4R becomes the runner's target
    prev = make_day("2026-10-28", path((104.5, 0), (104.6, 15), (104.0, 1), (103.7, 14), (103.6, 30)) + [103.6] * 300)
    gap = [b._replace(h=104.62, l=104.55) if b.min < 585 else b._replace(h=min(b.h, 104.2)) if b.min < 600 else b._replace(h=min(b.h, 103.9)) for b in prev]
    span = gap + day
    t = F.run_day(day, span, F.bars_15m(span), True, dict(K.RULES))[0]
    check("15-minute FVG above 4R is the runner target", t["magnet"] is not None and t["magnet"] > t["t1"])
    check("runner exits at the magnet", t["exit"] == "4R then magnet")


def test_rules_matter():
    flat = path((101.2, 0), (101.6, 5), (102.6, 20), (102.8, 30))[1:]
    closes = winner_closes(flat) + [102.8] * 300
    day = make_day("2026-10-29", closes)
    check("structure-only run trades as well", F.run_day(day, day, F.bars_15m(day), True, {r: False for r in K.RULES}))
    low_or = [c if i >= 15 else c + 1.5 for i, c in enumerate(closes)]   # opening range far above: never broken
    d2 = make_day("2026-10-29", low_or)
    check("no trade when the opening range was never broken upward", not F.run_day(d2, d2, F.bars_15m(d2), True, dict(K.RULES)))
    check("...but the same day trades with the opening-range rule off",
          bool(F.run_day(d2, d2, F.bars_15m(d2), True, {**K.RULES, "orb": False, "vwap": False})))


if __name__ == "__main__":
    test_core_trade()
    test_loser_and_breakeven()
    test_no_lookahead_and_magnet()
    test_rules_matter()
    print("All checks passed.")
