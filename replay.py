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
    "exit_time", "session_name", "snap_time", "base_qualified", "g_bias", "g_sweep", "g_rr", "g_risk", "g_time", "g_etf", "r_plan", "r_plan_net", "r_t1", "r_t2", "mfe", "mae", "mins_to_trigger", "mins_in_trade",
]
VARIANTS = [(e, b) for e in C.TESTS["entries"] for b in C.TESTS["stop_buffers"]]
LADDERS = C.TESTS.get("ladders", {})
COLUMNS.insert(COLUMNS.index("extreme"), "ote_62")
for _e, _b in VARIANTS:
    COLUMNS += [f"trig_{_e}_{_b}", f"r_{_e}_{_b}"]
for _l in LADDERS:
    COLUMNS += [f"trig_{_l}", f"r_{_l}", f"filled_{_l}"]


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
        "fvg_lo": r3(s["fvg_lo"]), "fvg_hi": r3(s["fvg_hi"]), "ce": r3(s["ce"]), "ote_62": r3(s["ote_a"]),
        "extreme": r3(s["extreme"]),
        "atr": r3(s["atr"]), "snap_min": s["snap_min"], "base_qualified": s.get("base_qualified", s["qualified"]),
        **{f"g_{k}": s.get("guards", {}).get(k, "") for k in ("bias", "sweep", "rr", "risk", "time", "etf")}, "freeze_ts": int(freeze_ts), "evaluated": False,
    }


def entry_price(row: dict, kind: str) -> float:
    long = row["side"] == "LONG"
    edge = row["fvg_hi"] if long else row["fvg_lo"]
    return {"ote_mid": row["entry"], "fvg_edge": edge, "fvg_ce": row["ce"], "blend": (edge + row["entry"]) / 2,
            "ote_62": row.get("ote_62")}[kind]


def variant_levels(row: dict, entry_kind: str, buf: float) -> dict:
    long = row["side"] == "LONG"
    entry = entry_price(row, entry_kind)
    stop = row["extreme"] - buf * row["atr"] if long else row["extreme"] + buf * row["atr"]
    return {"side": row["side"], "entry": entry, "stop": stop, "t1": row["t1"], "t2": row["t2"], "snap_min": row["snap_min"]}


def evaluate(row: dict, bars_after: list, sim: dict = C.SIM) -> dict:
    sim = {**sim, **C.SIDE_MGMT.get(row["side"], {})}   # shorts: closer management
    o = simulate({k: row[k] for k in ("side", "entry", "stop", "t1", "t2", "snap_min")}, bars_after, sim)
    row.update(evaluated=True, outcome=o["outcome"], triggered=o["triggered"], trigger_time=_clock(row, o["trigger_min"]),
               fill=r3(o["fill"]), exit_time=_clock(row, o["exit_min"]), r_plan=r3(o["r_plan"]), r_plan_net=r3(o["r_plan_net"]),
               r_t1=r3(o["r_t1"]), r_t2=r3(o["r_t2"]), mfe=r3(o["mfe"]), mae=r3(o["mae"]),
               mins_to_trigger=o["mins_to_trigger"], mins_in_trade=o["mins_in_trade"])
    for e, b in VARIANTS:
        lv = variant_levels(row, e, b)
        if lv["entry"] is None or not ((lv["entry"] > lv["stop"]) if row["side"] == "LONG" else (lv["entry"] < lv["stop"])):
            row[f"trig_{e}_{b}"], row[f"r_{e}_{b}"] = False, None
            continue
        v = simulate(lv, bars_after, sim)
        row[f"trig_{e}_{b}"], row[f"r_{e}_{b}"] = v["triggered"], r3(v["r_plan_net"])
    for name, legs in LADDERS.items():
        row[f"trig_{name}"], row[f"r_{name}"], row[f"filled_{name}"] = ladder(row, legs, bars_after, sim)
    return row


def _clock(row: dict, m):
    """Wall-clock New York time for a session minute (overnight sessions use a shifted clock)."""
    if m is None:
        return ""
    return E.hm((int(m) - C.RTH_OPEN + row.get("_start_min", C.RTH_OPEN)) % 1440)


def ladder(row: dict, legs: list, bars_after: list, sim: dict = C.SIM):
    """Scaled entries: each leg is its own limit order (same stop and targets). The result is
    the combined P&L divided by the risk of the FULL planned position, so a ladder that only
    fills its shallow leg shows a small result, as it would in the account."""
    planned, pnl, filled = 0.0, 0.0, 0.0
    for kind, w in legs:
        lv = variant_levels(row, kind, C.STOP_ATR_BUFFER)
        risk = abs(lv["entry"] - lv["stop"]) if lv["entry"] is not None else 0
        if not risk:
            continue
        planned += w * risk
        v = simulate(lv, bars_after, sim)
        if v["triggered"]:
            pnl += w * v["r_plan_net"] * risk
            filled += w
    if not planned:
        return False, None, 0
    return filled > 0, r3(pnl / planned), round(filled, 3)


def prepare(s: dict, ticker: str, session: str, price: float, bias: str, now_min: int, cfg: dict) -> dict:
    E.apply_live(s, price)
    s.update(ticker=ticker, session=session, price=price, bias=bias, snap_min=now_min)
    E.score(s, price, bias, now_min, cfg)
    E.qualify(s, cfg)
    s["key"] = E.setup_key(session, ticker, s)
    return s


def replay_session(ticker: str, rth: list, lv: dict, bias: str, today: str, source: str, cfg: dict,
                   sim: dict = C.SIM, name: str = "NY", start_min: int = C.RTH_OPEN) -> list[dict]:
    """Walks one session's bars every SIM["replay_step"] minutes (from 30 minutes after the open
    to the entry cutoff), freezes each setup as the live scanner would have, and backtests it.
    Overnight futures sessions use a shifted clock in which their open maps to 9:30."""
    snaps, k = {}, 0
    for step in range(C.OR_END, sim["entry_cutoff"] + 1, sim["replay_step"]):
        while k < len(rth) and rth[k].min < step:
            k += 1
        if k < 6:
            continue
        closed = rth[:k]
        price = closed[-1].c
        for s in E.find_setups(closed, lv):
            s["session_name"] = name
            prepare(s, ticker, today, price, bias, step, cfg)
            if name != "NY":
                s["key"] = f"{today}|{ticker}|{s['side']}|{name}{E.hhmm(s['sweep_min'])}"
            finished = s["status"] in ("Invalidated", "Target hit")
            known = snaps.get(s["key"])
            ts = closed[-1].ts + 300
            if known is None:
                if not finished:
                    snaps[s["key"]] = snapshot(s, source, ts, s["qualified"], "", cfg)
            elif s["qualified"] and not known["suggested"] and not finished:
                snaps[s["key"]] = snapshot(s, source, ts, True, "", cfg)
    out = []
    for row in snaps.values():
        row["session_name"], row["_start_min"] = name, start_min
        row["snap_time"] = _clock(row, row["snap_min"])
        evaluate(row, [b for b in rth if b.min >= row["snap_min"]], sim)
        row.pop("_start_min")
        out.append(row)
    return out


def replay_ticker(ticker: str, bars: list, closes_by_date: list, source: str, cfg: dict,
                  only_dates: set | None = None) -> list[dict]:
    """New York session (9:30-4:00 ET) for every symbol; for futures, also the overnight
    Asia and London sessions when SESSIONS_24H is on. bars: all intraday bars incl. extended
    hours; closes_by_date: [(date, close)] daily."""
    fut = E.is_future(ticker)
    dates = E.rth_dates(bars)
    by_date = {}
    for b in bars:
        by_date.setdefault(b.date, []).append(b)
    out = []
    for di in range(1, len(dates)):
        today, prev = dates[di], dates[di - 1]
        if only_dates and today not in only_dates:
            continue
        window = [b for d in sorted(by_date) if prev <= d <= today for b in by_date[d]]
        lv = E.levels_for(window, today, prev, fut)
        rth = [b for b in by_date[today] if E.is_rth(b)]
        bias = E.htf_bias([c for d, c in closes_by_date if d < today])
        out += replay_session(ticker, rth, lv, bias, today, source, cfg)
        if fut and C.SESSIONS_24H:
            out += replay_overnight(ticker, window, today, prev, bias, source, cfg)
    return out


def _ny_ts(date: str, minute: int, day_shift: int = 0) -> int:
    d = dt.date.fromisoformat(date) + dt.timedelta(days=day_shift)
    return int(dt.datetime(d.year, d.month, d.day, minute // 60, minute % 60, tzinfo=NY).timestamp())


def replay_overnight(ticker: str, bars: list, today: str, prev: str, bias: str, source: str, cfg: dict) -> list[dict]:
    """Futures 24-hour test: the Asia (6 PM-midnight ET, the evening before) and London
    (2-8 AM ET) sessions of trading day `today`, each replayed like the New York session.
    Liquidity levels per session:
      Asia   - PDH/PDL: prior 9:30-4:00 day; PMH/PML: the whole prior trading day (6 PM-5 PM);
               ORH/ORL: the first 30 minutes of Asia
      London - PDH/PDL: prior 9:30-4:00 day; PMH/PML: the Asia session; ORH/ORL: the first 30 minutes of London
    """
    prev_rth = [b for b in bars if b.date == prev and E.is_rth(b)]
    pd_h = max((b.h for b in prev_rth), default=None)
    pd_l = min((b.l for b in prev_rth), default=None)
    out, asia_bars = [], []
    for name, (start, length) in C.FUTURES_SESSIONS.items():
        shift = -1 if start >= 18 * 60 else 0
        t0 = _ny_ts(today, start, shift)
        t1 = t0 + length * 60
        ses = [b for b in bars if t0 <= b.ts < t1]
        if len(ses) < 12:
            continue
        # shifted clock: the session open maps to 9:30 so the standard timing rules apply
        sb = [b._replace(date=today, min=C.RTH_OPEN + (b.ts - t0) // 60) for b in ses]
        orng = [b for b in sb if b.min < C.OR_END]
        if name == "Asia":
            prior = [b for b in bars if _ny_ts(prev, 18 * 60, -1) <= b.ts < _ny_ts(prev, 17 * 60)]
            asia_bars = sb
        else:
            prior = asia_bars
        lv = {"PDH": pd_h, "PDL": pd_l, "PMH": max((b.h for b in prior), default=None),
              "PML": min((b.l for b in prior), default=None), "ORH": max((b.h for b in orng), default=None),
              "ORL": min((b.l for b in orng), default=None)}
        end = C.RTH_OPEN + length
        sim = {**C.SIM, "entry_cutoff": end - 30, "eod_exit": end - 5}
        out += replay_session(ticker, sb, lv, bias, today, source, cfg, sim, name, start)
    return out
