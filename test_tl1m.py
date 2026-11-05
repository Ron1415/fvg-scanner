"""Checks the trendline-break model on hand-built charts. Run: python test_tl1m.py"""
from __future__ import annotations

import tl1m as T
from test_fvg1m import make_day, path, winner_closes


T.K.FIRST_FILL = 585    # the hand-built charts set up before 10:30; the time rule is tested separately
T.K.MIN_TOUCH = 3       # the hand-built pullback has three lower highs (see test_two_touch_early_break)


def check(name, cond):
    print(("PASS " if cond else "FAIL ") + name)
    assert cond, name


def mirror(day, p=200.0):
    return [b._replace(o=p - b.o, h=p - b.l, l=p - b.h, c=p - b.c) for b in day]


def trades(day, over=None, trend=0):
    return [r for r in T.run_day(day, T.settings(over), trend) if r["kind"] == "trade"]


def test_long_and_mirrored_short():
    up = path((101.2, 0), (101.6, 5), (102.6, 20), (103.8, 30))[1:]
    day = make_day("2026-10-29", winner_closes(up) + [103.8] * 300)
    lt = [t for t in trades(day) if t["side"] == "LONG"]
    check("long: one trade after the trendline break", len(lt) == 1)
    t = lt[0]
    check("long: entry at the setup FVG midpoint", abs(t["entry"] - (t["gap_top"] + t["gap_bot"]) / 2) < 1e-9)
    check("long: stop below the FVG, at least 0.20%", t["stop"] < min(t["gap_top"], t["gap_bot"]) and t["risk_pct"] >= 0.2 - 1e-9)
    check("long: winner reaches 4R", t["exit"].startswith("4R") and t["r_real"] > 2)
    check("long: retracement inside the zone", 0.45 <= t["fib_ret"] <= 0.70)
    md = mirror(day)
    st = [x for x in trades(md) if x["side"] == "SHORT"]
    check("short: the mirrored chart gives one short trade", len(st) == 1)
    s = st[0]
    old, T.K.MIN_RISK_PCT = T.K.MIN_RISK_PCT, 0.0     # the 0.20% floor depends on the price level
    try:
        a = [x for x in trades(day) if x["side"] == "LONG"][0]
        b = [x for x in trades(md) if x["side"] == "SHORT"][0]
        check("short: same result as the long (mirror image)", abs(a["r_gross"] - b["r_gross"]) < 1e-9 and a["exit"] == b["exit"])
    finally:
        T.K.MIN_RISK_PCT = old
    check("short: prices are real (entry mirrored)", abs(s["entry"] - (200 - t["entry"])) < 1e-9 and s["stop"] > s["entry"])
    check("no short on the up chart, no long on the down chart",
          not [x for x in trades(day) if x["side"] == "SHORT" and x["fill_time"] == t["fill_time"]] and
          not [x for x in trades(md) if x["side"] == "LONG" and x["fill_time"] == t["fill_time"]])


def test_variants_and_filters():
    down = path((101.2, 0), (100.9, 4), (100.5, 10))[1:]
    day = make_day("2026-10-29", winner_closes(down) + [100.5] * 300)
    t = [x for x in trades(day) if x["side"] == "LONG"][0]
    check("loser stops out near -1R", t["exit"] == "stop" and -1.3 < t["r_real"] < -0.99)
    sw = [x for x in trades(day, {"stop": "swing"}) if x["side"] == "LONG"][0]
    check("swing-low stop sits below the swing low", sw["stop"] < sw["leg_low_px"])
    c2 = [x for x in trades(day, {"stop": "close2"}) if x["side"] == "LONG"][0]
    check("2-close exit: closes out after 2 closes below the swing low", c2["exit"] == "lower low confirmed")
    up = path((101.2, 0), (101.6, 5), (102.6, 20), (103.8, 30))[1:]
    d2 = make_day("2026-10-29", winner_closes(up) + [103.8] * 300)
    check("daily-trend rule is off by default", trades(d2, trend=-1))
    check("...and blocks when switched on", not [x for x in trades(d2, {"daily": True}, trend=-1) if x["side"] == "LONG"])
    T.K.FIRST_FILL = 700
    try:
        check("no fills before the first-fill time", not [x for x in trades(d2) if x["side"] == "LONG"])
    finally:
        T.K.FIRST_FILL = 585
    rows = T.run_day(d2, T.settings({"daily": True}), -1)
    check("a blocked setup is recorded with its reason", any(r["kind"] == "blocked" and "daily" in r["why"] for r in rows))


def test_two_touch_early_break():
    """With 2-touch lines (the default) a steep line from the rally top breaks on the first bounce of the
    pullback, before the real reversal: the known early-break failure the review measures."""
    T.K.MIN_TOUCH = 2
    try:
        up = path((101.2, 0), (101.6, 5), (102.6, 20), (103.8, 30))[1:]
        day = make_day("2026-10-29", winner_closes(up) + [103.8] * 300)
        lt = [t for t in trades(day) if t["side"] == "LONG"]
        check("2 touches: the early break is traded first and stops out", lt and lt[0]["tl_touches"] == 2 and lt[0]["exit"] == "stop")
    finally:
        T.K.MIN_TOUCH = 3


if __name__ == "__main__":
    test_long_and_mirrored_short()
    test_variants_and_filters()
    test_two_touch_early_break()
    print("All checks passed.")
