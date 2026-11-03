"""Replay: walk a session bar by bar exactly as the live scanner would have seen it,
freeze each setup, and backtest it (plus every side-by-side test variant)."""
from __future__ import annotations

import datetime as dt
from zoneinfo import ZoneInfo

import config as C
import engine as E
from simulate import simulate

NY = ZoneInfo("America/New_York")

COLUMNS = [
    "key", "source", "session", "ticker", "asset_type", "side", "first_seen", "suggested", "rank", "qualified",
    "filter_reason", "config_version", "score", "pts_sweep", "pts_mss", "pts_zone", "pts_ote", "pts_rr", "pts_bias",
    "pts_vol", "pts_time", "pts_prox", "swept", "prior_day_sweep", "ote_overlap", "in_zone", "bias_aligned",
    "htf_bias", "disp_vol", "rr1", "rr2", "price", "entry", "stop", "t1", "t2", "fvg_lo", "fvg_hi", "ce",
    "extreme", "atr", "snap_min", "freeze_ts", "evaluated", "outcome", "triggered", "trigger_time", "fill",
    "exit_time", "r_plan", "r_plan_net", "r_t1", "r_t2", "mfe", "mae", "mins_to_trigger", "mins_in_trade",
]
VARIANTS = [(e, b) for e in C.TESTS["entries"] for b in C.TESTS["stop_buffers"]]
for _e, _b in VARIANTS:
    COLUMNS += [f"trig_{_e}_{_b}", f"r_{_e}_{_b}"]


def r3(v):
    return None if v is None else round(float(v), 4)


def snapshot(s: dict, source: str, freeze_ts: float, suggested: bool, rank, cfg: dict) -> dict:
    p = s["pts"]
    return {
        "key": s["key"], "source": source, "session": s["session"], "ticker": s["ticker"],
        "asset_type": E.asset_type(s["ticker"]), "side": s["side"],
        "first_seen": dt.datetime.fromtimestamp(freeze_ts, NY).strftime("%Y-%m-%d %H:%M"),
        "suggested": suggested, "rank": rank or "", "qualified": s["qualified"],
        "filter_reason": "; ".join(s["filter_reasons"]), "config_version": cfg["version"], "score": s["score"],
        **{f"pts_{k}": r3(p[k]) for k in ("sweep", "mss", "zone", "ote", "rr", "bias", "vol", "time", "prox")},
        "swept": "/".join(s["swept"]), "prior_day_sweep": ("PDL" if s["side"] == "LONG" else "PDH") in s["swept"],
        "ote_overlap": s["overlap"], "in_zone": s["in_zone"], "bias_aligned": s["bias_aligned"], "htf_bias": s["bias"],
        "disp_vol": r3(s["rvol"]), "rr1": r3(s["rr1"]), "rr2": r3(s["rr2"]), "price": r3(s["price"]),
        "entry": r3(s["entry"]), "stop": r3(s["stop"]), "t1": r3(s["t1"]), "t2": r3(s["t2"]),
        "fvg_lo": r3(s["fvg_lo"]), "fvg_hi": r3(s["fvg_hi"]), "ce": r3(s["ce"]), "extreme": r3(s["extreme"]),
        "atr": r3(s["atr"]), "snap_min": s["snap_min"], "freeze_ts": int(freeze_ts), "evaluated": False,
    }


def variant_levels(row: dict, entry_kind: str, buf: float) -> dict:
    long = row["side"] == "LONG"
    entry = {"ote_mid": row["entry"], "fvg_edge": row["fvg_hi"] if long else row["fvg_lo"], "fvg_ce": row["ce"]}[entry_kind]
    stop = row["extreme"] - buf * row["atr"] if long else row["extreme"] + buf * row["atr"]
    return {"side": row["side"], "entry": entry, "stop": stop, "t1": row["t1"], "t2": row["t2"], "snap_min": row["snap_min"]}


def evaluate(row: dict, bars_after: list) -> dict:
    o = simulate({k: row[k] for k in ("side", "entry", "stop", "t1", "t2", "snap_min")}, bars_after)
    row.update(evaluated=True, outcome=o["outcome"], triggered=o["triggered"], trigger_time=E.hm(o["trigger_min"]),
               fill=r3(o["fill"]), exit_time=E.hm(o["exit_min"]), r_plan=r3(o["r_plan"]), r_plan_net=r3(o["r_plan_net"]),
               r_t1=r3(o["r_t1"]), r_t2=r3(o["r_t2"]), mfe=r3(o["mfe"]), mae=r3(o["mae"]),
               mins_to_trigger=o["mins_to_trigger"], mins_in_trade=o["mins_in_trade"])
    for e, b in VARIANTS:
        v = simulate(variant_levels(row, e, b), bars_after)
        row[f"trig_{e}_{b}"], row[f"r_{e}_{b}"] = v["triggered"], r3(v["r_plan_net"])
    return row


def prepare(s: dict, ticker: str, session: str, price: float, bias: str, now_min: int, cfg: dict) -> dict:
    E.apply_live(s, price)
    s.update(ticker=ticker, session=session, price=price, bias=bias, snap_min=now_min)
    E.score(s, price, bias, now_min, cfg)
    E.qualify(s, cfg)
    s["key"] = E.setup_key(session, ticker, s)
    return s


def replay_ticker(ticker: str, bars: list, closes_by_date: list, source: str, cfg: dict,
                  only_dates: set | None = None) -> list[dict]:
    """bars: all intraday bars (incl. extended hours); closes_by_date: [(date, close)] daily."""
    fut, cutoff, step_len = E.is_future(ticker), C.SIM["entry_cutoff"], C.SIM["replay_step"]
    dates = E.rth_dates(bars)
    out = []
    by_date = {}
    for b in bars:
        by_date.setdefault(b.date, []).append(b)
    for di in range(1, len(dates)):
        today, prev = dates[di], dates[di - 1]
        if only_dates and today not in only_dates:
            continue
        # levels need the prior day and (futures) the overnight session in between
        window = [b for d in sorted(by_date) if prev <= d <= today for b in by_date[d]]
        lv = E.levels_for(window, today, prev, fut)
        rth = [b for b in by_date[today] if E.is_rth(b)]
        bias = E.htf_bias([c for d, c in closes_by_date if d < today])
        snaps, k = {}, 0
        for step in range(C.OR_END, cutoff + 1, step_len):
            while k < len(rth) and rth[k].min < step:
                k += 1
            if k < 6:
                continue
            closed = rth[:k]
            price = closed[-1].c
            for s in E.find_setups(closed, lv):
                prepare(s, ticker, today, price, bias, step, cfg)
                finished = s["status"] in ("Invalidated", "Target hit")
                known = snaps.get(s["key"])
                ts = closed[-1].ts + 300
                if known is None:
                    if not finished:
                        snaps[s["key"]] = snapshot(s, source, ts, s["qualified"], "", cfg)
                elif s["qualified"] and not known["suggested"] and not finished:
                    snaps[s["key"]] = snapshot(s, source, ts, True, "", cfg)
        for row in snaps.values():
            out.append(evaluate(row, [b for b in rth if b.min >= row["snap_min"]]))
    return out
