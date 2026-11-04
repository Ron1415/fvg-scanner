"""Review statistics and the weekly auto-tune.

Sources:
  Live      - dashboard snapshots (validation only)
  Replay    - daily full-session replay after each close     } "systematic":
  Backtest  - 6-month (or 60-day) replay from backtest mode  } drives learning
Headline results are NET of SIM["cost_pct_per_side"] (slippage + fees).
"""
from __future__ import annotations

import datetime as dt
import json
from pathlib import Path
from zoneinfo import ZoneInfo

import numpy as np
import pandas as pd

import config as C
import engine as E
from replay import COLUMNS, LADDERS, VARIANTS

NY = ZoneInfo("America/New_York")
ROOT = Path(__file__).resolve().parent
SYSTEMATIC = ("Replay", "Backtest")


# ----------------------------------------------------------------- storage
def month_file(kind: str, session: str) -> Path:
    return ROOT / "history" / f"{kind}_{session[:7]}.csv"


def append_rows(path: Path, rows: list[dict], replace_keys: bool = True) -> None:
    if not rows:
        return
    path.parent.mkdir(exist_ok=True)
    new = pd.DataFrame(rows).reindex(columns=COLUMNS)
    if path.exists():
        old = pd.read_csv(path, dtype={"rank": str})
        if replace_keys:
            old = old[~old["key"].isin(new["key"])]
        new = pd.concat([old, new], ignore_index=True)
    new.to_csv(path, index=False)


TRUE = {"true", "1", "1.0", "yes"}


def as_bool(col: pd.Series) -> pd.Series:
    return col.astype(str).str.strip().str.lower().isin(TRUE)


def load_all() -> pd.DataFrame:
    frames = []
    files = sorted((ROOT / "history").glob("*.csv")) + sorted(ROOT.glob("sheets_import_*.csv"))   # root copy if uploaded flat
    for p in files:
        frames.append(pd.read_csv(p, dtype={"rank": str}))
    bt = ROOT / "backtest" / "backtest.csv.gz"
    if bt.exists():
        frames.append(pd.read_csv(bt, dtype={"rank": str}))
    if not frames:
        return pd.DataFrame(columns=COLUMNS)
    df = pd.concat(frames, ignore_index=True)
    for c in ("suggested", "qualified", "triggered", "evaluated", "ote_overlap", "in_zone", "bias_aligned", "prior_day_sweep"):
        df[c] = as_bool(df[c])
    for c in ("r_plan", "r_plan_net", "r_t1", "r_t2", "score", "rr1", "rr2", "snap_min", "disp_vol", "mins_to_trigger",
              "entry", "stop", "pts_time"):
        df[c] = pd.to_numeric(df[c], errors="coerce")
    if "asset_type" in df:
        df["asset_type"] = df["asset_type"].fillna(df["ticker"].map(E.asset_type))
    return df


# ----------------------------------------------------------------- metrics
def metrics(d: pd.DataFrame, rcol="r_plan_net", tcol="triggered") -> dict:
    n = len(d)
    t = d[d[tcol]] if n else d
    rs = t[rcol].fillna(0).to_numpy(float) if len(t) else np.array([])
    wins, losses = rs[rs > 0], rs[rs < 0]
    eq = np.cumsum(rs) if len(rs) else np.array([0.0])
    dd = float((eq - np.maximum.accumulate(np.maximum(eq, 0))).min()) if len(rs) else 0.0
    half = len(rs) // 2
    return {"n": n, "trig": int(len(rs)), "trig_rate": len(rs) / n if n else None,
            "win": float((rs > 0).mean()) if len(rs) else None, "avg_r": float(rs.mean()) if len(rs) else None,
            "exp": float(rs.sum() / n) if n else None,
            "pf": float(wins.sum() / -losses.sum()) if losses.sum() < 0 else None, "total": float(rs.sum()),
            "dd": dd, "h1": float(rs[:half].mean()) if half else None, "h2": float(rs[half:].mean()) if len(rs) - half else None}


HEAD = ["Group", "Setups", "Triggered", "Trigger rate", "Win rate", "Avg R", "Expectancy R", "Profit factor",
        "Total R", "Max DD R", "1st half avg R", "2nd half avg R"]


def _f(v, pct=False):
    if v is None or (isinstance(v, float) and np.isnan(v)):
        return ""
    return f"{v * 100:.1f}%" if pct else round(v, 2)


def mrow(label, m):
    return [label, m["n"], m["trig"], _f(m["trig_rate"], True), _f(m["win"], True), _f(m["avg_r"]), _f(m["exp"]),
            _f(m["pf"]), _f(m["total"]), _f(m["dd"]), _f(m["h1"]), _f(m["h2"])]


def prep(df: pd.DataFrame) -> pd.DataFrame:
    df = df[df["evaluated"]].copy()
    df["in_win"] = df["snap_min"] <= C.SIM["entry_cutoff"]
    df["plan_win"] = df["snap_min"] <= C.SIM["plan_window_end"]
    df["sys"] = df["source"].isin(SYSTEMATIC)
    if "session_name" not in df:
        df["session_name"] = "NY"
    df["session_name"] = df["session_name"].fillna("NY")
    # a session replayed both daily and by a later backtest is counted once (backtest copy kept)
    bt_keys = set(df.loc[df["source"] == "Backtest", "key"])
    df = df[~((df["source"] == "Replay") & df["key"].isin(bt_keys))]
    df["risk_pct"] = (df["entry"] - df["stop"]).abs() / df["entry"] * 100
    return df.sort_values(["session", "snap_min"])


FACTORS = [
    ("Prior-day level swept", "sweep_pd", lambda d: d["prior_day_sweep"]),
    ("Only PM/OR level swept", "sweep_other", lambda d: d["swept"].fillna("").ne("") & ~d["prior_day_sweep"]),
    ("FVG in discount/premium", "zone", lambda d: d["in_zone"]),
    ("FVG overlaps OTE", "ote", lambda d: d["ote_overlap"]),
    ("R:R to T1 of 2 or more", "rr", lambda d: d["rr1"] >= 2),
    ("HTF bias aligned", "bias", lambda d: d["bias_aligned"]),
    ("Displacement volume 1.5x+", "vol", lambda d: d["disp_vol"] >= 1.5),
    ("Formed 10:00-11:30", "time", lambda d: d["pts_time"] > 0),
]


def factor_stats(d: pd.DataFrame) -> list[dict]:
    t = d[d["sys"] & d["in_win"] & d["triggered"]]
    out = []
    for name, key, fn in FACTORS:
        m = fn(t).fillna(False).astype(bool)
        y, n_ = t[m]["r_plan_net"], t[~m]["r_plan_net"]
        out.append({"name": name, "key": key, "n_yes": len(y), "n_no": len(n_),
                    "avg_yes": float(y.mean()) if len(y) else None, "avg_no": float(n_.mean()) if len(n_) else None,
                    "delta": float(y.mean() - n_.mean()) if len(y) and len(n_) else None})
    return out


# ----------------------------------------------------------------- review
def review(kind="Manual", changes=None) -> dict:
    cfg, at = E.settings(), C.AUTO_TUNE
    df = prep(load_all())
    q = df[df["qualified"] & df["in_win"]]
    sysq = q[q["sys"]]
    tables = []

    def table(title, head, rows, note=""):
        tables.append({"title": title, "head": head, "rows": rows, "note": note})

    rows = [mrow("Live dashboard snapshots", metrics(q[q["source"] == "Live"])),
            mrow("Daily full-session replays", metrics(q[q["source"] == "Replay"])),
            mrow("Backtest", metrics(q[q["source"] == "Backtest"])),
            mrow("Systematic (replays + backtest)", metrics(sysq)),
            mrow("Systematic, before cost (gross)", metrics(sysq, "r_plan")),
            mrow(f"Systematic, plan window only (New York, formed by {E.hm(C.SIM['plan_window_end'])})", metrics(sysq[sysq["plan_win"] & (sysq["session_name"] == "NY")])),
            mrow("Live top-5 suggestions only", metrics(q[(q["source"] == "Live") & q["suggested"]]))]
    trades = load_trades()
    tr = [t["r"] for t in trades if t.get("r") is not None]
    rows.append(["Your actual trades", len(tr), len(tr), "", _f(float(np.mean([x > 0 for x in tr])) if tr else None, True),
                 _f(float(np.mean(tr)) if tr else None), "", "", _f(float(sum(tr))), "", "", ""])
    ny = sysq[sysq["session_name"] == "NY"]
    fut = sysq[sysq["asset_type"] == "Future"]
    rows += [mrow("Stocks and ETFs, New York session only", metrics(ny[ny["asset_type"] != "Future"])),
             mrow("Futures, New York session", metrics(fut[fut["session_name"] == "NY"])),
             mrow("Futures, all 24-hour sessions", metrics(fut))]
    table("1. Strategy performance (qualified setups; results net of costs)", HEAD, rows,
          f"Costs: {C.SIM['cost_pct_per_side']}% of price per side. Entries allowed until {E.hm(C.SIM['entry_cutoff'])} ET.")

    rows = [mrow(f"Futures, {n} session" + (" (6 PM-midnight ET)" if n == "Asia" else " (2-8 AM ET)" if n == "London" else " (9:30-4:00 ET)"),
                 metrics(fut[fut["session_name"] == n])) for n in ("Asia", "London", "NY")]
    for t in sorted(fut["ticker"].unique()):
        for n in ("Asia", "London", "NY"):
            rows.append(mrow(f"{t} {n}", metrics(fut[(fut["ticker"] == t) & (fut["session_name"] == n)])))
    table("1c. Futures by session (24-hour test; qualified, net of costs)", HEAD, rows,
          "Asia and London use their own levels: prior-day high/low, the previous session's high/low, and the session's first 30 minutes.")

    rows = [mrow(a, metrics(ny[ny["asset_type"] == a])) for a in ("ETF", "Stock", "Future")]
    rows.append(mrow("Leveraged/inverse ETFs", metrics(ny[ny["ticker"].isin(C.LEVERAGED_ETFS)])))
    rows += [mrow(s_, metrics(ny[ny["side"] == s_])) for s_ in ("LONG", "SHORT")]
    for lo, hi in [(600, 630), (630, 690), (690, 780), (780, 870), (870, 960)]:
        rows.append(mrow(f"Formed {E.hm(lo)}-{E.hm(hi)}", metrics(ny[(ny["snap_min"] >= lo) & (ny["snap_min"] < hi)])))
    for lo, hi in [(0, .15), (.15, .3), (.3, .6), (.6, 99)]:
        rows.append(mrow(f"Risk {lo}-{hi}% of price" if hi < 99 else f"Risk {lo}%+", metrics(sysq[(sysq["risk_pct"] >= lo) & (sysq["risk_pct"] < hi)])))
    table("2. New York session: by asset, side, time of day, risk size (systematic, qualified)", HEAD, rows)

    # short guardrails: all shorts that passed the normal filters, with and without each check
    w_all = df[df["in_win"] & df["sys"]]
    if "base_qualified" in w_all:
        bq = as_bool(w_all["base_qualified"]) | (w_all["base_qualified"].isna() & w_all["qualified"])
        shorts, longs = w_all[bq & (w_all["side"] == "SHORT")], w_all[bq & (w_all["side"] == "LONG")]
        rows = [mrow("Longs passing the normal filters", metrics(longs)),
                mrow("Shorts passing the normal filters (before guardrails)", metrics(shorts)),
                mrow("Shorts passing every guardrail (traded)", metrics(shorts[shorts["qualified"]]))]
        names = {"g_bias": "bearish daily trend", "g_sweep": "PDH or 2+ level sweep", "g_rr": f"R:R to T2 {C.SHORT_RULES['min_rr_t2']}+",
                 "g_risk": f"risk {C.SHORT_RULES['min_risk_pct']}%+ of price", "g_time": "formed 10:30 or later", "g_etf": "not a leveraged ETF"}
        for col, label in names.items():
            if col in shorts and shorts[col].notna().any():
                ok = as_bool(shorts[col])
                rows += [mrow(f"Shorts passing: {label}", metrics(shorts[ok])), mrow(f"Shorts failing: {label}", metrics(shorts[~ok]))]
        table("2b. Short guardrails (systematic; shorts use full exit at T1, breakeven at +0.5R, 60-minute time stop)", HEAD, rows,
              f"Sizing: longs {C.SIZING['LONG']['risk_pct']}% risk (cap {C.SIZING['LONG']['max_position_pct']}% of account), "
              f"shorts {C.SIZING['SHORT']['risk_pct']}% risk (cap {C.SIZING['SHORT']['max_position_pct']}%). Results here are in R, before sizing.")

    oc = sysq.groupby("outcome")["r_plan_net"].agg(["count", "mean"]).sort_values("count", ascending=False)
    table("3. Outcomes (systematic, qualified)", ["Outcome", "Count", "Share", "Avg R"],
          [[k, int(r["count"]), _f(r["count"] / max(len(sysq), 1), True), _f(r["mean"])] for k, r in oc.iterrows()])

    rows = [mrow(f"Score {lab}", metrics(sysq[(sysq["score"] >= lo) & (sysq["score"] < hi)]))
            for lab, lo, hi in [("90+", 90, 101), ("75-89", 75, 90), ("60-74", 60, 75), ("under 60", -1, 60)]]
    table("4. Score calibration. A useful score shows results improving band by band.", HEAD, rows)

    fs = factor_stats(df)
    rows = []
    for f in fs:
        enough = f["n_yes"] >= at["min_samples"] and f["n_no"] >= at["min_samples"]
        read = "Not enough data" if not enough else "Helps" if f["delta"] > at["delta_r"] else "Hurts" if f["delta"] < -at["delta_r"] else "No clear effect"
        rows.append([f["name"], f["key"], cfg["weights"][f["key"]], f["n_yes"], _f(f["avg_yes"]), f["n_no"], _f(f["avg_no"]), _f(f["delta"]), read])
    table("5. Factor attribution (all triggered systematic setups, qualified or not)",
          ["Factor", "Weight key", "Weight", "With", "Avg R with", "Without", "Avg R without", "Difference", "Read"], rows)

    w = df[df["in_win"] & df["sys"]]
    rows = [mrow("Passed filters", metrics(w[w["qualified"]])), mrow("Filtered out", metrics(w[~w["qualified"]])),
            mrow("No OTE overlap", metrics(w[~w["ote_overlap"]]))]
    for lo, hi in [(1.5, 2), (2, 2.5), (2.5, 3), (3, 99)]:
        rows.append(mrow(f"OTE overlap, R:R to T2 {lo}" + (f"-{hi}" if hi < 99 else "+"),
                         metrics(w[w["ote_overlap"] & (w["rr2"] >= lo) & (w["rr2"] < hi)])))
    table("6. Filter check (systematic)", HEAD, rows)

    # side-by-side tests: entry type x stop buffer, under several filters
    nyq = sysq["session_name"] == "NY"
    filt = {"All qualified": sysq, "Plan window (by 11:30)": sysq[nyq & sysq["plan_win"]],
            "Midday 11:30-14:30": sysq[nyq & (sysq["snap_min"] >= 690) & (sysq["snap_min"] < 870)],
            "Stocks only": sysq[sysq["asset_type"] == "Stock"], "R:R to T2 2.5+": sysq[sysq["rr2"] >= 2.5],
            "Risk 0.15%+": sysq[sysq["risk_pct"] >= 0.15]}
    combo = sysq[nyq & (sysq["snap_min"] >= 690) & (sysq["snap_min"] < 870) & (sysq["rr2"] >= 2.5) & (sysq["risk_pct"] >= 0.15)]
    filt["Midday + R:R 2.5+ + risk 0.15%+"] = combo
    rows = []
    tests = [(f"Entry {e}, stop {b} ATR", f"trig_{e}_{b}", f"r_{e}_{b}") for e, b in VARIANTS]
    tests += [(f"Scaled {n} ({', '.join(f'{k} {w:.0%}' for k, w in legs)})", f"trig_{n}", f"r_{n}") for n, legs in LADDERS.items()]
    for label, tc, rc in tests:
        for name, d in filt.items():
            if tc not in d or d[tc].isna().all():
                continue
            dd = d.copy(); dd[tc] = as_bool(dd[tc]); dd[rc] = pd.to_numeric(dd[rc], errors="coerce")
            rows.append(mrow(f"{label} · {name}", metrics(dd, rc, tc)))
    table("7. Improvement tests: entry type x stop buffer x filter (net of costs)", HEAD, rows,
          "ote_mid = current entry (middle of the FVG/OTE overlap); fvg_edge = first touch of the gap; fvg_ce = gap midpoint; "
          "blend = halfway between the gap edge and ote_mid; ote_62 = first touch of the OTE zone. Scaled rows are in R of the "
          "full planned position (a partial fill counts only what filled).")

    t = sysq[sysq["triggered"]]
    rows = []
    for lab, col in [("Plan: half at T1, rest to T2 (gross)", "r_plan"), ("Plan, net of costs", "r_plan_net"),
                     ("Full position to T1 (gross)", "r_t1"), ("Full position to T2 (gross)", "r_t2")]:
        v = pd.to_numeric(t[col], errors="coerce").fillna(0)
        rows.append([lab, len(v), _f(float(v.mean()) if len(v) else None), _f(float((v > 0).mean()) if len(v) else None, True)])
    table("8. Trade management (systematic, qualified, triggered)", ["Method", "Trades", "Avg R", "Win rate"], rows)

    # v3 candidate tests (Nov 3): filters x methods, New York session
    v3c = C.TESTS.get("v3")
    if v3c and "gap_atr" in sysq:
        x = sysq[sysq["session_name"] == "NY"].copy()
        for c in ("gap_atr", "open_rvol", "r_runner", "r_confirm", "r_t2"):
            x[c] = pd.to_numeric(x.get(c), errors="coerce")
        x["vwap_ok_b"] = as_bool(x["vwap_ok"]) if "vwap_ok" in x else False
        x["trig_confirm_b"] = as_bool(x["trig_confirm"]) if "trig_confirm" in x else False
        x["t2_net"] = x["r_t2"] - (x["r_plan"] - x["r_plan_net"])
        w0, w1 = v3c["window"]
        v3 = (x["snap_min"] >= w0) & (x["snap_min"] < w1) & (x["risk_pct"] >= v3c["min_risk_pct"]) & (x["gap_atr"] >= v3c["min_gap_atr"])
        inplay = x["open_rvol"] >= v3c["in_play_rvol"]
        filt = {"All (New York)": x.index == x.index, f"v3: {E.hm(w0)}-{E.hm(w1)} + risk {v3c['min_risk_pct']}%+ + FVG {v3c['min_gap_atr']}+ ATR": v3,
                "v3 + longs": v3 & (x["side"] == "LONG"), "v3 + VWAP side": v3 & x["vwap_ok_b"],
                f"v3 + in play (open volume {v3c['in_play_rvol']}x+)": v3 & inplay, "v3 + longs + VWAP side": v3 & (x["side"] == "LONG") & x["vwap_ok_b"],
                "VWAP side only": x["vwap_ok_b"], "In play only": inplay}
        methods = [("Current plan", "r_plan_net", "triggered"), ("Runner to the close", "r_runner", "triggered"),
                   ("Full position to T2", "t2_net", "triggered"), ("Confirmation entry", "r_confirm", "trig_confirm_b")]
        rows = []
        for fname, m in filt.items():
            for mname, rc, tc in methods:
                rows.append(mrow(f"{fname} · {mname}", metrics(x[m], rc, tc)))
        tf = x["confirm_tf"].value_counts().to_dict() if "confirm_tf" in x else {}
        table("10. v3 candidate tests (New York session, qualified, net of costs)", HEAD, rows,
              "Confirmation entry = wait for price to reach the FVG, then enter on the first bar that closes beyond the "
              f"prior 3 bars (bars used: {tf}). Runner = half at T1, rest to the close with a breakeven stop. "
              "1st/2nd half columns are the out-of-sample check.")

    ch = changes or []
    table("9. Automatic changes in this run", ["Key", "Old", "New", "Evidence"],
          [[c["key"], c["old"], c["new"], c["why"]] for c in ch] or [["None", "", "", ""]])

    out = {"generated": dt.datetime.now(NY).strftime("%Y-%m-%d %H:%M ET"), "kind": kind, "config_version": cfg["version"],
           "sessions": int(df["session"].nunique()) if len(df) else 0,
           "range": [str(df["session"].min()), str(df["session"].max())] if len(df) else [], "tables": tables}
    (ROOT / "site" / "data").mkdir(parents=True, exist_ok=True)
    (ROOT / "site" / "data" / "review.json").write_text(json.dumps(out, default=str))
    (ROOT / "review.md").write_text(to_markdown(out))
    log_path = ROOT / "review_log.csv"
    m = metrics(sysq)
    pd.DataFrame([{"run_at": out["generated"], "kind": kind, "systematic_setups": m["n"], "triggered": m["trig"],
                   "avg_r_net": _f(m["avg_r"]), "win_rate": _f(m["win"]), "changes": len(ch)}]).to_csv(
        log_path, mode="a", header=not log_path.exists(), index=False)
    return out


def to_markdown(rv: dict) -> str:
    lines = [f"# FVG review: {rv['generated']} ({rv['kind']})", "",
             f"Sessions: {rv['sessions']} ({' to '.join(rv['range'])}). Config version {rv['config_version']}.", ""]
    for t in rv["tables"]:
        lines += [f"## {t['title']}", ""]
        if t["note"]:
            lines += [t["note"], ""]
        lines += ["| " + " | ".join(map(str, t["head"])) + " |", "|" + "---|" * len(t["head"])]
        lines += ["| " + " | ".join("" if v is None else str(v) for v in r) + " |" for r in t["rows"]]
        lines.append("")
    return "\n".join(lines)


# ----------------------------------------------------------------- trades (from the dashboard)
def load_trades() -> list[dict]:
    p = ROOT / "trades.json"
    if not p.exists():
        return []
    try:
        trades = json.loads(p.read_text() or "[]")
    except json.JSONDecodeError:
        return []
    for t in trades:
        if t.get("exit_price") is not None and t.get("entry_price") and t.get("stop"):
            risk = abs(t["entry_price"] - t["stop"])
            mv = (t["exit_price"] - t["entry_price"]) if t["side"] == "LONG" else (t["entry_price"] - t["exit_price"])
            t["r"] = mv / risk if risk else None
    return trades


# ----------------------------------------------------------------- auto-tune
def autotune() -> list[dict]:
    at = C.AUTO_TUNE
    if not at["enabled"]:
        return []
    cfg = E.settings()
    df = prep(load_all())
    changes = []
    lo_w, hi_w = at["weight_bounds"]
    for f in factor_stats(df):
        if f["delta"] is None or f["n_yes"] < at["min_samples"] or f["n_no"] < at["min_samples"] or abs(f["delta"]) < at["delta_r"]:
            continue
        old = cfg["weights"][f["key"]]
        new = max(lo_w, min(hi_w, old + (at["weight_step"] if f["delta"] > 0 else -at["weight_step"])))
        if new != old:
            changes.append({"section": "weights", "key": f["key"], "old": old, "new": new, "strength": abs(f["delta"]),
                            "why": f"{f['name']}: {f['avg_yes']:.2f}R with (n={f['n_yes']}) vs {f['avg_no']:.2f}R without (n={f['n_no']})"})
    w = df[df["sys"] & df["in_win"] & df["ote_overlap"] & (df["rr1"] >= cfg["filters"]["min_rr_t1"])]
    cur = cfg["filters"]["min_rr_t2"]
    below = metrics(w[(w["rr2"] >= cur - 0.5) & (w["rr2"] < cur)])
    above = metrics(w[(w["rr2"] >= cur) & (w["rr2"] < cur + 0.5)])
    lo_r, hi_r = at["min_rr_t2_bounds"]
    if below["trig"] >= at["min_samples"] and (below["avg_r"] or 0) > at["delta_r"] and cur - 0.25 >= lo_r:
        changes.append({"section": "filters", "key": "min_rr_t2", "old": cur, "new": cur - 0.25, "strength": below["avg_r"],
                        "why": f"Setups just below the R:R filter averaged {below['avg_r']:.2f}R (n={below['trig']})"})
    elif above["trig"] >= at["min_samples"] and (above["avg_r"] or 0) < -at["delta_r"] and cur + 0.25 <= hi_r:
        changes.append({"section": "filters", "key": "min_rr_t2", "old": cur, "new": cur + 0.25, "strength": -above["avg_r"],
                        "why": f"Setups just above the R:R filter averaged {above['avg_r']:.2f}R (n={above['trig']})"})
    changes = sorted(changes, key=lambda c: -c["strength"])[:at["max_changes"]]
    if changes:
        p = ROOT / "tuning.json"
        t = json.loads(p.read_text()) if p.exists() else {}
        t["version"] = t.get("version", 1) + 1
        for c in changes:
            t.setdefault(c["section"], {})[c["key"]] = c["new"]
        p.write_text(json.dumps(t, indent=1))
        lp = ROOT / "config_changes.json"
        log = json.loads(lp.read_text()) if lp.exists() else []
        stamp = dt.datetime.now(NY).strftime("%Y-%m-%d %H:%M ET")
        log += [{"changed_at": stamp, "version": t["version"], **{k: c[k] for k in ("section", "key", "old", "new", "why")}} for c in changes]
        lp.write_text(json.dumps(log, indent=1))
    return changes
