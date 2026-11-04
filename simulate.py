"""Backtests one frozen setup on the bars that follow it.

Conservative rules (identical to the Apps Script version):
- limit order at the entry, fills only from SIM["entry_start"] to SIM["entry_cutoff"];
  a gap through the entry fills at the open; the order is cancelled if the stop trades first
- the fill bar can only stop out; when a bar touches both stop and target, the stop wins
- plan: PARTIAL_AT_T1 off at T1, stop to breakeven, rest to T2; anything open exits at EOD_EXIT
- also records full-position-to-T1 and full-position-to-T2 results
"""
from __future__ import annotations

import config as C


def simulate(sn: dict, bars: list, sim: dict = C.SIM) -> dict:
    long = sn["side"] == "LONG"
    d = 1 if long else -1
    E, S, T1, T2 = d * sn["entry"], d * sn["stop"], d * sn["t1"], d * sn["t2"]
    risk = E - S
    out = dict(outcome="Not triggered (no data)", triggered=False, trigger_min=None, fill=None, exit_min=None,
               r_plan=0.0, r_t1=0.0, r_t2=0.0, mfe=None, mae=None, mins_to_trigger=None, mins_in_trade=None,
               r_plan_net=0.0)
    if not risk > 0 or not bars:
        return out
    start = max(sn["snap_min"], sim["entry_start"])
    cutoff, p = sim["entry_cutoff"], sim["partial_at_t1"]
    be_r, ts_min = sim.get("be_after_r"), sim.get("time_stop_min")   # optional closer management (shorts)
    stop_now, plan_exit = S, None
    runner = sim.get("runner_to_close")   # half at T1, the rest held to the close (breakeven stop)
    fill = fill_min = None
    hi, lo, ran_away = float("-inf"), float("inf"), False
    a = b2 = leg1 = leg2 = None
    t1_hit, plan, last_c, last_min = False, None, None, None
    R = lambda x: (x - fill) / risk
    for bar in bars:
        H, L = (bar.h, bar.l) if long else (-bar.l, -bar.h)
        O, Cc = d * bar.o, d * bar.c
        last_c, last_min = Cc, bar.min
        if fill is None:
            if bar.min >= cutoff:
                out["outcome"] = "Not triggered (ran to T1 first)" if ran_away else "Not triggered (cutoff)"
                break
            if bar.min >= start and (L <= E or sn.get("market")):
                fill = E if sn.get("market") else min(E, O)
                if fill <= S:
                    out["outcome"] = "Invalidated before entry"; fill = None
                    break
                fill_min, hi, lo = bar.min, H, L
                if L <= S:
                    a = b2 = leg1 = leg2 = R(S); plan = "Stop"; out["exit_min"] = bar.min
                    break
                continue
            if L <= S:
                out["outcome"] = "Invalidated before entry"
                break
            if H >= T1:
                ran_away = True
            out["outcome"] = "Not triggered (ran to T1 first)" if ran_away else "Not triggered"
            continue
        hi, lo = max(hi, H), min(lo, L)
        if bar.min >= sim["eod_exit"]:
            if a is None: a = R(Cc)
            if b2 is None: b2 = R(Cc)
            if leg1 is None:
                leg1 = leg2 = R(Cc); plan = "EOD exit"
            elif leg2 is None:
                leg2 = R(Cc); plan = "T1 then EOD"
            out["exit_min"] = bar.min
            break
        if ts_min and not t1_hit and leg1 is None and bar.min - fill_min >= ts_min:
            leg1 = leg2 = R(Cc); plan = "Time stop"
        if a is None:
            a = R(S) if L <= S else R(T1) if H >= T1 else None
        if b2 is None:
            b2 = R(S) if L <= S else R(T2) if H >= T2 else None
        if leg1 is not None and not t1_hit:
            pass                                    # time stop already closed the plan legs
        elif not t1_hit:
            if L <= stop_now:
                leg1 = leg2 = R(stop_now); plan = "Stop" if stop_now == S else "Breakeven stop"
            elif H >= T1:
                t1_hit, leg1 = True, R(T1)
                if H >= T2 and not runner:
                    leg2 = R(T2); plan = "T1 then T2"
        elif leg2 is None:
            if L <= fill:
                leg2 = 0.0; plan = "T1 then breakeven"
            elif H >= T2 and not runner:
                leg2 = R(T2); plan = "T1 then T2"
        if plan_exit is None and leg1 is not None and leg2 is not None:
            plan_exit = bar.min                     # when the plan itself was fully closed
        if be_r and not t1_hit and (H - fill) / risk >= be_r:
            stop_now = max(stop_now, fill)          # takes effect from the next bar (conservative)
        if None not in (leg1, leg2, a, b2):
            out["exit_min"] = bar.min
            break
    if fill is not None:
        if a is None: a = R(last_c)
        if b2 is None: b2 = R(last_c)
        if leg1 is None:
            leg1 = leg2 = R(last_c); plan = "EOD exit"
        elif leg2 is None:
            leg2 = R(last_c); plan = "T1 then EOD"
        if out["exit_min"] is None:
            out["exit_min"] = last_min
        if plan_exit is not None:
            out["exit_min"] = plan_exit
        r_plan = p * leg1 + (1 - p) * leg2
        per_side = sim.get("cost_abs_per_side") or sim["cost_pct_per_side"] / 100 * abs(fill)
        cost_r = 2 * per_side / risk   # round trip, in R
        out.update(triggered=True, trigger_min=fill_min, fill=d * fill, outcome=plan, r_plan=r_plan, r_t1=a, r_t2=b2,
                   mfe=max(0.0, (hi - fill) / risk), mae=max(0.0, (fill - lo) / risk), r_plan_net=r_plan - cost_r,
                   mins_to_trigger=fill_min - sn["snap_min"], mins_in_trade=out["exit_min"] - fill_min)
    return out


def confirm_entry(sn: dict, bars: list, sim: dict = C.SIM, lookback: int = 3):
    """Confirmation entry: wait until price trades into the FVG (its near edge), then enter
    at the close of the first bar that closes beyond the highs (longs) / lows (shorts) of the
    previous `lookback` bars, i.e. a small structure shift on the bar series given (1-minute
    bars when available). No trade if the stop trades first, if the cutoff passes, or if the
    entry is already at/through Target 1. Returns (index of the entry bar, entry price) or None."""
    long = sn["side"] == "LONG"
    d = 1 if long else -1
    zone, S, T1 = d * sn["zone"], d * sn["stop"], d * sn["t1"]
    start = max(sn["snap_min"], sim["entry_start"])
    touched, hist = False, []
    for i, bar in enumerate(bars):
        H, L, Cc = (bar.h, bar.l, bar.c) if long else (-bar.l, -bar.h, -bar.c)
        if bar.min >= sim["entry_cutoff"]:
            return None
        if L <= S:
            return None
        if bar.min >= start:
            touched = touched or L <= zone
            if touched and len(hist) >= lookback and Cc > max(hist[-lookback:]):
                return (i, d * Cc) if Cc < T1 else None
        hist.append(H)
    return None
