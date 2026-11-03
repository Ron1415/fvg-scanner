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


if __name__ == "__main__":
    test_simulate()
    test_detection_and_replay()
    print("All checks passed.")
