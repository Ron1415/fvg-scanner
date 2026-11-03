#!/usr/bin/env python3
"""FVG opening-range scanner, trainer and backtester.

Usage
  python scanner.py --auto            # scheduler: live scan 9:25-4:05 ET; end-of-day job after 4:15 PM ET
  python scanner.py --live            # one live scan now
  python scanner.py --eod             # evaluate today's live snapshots, replay today, review (+ Friday auto-tune)
  python scanner.py --backtest 125    # replay the last 125 trading days (~6 months) and review
  python scanner.py --review          # rebuild the review and pages only
"""
from __future__ import annotations

import argparse
import datetime as dt
import gzip
import json
import logging
import os
import sys
from concurrent.futures import ProcessPoolExecutor
from pathlib import Path
from zoneinfo import ZoneInfo

import pandas as pd

import config as C
import data as D
import engine as E
import learn as L
import report
from replay import COLUMNS, entry_price, evaluate, prepare, replay_ticker, snapshot

NY = ZoneInfo("America/New_York")
ROOT = Path(__file__).resolve().parent
log = logging.getLogger("scanner")


def now_ny() -> dt.datetime:
    return dt.datetime.now(NY)


# ----------------------------------------------------------------- universe
def universe(force: bool = False) -> dict:
    """Ranks candidates by 20-day average dollar volume (futures: notional) once per day.
    Saved to universe.json with each symbol's higher-timeframe bias and daily closes."""
    path, today = ROOT / "universe.json", now_ny().strftime("%Y-%m-%d")
    if path.exists() and not force:
        u = json.loads(path.read_text())
        if u.get("date") == today:
            return u
    cands = C.ETF_CANDIDATES + C.STOCK_CANDIDATES + (list(C.FUTURES) if C.INCLUDE_FUTURES else [])
    daily = D.yahoo_daily(cands, "1y")
    stats = []
    for t, df in daily.items():
        df = df[df.index < today]
        df = df[df["Volume"] > 0] if E.is_future(t) else df
        if len(df) < 26:
            continue
        last = df.tail(20)
        price = float(last["Close"].iloc[-1])
        dv = float((last["Close"] * last["Volume"]).mean()) * E.mult_of(t)
        stats.append({"t": t, "type": E.asset_type(t), "dv_m": round(dv / 1e6, 1), "price": round(price, 2),
                      "bias": E.htf_bias(df["Close"].tolist()),
                      "closes": [[d, round(float(c), 4)] for d, c in df["Close"].tail(260).items()]})
    stocks = sorted([s for s in stats if s["type"] != "Future" and s["price"] >= C.MIN_PRICE], key=lambda s: -s["dv_m"])[:C.UNIVERSE_SIZE]
    futs = sorted([s for s in stats if s["type"] == "Future"], key=lambda s: -s["dv_m"])[:C.FUTURES_SIZE]
    rows = stocks + futs
    if not rows:
        raise SystemExit("No daily data from Yahoo; try again later.")
    u = {"date": today, "tickers": [r["t"] for r in rows],
         "rows": [{k: r[k] for k in ("t", "type", "dv_m", "price", "bias")} for r in rows],
         "closes": {r["t"]: r["closes"] for r in rows}}
    path.write_text(json.dumps(u))
    return u


# ----------------------------------------------------------------- live scan
def live_scan() -> None:
    now, cfg = now_ny(), E.settings()
    u = universe()
    held = [t["ticker"] for t in L.load_trades() if t.get("exit_price") is None]
    tickers = list(dict.fromkeys(u["tickers"] + held))
    bars_by = D.yahoo_intraday(tickers, "5d", "5m")
    bias = {r["t"]: r["bias"] for r in u["rows"]}
    detected, prices, charts = [], {}, {}
    for t, bars in bars_by.items():
        prices[t] = bars[-1].c
        dates = E.rth_dates(bars)
        if len(dates) < 2:
            continue
        today, prev = dates[-1], dates[-2]
        lv = E.levels_for(bars, today, prev, E.is_future(t))
        rth = [b for b in bars if b.date == today and E.is_rth(b)]
        live = today == now.strftime("%Y-%m-%d") and now.hour * 60 + now.minute < C.RTH_CLOSE
        closed = rth[:-1] if live and len(rth) > 1 else rth
        for s in E.find_setups(closed, lv):
            prepare(s, t, today, bars[-1].c, bias.get(t, "Neutral"), now.hour * 60 + now.minute, cfg)
            s["levels"], s["asset"], s["mult"] = lv, E.asset_type(t), E.mult_of(t)
            row = {"side": s["side"], "fvg_hi": s["fvg_hi"], "fvg_lo": s["fvg_lo"], "entry": s["entry"], "ce": s["ce"], "ote_62": s["ote_a"]}
            s["ladder"] = [{"kind": k, "price": round(entry_price(row, k), 4), "weight": w}
                           for k, w in C.TESTS["ladders"][C.DASHBOARD_LADDER]]
            charts[s["key"]] = [[round(b.o, 4), round(b.h, 4), round(b.l, 4), round(b.c, 4), b.min] for b in closed]
            detected.append(s)
    active = [s for s in detected if s["status"] not in ("Invalidated", "Target hit")]
    best = {}
    for s in active:
        if s["qualified"] and (s["ticker"] not in best or s["score"] > best[s["ticker"]]["score"]):
            best[s["ticker"]] = s
    ranked = sorted(best.values(), key=lambda s: (-s["score"], s["dist_pct"]))
    top = ranked[:C.TOP_N]
    record_live(detected, [s["key"] for s in top], cfg)
    keep = ["key", "ticker", "side", "status", "score", "notes", "price", "entry", "stop", "t1", "t2", "rr1", "rr2",
            "fvg_lo", "fvg_hi", "ce", "eq", "ote_a", "ote_mid", "ote_b", "ote_lo", "ote_hi", "extreme", "swing", "mss",
            "proximity", "dist_pct", "bias", "overlap", "swept", "rvol", "levels", "session", "sweep_idx", "fvg_idx",
            "asset", "mult", "pts", "filter_reasons", "ladder"]
    state = {"updated": now.strftime("%a %b %d, %Y %I:%M %p ET"), "updated_iso": now.isoformat(),
             "scanned": len(bars_by), "total": len(ranked), "filtered": len(active) - len(ranked),
             "top": [{**{k: s.get(k) for k in keep}, "bars": charts[s["key"]]} for s in top],
             "prices": {t: round(p, 4) for t, p in prices.items()}, "universe": u["rows"],
             "mults": {t: E.mult_of(t) for t in prices}, "config_version": cfg["version"],
             "sizing": {**C.SIZING, "ladder": C.DASHBOARD_LADDER}}
    out = ROOT / "site" / "data"
    out.mkdir(parents=True, exist_ok=True)
    (out / "state.json").write_text(json.dumps(state, default=float))
    log.info("Live scan: %d symbols, %d qualifying, top: %s", len(bars_by), len(ranked),
             ", ".join(f"{s['ticker']} {s['side']} {s['score']}" for s in top) or "none")


def record_live(detected: list, top_keys: list, cfg: dict) -> None:
    """Freeze each live setup the first time it is seen; re-freeze once when it first enters the top list."""
    if not detected:
        return
    path = L.month_file("live", detected[0]["session"])
    old = pd.read_csv(path, dtype={"rank": str}) if path.exists() else pd.DataFrame(columns=COLUMNS)
    known = dict(zip(old["key"], L.as_bool(old["suggested"]))) if len(old) else {}
    rows, ts = [], now_ny().timestamp()
    for s in detected:
        rank = top_keys.index(s["key"]) + 1 if s["key"] in top_keys else None
        finished = s["status"] in ("Invalidated", "Target hit")
        if s["key"] not in known:
            if not finished:
                rows.append(snapshot(s, "Live", ts, rank is not None, rank, cfg))
        elif rank and not known[s["key"]]:
            rows.append(snapshot(s, "Live", ts, True, rank, cfg))
    L.append_rows(path, rows)


# ----------------------------------------------------------------- end of day
def end_of_day(force: bool = False) -> None:
    now, cfg = now_ny(), E.settings()
    today = now.strftime("%Y-%m-%d")
    marker = ROOT / "history" / "eod_done.txt"
    if not force and marker.exists() and marker.read_text().strip() == today:
        log.info("End-of-day job already done for %s", today)
        return
    u = universe()
    # 1. live snapshots: backtest on 1-minute bars
    lp = L.month_file("live", today)
    if lp.exists():
        df = pd.read_csv(lp, dtype={"rank": str})
        pend = df[~L.as_bool(df["evaluated"])]
        if len(pend):
            m1 = D.yahoo_intraday(sorted(pend["ticker"].unique()), "5d", "1m")
            rows = []
            for _, r in pend.iterrows():
                row = r.to_dict()
                bars = [b for b in m1.get(row["ticker"], []) if b.date == row["session"] and E.is_rth(b) and b.ts >= row["freeze_ts"]]
                if row["session"] < today or now.hour * 60 + now.minute >= C.RTH_CLOSE:
                    rows.append(evaluate(row, bars))
            L.append_rows(lp, rows)
    # 2. full-session replay of today for every symbol (training mode)
    if C.TRAINING_MODE:
        bars_by = D.yahoo_intraday(u["tickers"], "5d", "5m")
        rows = []
        for t, bars in bars_by.items():
            rows += replay_ticker(t, bars, [tuple(x) for x in u["closes"].get(t, [])], "Replay", cfg, {today})
        L.append_rows(L.month_file("replay", today), rows)
        log.info("Replay %s: %d setups from %d symbols", today, len(rows), len(bars_by))
    changes = L.autotune() if now.weekday() == 4 else []
    L.review("Weekly" if now.weekday() == 4 else "Daily", changes)
    marker.parent.mkdir(exist_ok=True)
    marker.write_text(today)


# ----------------------------------------------------------------- backtest
def _bt_worker(args):
    t, bars, closes, cfg, dates = args
    return replay_ticker(t, bars, closes, "Backtest", cfg, dates)


def backtest(days: int) -> None:
    cfg, u = E.settings(), universe()
    spy = D.yahoo_daily(["SPY"], "2y")["SPY"]
    today = now_ny().strftime("%Y-%m-%d")
    sessions = [d for d in spy.index if d < today or now_ny().hour * 60 + now_ny().minute >= C.RTH_CLOSE + 15]
    sessions = sessions[-days:]
    start = dt.date.fromisoformat(sessions[0]) - dt.timedelta(days=5)
    end = dt.date.fromisoformat(sessions[-1])
    daily = D.yahoo_daily(u["tickers"], "2y")
    closes = {t: list(zip(df.index, df["Close"].astype(float))) for t, df in daily.items()}
    use_alpaca = D.alpaca_enabled()
    yahoo_set = [t for t in u["tickers"] if E.is_future(t) or not use_alpaca]
    y60 = D.yahoo_intraday(yahoo_set, "60d", "5m") if yahoo_set else {}
    jobs, coverage = [], {}
    for t in u["tickers"]:
        bars = y60.get(t, []) if t in y60 or t in yahoo_set else D.alpaca_5m(t, start, end)
        if not bars:
            continue
        have = sorted({b.date for b in bars})
        coverage[t] = [have[0], have[-1]]
        jobs.append((t, bars, closes.get(t, []), cfg, set(sessions)))
    rows = []
    with ProcessPoolExecutor(max_workers=os.cpu_count() or 2) as ex:
        for r in ex.map(_bt_worker, jobs, chunksize=1):
            rows += r
    out = ROOT / "backtest"
    out.mkdir(exist_ok=True)
    df = pd.DataFrame(rows).reindex(columns=COLUMNS)
    with gzip.open(out / "backtest.csv.gz", "wt") as f:
        df.to_csv(f, index=False)
    meta = {"run_at": now_ny().strftime("%Y-%m-%d %H:%M ET"), "days_requested": days,
            "sessions": [sessions[0], sessions[-1]], "symbols": len(jobs), "setups": len(df),
            "stock_source": "Alpaca (SIP)" if use_alpaca else "Yahoo (about 60 days only)",
            "futures_source": "Yahoo (about 60 days only)", "coverage": coverage, "config_version": cfg["version"]}
    (out / "meta.json").write_text(json.dumps(meta, indent=1))
    log.info("Backtest: %d setups, %d symbols, %s to %s (%s)", len(df), len(jobs), sessions[0], sessions[-1], meta["stock_source"])
    L.review("Backtest")


# ----------------------------------------------------------------- main
def main() -> None:
    logging.basicConfig(level=logging.INFO, format="%(asctime)s %(levelname)s %(message)s")
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--auto", action="store_true")
    ap.add_argument("--live", action="store_true")
    ap.add_argument("--eod", action="store_true")
    ap.add_argument("--backtest", type=int, metavar="DAYS")
    ap.add_argument("--review", action="store_true")
    a = ap.parse_args()
    now = now_ny()
    mins = now.hour * 60 + now.minute
    if a.backtest:
        backtest(a.backtest)
    elif a.eod:
        end_of_day(force=True)
    elif a.live:
        live_scan()
    elif a.review:
        L.review("Manual")
    elif a.auto:
        if now.weekday() >= 5:
            log.info("Weekend; nothing to do.")
        elif C.LIVE_WINDOW[0] <= mins <= C.LIVE_WINDOW[1]:
            live_scan()
        elif mins >= C.EOD_AFTER:
            end_of_day()
        else:
            log.info("Outside the scan window (%s ET).", now.strftime("%H:%M"))
    else:
        ap.print_help()
        sys.exit(0)
    report.write_pages()


if __name__ == "__main__":
    try:
        main()
    except SystemExit:
        raise
    except Exception:
        import traceback
        tb = traceback.format_exc()
        print(tb, file=sys.stderr)
        # Show the error on the run's summary page (GitHub annotation), not only in the log
        last = tb.strip().splitlines()
        msg = "%0A".join(last[-12:]).replace("::", ": :")
        print(f"::error title=FVG scanner error::{msg}")
        sys.exit(1)
