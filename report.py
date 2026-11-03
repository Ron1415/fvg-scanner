"""Builds the GitHub Pages site in ./site from the templates and the data files."""
from __future__ import annotations

import html
import json
import os
import shutil
from pathlib import Path

import config as C

ROOT = Path(__file__).resolve().parent
# Templates normally live in templates/. If the files were uploaded without the folder
# (GitHub's web upload can flatten folders), they are found in the repository root instead.
TPL = ROOT / "templates" if (ROOT / "templates" / "dashboard_template.html").exists() else ROOT


def _cfg() -> str:
    repo = os.environ.get("GITHUB_REPOSITORY", "")
    return json.dumps({"repo": repo, "branch": "main", "workflow": "fvg.yml"})


def write_pages() -> None:
    site = ROOT / "site"
    (site / "data").mkdir(parents=True, exist_ok=True)
    for name in ("style.css", "store.js"):
        shutil.copy(TPL / name, site / name)
    for src, dst in (("dashboard_template.html", "index.html"), ("review_template.html", "review.html")):
        text = (TPL / src).read_text().replace("__CFG__", _cfg()).replace("__RISK__", str(C.RISK_PCT))
        (site / dst).write_text(text)
    for src, dst in (("trades.json", "trades.json"), ("config_changes.json", "config_changes.json"),
                     ("backtest/meta.json", "backtest_meta.json")):
        p = ROOT / src
        if p.exists():
            shutil.copy(p, site / "data" / dst)
    if not (site / "data" / "trades.json").exists():
        (site / "data" / "trades.json").write_text("[]")
    # universe page
    u = json.loads((ROOT / "universe.json").read_text()) if (ROOT / "universe.json").exists() else {"date": "", "rows": []}
    rows = "".join(f"<tr><td>{i + 1}</td><td>{html.escape(r['t'])}</td><td>{r['type']}</td><td>{r['dv_m']:,}</td>"
                   f"<td>{r['price']}</td><td>{r['bias']}</td></tr>" for i, r in enumerate(u["rows"]))
    (site / "universe.html").write_text(
        f"""<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>FVG Universe</title><link rel="stylesheet" href="style.css"></head><body><div class="wrap"><h1>Universe</h1>
<div class="sub">Ranked {html.escape(u['date'])} by 20-day average dollar volume (futures: notional = price x volume x multiplier).</div>
<div class="toplinks"><a href="index.html">Dashboard</a><a href="review.html">Review</a></div>
<div class="card tbl"><table><tr><th>#</th><th>Symbol</th><th>Type</th><th>Avg daily $ volume ($M)</th><th>Last close</th><th>Daily bias</th></tr>{rows}</table></div>
</div></body></html>""")
    if not (site / "data" / "state.json").exists():
        (site / "data" / "state.json").write_text(json.dumps({"updated": "never", "updated_iso": "1970-01-01T00:00:00Z", "scanned": 0,
                                                             "total": 0, "filtered": 0, "top": [], "prices": {}, "config_version": 1}))
