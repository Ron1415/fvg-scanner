# FVG Trading Journal review (November 3, 2026)

**Data reviewed**

- 4,329 frozen setups from the Google Sheets journal:
  - Baseline: 4,116 setups over 59 sessions, August 11 to November 2, on 100 symbols
  - Daily replay: 74 setups (November 2)
  - Live: 139 setups (November 2–3)
- 1 actual trade.

All results below are hypothetical and before costs, unless a cost is stated.

## What the data says

1. **There is no edge yet.**
   - Qualified setups that triggered (726) averaged +0.02R per trade, with a 41% win rate, a profit factor of 1.03 and a maximum drawdown of -47.6R.
   - Even a small cost turns this negative. At 0.02% per side, many of these tight-stop trades lose 0.1–0.3R in costs alone.
2. **The plan window is the weakest time of day.**

   | Formed | Avg R |
   |---|---|
   | 10:00–10:30 | -0.22 |
   | 10:30–11:30 | -0.06 |
   | 11:30–13:00 | +0.13 |
   | 13:00–14:30 | +0.20 |
   | 14:30–16:00 | -0.12 |

   Setups formed by 11:30 averaged -0.10R. Midday (11:30–14:30) is the only clearly positive window.
3. **The Setup Score does not predict results.**
   - Scores of 75–89 averaged -0.04R, 60–74 averaged +0.04R, and under 60 averaged +0.08R.
   - Every factor showed "no clear effect" (a difference under 0.15R), so the auto-tune correctly changed nothing.
4. **Most qualified setups never fill.** 63% of them ran to Target 1 without coming back to the entry. Trades that fill within 15 minutes do worst (-0.15R); fills after an hour or more do best (+0.09R). The deep OTE entry fills mostly on the moves that keep going against the trade.
5. **The OTE filter barely matters.** Setups filtered out for no OTE overlap averaged -0.02R, against +0.02R for those that passed.
6. **R:R to Target 2 does matter.**

   | R:R to Target 2 | Avg R |
   |---|---|
   | 2–2.5 | -0.15 |
   | 2.5–3 | +0.02 |
   | 3 or more | +0.07 |
7. **Longs beat shorts, and stocks beat ETFs.**
   - Longs averaged +0.11R and shorts -0.07R.
   - Stocks averaged +0.06R and ETFs -0.04R.
   - Leveraged ETFs (-0.03R) add no value. They largely duplicate SPY and QQQ setups at the same moment, with up to 11 setups on the same side in the same 5 minutes.
8. **Target 2 adds nothing.** The plan (half at T1, rest to T2) returned the same +0.02R as taking the full position off at T1. Runners only paid when held to the close.
9. **Your one trade.** XLP short, taken at 11:49 (outside the plan window) against a bullish daily bias. The exit at 90.80 was 0.23 beyond the 90.57 stop, a result of -1.77R instead of -1R. Use a hard stop order at entry.
10. **Data gaps.**
    - The baseline has no futures, because it ran before futures were added.
    - 38 rows have no asset type.
    - Live and replay disagreed on November 2 (28 qualified live setups against 50 in the replay), because the live scanner only sees the market every 15 minutes.

## Suggestions (for your approval; none are applied yet)

1. **Rebuild the evidence on 6 months of data.** The GitHub version runs it (125 sessions, Alpaca 5-minute bars), with costs included.
2. **Test the entry.** The new backtest re-runs every setup with three entries: current (OTE overlap midpoint), the first touch of the gap, and the gap midpoint. It also tests two stop buffers.
3. **Restrict to the window that works.** Test midday entries (11:30–14:30), and reconsider the 10:00–10:30 window.
4. **Raise MIN_RR_T2 from 2.0 to 2.5.** The auto-tune can do this itself once the 6-month sample confirms it.
5. **Add a minimum risk of about 0.15% of price**, so costs do not swamp tiny stops.
6. **Drop the leveraged/inverse ETFs**, or take only one setup per correlated group (SPY/QQQ/IWM and their leveraged versions) at a time.
7. **Rebuild or retire the Setup Score.** After the 6-month backtest, keep only the factors that show an effect.
8. **Use a full exit at Target 1 for the bot,** unless the 6-month data shows runners paying.
9. **Paper trade before any automation.** The bar for moving on is a positive net result in both halves of the 6-month test and in the first 4 weeks of live replay.
