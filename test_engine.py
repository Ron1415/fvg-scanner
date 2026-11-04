"""Checks the engine and the backtest rules on hand-built charts. Run: python test_engine.py"""
from __future__ import annotations

import datetime as dt
from zoneinfo import ZoneInfo

import engine as E
from engine import Bar
from replay import replay_ticker
from simulate import simulate

NY = ZoneInfo("America/New_York")
SIM = {"entry_start": 600, "entry_cutoff": 930, "eod_exit": 955, "partial_at_t1": 0.5, "cost_pct_per_side": 0.0}


def bars(rows, start=620):
    return [Bar(0, "2026-10-29", start + i, o, h, l, c, 0) for i, (o, h, l, c) in enumerate(rows)]


def check(name, cond):
    print(("PASS " if cond else "FAIL ") + name)
    assert cond, name


def test_simulate():
    sn = {"side": "LONG", "entry": 100, "stop": 99, "t1": 102, "t2": 103, "snap_min": 620}
    o = simulate(sn, bars([[100.5, 100.6, 99.9, 100], [100, 100.2, 98.9, 99]]), SIM)
    check("stop after fill = -1R", o["outcome"] == "Stop" and o["r_plan"] == -1)
    o = simulate(sn, bars([[100.5, 100.6, 99.9, 100.1], [100.1, 102.1, 100, 102], [102, 103.2, 101.5, 103]]), SIM)
    check("T1 then T2 = +2.5R", o["outcome"] == "T1 then T2" and abs(o["r_plan"] - 2.5) < 1e-9)
    o = simulate(sn, bars([[100.5, 100.6, 99.9, 100.1], [100.1, 102.1, 100, 102], [102, 102, 99.9, 100]]), SIM)
    check("T1 then breakeven = +1R", o["outcome"] == "T1 then breakeven" and abs(o["r_plan"] - 1) < 1e-9)
    o = simulate(sn, bars([[100.5, 100.6, 99.9, 100.1], [100.1, 102.5, 98.5, 101]]), SIM)
    check("bar touching stop and target counts as stop", o["outcome"] == "Stop")
    o = simulate(sn, bars([[100.5, 102.2, 100.1, 102]]), SIM)
    check("ran to T1 without a fill = no trade", not o["triggered"])
    o = simulate(sn, bars([[99.5, 99.8, 99.4, 99.7], [99.7, 102.1, 99.6, 102], [102, 103.1, 102, 103]]), SIM)
    check("gap through the entry fills at the open", o["fill"] == 99.5 and abs(o["r_plan"] - 3.0) < 1e-9)
    o = simulate(sn, [Bar(0, "d", 930, 101, 101, 99.5, 100, 0)], SIM)
    check("no fills after the cutoff", not o["triggered"])
    sh = {"side": "SHORT", "entry": 100, "stop": 101, "t1": 98, "t2": 97, "snap_min": 620}
    o = simulate(sh, bars([[99.5, 100.1, 99.4, 99.9], [99.9, 100, 97.9, 98], [98, 98.2, 96.9, 97]]), SIM)
    check("short T1 then T2 = +2.5R", o["outcome"] == "T1 then T2" and abs(o["r_plan"] - 2.5) < 1e-9)
    o = simulate(sn, bars([[100.5, 100.6, 99.9, 100.1], [100.1, 100.5, 100.0, 100.2]]), {**SIM, "cost_pct_per_side": 0.05})
    check("costs reduce the net result", o["r_plan_net"] < o["r_plan"])


def synthetic_day(date, kind):
    """Opening range, a sweep of the lows at 10:25, displacement up (FVG), then a pullback."""
    base = [101.2, 101.5, 101.7, 101.4, 101.2, 101.3, 101.0, 100.7, 100.4, 100.1, 99.8, 99.7, 100.4, 101.3, 102.2, 102.4,
            102.1, 101.8, 101.6, 101.5]
    cont = {"win": [101.0, 100.45, 100.9, 101.6, 102.3, 102.8, 103.5, 104.0], "loss": [101.0, 100.45, 100.2, 99.5, 99.0]}[kind]
    path = base + cont
    path += [path[-1]] * (78 - len(path))
    out, d0 = [], dt.datetime.fromisoformat(date + "T09:30").replace(tzinfo=NY)
    for i, c in enumerate(path):
        o = path[i - 1] if i else c
        t = d0 + dt.timedelta(minutes=5 * i)
        out.append(Bar(int(t.timestamp()), date, 570 + 5 * i, o, max(o, c) + .05, min(o, c) - .05, c, 4000 if i == 13 else 1000))
    return out


def test_detection_and_replay():
    prev = synthetic_day("2026-10-28", "win")
    day = synthetic_day("2026-10-29", "win")
    lv = E.levels_for(prev + day, "2026-10-29", "2026-10-28", False)
    rth = [b for b in day if b.min < 655]   # bars closed by 10:55
    st = [s for s in E.find_setups(rth, lv) if s["side"] == "LONG"]
    check("long setup found after the sweep and displacement", len(st) == 1)
    s = st[0]
    check("entry sits inside the FVG", s["fvg_lo"] <= s["entry"] <= s["fvg_hi"])
    check("stop is below the sweep low", s["stop"] < s["extreme"])
    cfg = E.settings()
    closes = [(f"2026-{m:02d}-{d:02d}", 90 + i * 0.1) for i, (m, d) in enumerate([(9, x) for x in range(1, 29)] + [(10, x) for x in range(1, 28)])]
    rows = replay_ticker("TEST", prev + day, closes, "Backtest", cfg, {"2026-10-29"})
    longs = [r for r in rows if r["side"] == "LONG"]
    check("replay records the long setup once", len(longs) == 1)
    check("replayed winner is triggered and positive", longs[0]["triggered"] and longs[0]["r_plan"] > 0)
    loss = synthetic_day("2026-10-29", "loss")
    rows = [r for r in replay_ticker("TEST", prev + loss, closes, "Backtest", cfg, {"2026-10-29"}) if r["side"] == "LONG"]
    check("replayed loser stops out", rows and rows[0]["outcome"] == "Stop")


def test_ladder():
    from replay import ladder
    row = {"side": "LONG", "entry": 100.0, "fvg_hi": 101.0, "fvg_lo": 99.5, "ce": 100.25, "ote_62": 100.8,
           "extreme": 99.0, "atr": 0.0, "t1": 103.0, "t2": 104.0, "snap_min": 620}
    legs = [("fvg_edge", 0.2), ("blend", 0.3), ("ote_mid", 0.5)]   # limits at 101, 100.5, 100; stop 99
    # dips to 100.4 (edge and blend fill, the deepest leg does not), then runs through T2
    b = bars([[101.5, 101.6, 100.4, 100.6], [100.6, 103.1, 100.5, 103], [103, 104.2, 102.9, 104]])
    trig, r, filled = ladder(row, legs, b)
    check("scaled entry: partial fill recorded", trig and abs(filled - 0.5) < 1e-9)
    planned = 0.2 * 2 + 0.3 * 1.5 + 0.5 * 1.0
    got = (0.2 * (0.5 * 2 + 0.5 * 3) + 0.3 * (0.5 * 2.5 + 0.5 * 3.5)) / planned
    check("scaled entry: result in R of the full planned risk", abs(r - got) < 0.02)


def test_overnight_futures():
    """A sweep-and-reverse during the London session (2-8 AM ET) is found and simulated."""
    import config as C
    from replay import replay_ticker
    prev = synthetic_day("2026-10-28", "win")
    day = synthetic_day("2026-10-29", "win")
    lon = synthetic_day("2026-10-29", "win")   # same shape, moved to 2:00 AM
    shift = (9 * 60 + 30 - 2 * 60) * 60
    lon = [b._replace(ts=b.ts - shift, min=b.min - (9 * 60 + 30 - 2 * 60)) for b in lon][:72]
    rows = replay_ticker("ES=F", prev + sorted(lon + day, key=lambda b: b.ts), [], "Backtest", E.settings(), {"2026-10-29"})
    names = {r["session_name"] for r in rows}
    check("futures replay covers New York and London", {"NY", "London"} <= names)
    lr = [r for r in rows if r["session_name"] == "London" and r["side"] == "LONG"]
    check("London long setup triggered with London clock times", lr and lr[0]["triggered"] and lr[0]["trigger_time"] < "08:00")
    rows = replay_ticker("SPY", prev + sorted(lon + day, key=lambda b: b.ts), [], "Backtest", E.settings(), {"2026-10-29"})
    check("stocks and ETFs stay New York only", {r["session_name"] for r in rows} == {"NY"})


def test_short_rules():
    sim = {**SIM, "partial_at_t1": 1.0, "be_after_r": 0.5, "time_stop_min": 60}
    sh = {"side": "SHORT", "entry": 100, "stop": 101, "t1": 98, "t2": 97, "snap_min": 620}
    # fills, moves 0.6R in favour, then comes back through the entry: breakeven, not -1R
    o = simulate(sh, bars([[99.5, 100.1, 99.6, 99.9], [99.9, 100.0, 99.4, 99.5], [99.5, 101.2, 99.5, 101]]), sim)
    check("short: breakeven after +0.5R", o["outcome"] == "Breakeven stop" and abs(o["r_plan"]) < 1e-9)
    flat = [[99.5, 100.1, 99.6, 99.9]] + [[99.9, 100.0, 99.7, 99.85]] * 70
    o = simulate(sh, bars(flat), sim)
    check("short: 60-minute time stop", o["outcome"] == "Time stop" and o["mins_in_trade"] <= 61)
    s = {"side": "SHORT", "overlap": True, "rr1": 1.5, "rr2": 2.2, "score": 70, "entry": 100.0, "stop": 100.1,
         "swept": ["ORH"], "bias": "Bullish", "snap_min": 615, "ticker": "SQQQ"}
    E.qualify(s, E.settings())
    check("short guardrails block a weak short", not s["qualified"] and s["base_qualified"] and len(s["filter_reasons"]) == 6)
    l = {**s, "side": "LONG"}
    E.qualify(l, E.settings())
    check("longs are not held to the short guardrails", l["qualified"])


def test_confirmation_and_runner():
    from simulate import confirm_entry
    sn = {"side": "LONG", "zone": 100.5, "stop": 99, "t1": 103, "snap_min": 620}
    # touches the gap at bar 1, pushes lower, then bar 4 closes above the prior 3 highs (101.0) -> enter at 101.05
    b = bars([[101.2, 101.3, 100.9, 101.0], [101.0, 101.0, 100.4, 100.5], [100.5, 100.6, 100.1, 100.2],
              [100.2, 100.4, 100.0, 100.3], [100.3, 101.2, 100.2, 101.05]])
    check("confirmation entry waits for a close above the prior 3 bars", confirm_entry(sn, b, SIM) == (4, 101.05))
    b2 = bars([[101.2, 101.3, 100.4, 100.5], [100.5, 100.6, 98.9, 99.2], [99.2, 101.5, 99.1, 101.4]])
    check("no confirmation entry if the stop trades first", confirm_entry(sn, b2, SIM) is None)
    sl = {"side": "LONG", "entry": 100, "stop": 99, "t1": 102, "t2": 103, "snap_min": 620}
    b3 = bars([[100.5, 100.6, 99.9, 100.1], [100.1, 102.1, 100, 102], [102, 103.5, 101.8, 103.4]], start=640) + \
        [Bar(0, "2026-10-29", 955, 103.4, 104.6, 103.3, 104.5, 0)]
    o = simulate(sl, b3, {**SIM, "runner_to_close": True})
    check("runner holds past T2 until the close", o["outcome"] == "T1 then EOD" and o["r_plan"] > 2.5)


if __name__ == "__main__":
    test_confirmation_and_runner()
    test_short_rules()
    test_overnight_futures()
    test_ladder()
    test_simulate()
    test_detection_and_replay()
    print("All checks passed.")
