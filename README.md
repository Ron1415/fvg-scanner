# FVG Scanner

A day-trading scanner and trainer for the ICT Fair Value Gap strategy on 5-minute charts. It runs on GitHub in the same way as the reversal scanner: GitHub Actions runs the Python code on a schedule, and GitHub Pages publishes the dashboard.

**What it does**

- Scans the 100 most liquid stocks and ETFs plus the 10 most liquid futures, every 15 minutes from 9:25 AM to 4:05 PM ET.
- After the close, it replays the whole session for every symbol. Each setup the scanner would have flagged is frozen and backtested. The results feed a review page and a weekly, guard-railed auto-tune.

**The setup rules**

1. **Liquidity sweep:** price trades through a key level: the prior-day high or low, the pre-market high or low (for futures, the overnight session), or the opening-range high or low.
2. **Market structure shift:** price closes beyond the last swing on the other side.
3. **Displacement FVG:** the move leaves a fair value gap.
4. **Entry:** the middle of the overlap between the FVG and the OTE zone (62–79%).
5. **Stop and targets:** the stop sits just beyond the sweep. Target 1 is the swing extreme, and Target 2 is the next key level.

## Files

| File | Purpose |
|---|---|
| scanner.py | Main program. Modes: `--auto`, `--live`, `--eod`, `--backtest DAYS`, `--review` |
| engine.py | Session levels, setup detection, Setup Score, plan filters |
| simulate.py | Backtest of one setup (conservative fills, partial at T1, breakeven, end-of-day exit, costs) |
| replay.py | Replays a session bar by bar and freezes every setup; runs the improvement tests |
| learn.py | Review statistics, review.md, the weekly auto-tune |
| data.py | Yahoo Finance (live, daily, futures, about 60 days of 5-minute bars) and Alpaca (6+ months of 5-minute stock and ETF bars) |
| report.py, templates/ | Dashboard, review and universe pages |
| config.py | Every setting and threshold |
| tuning.json, config_changes.json | Values changed by the auto-tune, and the log of every change |
| trades.json | Your trade journal, saved from the dashboard |
| history/ | Live snapshots and daily replays, one CSV per month (includes the Google Sheets import) |
| backtest/ | The latest backtest (backtest.csv.gz and meta.json) |
| review.md | The latest review as plain text. Claude can read it from GitHub directly. |
| test_engine.py | Rule checks on hand-built charts: `python test_engine.py` |
| tradingview/FVG_Setup_Levels.pine | TradingView indicator that draws the same levels |
| .github/workflows/fvg.yml | GitHub automation |

## Setup (about 15 minutes)

1. **Create the repository.** On GitHub, select **New repository** and name it `fvg-scanner`.
   - Choose **Public** if you want free, unlimited Actions minutes and free GitHub Pages (this is what the reversal scanner uses).
   - A private repository has 2,000 free Actions minutes per month. This scanner needs roughly 1,500–2,500 minutes per month.
2. **Upload the files.** Select **Add file > Upload files** and drag in everything from this folder except the `.github` folder.
3. **Add the workflow.** Select **Actions > set up a workflow yourself**, name the file `fvg.yml`, paste in the contents of `.github/workflows/fvg.yml`, and select **Commit**.
4. **Turn on Pages.** Go to **Settings > Pages > Build and deployment > Source** and choose **GitHub Actions**.
5. **Allow the workflow to save results.** Go to **Settings > Actions > General > Workflow permissions** and choose **Read and write permissions**.
6. **Add Alpaca keys for the 6-month backtest (recommended).**
   - Create a free account at alpaca.markets. Paper trading is enough.
   - Copy the API Key ID and Secret Key.
   - In GitHub, go to **Settings > Secrets and variables > Actions > New repository secret** and add `ALPACA_KEY_ID` and `ALPACA_SECRET_KEY`.
   - Without these keys, the backtest covers only the roughly 60 days of 5-minute bars that Yahoo keeps.
7. **Run the first backtest.** Go to **Actions > fvg-scan > Run workflow**, set mode to `backtest`, and keep 125 days (about 6 months). Expect it to take about 30–90 minutes. When it finishes, the dashboard is published at `https://<your-username>.github.io/fvg-scanner/`.
8. **Set up saving from the dashboard.**
   - Open the dashboard, then **Settings**, and paste in a fine-grained GitHub token for this repository with **Contents** and **Actions** set to read and write.
   - Add a free Finnhub key for live stock prices, the same as on the reversal dashboard.

From then on, everything runs on its own on weekdays.

## 1-minute long model (added November 4, 2026)

A separate, simpler model on 1-minute bars: `fvg1m.py`, settings in `config_1m.py`, checks in `test_fvg1m.py`, and the same rules as a TradingView strategy in `FVG_1m_Strategy.pine`.

1. **Up-trend bias only (long only):** the prior daily close is above a rising 20-day average, the entry is above VWAP, and a 1-minute close has broken above the 9:30-9:45 opening range.
2. **Break of structure:** the first close above the last lower high.
3. **FVG:** a bullish fair value gap in the move up.
4. **Entry:** a limit order at the FVG midpoint, which must sit at the 50-61.8% retracement of the move and on the broken falling trendline.
5. **Risk and exits:** stop below the FVG (at least 0.20% of price); half off at 4R; stop to breakeven once a close clears the recent high; the rest rides to the next untouched 15-minute FVG above, or the 3:55 PM close.

**Version 2 (Nov 4, 2026):** stocks plus SPY only; fills from 10:30; a limit order fills only if price trades a cent through it; a realistic cost column (limit orders free, $0.01/share on stops and the close); stop variants (below the FVG or below the swing low) with 4R and 3R targets. The review chooses the variant on May-August and confirms it on September onward.

**Version 3 exits (Nov 4, 2026):** no stop loss at the start. The trade is closed at the 2nd consecutive 1-minute close below the recent swing low. Once 2 consecutive closes are above the recent high, a breakeven stop is set. 1R = entry minus the swing low (at least 0.20% of price); half is sold at 4R. The review compares this with the version 2 stop order.

**Backtest:** run the workflow with mode `fvg1m` and 125 days (needs the Alpaca keys for 1-minute history). Results go to `review_1m.md` and `backtest_1m/trades.csv.gz`. Section 1 of the review switches each rule off in turn, so it shows what every rule adds.

## Trendline retest confluence (added November 4, 2026)

Each setup now records the counter-trend line of the leg into the sweep: for longs, a falling line across the lower highs; for shorts, a rising line across the higher lows. The line must have held (no close beyond it) until the sweep, and must then be broken by a close.

- **Confluence (`tl_conf`):** the line has not failed, and its level at the next bar sits inside the entry zone (FVG near edge to the entry), within 0.25 ATR. A pullback into the FVG would then also retest the broken line.
- **Score:** confluence adds the `tl` weight (10 points). The weekly auto-tune adjusts it like the other weights.
- **Retest at the fill (`r_tl`):** the plan result, counted only when the line was within 0.3 ATR of the fill price at the moment of the fill.
- **Entry variant (`tl_line`):** a limit order at the line's level, tested with both stop buffers.
- **Review:** section 11 compares setups with and without the confluence. Only rows recorded from November 4 carry the trendline, so rerun the backtest (mode `backtest`, 125 days) to fill in history.
- **Settings:** `TESTS["trendline"]` and `WEIGHTS["tl"]` in `config.py`; `TL_ZONE_ATR` in `engine.py`.

## Schedule

- **Every 15 minutes, 9:25 AM–4:05 PM ET:** a live scan updates the dashboard and freezes any new setups into `history/live_YYYY-MM.csv`. GitHub schedules can start 5–15 minutes late.
- **After 4:15 PM ET:**
  - The day's live snapshots are backtested on 1-minute bars.
  - The full session is replayed for every symbol into `history/replay_YYYY-MM.csv`.
  - The review is rebuilt.
- **Fridays:** the auto-tune runs.

## Backtest rules

- **Entry:** a limit order at the frozen entry.
  - It can fill from 10:00 AM until 3:30 PM, so every time of day is tested.
  - The order is cancelled if price hits the stop first.
  - It stays working if price runs to Target 1 before it fills.
- **Same-bar conflicts:**
  - If one bar touches both the stop and a target, the stop is assumed to come first.
  - The bar that fills the order can only stop out.
- **Management:**
  - Half the position closes at Target 1.
  - The stop then moves to breakeven, and the rest runs to Target 2.
  - Anything still open closes at 3:55 PM.
- **Costs:** 0.02% of price per side (`SIM["cost_pct_per_side"]`). Headline results are net of this cost.
- **Improvement tests:** every setup is re-run with three entries (current, first touch of the gap, middle of the gap) and two stop buffers (0.1 and 0.3 ATR). The review compares them under several filters. The live rules change only after you approve a winner.

## Auto-tune (your choice: automatic, with guardrails)

- **When a weight changes:** at least 20 triggered trades on each side of a comparison, and a difference of 0.15R or more.
- **Change limits:** at most 2 points per week per weight, and no more than 3 changes per week.
- **Records:** changes are written to `tuning.json` and logged in `config_changes.json`.
- **Undoing a change:** edit `tuning.json` (pencil icon on GitHub).
- **Turning it off:** set `AUTO_TUNE["enabled"] = False` in config.py.

## Limits

- **Survivorship bias:** the universe is today's most liquid list, used for the whole backtest period.
- **Futures data:** futures history comes from Yahoo's continuous front-month contracts, about 60 days of 5-minute bars. Roll dates can create price jumps.
- **Data quality:** Yahoo data is free and unofficial and may be delayed. Alpaca's free plan excludes the latest 15 minutes, which does not matter for backtests.
- **Results are hypothetical:** live fills, slippage and fees will differ.

This is an educational tool, not financial advice.
