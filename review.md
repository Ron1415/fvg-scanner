# FVG review: 2026-11-16 16:22 ET (Daily)

Sessions: 134 (2026-05-07 to 2026-11-16). Config version 2.

## 1. Strategy performance (qualified setups; results net of costs)

Costs: 0.02% of price per side. Entries allowed until 15:30 ET.

| Group | Setups | Triggered | Trigger rate | Win rate | Avg R | Expectancy R | Profit factor | Total R | Max DD R | 1st half avg R | 2nd half avg R |
|---|---|---|---|---|---|---|---|---|---|---|---|
| Live dashboard snapshots | 149 | 43 | 28.9% | 39.5% | -0.22 | -0.06 | 0.6 | -9.63 | -12.11 | -0.05 | -0.39 |
| Daily full-session replays | 257 | 90 | 35.0% | 42.2% | -0.23 | -0.08 | 0.66 | -20.53 | -30.6 | -0.07 | -0.38 |
| Backtest | 3224 | 1010 | 31.3% | 41.1% | -0.1 | -0.03 | 0.84 | -104.96 | -135.21 | -0.08 | -0.13 |
| Systematic (replays + backtest) | 3481 | 1100 | 31.6% | 41.2% | -0.11 | -0.04 | 0.82 | -125.5 | -154.03 | -0.12 | -0.11 |
| Systematic, before cost (gross) | 3481 | 1100 | 31.6% | 42.8% | 0.09 | 0.03 | 1.18 | 102.3 | -37.49 | 0.07 | 0.12 |
| Systematic, plan window only (New York, formed by 11:30) | 974 | 385 | 39.5% | 38.4% | -0.19 | -0.07 | 0.71 | -72.4 | -74.22 | -0.26 | -0.12 |
| Live top-5 suggestions only | 100 | 31 | 31.0% | 35.5% | -0.34 | -0.11 | 0.46 | -10.62 | -10.62 | -0.22 | -0.46 |
| Your actual trades | 1 | 1 |  | 0.0% | -1.77 |  |  | -1.77 |  |  |  |
| Stocks and ETFs, New York session only | 2930 | 855 | 29.2% | 42.3% | -0.08 | -0.02 | 0.86 | -71.95 | -98.55 | -0.07 | -0.1 |
| Futures, New York session | 152 | 52 | 34.2% | 46.2% | -0.07 | -0.02 | 0.89 | -3.51 | -12.11 | 0.21 | -0.35 |
| Futures, all 24-hour sessions | 551 | 245 | 44.5% | 37.1% | -0.22 | -0.1 | 0.7 | -53.55 | -56.13 | -0.19 | -0.25 |

## 1c. Futures by session (24-hour test; qualified, net of costs)

Asia and London use their own levels: prior-day high/low, the previous session's high/low, and the session's first 30 minutes.

| Group | Setups | Triggered | Trigger rate | Win rate | Avg R | Expectancy R | Profit factor | Total R | Max DD R | 1st half avg R | 2nd half avg R |
|---|---|---|---|---|---|---|---|---|---|---|---|
| Futures, Asia session (6 PM-midnight ET) | 175 | 77 | 44.0% | 29.9% | -0.26 | -0.12 | 0.66 | -20.24 | -21.96 | -0.23 | -0.29 |
| Futures, London session (2-8 AM ET) | 224 | 116 | 51.8% | 37.9% | -0.26 | -0.13 | 0.67 | -29.8 | -38.05 | -0.46 | -0.05 |
| Futures, NY session (9:30-4:00 ET) | 152 | 52 | 34.2% | 46.2% | -0.07 | -0.02 | 0.89 | -3.51 | -12.11 | 0.21 | -0.35 |
| CL=F Asia | 21 | 11 | 52.4% | 45.5% | 0.4 | 0.21 | 1.65 | 4.39 | -2.35 | -0.11 | 0.82 |
| CL=F London | 26 | 10 | 38.5% | 40.0% | 0.09 | 0.03 | 1.15 | 0.87 | -2.21 | -0.14 | 0.31 |
| CL=F NY | 21 | 7 | 33.3% | 28.6% | -0.38 | -0.13 | 0.5 | -2.66 | -3.18 | -1.06 | 0.13 |
| ES=F Asia | 16 | 6 | 37.5% | 33.3% | -0.45 | -0.17 | 0.43 | -2.72 | -4.64 | 0.28 | -1.18 |
| ES=F London | 27 | 16 | 59.3% | 43.8% | 0.19 | 0.11 | 1.28 | 2.98 | -5.2 | -0.57 | 0.94 |
| ES=F NY | 19 | 8 | 42.1% | 75.0% | 0.85 | 0.36 | 5.84 | 6.83 | -1.41 | 1.23 | 0.48 |
| GC=F Asia | 37 | 24 | 64.9% | 25.0% | -0.06 | -0.04 | 0.91 | -1.52 | -10.46 | 0.07 | -0.2 |
| GC=F London | 16 | 6 | 37.5% | 66.7% | 0.35 | 0.13 | 2.0 | 2.09 | -1.05 | 0.05 | 0.64 |
| GC=F NY | 17 | 6 | 35.3% | 50.0% | 0.08 | 0.03 | 1.16 | 0.51 | -1.64 | 0.72 | -0.55 |
| NQ=F Asia | 14 | 7 | 50.0% | 28.6% | -0.32 | -0.16 | 0.57 | -2.21 | -5.19 | -1.04 | 0.23 |
| NQ=F London | 21 | 7 | 33.3% | 0.0% | -0.79 | -0.26 | 0.0 | -5.53 | -5.53 | -1.03 | -0.61 |
| NQ=F NY | 13 | 4 | 30.8% | 25.0% | -0.32 | -0.1 | 0.38 | -1.29 | -2.08 | -1.01 | 0.37 |
| RTY=F Asia | 19 | 5 | 26.3% | 60.0% | 0.4 | 0.11 | 1.9 | 2.01 | -2.23 | 1.12 | -0.08 |
| RTY=F London | 33 | 22 | 66.7% | 31.8% | -0.29 | -0.19 | 0.6 | -6.3 | -10.2 | -0.54 | -0.04 |
| RTY=F NY | 15 | 2 | 13.3% | 50.0% | -0.1 | -0.01 | 0.82 | -0.19 | -1.04 | -1.04 | 0.85 |
| YM=F Asia | 21 | 6 | 28.6% | 16.7% | -0.8 | -0.23 | 0.15 | -4.81 | -5.67 | -0.51 | -1.09 |
| YM=F London | 30 | 15 | 50.0% | 60.0% | 0.4 | 0.2 | 1.89 | 6.03 | -2.29 | 0.32 | 0.48 |
| YM=F NY | 16 | 3 | 18.8% | 33.3% | 0.43 | 0.08 | 1.63 | 1.3 | -2.05 | 3.35 | -1.03 |
| ZB=F Asia | 17 | 7 | 41.2% | 28.6% | -1.07 | -0.44 | 0.05 | -7.49 | -7.73 | -0.65 | -1.38 |
| ZB=F London | 14 | 9 | 64.3% | 44.4% | -0.37 | -0.24 | 0.54 | -3.3 | -3.38 | -0.7 | -0.1 |
| ZB=F NY | 17 | 8 | 47.1% | 62.5% | 0.26 | 0.12 | 1.45 | 2.07 | -1.65 | 0.8 | -0.28 |
| ZF=F Asia | 16 | 6 | 37.5% | 16.7% | -0.85 | -0.32 | 0.13 | -5.09 | -5.09 | -1.24 | -0.46 |
| ZF=F London | 22 | 14 | 63.6% | 28.6% | -1.07 | -0.68 | 0.2 | -14.95 | -14.95 | -1.34 | -0.79 |
| ZF=F NY | 14 | 6 | 42.9% | 50.0% | -0.72 | -0.31 | 0.14 | -4.31 | -4.64 | -0.53 | -0.9 |
| ZN=F Asia | 9 | 4 | 44.4% | 25.0% | -0.49 | -0.22 | 0.37 | -1.95 | -2.63 | -1.31 | 0.34 |
| ZN=F London | 14 | 8 | 57.1% | 25.0% | -0.68 | -0.39 | 0.33 | -5.44 | -5.44 | -0.54 | -0.82 |
| ZN=F NY | 9 | 6 | 66.7% | 33.3% | -0.52 | -0.35 | 0.37 | -3.11 | -3.11 | -0.01 | -1.03 |
| ZS=F Asia | 5 | 1 | 20.0% | 0.0% | -0.85 | -0.17 | 0.0 | -0.85 | -0.85 |  | -0.85 |
| ZS=F London | 21 | 9 | 42.9% | 33.3% | -0.69 | -0.3 | 0.32 | -6.25 | -7.26 | -0.95 | -0.49 |
| ZS=F NY | 11 | 2 | 18.2% | 0.0% | -1.33 | -0.24 | 0.0 | -2.66 | -2.66 | -1.32 | -1.34 |

## 2. New York session: by asset, side, time of day, risk size (systematic, qualified)

| Group | Setups | Triggered | Trigger rate | Win rate | Avg R | Expectancy R | Profit factor | Total R | Max DD R | 1st half avg R | 2nd half avg R |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ETF | 955 | 324 | 33.9% | 41.0% | -0.18 | -0.06 | 0.74 | -57.18 | -69.61 | -0.09 | -0.26 |
| Stock | 1975 | 531 | 26.9% | 43.1% | -0.03 | -0.01 | 0.95 | -14.77 | -41.36 | -0.06 | 0.0 |
| Future | 152 | 52 | 34.2% | 46.2% | -0.07 | -0.02 | 0.89 | -3.51 | -12.11 | 0.21 | -0.35 |
| Leveraged/inverse ETFs | 139 | 44 | 31.7% | 50.0% | 0.33 | 0.11 | 1.76 | 14.65 | -6.42 | 0.77 | -0.11 |
| LONG | 2729 | 823 | 30.2% | 42.5% | -0.09 | -0.03 | 0.86 | -73.12 | -98.95 | -0.08 | -0.1 |
| SHORT | 353 | 84 | 23.8% | 42.9% | -0.03 | -0.01 | 0.93 | -2.34 | -9.63 | -0.1 | 0.05 |
| Formed 10:00-10:30 | 317 | 152 | 47.9% | 30.9% | -0.31 | -0.15 | 0.59 | -46.38 | -46.38 | -0.28 | -0.33 |
| Formed 10:30-11:30 | 607 | 217 | 35.7% | 42.9% | -0.12 | -0.04 | 0.79 | -25.99 | -33.43 | -0.25 | 0.01 |
| Formed 11:30-13:00 | 865 | 275 | 31.8% | 48.4% | -0.02 | -0.01 | 0.97 | -5.15 | -22.07 | 0.04 | -0.08 |
| Formed 13:00-14:30 | 761 | 200 | 26.3% | 41.0% | -0.06 | -0.01 | 0.91 | -11.17 | -34.2 | -0.21 | 0.1 |
| Formed 14:30-16:00 | 532 | 63 | 11.8% | 49.2% | 0.21 | 0.02 | 1.38 | 13.24 | -16.45 | 0.75 | -0.31 |
| Risk 0-0.15% of price | 645 | 315 | 48.8% | 34.0% | -0.42 | -0.2 | 0.53 | -131.39 | -134.93 | -0.4 | -0.43 |
| Risk 0.15-0.3% of price | 682 | 251 | 36.8% | 41.0% | -0.1 | -0.04 | 0.84 | -25.54 | -45.15 | -0.16 | -0.04 |
| Risk 0.3-0.6% of price | 1096 | 301 | 27.5% | 45.5% | 0.06 | 0.02 | 1.12 | 18.77 | -20.24 | 0.06 | 0.06 |
| Risk 0.6%+ | 1058 | 233 | 22.0% | 45.5% | 0.05 | 0.01 | 1.12 | 12.66 | -16.61 | 0.1 | 0.01 |

## 2b. Short guardrails (systematic; shorts use full exit at T1, breakeven at +0.5R, 60-minute time stop)

Sizing: longs 1.25% risk (cap 5.0% of account), shorts 0.5% risk (cap 2.5%). Results here are in R, before sizing.

| Group | Setups | Triggered | Trigger rate | Win rate | Avg R | Expectancy R | Profit factor | Total R | Max DD R | 1st half avg R | 2nd half avg R |
|---|---|---|---|---|---|---|---|---|---|---|---|
| Longs passing the normal filters | 3125 | 1016 | 32.5% | 41.0% | -0.12 | -0.04 | 0.82 | -123.15 | -150.93 | -0.12 | -0.12 |
| Shorts passing the normal filters (before guardrails) | 2246 | 802 | 35.7% | 27.7% | -0.18 | -0.06 | 0.64 | -145.89 | -148.2 | -0.07 | -0.29 |
| Shorts passing every guardrail (traded) | 356 | 84 | 23.6% | 42.9% | -0.03 | -0.01 | 0.93 | -2.34 | -9.63 | -0.1 | 0.05 |
| Shorts passing: bearish daily trend | 969 | 353 | 36.4% | 29.5% | -0.21 | -0.08 | 0.6 | -73.17 | -80.64 | -0.12 | -0.29 |
| Shorts failing: bearish daily trend | 1277 | 449 | 35.2% | 26.3% | -0.16 | -0.06 | 0.67 | -72.72 | -73.61 | -0.09 | -0.23 |
| Shorts passing: PDH or 2+ level sweep | 1601 | 540 | 33.7% | 29.6% | -0.11 | -0.04 | 0.74 | -61.78 | -66.59 | -0.03 | -0.19 |
| Shorts failing: PDH or 2+ level sweep | 645 | 262 | 40.6% | 23.7% | -0.32 | -0.13 | 0.48 | -84.1 | -84.96 | -0.26 | -0.38 |
| Shorts passing: R:R to T2 3.0+ | 1643 | 589 | 35.8% | 28.0% | -0.19 | -0.07 | 0.63 | -112.61 | -116.18 | -0.05 | -0.33 |
| Shorts failing: R:R to T2 3.0+ | 603 | 213 | 35.3% | 26.8% | -0.16 | -0.06 | 0.65 | -33.28 | -38.04 | -0.12 | -0.19 |
| Shorts passing: risk 0.3%+ of price | 1200 | 351 | 29.2% | 32.8% | -0.02 | -0.01 | 0.94 | -7.19 | -25.88 | 0.05 | -0.09 |
| Shorts failing: risk 0.3%+ of price | 1046 | 451 | 43.1% | 23.7% | -0.31 | -0.13 | 0.5 | -138.69 | -139.58 | -0.26 | -0.35 |
| Shorts passing: formed 10:30 or later | 2001 | 674 | 33.7% | 27.0% | -0.2 | -0.07 | 0.62 | -134.39 | -135.28 | -0.12 | -0.28 |
| Shorts failing: formed 10:30 or later | 245 | 128 | 52.2% | 31.2% | -0.09 | -0.05 | 0.79 | -11.49 | -20.84 | 0.1 | -0.28 |
| Shorts passing: not a leveraged ETF | 2158 | 776 | 36.0% | 27.3% | -0.2 | -0.07 | 0.61 | -154.52 | -155.41 | -0.11 | -0.29 |
| Shorts failing: not a leveraged ETF | 88 | 26 | 29.5% | 38.5% | 0.33 | 0.1 | 2.07 | 8.63 | -2.49 | 0.81 | -0.14 |

## 3. Outcomes (systematic, qualified)

| Outcome | Count | Share | Avg R |
|---|---|---|---|
| Not triggered (ran to T1 first) | 2181 | 62.7% | 0.0 |
| Stop | 527 | 15.1% | -1.22 |
| EOD exit | 224 | 6.4% | 0.2 |
| Not triggered (cutoff) | 199 | 5.7% | 0.0 |
| T1 then EOD | 147 | 4.2% | 1.79 |
| T1 then breakeven | 80 | 2.3% | 0.58 |
| T1 then T2 | 78 | 2.2% | 1.99 |
| Time stop | 27 | 0.8% | 0.47 |
| Breakeven stop | 17 | 0.5% | -0.1 |
| Invalidated before entry | 1 | 0.0% | 0.0 |

## 4. Score calibration. A useful score shows results improving band by band.

| Group | Setups | Triggered | Trigger rate | Win rate | Avg R | Expectancy R | Profit factor | Total R | Max DD R | 1st half avg R | 2nd half avg R |
|---|---|---|---|---|---|---|---|---|---|---|---|
| Score 90+ | 20 | 12 | 60.0% | 75.0% | 0.92 | 0.55 | 6.01 | 11.09 | -2.22 | 1.18 | 0.67 |
| Score 75-89 | 1263 | 372 | 29.5% | 40.6% | -0.12 | -0.04 | 0.8 | -45.37 | -74.93 | -0.15 | -0.09 |
| Score 60-74 | 1918 | 598 | 31.2% | 42.0% | -0.08 | -0.03 | 0.87 | -50.05 | -61.61 | -0.04 | -0.13 |
| Score under 60 | 280 | 118 | 42.1% | 35.6% | -0.35 | -0.15 | 0.55 | -41.16 | -44.28 | -0.36 | -0.34 |

## 5. Factor attribution (all triggered systematic setups, qualified or not)

| Factor | Weight key | Weight | With | Avg R with | Without | Avg R without | Difference | Read |
|---|---|---|---|---|---|---|---|---|
| Prior-day level swept | sweep_pd | 20 | 2738 | -0.11 | 3145 | -0.17 | 0.06 | No clear effect |
| Only PM/OR level swept | sweep_other | 15 | 2487 | -0.15 | 3396 | -0.13 | -0.02 | No clear effect |
| FVG in discount/premium | zone | 10 | 2143 | -0.17 | 3740 | -0.12 | -0.05 | No clear effect |
| FVG overlaps OTE | ote | 15 | 1891 | -0.16 | 3992 | -0.13 | -0.02 | No clear effect |
| R:R to T1 of 2 or more | rr | 10 | 448 | -0.28 | 5435 | -0.13 | -0.15 | Hurts |
| HTF bias aligned | bias | 10 | 2268 | -0.15 | 3615 | -0.14 | -0.01 | No clear effect |
| Displacement volume 1.5x+ | vol | 5 | 715 | -0.1 | 5168 | -0.15 | 0.05 | No clear effect |
| Formed 10:00-11:30 | time | 5 | 2774 | -0.19 | 3109 | -0.1 | -0.09 | No clear effect |
| Trendline retest confluence | tl | 12 | 39 | 0.12 | 359 | -0.27 | 0.39 | Helps |

## 6. Filter check (systematic)

| Group | Setups | Triggered | Trigger rate | Win rate | Avg R | Expectancy R | Profit factor | Total R | Max DD R | 1st half avg R | 2nd half avg R |
|---|---|---|---|---|---|---|---|---|---|---|---|
| Passed filters | 3481 | 1100 | 31.6% | 41.2% | -0.11 | -0.04 | 0.82 | -125.5 | -154.03 | -0.12 | -0.11 |
| Filtered out | 7984 | 4783 | 59.9% | 47.6% | -0.15 | -0.09 | 0.61 | -703.51 | -705.26 | -0.11 | -0.19 |
| No OTE overlap | 5942 | 3992 | 67.2% | 51.9% | -0.13 | -0.09 | 0.62 | -535.41 | -536.28 | -0.11 | -0.15 |
| OTE overlap, R:R to T2 1.5-2 | 147 | 69 | 46.9% | 30.4% | -0.3 | -0.14 | 0.5 | -20.42 | -20.51 | -0.13 | -0.46 |
| OTE overlap, R:R to T2 2-2.5 | 1221 | 359 | 29.4% | 35.4% | -0.16 | -0.05 | 0.72 | -57.62 | -59.56 | -0.13 | -0.2 |
| OTE overlap, R:R to T2 2.5-3 | 630 | 203 | 32.2% | 37.4% | -0.03 | -0.01 | 0.95 | -5.57 | -43.27 | -0.27 | 0.22 |
| OTE overlap, R:R to T2 3+ | 3525 | 1260 | 35.7% | 34.6% | -0.17 | -0.06 | 0.73 | -209.99 | -244.98 | -0.07 | -0.26 |

## 7. Improvement tests: entry type x stop buffer x filter (net of costs)

ote_mid = current entry (middle of the FVG/OTE overlap); fvg_edge = first touch of the gap; fvg_ce = gap midpoint; blend = halfway between the gap edge and ote_mid; ote_62 = first touch of the OTE zone; tl_line = limit at the broken trendline (only setups with trendline confluence). Scaled rows are in R of the full planned position (a partial fill counts only what filled).

| Group | Setups | Triggered | Trigger rate | Win rate | Avg R | Expectancy R | Profit factor | Total R | Max DD R | 1st half avg R | 2nd half avg R |
|---|---|---|---|---|---|---|---|---|---|---|---|
| Entry ote_mid, stop 0.1 ATR · All qualified | 3481 | 1100 | 31.6% | 41.2% | -0.11 | -0.04 | 0.82 | -125.48 | -154.02 | -0.12 | -0.11 |
| Entry ote_mid, stop 0.1 ATR · Plan window (by 11:30) | 974 | 385 | 39.5% | 38.4% | -0.19 | -0.07 | 0.71 | -72.39 | -74.21 | -0.26 | -0.12 |
| Entry ote_mid, stop 0.1 ATR · Midday 11:30-14:30 | 1626 | 475 | 29.2% | 45.3% | -0.03 | -0.01 | 0.94 | -16.31 | -35.77 | -0.06 | -0.01 |
| Entry ote_mid, stop 0.1 ATR · Stocks only | 1975 | 531 | 26.9% | 43.1% | -0.03 | -0.01 | 0.95 | -14.77 | -41.36 | -0.06 | 0.0 |
| Entry ote_mid, stop 0.1 ATR · R:R to T2 2.5+ | 2628 | 875 | 33.3% | 41.1% | -0.12 | -0.04 | 0.82 | -104.81 | -138.44 | -0.12 | -0.12 |
| Entry ote_mid, stop 0.1 ATR · Risk 0.15%+ | 2836 | 785 | 27.7% | 44.1% | 0.01 | 0.0 | 1.01 | 5.9 | -51.41 | 0.0 | 0.01 |
| Entry ote_mid, stop 0.1 ATR · Midday + R:R 2.5+ + risk 0.15%+ | 1098 | 338 | 30.8% | 47.0% | 0.06 | 0.02 | 1.11 | 19.26 | -22.62 | 0.03 | 0.08 |
| Entry ote_mid, stop 0.3 ATR · All qualified | 3481 | 1100 | 31.6% | 44.0% | -0.1 | -0.03 | 0.83 | -107.56 | -132.54 | -0.08 | -0.12 |
| Entry ote_mid, stop 0.3 ATR · Plan window (by 11:30) | 974 | 385 | 39.5% | 41.3% | -0.18 | -0.07 | 0.7 | -67.55 | -68.9 | -0.24 | -0.11 |
| Entry ote_mid, stop 0.3 ATR · Midday 11:30-14:30 | 1626 | 475 | 29.2% | 48.2% | -0.02 | -0.0 | 0.97 | -7.58 | -26.45 | -0.01 | -0.02 |
| Entry ote_mid, stop 0.3 ATR · Stocks only | 1975 | 531 | 26.9% | 46.1% | -0.03 | -0.01 | 0.95 | -14.25 | -38.05 | -0.01 | -0.04 |
| Entry ote_mid, stop 0.3 ATR · R:R to T2 2.5+ | 2628 | 875 | 33.3% | 44.5% | -0.09 | -0.03 | 0.84 | -81.58 | -111.74 | -0.07 | -0.12 |
| Entry ote_mid, stop 0.3 ATR · Risk 0.15%+ | 2836 | 785 | 27.7% | 47.0% | 0.02 | 0.0 | 1.03 | 11.84 | -36.54 | 0.02 | 0.01 |
| Entry ote_mid, stop 0.3 ATR · Midday + R:R 2.5+ + risk 0.15%+ | 1098 | 338 | 30.8% | 50.6% | 0.08 | 0.02 | 1.17 | 26.38 | -17.07 | 0.11 | 0.05 |
| Entry fvg_edge, stop 0.1 ATR · All qualified | 3481 | 1457 | 41.9% | 49.8% | -0.09 | -0.04 | 0.8 | -135.39 | -144.23 | -0.1 | -0.09 |
| Entry fvg_edge, stop 0.1 ATR · Plan window (by 11:30) | 974 | 491 | 50.4% | 48.9% | -0.15 | -0.08 | 0.68 | -73.46 | -74.79 | -0.15 | -0.14 |
| Entry fvg_edge, stop 0.1 ATR · Midday 11:30-14:30 | 1626 | 644 | 39.6% | 51.7% | -0.07 | -0.03 | 0.85 | -43.25 | -49.53 | -0.08 | -0.05 |
| Entry fvg_edge, stop 0.1 ATR · Stocks only | 1975 | 716 | 36.3% | 50.0% | -0.08 | -0.03 | 0.81 | -60.25 | -66.33 | -0.11 | -0.05 |
| Entry fvg_edge, stop 0.1 ATR · R:R to T2 2.5+ | 2628 | 1138 | 43.3% | 49.3% | -0.11 | -0.05 | 0.78 | -120.28 | -134.44 | -0.12 | -0.09 |
| Entry fvg_edge, stop 0.1 ATR · Risk 0.15%+ | 2836 | 1062 | 37.4% | 52.7% | -0.03 | -0.01 | 0.92 | -36.34 | -67.32 | -0.01 | -0.06 |
| Entry fvg_edge, stop 0.1 ATR · Midday + R:R 2.5+ + risk 0.15%+ | 1098 | 440 | 40.1% | 52.7% | -0.05 | -0.02 | 0.88 | -21.88 | -31.79 | -0.03 | -0.07 |
| Entry fvg_edge, stop 0.3 ATR · All qualified | 3481 | 1457 | 41.9% | 52.0% | -0.08 | -0.03 | 0.81 | -115.38 | -125.6 | -0.07 | -0.09 |
| Entry fvg_edge, stop 0.3 ATR · Plan window (by 11:30) | 974 | 491 | 50.4% | 50.9% | -0.14 | -0.07 | 0.68 | -68.83 | -69.74 | -0.15 | -0.13 |
| Entry fvg_edge, stop 0.3 ATR · Midday 11:30-14:30 | 1626 | 644 | 39.6% | 53.9% | -0.05 | -0.02 | 0.87 | -33.03 | -39.32 | -0.04 | -0.06 |
| Entry fvg_edge, stop 0.3 ATR · Stocks only | 1975 | 716 | 36.3% | 52.4% | -0.07 | -0.03 | 0.82 | -51.55 | -56.12 | -0.07 | -0.07 |
| Entry fvg_edge, stop 0.3 ATR · R:R to T2 2.5+ | 2628 | 1138 | 43.3% | 51.9% | -0.08 | -0.04 | 0.81 | -95.4 | -111.08 | -0.08 | -0.09 |
| Entry fvg_edge, stop 0.3 ATR · Risk 0.15%+ | 2836 | 1062 | 37.4% | 54.9% | -0.02 | -0.01 | 0.94 | -24.21 | -52.06 | 0.01 | -0.06 |
| Entry fvg_edge, stop 0.3 ATR · Midday + R:R 2.5+ + risk 0.15%+ | 1098 | 440 | 40.1% | 55.5% | -0.03 | -0.01 | 0.93 | -11.14 | -23.34 | 0.03 | -0.08 |
| Entry fvg_ce, stop 0.1 ATR · All qualified | 3481 | 1211 | 34.8% | 44.2% | -0.12 | -0.04 | 0.79 | -142.88 | -157.99 | -0.12 | -0.11 |
| Entry fvg_ce, stop 0.1 ATR · Plan window (by 11:30) | 974 | 423 | 43.4% | 43.0% | -0.17 | -0.07 | 0.71 | -71.57 | -73.17 | -0.22 | -0.12 |
| Entry fvg_ce, stop 0.1 ATR · Midday 11:30-14:30 | 1626 | 529 | 32.5% | 47.3% | -0.06 | -0.02 | 0.88 | -33.4 | -43.33 | -0.08 | -0.05 |
| Entry fvg_ce, stop 0.1 ATR · Stocks only | 1975 | 589 | 29.8% | 45.8% | -0.06 | -0.02 | 0.89 | -34.22 | -52.09 | -0.09 | -0.02 |
| Entry fvg_ce, stop 0.1 ATR · R:R to T2 2.5+ | 2628 | 956 | 36.4% | 43.8% | -0.12 | -0.04 | 0.8 | -111.28 | -132.41 | -0.14 | -0.09 |
| Entry fvg_ce, stop 0.1 ATR · Risk 0.15%+ | 2836 | 872 | 30.7% | 46.9% | -0.02 | -0.01 | 0.96 | -18.65 | -58.75 | -0.04 | -0.01 |
| Entry fvg_ce, stop 0.1 ATR · Midday + R:R 2.5+ + risk 0.15%+ | 1098 | 370 | 33.7% | 48.6% | -0.01 | -0.0 | 0.98 | -3.2 | -24.3 | 0.02 | -0.04 |
| Entry fvg_ce, stop 0.3 ATR · All qualified | 3481 | 1211 | 34.8% | 46.7% | -0.1 | -0.03 | 0.81 | -120.58 | -134.7 | -0.08 | -0.11 |
| Entry fvg_ce, stop 0.3 ATR · Plan window (by 11:30) | 974 | 423 | 43.4% | 45.4% | -0.16 | -0.07 | 0.7 | -66.97 | -68.12 | -0.21 | -0.11 |
| Entry fvg_ce, stop 0.3 ATR · Midday 11:30-14:30 | 1626 | 529 | 32.5% | 50.1% | -0.04 | -0.01 | 0.92 | -20.92 | -30.78 | -0.02 | -0.06 |
| Entry fvg_ce, stop 0.3 ATR · Stocks only | 1975 | 589 | 29.8% | 48.6% | -0.05 | -0.01 | 0.9 | -28.71 | -43.47 | -0.04 | -0.05 |
| Entry fvg_ce, stop 0.3 ATR · R:R to T2 2.5+ | 2628 | 956 | 36.4% | 47.0% | -0.09 | -0.03 | 0.83 | -85.23 | -105.09 | -0.08 | -0.1 |
| Entry fvg_ce, stop 0.3 ATR · Risk 0.15%+ | 2836 | 872 | 30.7% | 49.5% | -0.01 | -0.0 | 0.98 | -7.54 | -40.93 | -0.01 | -0.01 |
| Entry fvg_ce, stop 0.3 ATR · Midday + R:R 2.5+ + risk 0.15%+ | 1098 | 370 | 33.7% | 52.2% | 0.02 | 0.01 | 1.05 | 8.6 | -16.67 | 0.1 | -0.05 |
| Entry blend, stop 0.1 ATR · All qualified | 3481 | 1257 | 36.1% | 45.4% | -0.11 | -0.04 | 0.79 | -141.69 | -158.76 | -0.11 | -0.12 |
| Entry blend, stop 0.1 ATR · Plan window (by 11:30) | 974 | 436 | 44.8% | 44.0% | -0.18 | -0.08 | 0.68 | -76.95 | -78.48 | -0.21 | -0.14 |
| Entry blend, stop 0.1 ATR · Midday 11:30-14:30 | 1626 | 553 | 34.0% | 48.3% | -0.05 | -0.02 | 0.89 | -29.75 | -40.86 | -0.07 | -0.04 |
| Entry blend, stop 0.1 ATR · Stocks only | 1975 | 614 | 31.1% | 45.9% | -0.07 | -0.02 | 0.85 | -46.04 | -57.3 | -0.11 | -0.04 |
| Entry blend, stop 0.1 ATR · R:R to T2 2.5+ | 2628 | 993 | 37.8% | 45.0% | -0.12 | -0.05 | 0.79 | -118.53 | -140.68 | -0.12 | -0.12 |
| Entry blend, stop 0.1 ATR · Risk 0.15%+ | 2836 | 910 | 32.1% | 48.0% | -0.02 | -0.01 | 0.95 | -19.94 | -61.02 | -0.02 | -0.03 |
| Entry blend, stop 0.1 ATR · Midday + R:R 2.5+ + risk 0.15%+ | 1098 | 381 | 34.7% | 48.8% | -0.02 | -0.01 | 0.95 | -8.4 | -24.13 | 0.0 | -0.05 |
| Entry blend, stop 0.3 ATR · All qualified | 3481 | 1257 | 36.1% | 47.8% | -0.1 | -0.03 | 0.81 | -120.3 | -136.07 | -0.08 | -0.12 |
| Entry blend, stop 0.3 ATR · Plan window (by 11:30) | 974 | 436 | 44.8% | 46.3% | -0.16 | -0.07 | 0.68 | -71.71 | -72.8 | -0.2 | -0.12 |
| Entry blend, stop 0.3 ATR · Midday 11:30-14:30 | 1626 | 553 | 34.0% | 50.8% | -0.03 | -0.01 | 0.93 | -18.47 | -29.81 | -0.02 | -0.05 |
| Entry blend, stop 0.3 ATR · Stocks only | 1975 | 614 | 31.1% | 48.4% | -0.06 | -0.02 | 0.86 | -39.31 | -50.19 | -0.06 | -0.07 |
| Entry blend, stop 0.3 ATR · R:R to T2 2.5+ | 2628 | 993 | 37.8% | 47.9% | -0.09 | -0.04 | 0.82 | -92.8 | -113.59 | -0.07 | -0.11 |
| Entry blend, stop 0.3 ATR · Risk 0.15%+ | 2836 | 910 | 32.1% | 50.4% | -0.01 | -0.0 | 0.98 | -8.91 | -43.44 | 0.01 | -0.03 |
| Entry blend, stop 0.3 ATR · Midday + R:R 2.5+ + risk 0.15%+ | 1098 | 381 | 34.7% | 52.0% | 0.01 | 0.0 | 1.02 | 3.16 | -17.84 | 0.08 | -0.06 |
| Entry ote_62, stop 0.1 ATR · All qualified | 3481 | 1197 | 34.4% | 43.9% | -0.09 | -0.03 | 0.84 | -110.53 | -136.25 | -0.11 | -0.08 |
| Entry ote_62, stop 0.1 ATR · Plan window (by 11:30) | 974 | 409 | 42.0% | 40.8% | -0.18 | -0.07 | 0.71 | -71.7 | -73.09 | -0.24 | -0.11 |
| Entry ote_62, stop 0.1 ATR · Midday 11:30-14:30 | 1626 | 523 | 32.2% | 46.7% | -0.03 | -0.01 | 0.94 | -17.66 | -38.99 | -0.08 | 0.01 |
| Entry ote_62, stop 0.1 ATR · Stocks only | 1975 | 582 | 29.5% | 44.3% | -0.05 | -0.01 | 0.91 | -26.78 | -47.69 | -0.06 | -0.03 |
| Entry ote_62, stop 0.1 ATR · R:R to T2 2.5+ | 2628 | 954 | 36.3% | 43.6% | -0.1 | -0.04 | 0.83 | -96.58 | -126.72 | -0.12 | -0.09 |
| Entry ote_62, stop 0.1 ATR · Risk 0.15%+ | 2836 | 852 | 30.0% | 45.8% | -0.01 | -0.0 | 0.98 | -6.81 | -58.52 | -0.01 | -0.01 |
| Entry ote_62, stop 0.1 ATR · Midday + R:R 2.5+ + risk 0.15%+ | 1098 | 363 | 33.1% | 47.1% | 0.01 | 0.0 | 1.03 | 4.77 | -22.42 | 0.01 | 0.02 |
| Entry ote_62, stop 0.3 ATR · All qualified | 3481 | 1197 | 34.4% | 46.8% | -0.08 | -0.03 | 0.86 | -90.97 | -114.9 | -0.07 | -0.08 |
| Entry ote_62, stop 0.3 ATR · Plan window (by 11:30) | 974 | 409 | 42.0% | 44.0% | -0.16 | -0.07 | 0.71 | -65.45 | -66.47 | -0.22 | -0.1 |
| Entry ote_62, stop 0.3 ATR · Midday 11:30-14:30 | 1626 | 523 | 32.2% | 49.3% | -0.02 | -0.01 | 0.96 | -9.32 | -27.85 | -0.03 | -0.01 |
| Entry ote_62, stop 0.3 ATR · Stocks only | 1975 | 582 | 29.5% | 47.6% | -0.04 | -0.01 | 0.93 | -20.48 | -42.7 | -0.01 | -0.06 |
| Entry ote_62, stop 0.3 ATR · R:R to T2 2.5+ | 2628 | 954 | 36.3% | 47.0% | -0.08 | -0.03 | 0.86 | -71.63 | -99.99 | -0.06 | -0.09 |
| Entry ote_62, stop 0.3 ATR · Risk 0.15%+ | 2836 | 852 | 30.0% | 48.8% | 0.01 | 0.0 | 1.01 | 4.88 | -39.76 | 0.02 | -0.01 |
| Entry ote_62, stop 0.3 ATR · Midday + R:R 2.5+ + risk 0.15%+ | 1098 | 363 | 33.1% | 50.4% | 0.04 | 0.01 | 1.08 | 13.02 | -17.37 | 0.08 | -0.01 |
| Entry tl_line, stop 0.1 ATR · All qualified | 3481 | 4 | 0.1% | 75.0% | 0.52 | 0.0 | 2.93 | 2.07 | -1.07 | 0.43 | 0.6 |
| Entry tl_line, stop 0.1 ATR · Plan window (by 11:30) | 974 | 1 | 0.1% | 100.0% | 0.32 | 0.0 |  | 0.32 | 0.0 |  | 0.32 |
| Entry tl_line, stop 0.1 ATR · Midday 11:30-14:30 | 1626 | 3 | 0.2% | 66.7% | -0.07 | -0.0 | 0.8 | -0.21 | -1.07 | 0.32 | -0.27 |
| Entry tl_line, stop 0.1 ATR · Stocks only | 1975 | 3 | 0.2% | 66.7% | -0.07 | -0.0 | 0.8 | -0.21 | -1.07 | 0.32 | -0.27 |
| Entry tl_line, stop 0.1 ATR · R:R to T2 2.5+ | 2628 | 4 | 0.2% | 75.0% | 0.52 | 0.0 | 2.93 | 2.07 | -1.07 | 0.43 | 0.6 |
| Entry tl_line, stop 0.1 ATR · Risk 0.15%+ | 2836 | 4 | 0.1% | 75.0% | 0.52 | 0.0 | 2.93 | 2.07 | -1.07 | 0.43 | 0.6 |
| Entry tl_line, stop 0.1 ATR · Midday + R:R 2.5+ + risk 0.15%+ | 1098 | 3 | 0.3% | 66.7% | -0.07 | -0.0 | 0.8 | -0.21 | -1.07 | 0.32 | -0.27 |
| Entry tl_line, stop 0.3 ATR · All qualified | 3481 | 4 | 0.1% | 75.0% | 0.39 | 0.0 | 2.48 | 1.57 | -1.06 | 0.36 | 0.43 |
| Entry tl_line, stop 0.3 ATR · Plan window (by 11:30) | 974 | 1 | 0.1% | 100.0% | 0.29 | 0.0 |  | 0.29 | 0.0 |  | 0.29 |
| Entry tl_line, stop 0.3 ATR · Midday 11:30-14:30 | 1626 | 3 | 0.2% | 66.7% | -0.12 | -0.0 | 0.67 | -0.35 | -1.06 | 0.29 | -0.32 |
| Entry tl_line, stop 0.3 ATR · Stocks only | 1975 | 3 | 0.2% | 66.7% | -0.12 | -0.0 | 0.67 | -0.35 | -1.06 | 0.29 | -0.32 |
| Entry tl_line, stop 0.3 ATR · R:R to T2 2.5+ | 2628 | 4 | 0.2% | 75.0% | 0.39 | 0.0 | 2.48 | 1.57 | -1.06 | 0.36 | 0.43 |
| Entry tl_line, stop 0.3 ATR · Risk 0.15%+ | 2836 | 4 | 0.1% | 75.0% | 0.39 | 0.0 | 2.48 | 1.57 | -1.06 | 0.36 | 0.43 |
| Entry tl_line, stop 0.3 ATR · Midday + R:R 2.5+ + risk 0.15%+ | 1098 | 3 | 0.3% | 66.7% | -0.12 | -0.0 | 0.67 | -0.35 | -1.06 | 0.29 | -0.32 |
| Scaled ladder_equal (fvg_edge 33%, blend 33%, ote_mid 33%) · All qualified | 3481 | 1457 | 41.9% | 51.1% | -0.09 | -0.04 | 0.8 | -134.22 | -150.86 | -0.09 | -0.1 |
| Scaled ladder_equal (fvg_edge 33%, blend 33%, ote_mid 33%) · Plan window (by 11:30) | 974 | 491 | 50.4% | 49.5% | -0.15 | -0.08 | 0.69 | -74.0 | -75.54 | -0.16 | -0.14 |
| Scaled ladder_equal (fvg_edge 33%, blend 33%, ote_mid 33%) · Midday 11:30-14:30 | 1626 | 644 | 39.6% | 53.9% | -0.05 | -0.02 | 0.89 | -31.35 | -41.3 | -0.06 | -0.04 |
| Scaled ladder_equal (fvg_edge 33%, blend 33%, ote_mid 33%) · Stocks only | 1975 | 716 | 36.3% | 51.8% | -0.06 | -0.02 | 0.86 | -42.56 | -54.53 | -0.09 | -0.03 |
| Scaled ladder_equal (fvg_edge 33%, blend 33%, ote_mid 33%) · R:R to T2 2.5+ | 2628 | 1138 | 43.3% | 50.7% | -0.1 | -0.04 | 0.79 | -114.44 | -136.37 | -0.1 | -0.1 |
| Scaled ladder_equal (fvg_edge 33%, blend 33%, ote_mid 33%) · Risk 0.15%+ | 2836 | 1062 | 37.4% | 53.9% | -0.02 | -0.01 | 0.96 | -18.61 | -60.12 | -0.0 | -0.03 |
| Scaled ladder_equal (fvg_edge 33%, blend 33%, ote_mid 33%) · Midday + R:R 2.5+ + risk 0.15%+ | 1098 | 440 | 40.1% | 54.5% | -0.01 | -0.01 | 0.96 | -6.21 | -21.93 | -0.01 | -0.02 |
| Scaled ladder_deep (fvg_edge 20%, blend 30%, ote_mid 50%) · All qualified | 3481 | 1457 | 41.9% | 51.4% | -0.09 | -0.04 | 0.81 | -132.49 | -152.03 | -0.09 | -0.1 |
| Scaled ladder_deep (fvg_edge 20%, blend 30%, ote_mid 50%) · Plan window (by 11:30) | 974 | 491 | 50.4% | 49.9% | -0.15 | -0.08 | 0.69 | -73.78 | -75.4 | -0.17 | -0.13 |
| Scaled ladder_deep (fvg_edge 20%, blend 30%, ote_mid 50%) · Midday 11:30-14:30 | 1626 | 644 | 39.6% | 54.3% | -0.04 | -0.02 | 0.9 | -27.31 | -38.98 | -0.05 | -0.03 |
| Scaled ladder_deep (fvg_edge 20%, blend 30%, ote_mid 50%) · Stocks only | 1975 | 716 | 36.3% | 52.5% | -0.05 | -0.02 | 0.88 | -35.52 | -50.6 | -0.08 | -0.02 |
| Scaled ladder_deep (fvg_edge 20%, blend 30%, ote_mid 50%) · R:R to T2 2.5+ | 2628 | 1138 | 43.3% | 50.8% | -0.1 | -0.04 | 0.8 | -111.86 | -136.85 | -0.1 | -0.1 |
| Scaled ladder_deep (fvg_edge 20%, blend 30%, ote_mid 50%) · Risk 0.15%+ | 2836 | 1062 | 37.4% | 54.3% | -0.01 | -0.0 | 0.97 | -12.2 | -57.72 | 0.0 | -0.03 |
| Scaled ladder_deep (fvg_edge 20%, blend 30%, ote_mid 50%) · Midday + R:R 2.5+ + risk 0.15%+ | 1098 | 440 | 40.1% | 55.0% | 0.0 | 0.0 | 1.0 | 0.09 | -21.89 | 0.0 | -0.0 |

## 8. Trade management (systematic, qualified, triggered)

| Method | Trades | Avg R | Win rate |
|---|---|---|---|
| Plan: half at T1, rest to T2 (gross) | 1100 | 0.09 | 42.8% |
| Plan, net of costs | 1100 | -0.11 | 41.2% |
| Full position to T1 (gross) | 1100 | 0.1 | 43.1% |
| Full position to T2 (gross) | 1100 | 0.1 | 37.5% |

## 10. v3 candidate tests (New York session, qualified, net of costs)

Confirmation entry = wait for price to reach the FVG, then enter on the first bar that closes beyond the prior 3 bars (bars used: {'1m': 2927, '5m': 152}). Runner = half at T1, rest to the close with a breakeven stop. 1st/2nd half columns are the out-of-sample check.

| Group | Setups | Triggered | Trigger rate | Win rate | Avg R | Expectancy R | Profit factor | Total R | Max DD R | 1st half avg R | 2nd half avg R |
|---|---|---|---|---|---|---|---|---|---|---|---|
| All (New York) · Current plan | 3082 | 907 | 29.4% | 42.6% | -0.08 | -0.02 | 0.86 | -75.46 | -102.05 | -0.1 | -0.07 |
| All (New York) · Runner to the close | 3082 | 907 | 29.4% | 42.6% | -0.08 | -0.02 | 0.87 | -71.81 | -100.16 | -0.07 | -0.08 |
| All (New York) · Full position to T2 | 3082 | 907 | 29.4% | 37.9% | -0.08 | -0.02 | 0.89 | -69.61 | -108.61 | -0.1 | -0.05 |
| All (New York) · Confirmation entry | 3082 | 1003 | 32.5% | 52.1% | -0.1 | -0.03 | 0.74 | -99.44 | -100.4 | -0.11 | -0.09 |
| v3: 11:30-14:30 + risk 0.3%+ + FVG 0.5+ ATR · Current plan | 798 | 155 | 19.4% | 48.4% | 0.09 | 0.02 | 1.19 | 14.07 | -13.05 | 0.1 | 0.08 |
| v3: 11:30-14:30 + risk 0.3%+ + FVG 0.5+ ATR · Runner to the close | 798 | 155 | 19.4% | 48.4% | 0.08 | 0.02 | 1.16 | 12.03 | -13.05 | 0.1 | 0.06 |
| v3: 11:30-14:30 + risk 0.3%+ + FVG 0.5+ ATR · Full position to T2 | 798 | 155 | 19.4% | 45.8% | 0.12 | 0.02 | 1.22 | 18.38 | -15.55 | 0.1 | 0.14 |
| v3: 11:30-14:30 + risk 0.3%+ + FVG 0.5+ ATR · Confirmation entry | 798 | 214 | 26.8% | 57.0% | 0.03 | 0.01 | 1.11 | 6.46 | -8.1 | 0.08 | -0.02 |
| v3 + longs · Current plan | 651 | 118 | 18.1% | 52.5% | 0.19 | 0.04 | 1.42 | 22.92 | -8.87 | 0.22 | 0.17 |
| v3 + longs · Runner to the close | 651 | 118 | 18.1% | 52.5% | 0.18 | 0.03 | 1.38 | 20.88 | -8.87 | 0.22 | 0.14 |
| v3 + longs · Full position to T2 | 651 | 118 | 18.1% | 48.3% | 0.19 | 0.03 | 1.37 | 22.07 | -10.61 | 0.19 | 0.18 |
| v3 + longs · Confirmation entry | 651 | 174 | 26.7% | 58.0% | 0.06 | 0.01 | 1.2 | 9.73 | -6.21 | 0.13 | -0.02 |
| v3 + VWAP side · Current plan | 602 | 89 | 14.8% | 51.7% | 0.08 | 0.01 | 1.18 | 7.12 | -6.87 | 0.06 | 0.1 |
| v3 + VWAP side · Runner to the close | 602 | 89 | 14.8% | 51.7% | 0.06 | 0.01 | 1.13 | 5.08 | -6.87 | 0.06 | 0.05 |
| v3 + VWAP side · Full position to T2 | 602 | 89 | 14.8% | 49.4% | 0.09 | 0.01 | 1.17 | 7.7 | -8.65 | 0.02 | 0.15 |
| v3 + VWAP side · Confirmation entry | 602 | 134 | 22.3% | 53.0% | 0.02 | 0.0 | 1.07 | 2.51 | -6.91 | 0.06 | -0.02 |
| v3 + in play (open volume 1.5x+) · Current plan | 115 | 22 | 19.1% | 45.5% | 0.08 | 0.02 | 1.21 | 1.79 | -3.73 | -0.14 | 0.3 |
| v3 + in play (open volume 1.5x+) · Runner to the close | 115 | 22 | 19.1% | 45.5% | 0.08 | 0.02 | 1.21 | 1.79 | -3.73 | -0.14 | 0.3 |
| v3 + in play (open volume 1.5x+) · Full position to T2 | 115 | 22 | 19.1% | 45.5% | -0.08 | -0.02 | 0.83 | -1.79 | -4.62 | -0.18 | 0.02 |
| v3 + in play (open volume 1.5x+) · Confirmation entry | 115 | 30 | 26.1% | 60.0% | 0.06 | 0.01 | 1.18 | 1.66 | -2.61 | 0.02 | 0.09 |
| v3 + longs + VWAP side · Current plan | 512 | 73 | 14.3% | 53.4% | 0.16 | 0.02 | 1.36 | 11.69 | -5.26 | 0.12 | 0.2 |
| v3 + longs + VWAP side · Runner to the close | 512 | 73 | 14.3% | 53.4% | 0.13 | 0.02 | 1.3 | 9.65 | -5.26 | 0.12 | 0.14 |
| v3 + longs + VWAP side · Full position to T2 | 512 | 73 | 14.3% | 52.1% | 0.2 | 0.03 | 1.44 | 14.84 | -5.56 | 0.14 | 0.26 |
| v3 + longs + VWAP side · Confirmation entry | 512 | 115 | 22.5% | 53.0% | 0.03 | 0.01 | 1.09 | 2.9 | -7.31 | 0.09 | -0.04 |
| VWAP side only · Current plan | 2103 | 554 | 26.3% | 41.7% | -0.14 | -0.04 | 0.77 | -77.94 | -78.43 | -0.16 | -0.12 |
| VWAP side only · Runner to the close | 2103 | 554 | 26.3% | 41.7% | -0.14 | -0.04 | 0.77 | -77.68 | -81.6 | -0.12 | -0.16 |
| VWAP side only · Full position to T2 | 2103 | 554 | 26.3% | 38.1% | -0.14 | -0.04 | 0.79 | -75.62 | -85.9 | -0.15 | -0.12 |
| VWAP side only · Confirmation entry | 2103 | 642 | 30.5% | 50.9% | -0.12 | -0.04 | 0.7 | -74.78 | -75.48 | -0.11 | -0.12 |
| In play only · Current plan | 382 | 103 | 27.0% | 37.9% | -0.24 | -0.06 | 0.63 | -24.42 | -32.79 | -0.51 | 0.03 |
| In play only · Runner to the close | 382 | 103 | 27.0% | 37.9% | -0.25 | -0.07 | 0.61 | -25.43 | -33.9 | -0.51 | 0.01 |
| In play only · Full position to T2 | 382 | 103 | 27.0% | 33.0% | -0.35 | -0.1 | 0.51 | -36.53 | -41.15 | -0.59 | -0.12 |
| In play only · Confirmation entry | 382 | 121 | 31.7% | 52.9% | -0.11 | -0.04 | 0.71 | -13.7 | -23.63 | -0.27 | 0.04 |

## 11. Trendline retest confluence (New York session, qualified, net of costs)

Trendline = the falling line across the lower highs into the sweep (rising line across higher lows for shorts), broken by a close and not failed. Confluence = its level at the snapshot sits in the entry zone (FVG near edge to entry) within 0.25 ATR. Retest at fill = the line was within 0.3 ATR of the fill price when the order filled. Only rows recorded since Nov 4, 2026 (rerun the backtest to fill history).

| Group | Setups | Triggered | Trigger rate | Win rate | Avg R | Expectancy R | Profit factor | Total R | Max DD R | 1st half avg R | 2nd half avg R |
|---|---|---|---|---|---|---|---|---|---|---|---|
| All (New York, trendline recorded) · current plan | 169 | 60 | 35.5% | 38.3% | -0.34 | -0.12 | 0.52 | -20.32 | -22.62 | -0.3 | -0.38 |
| No trendline found/broken · current plan | 92 | 34 | 37.0% | 35.3% | -0.46 | -0.17 | 0.39 | -15.72 | -18.73 | -0.53 | -0.4 |
| Trendline found and broken · current plan | 77 | 26 | 33.8% | 42.3% | -0.18 | -0.06 | 0.71 | -4.61 | -7.21 | -0.0 | -0.35 |
| Trendline confluence at snapshot · current plan | 9 | 3 | 33.3% | 66.7% | 0.11 | 0.04 | 1.31 | 0.33 | -1.07 | 0.84 | -0.25 |
| No confluence at snapshot · current plan | 160 | 57 | 35.6% | 36.8% | -0.36 | -0.13 | 0.5 | -20.66 | -22.95 | -0.32 | -0.41 |
| Confluence, 3+ touches · current plan | 2 | 0 | 0.0% |  |  | 0.0 |  | 0.0 | 0.0 |  |  |
| Confluence + longs · current plan | 7 | 3 | 42.9% | 66.7% | 0.11 | 0.05 | 1.31 | 0.33 | -1.07 | 0.84 | -0.25 |
| Confluence + midday (11:30-14:30) · current plan | 7 | 3 | 42.9% | 66.7% | 0.11 | 0.05 | 1.31 | 0.33 | -1.07 | 0.84 | -0.25 |
| Confluence + risk 0.3%+ · current plan | 6 | 2 | 33.3% | 50.0% | -0.12 | -0.04 | 0.78 | -0.24 | -1.07 | 0.84 | -1.07 |
| Confluence + VWAP side · current plan | 3 | 1 | 33.3% | 100.0% | 0.84 | 0.28 |  | 0.84 | 0.0 |  | 0.84 |
| Confluence + longs + midday + risk 0.3%+ · current plan | 4 | 2 | 50.0% | 50.0% | -0.12 | -0.06 | 0.78 | -0.24 | -1.07 | 0.84 | -1.07 |
| Fill was a trendline retest (any setup) | 169 | 2 | 1.2% | 50.0% | -0.25 | -0.0 | 0.53 | -0.5 | -1.07 | 0.57 | -1.07 |
| Fill was a trendline retest + longs | 148 | 2 | 1.4% | 50.0% | -0.25 | -0.0 | 0.53 | -0.5 | -1.07 | 0.57 | -1.07 |
| Entry at the trendline (stop 0.1 ATR) | 9 | 3 | 33.3% | 66.7% | -0.07 | -0.02 | 0.8 | -0.21 | -1.07 | 0.32 | -0.27 |
| Entry at the trendline (stop 0.3 ATR) | 9 | 3 | 33.3% | 66.7% | -0.12 | -0.04 | 0.67 | -0.35 | -1.06 | 0.29 | -0.32 |

## 9. Automatic changes in this run

| Key | Old | New | Evidence |
|---|---|---|---|
| None |  |  |  |
