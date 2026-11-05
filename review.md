# FVG review: 2026-11-05 16:28 ET (Daily)

Sessions: 127 (2026-05-07 to 2026-11-05). Config version 1.

## 1. Strategy performance (qualified setups; results net of costs)

Costs: 0.02% of price per side. Entries allowed until 15:30 ET.

| Group | Setups | Triggered | Trigger rate | Win rate | Avg R | Expectancy R | Profit factor | Total R | Max DD R | 1st half avg R | 2nd half avg R |
|---|---|---|---|---|---|---|---|---|---|---|---|
| Live dashboard snapshots | 63 | 20 | 31.7% | 45.0% | -0.0 | -0.0 | 1.0 | -0.02 | -4.34 | 0.25 | -0.25 |
| Daily full-session replays | 65 | 26 | 40.0% | 50.0% | 0.01 | 0.01 | 1.03 | 0.37 | -7.09 | 0.2 | -0.18 |
| Backtest | 3224 | 1010 | 31.3% | 41.1% | -0.1 | -0.03 | 0.84 | -104.96 | -135.21 | -0.08 | -0.13 |
| Systematic (replays + backtest) | 3289 | 1036 | 31.5% | 41.3% | -0.1 | -0.03 | 0.84 | -104.59 | -135.21 | -0.09 | -0.11 |
| Systematic, before cost (gross) | 3289 | 1036 | 31.5% | 43.0% | 0.1 | 0.03 | 1.2 | 104.36 | -37.49 | 0.08 | 0.12 |
| Systematic, plan window only (New York, formed by 11:30) | 930 | 366 | 39.4% | 39.1% | -0.17 | -0.07 | 0.73 | -62.25 | -63.51 | -0.24 | -0.1 |
| Live top-5 suggestions only | 37 | 13 | 35.1% | 46.2% | -0.09 | -0.03 | 0.83 | -1.11 | -3.49 | -0.06 | -0.11 |
| Your actual trades | 1 | 1 |  | 0.0% | -1.77 |  |  | -1.77 |  |  |  |
| Stocks and ETFs, New York session only | 2797 | 818 | 29.2% | 42.4% | -0.08 | -0.02 | 0.87 | -63.84 | -91.99 | -0.07 | -0.08 |
| Futures, New York session | 138 | 45 | 32.6% | 48.9% | 0.06 | 0.02 | 1.1 | 2.58 | -9.25 | 0.39 | -0.26 |
| Futures, all 24-hour sessions | 492 | 218 | 44.3% | 37.2% | -0.19 | -0.08 | 0.74 | -40.75 | -47.51 | -0.29 | -0.08 |

## 1c. Futures by session (24-hour test; qualified, net of costs)

Asia and London use their own levels: prior-day high/low, the previous session's high/low, and the session's first 30 minutes.

| Group | Setups | Triggered | Trigger rate | Win rate | Avg R | Expectancy R | Profit factor | Total R | Max DD R | 1st half avg R | 2nd half avg R |
|---|---|---|---|---|---|---|---|---|---|---|---|
| Futures, Asia session (6 PM-midnight ET) | 163 | 70 | 42.9% | 30.0% | -0.25 | -0.11 | 0.67 | -17.77 | -19.47 | -0.27 | -0.24 |
| Futures, London session (2-8 AM ET) | 191 | 103 | 53.9% | 36.9% | -0.25 | -0.13 | 0.68 | -25.56 | -38.05 | -0.64 | 0.14 |
| Futures, NY session (9:30-4:00 ET) | 138 | 45 | 32.6% | 48.9% | 0.06 | 0.02 | 1.1 | 2.58 | -9.25 | 0.39 | -0.26 |
| CL=F Asia | 21 | 11 | 52.4% | 45.5% | 0.4 | 0.21 | 1.65 | 4.39 | -2.35 | -0.11 | 0.82 |
| CL=F London | 19 | 8 | 42.1% | 50.0% | 0.38 | 0.16 | 1.81 | 3.02 | -2.21 | -0.35 | 1.1 |
| CL=F NY | 20 | 7 | 35.0% | 28.6% | -0.38 | -0.13 | 0.5 | -2.66 | -3.18 | -1.06 | 0.13 |
| ES=F Asia | 15 | 6 | 40.0% | 33.3% | -0.45 | -0.18 | 0.43 | -2.72 | -4.64 | 0.28 | -1.18 |
| ES=F London | 22 | 15 | 68.2% | 46.7% | 0.27 | 0.19 | 1.44 | 4.11 | -5.2 | -0.5 | 0.95 |
| ES=F NY | 17 | 8 | 47.1% | 75.0% | 0.85 | 0.4 | 5.84 | 6.83 | -1.41 | 1.23 | 0.48 |
| GC=F Asia | 33 | 22 | 66.7% | 27.3% | -0.02 | -0.01 | 0.97 | -0.43 | -10.46 | 0.18 | -0.22 |
| GC=F London | 15 | 6 | 40.0% | 66.7% | 0.35 | 0.14 | 2.0 | 2.09 | -1.05 | 0.05 | 0.64 |
| GC=F NY | 14 | 4 | 28.6% | 50.0% | 0.28 | 0.08 | 1.54 | 1.11 | -1.04 | 0.66 | -0.1 |
| NQ=F Asia | 12 | 6 | 50.0% | 16.7% | -0.74 | -0.37 | 0.15 | -4.41 | -5.19 | -1.04 | -0.43 |
| NQ=F London | 16 | 7 | 43.8% | 0.0% | -0.79 | -0.35 | 0.0 | -5.53 | -5.53 | -1.03 | -0.61 |
| NQ=F NY | 12 | 4 | 33.3% | 25.0% | -0.32 | -0.11 | 0.38 | -1.29 | -2.08 | -1.01 | 0.37 |
| RTY=F Asia | 19 | 5 | 26.3% | 60.0% | 0.4 | 0.11 | 1.9 | 2.01 | -2.23 | 1.12 | -0.08 |
| RTY=F London | 29 | 20 | 69.0% | 25.0% | -0.44 | -0.31 | 0.43 | -8.9 | -10.2 | -0.79 | -0.1 |
| RTY=F NY | 15 | 2 | 13.3% | 50.0% | -0.1 | -0.01 | 0.82 | -0.19 | -1.04 | -1.04 | 0.85 |
| YM=F Asia | 20 | 6 | 30.0% | 16.7% | -0.8 | -0.24 | 0.15 | -4.81 | -5.67 | -0.51 | -1.09 |
| YM=F London | 27 | 14 | 51.9% | 57.1% | 0.38 | 0.2 | 1.78 | 5.29 | -2.29 | 0.32 | 0.44 |
| YM=F NY | 14 | 2 | 14.3% | 50.0% | 1.16 | 0.17 | 3.24 | 2.31 | -1.03 | 3.35 | -1.03 |
| ZB=F Asia | 15 | 5 | 33.3% | 20.0% | -1.21 | -0.4 | 0.02 | -6.04 | -6.04 | -0.93 | -1.4 |
| ZB=F London | 12 | 7 | 58.3% | 42.9% | -0.33 | -0.19 | 0.57 | -2.28 | -3.38 | -0.39 | -0.28 |
| ZB=F NY | 14 | 6 | 42.9% | 66.7% | 0.6 | 0.26 | 2.23 | 3.62 | -1.6 | 0.58 | 0.63 |
| ZF=F Asia | 14 | 4 | 28.6% | 25.0% | -0.74 | -0.21 | 0.21 | -2.96 | -3.73 | -0.87 | -0.61 |
| ZF=F London | 19 | 12 | 63.2% | 25.0% | -1.1 | -0.7 | 0.2 | -13.21 | -13.21 | -1.84 | -0.36 |
| ZF=F NY | 14 | 6 | 42.9% | 50.0% | -0.72 | -0.31 | 0.14 | -4.31 | -4.64 | -0.53 | -0.9 |
| ZN=F Asia | 9 | 4 | 44.4% | 25.0% | -0.49 | -0.22 | 0.37 | -1.95 | -2.63 | -1.31 | 0.34 |
| ZN=F London | 13 | 7 | 53.8% | 28.6% | -0.7 | -0.38 | 0.36 | -4.88 | -4.88 | -0.59 | -0.78 |
| ZN=F NY | 8 | 5 | 62.5% | 40.0% | -0.31 | -0.19 | 0.54 | -1.53 | -1.81 | -0.77 | 0.0 |
| ZS=F Asia | 5 | 1 | 20.0% | 0.0% | -0.85 | -0.17 | 0.0 | -0.85 | -0.85 |  | -0.85 |
| ZS=F London | 19 | 7 | 36.8% | 28.6% | -0.75 | -0.28 | 0.3 | -5.28 | -7.26 | -0.78 | -0.73 |
| ZS=F NY | 10 | 1 | 10.0% | 0.0% | -1.32 | -0.13 | 0.0 | -1.32 | -1.32 |  | -1.32 |

## 2. New York session: by asset, side, time of day, risk size (systematic, qualified)

| Group | Setups | Triggered | Trigger rate | Win rate | Avg R | Expectancy R | Profit factor | Total R | Max DD R | 1st half avg R | 2nd half avg R |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ETF | 915 | 312 | 34.1% | 41.7% | -0.16 | -0.05 | 0.77 | -48.99 | -63.67 | -0.06 | -0.25 |
| Stock | 1882 | 506 | 26.9% | 42.9% | -0.03 | -0.01 | 0.95 | -14.85 | -41.36 | -0.07 | 0.02 |
| Future | 138 | 45 | 32.6% | 48.9% | 0.06 | 0.02 | 1.1 | 2.58 | -9.25 | 0.39 | -0.26 |
| Leveraged/inverse ETFs | 135 | 44 | 32.6% | 50.0% | 0.33 | 0.11 | 1.76 | 14.65 | -6.42 | 0.77 | -0.11 |
| LONG | 2603 | 786 | 30.2% | 42.7% | -0.07 | -0.02 | 0.88 | -58.19 | -85.82 | -0.08 | -0.07 |
| SHORT | 332 | 77 | 23.2% | 42.9% | -0.04 | -0.01 | 0.9 | -3.06 | -9.63 | -0.08 | -0.0 |
| Formed 10:00-10:30 | 304 | 147 | 48.4% | 32.0% | -0.26 | -0.13 | 0.64 | -38.92 | -38.92 | -0.3 | -0.23 |
| Formed 10:30-11:30 | 579 | 205 | 35.4% | 43.4% | -0.11 | -0.04 | 0.8 | -23.14 | -33.43 | -0.26 | 0.03 |
| Formed 11:30-13:00 | 821 | 259 | 31.5% | 49.4% | 0.02 | 0.01 | 1.04 | 5.27 | -13.55 | 0.04 | 0.0 |
| Formed 13:00-14:30 | 724 | 192 | 26.5% | 40.1% | -0.08 | -0.02 | 0.87 | -15.32 | -34.2 | -0.2 | 0.04 |
| Formed 14:30-16:00 | 507 | 60 | 11.8% | 46.7% | 0.18 | 0.02 | 1.31 | 10.84 | -16.45 | 0.73 | -0.37 |
| Risk 0-0.15% of price | 600 | 290 | 48.3% | 33.8% | -0.4 | -0.19 | 0.54 | -115.99 | -120.27 | -0.42 | -0.38 |
| Risk 0.15-0.3% of price | 653 | 242 | 37.1% | 41.7% | -0.08 | -0.03 | 0.87 | -19.48 | -45.15 | -0.13 | -0.03 |
| Risk 0.3-0.6% of price | 1036 | 284 | 27.4% | 45.8% | 0.07 | 0.02 | 1.13 | 19.33 | -20.24 | 0.05 | 0.08 |
| Risk 0.6%+ | 1000 | 220 | 22.0% | 45.0% | 0.05 | 0.01 | 1.11 | 11.54 | -14.27 | 0.08 | 0.02 |

## 2b. Short guardrails (systematic; shorts use full exit at T1, breakeven at +0.5R, 60-minute time stop)

Sizing: longs 1.25% risk (cap 5.0% of account), shorts 0.5% risk (cap 2.5%). Results here are in R, before sizing.

| Group | Setups | Triggered | Trigger rate | Win rate | Avg R | Expectancy R | Profit factor | Total R | Max DD R | 1st half avg R | 2nd half avg R |
|---|---|---|---|---|---|---|---|---|---|---|---|
| Longs passing the normal filters | 2956 | 959 | 32.4% | 41.2% | -0.11 | -0.03 | 0.84 | -101.53 | -129.84 | -0.1 | -0.11 |
| Shorts passing the normal filters (before guardrails) | 2122 | 748 | 35.2% | 27.7% | -0.17 | -0.06 | 0.65 | -129.22 | -131.26 | -0.07 | -0.27 |
| Shorts passing every guardrail (traded) | 333 | 77 | 23.1% | 42.9% | -0.04 | -0.01 | 0.9 | -3.06 | -9.63 | -0.08 | -0.0 |
| Shorts passing: bearish daily trend | 912 | 333 | 36.5% | 30.0% | -0.19 | -0.07 | 0.62 | -64.77 | -74.37 | -0.12 | -0.27 |
| Shorts failing: bearish daily trend | 1210 | 415 | 34.3% | 25.8% | -0.16 | -0.05 | 0.68 | -64.46 | -65.07 | -0.08 | -0.23 |
| Shorts passing: PDH or 2+ level sweep | 1518 | 505 | 33.3% | 29.3% | -0.12 | -0.04 | 0.74 | -58.14 | -59.94 | -0.05 | -0.18 |
| Shorts failing: PDH or 2+ level sweep | 604 | 243 | 40.2% | 24.3% | -0.29 | -0.12 | 0.51 | -71.09 | -73.01 | -0.27 | -0.32 |
| Shorts passing: R:R to T2 3.0+ | 1547 | 544 | 35.2% | 27.8% | -0.18 | -0.06 | 0.64 | -98.76 | -102.06 | -0.07 | -0.3 |
| Shorts failing: R:R to T2 3.0+ | 575 | 204 | 35.5% | 27.5% | -0.15 | -0.05 | 0.67 | -30.47 | -38.04 | -0.1 | -0.2 |
| Shorts passing: risk 0.3%+ of price | 1151 | 337 | 29.3% | 32.0% | -0.03 | -0.01 | 0.91 | -10.96 | -25.88 | 0.06 | -0.12 |
| Shorts failing: risk 0.3%+ of price | 971 | 411 | 42.3% | 24.1% | -0.29 | -0.12 | 0.52 | -118.26 | -118.87 | -0.24 | -0.34 |
| Shorts passing: formed 10:30 or later | 1880 | 621 | 33.0% | 27.1% | -0.19 | -0.06 | 0.63 | -116.87 | -117.77 | -0.1 | -0.28 |
| Shorts failing: formed 10:30 or later | 242 | 127 | 52.5% | 30.7% | -0.1 | -0.05 | 0.77 | -12.35 | -20.84 | 0.1 | -0.29 |
| Shorts passing: not a leveraged ETF | 2035 | 722 | 35.5% | 27.3% | -0.19 | -0.07 | 0.62 | -137.86 | -138.47 | -0.1 | -0.28 |
| Shorts failing: not a leveraged ETF | 87 | 26 | 29.9% | 38.5% | 0.33 | 0.1 | 2.07 | 8.63 | -2.49 | 0.81 | -0.14 |

## 3. Outcomes (systematic, qualified)

| Outcome | Count | Share | Avg R |
|---|---|---|---|
| Not triggered (ran to T1 first) | 2072 | 63.0% | 0.0 |
| Stop | 493 | 15.0% | -1.22 |
| EOD exit | 210 | 6.4% | 0.18 |
| Not triggered (cutoff) | 181 | 5.5% | 0.0 |
| T1 then EOD | 141 | 4.3% | 1.83 |
| T1 then breakeven | 76 | 2.3% | 0.58 |
| T1 then T2 | 74 | 2.2% | 2.0 |
| Time stop | 26 | 0.8% | 0.46 |
| Breakeven stop | 16 | 0.5% | -0.1 |

## 4. Score calibration. A useful score shows results improving band by band.

| Group | Setups | Triggered | Trigger rate | Win rate | Avg R | Expectancy R | Profit factor | Total R | Max DD R | 1st half avg R | 2nd half avg R |
|---|---|---|---|---|---|---|---|---|---|---|---|
| Score 90+ | 20 | 12 | 60.0% | 75.0% | 0.92 | 0.55 | 6.01 | 11.09 | -2.22 | 1.18 | 0.67 |
| Score 75-89 | 1251 | 370 | 29.6% | 40.3% | -0.13 | -0.04 | 0.79 | -47.69 | -74.93 | -0.14 | -0.11 |
| Score 60-74 | 1799 | 556 | 30.9% | 42.6% | -0.06 | -0.02 | 0.9 | -34.26 | -53.11 | -0.01 | -0.11 |
| Score under 60 | 219 | 98 | 44.7% | 33.7% | -0.34 | -0.15 | 0.57 | -33.74 | -35.63 | -0.66 | -0.03 |

## 5. Factor attribution (all triggered systematic setups, qualified or not)

| Factor | Weight key | Weight | With | Avg R with | Without | Avg R without | Difference | Read |
|---|---|---|---|---|---|---|---|---|
| Prior-day level swept | sweep_pd | 20 | 2613 | -0.11 | 2926 | -0.15 | 0.04 | No clear effect |
| Only PM/OR level swept | sweep_other | 15 | 2321 | -0.13 | 3218 | -0.14 | 0.0 | No clear effect |
| FVG in discount/premium | zone | 10 | 2012 | -0.16 | 3527 | -0.12 | -0.05 | No clear effect |
| FVG overlaps OTE | ote | 15 | 1772 | -0.14 | 3767 | -0.13 | -0.01 | No clear effect |
| R:R to T1 of 2 or more | rr | 10 | 415 | -0.26 | 5124 | -0.12 | -0.14 | No clear effect |
| HTF bias aligned | bias | 10 | 2118 | -0.14 | 3421 | -0.13 | -0.01 | No clear effect |
| Displacement volume 1.5x+ | vol | 5 | 665 | -0.09 | 4874 | -0.14 | 0.05 | No clear effect |
| Formed 10:00-11:30 | time | 5 | 2598 | -0.18 | 2941 | -0.09 | -0.09 | No clear effect |
| Trendline retest confluence | tl | 10 | 13 | -0.03 | 41 | -0.16 | 0.13 | Not enough data |

## 6. Filter check (systematic)

| Group | Setups | Triggered | Trigger rate | Win rate | Avg R | Expectancy R | Profit factor | Total R | Max DD R | 1st half avg R | 2nd half avg R |
|---|---|---|---|---|---|---|---|---|---|---|---|
| Passed filters | 3289 | 1036 | 31.5% | 41.3% | -0.1 | -0.03 | 0.84 | -104.59 | -135.21 | -0.09 | -0.11 |
| Filtered out | 7524 | 4503 | 59.8% | 47.9% | -0.14 | -0.09 | 0.62 | -640.6 | -641.77 | -0.11 | -0.18 |
| No OTE overlap | 5596 | 3767 | 67.3% | 52.2% | -0.13 | -0.09 | 0.62 | -495.04 | -496.2 | -0.11 | -0.15 |
| OTE overlap, R:R to T2 1.5-2 | 139 | 65 | 46.8% | 29.2% | -0.3 | -0.14 | 0.5 | -19.41 | -19.76 | -0.24 | -0.36 |
| OTE overlap, R:R to T2 2-2.5 | 1156 | 339 | 29.3% | 36.0% | -0.15 | -0.04 | 0.74 | -49.35 | -55.24 | -0.11 | -0.18 |
| OTE overlap, R:R to T2 2.5-3 | 595 | 189 | 31.8% | 37.6% | -0.02 | -0.0 | 0.97 | -2.84 | -43.27 | -0.27 | 0.24 |
| OTE overlap, R:R to T2 3+ | 3327 | 1179 | 35.4% | 34.7% | -0.15 | -0.05 | 0.75 | -178.56 | -218.32 | -0.04 | -0.26 |

## 7. Improvement tests: entry type x stop buffer x filter (net of costs)

ote_mid = current entry (middle of the FVG/OTE overlap); fvg_edge = first touch of the gap; fvg_ce = gap midpoint; blend = halfway between the gap edge and ote_mid; ote_62 = first touch of the OTE zone; tl_line = limit at the broken trendline (only setups with trendline confluence). Scaled rows are in R of the full planned position (a partial fill counts only what filled).

| Group | Setups | Triggered | Trigger rate | Win rate | Avg R | Expectancy R | Profit factor | Total R | Max DD R | 1st half avg R | 2nd half avg R |
|---|---|---|---|---|---|---|---|---|---|---|---|
| Entry ote_mid, stop 0.1 ATR · All qualified | 3289 | 1036 | 31.5% | 41.3% | -0.1 | -0.03 | 0.84 | -104.58 | -135.19 | -0.09 | -0.11 |
| Entry ote_mid, stop 0.1 ATR · Plan window (by 11:30) | 930 | 366 | 39.4% | 39.1% | -0.17 | -0.07 | 0.73 | -62.24 | -63.51 | -0.24 | -0.1 |
| Entry ote_mid, stop 0.1 ATR · Midday 11:30-14:30 | 1545 | 451 | 29.2% | 45.5% | -0.02 | -0.01 | 0.96 | -10.04 | -35.77 | -0.05 | 0.0 |
| Entry ote_mid, stop 0.1 ATR · Stocks only | 1882 | 506 | 26.9% | 42.9% | -0.03 | -0.01 | 0.95 | -14.85 | -41.36 | -0.07 | 0.02 |
| Entry ote_mid, stop 0.1 ATR · R:R to T2 2.5+ | 2481 | 821 | 33.1% | 41.3% | -0.11 | -0.03 | 0.84 | -86.51 | -128.51 | -0.09 | -0.13 |
| Entry ote_mid, stop 0.1 ATR · Risk 0.15%+ | 2689 | 746 | 27.7% | 44.2% | 0.02 | 0.0 | 1.03 | 11.4 | -51.41 | 0.02 | 0.01 |
| Entry ote_mid, stop 0.1 ATR · Midday + R:R 2.5+ + risk 0.15%+ | 1043 | 321 | 30.8% | 47.0% | 0.06 | 0.02 | 1.12 | 19.88 | -22.62 | 0.04 | 0.09 |
| Entry ote_mid, stop 0.3 ATR · All qualified | 3289 | 1036 | 31.5% | 44.3% | -0.08 | -0.03 | 0.86 | -84.85 | -111.22 | -0.07 | -0.1 |
| Entry ote_mid, stop 0.3 ATR · Plan window (by 11:30) | 930 | 366 | 39.4% | 42.1% | -0.16 | -0.06 | 0.73 | -56.97 | -57.69 | -0.23 | -0.08 |
| Entry ote_mid, stop 0.3 ATR · Midday 11:30-14:30 | 1545 | 451 | 29.2% | 48.6% | -0.0 | -0.0 | 1.0 | -0.55 | -26.45 | 0.01 | -0.01 |
| Entry ote_mid, stop 0.3 ATR · Stocks only | 1882 | 506 | 26.9% | 46.0% | -0.02 | -0.01 | 0.95 | -12.63 | -38.05 | -0.03 | -0.02 |
| Entry ote_mid, stop 0.3 ATR · R:R to T2 2.5+ | 2481 | 821 | 33.1% | 44.8% | -0.08 | -0.02 | 0.87 | -61.96 | -98.84 | -0.05 | -0.11 |
| Entry ote_mid, stop 0.3 ATR · Risk 0.15%+ | 2689 | 746 | 27.7% | 47.3% | 0.03 | 0.01 | 1.05 | 19.32 | -36.54 | 0.04 | 0.01 |
| Entry ote_mid, stop 0.3 ATR · Midday + R:R 2.5+ + risk 0.15%+ | 1043 | 321 | 30.8% | 50.8% | 0.09 | 0.03 | 1.19 | 27.94 | -17.07 | 0.12 | 0.06 |
| Entry fvg_edge, stop 0.1 ATR · All qualified | 3289 | 1376 | 41.8% | 50.4% | -0.08 | -0.03 | 0.82 | -113.91 | -131.96 | -0.09 | -0.07 |
| Entry fvg_edge, stop 0.1 ATR · Plan window (by 11:30) | 930 | 468 | 50.3% | 50.0% | -0.13 | -0.07 | 0.71 | -62.69 | -63.14 | -0.13 | -0.14 |
| Entry fvg_edge, stop 0.1 ATR · Midday 11:30-14:30 | 1545 | 613 | 39.7% | 51.9% | -0.06 | -0.03 | 0.85 | -38.68 | -48.04 | -0.08 | -0.05 |
| Entry fvg_edge, stop 0.1 ATR · Stocks only | 1882 | 681 | 36.2% | 49.9% | -0.09 | -0.03 | 0.8 | -60.54 | -65.85 | -0.12 | -0.06 |
| Entry fvg_edge, stop 0.1 ATR · R:R to T2 2.5+ | 2481 | 1070 | 43.1% | 49.9% | -0.1 | -0.04 | 0.8 | -102.27 | -120.22 | -0.1 | -0.09 |
| Entry fvg_edge, stop 0.1 ATR · Risk 0.15%+ | 2689 | 1010 | 37.6% | 53.0% | -0.03 | -0.01 | 0.92 | -32.49 | -67.32 | -0.01 | -0.05 |
| Entry fvg_edge, stop 0.1 ATR · Midday + R:R 2.5+ + risk 0.15%+ | 1043 | 418 | 40.1% | 52.4% | -0.05 | -0.02 | 0.87 | -22.23 | -31.79 | -0.02 | -0.09 |
| Entry fvg_edge, stop 0.3 ATR · All qualified | 3289 | 1376 | 41.8% | 52.6% | -0.07 | -0.03 | 0.84 | -91.71 | -110.47 | -0.07 | -0.07 |
| Entry fvg_edge, stop 0.3 ATR · Plan window (by 11:30) | 930 | 468 | 50.3% | 52.1% | -0.12 | -0.06 | 0.71 | -57.68 | -58.08 | -0.12 | -0.12 |
| Entry fvg_edge, stop 0.3 ATR · Midday 11:30-14:30 | 1545 | 613 | 39.7% | 54.2% | -0.04 | -0.02 | 0.89 | -26.82 | -36.33 | -0.03 | -0.05 |
| Entry fvg_edge, stop 0.3 ATR · Stocks only | 1882 | 681 | 36.2% | 52.4% | -0.07 | -0.03 | 0.82 | -49.56 | -54.94 | -0.08 | -0.07 |
| Entry fvg_edge, stop 0.3 ATR · R:R to T2 2.5+ | 2481 | 1070 | 43.1% | 52.7% | -0.07 | -0.03 | 0.83 | -75.45 | -95.31 | -0.06 | -0.08 |
| Entry fvg_edge, stop 0.3 ATR · Risk 0.15%+ | 2689 | 1010 | 37.6% | 55.2% | -0.02 | -0.01 | 0.95 | -17.72 | -52.06 | 0.01 | -0.04 |
| Entry fvg_edge, stop 0.3 ATR · Midday + R:R 2.5+ + risk 0.15%+ | 1043 | 418 | 40.1% | 55.3% | -0.02 | -0.01 | 0.94 | -9.78 | -22.64 | 0.03 | -0.07 |
| Entry fvg_ce, stop 0.1 ATR · All qualified | 3289 | 1139 | 34.6% | 44.2% | -0.11 | -0.04 | 0.81 | -124.15 | -140.72 | -0.11 | -0.11 |
| Entry fvg_ce, stop 0.1 ATR · Plan window (by 11:30) | 930 | 402 | 43.2% | 43.8% | -0.15 | -0.07 | 0.73 | -61.28 | -62.11 | -0.21 | -0.09 |
| Entry fvg_ce, stop 0.1 ATR · Midday 11:30-14:30 | 1545 | 502 | 32.5% | 47.2% | -0.06 | -0.02 | 0.89 | -29.18 | -43.12 | -0.06 | -0.06 |
| Entry fvg_ce, stop 0.1 ATR · Stocks only | 1882 | 559 | 29.7% | 45.4% | -0.06 | -0.02 | 0.88 | -35.88 | -52.09 | -0.12 | -0.01 |
| Entry fvg_ce, stop 0.1 ATR · R:R to T2 2.5+ | 2481 | 896 | 36.1% | 44.0% | -0.11 | -0.04 | 0.82 | -95.27 | -123.85 | -0.11 | -0.11 |
| Entry fvg_ce, stop 0.1 ATR · Risk 0.15%+ | 2689 | 827 | 30.8% | 46.9% | -0.02 | -0.01 | 0.96 | -14.99 | -58.75 | -0.01 | -0.02 |
| Entry fvg_ce, stop 0.1 ATR · Midday + R:R 2.5+ + risk 0.15%+ | 1043 | 352 | 33.7% | 48.6% | -0.01 | -0.0 | 0.98 | -3.13 | -24.3 | 0.01 | -0.03 |
| Entry fvg_ce, stop 0.3 ATR · All qualified | 3289 | 1139 | 34.6% | 47.0% | -0.09 | -0.03 | 0.83 | -100.15 | -114.78 | -0.07 | -0.1 |
| Entry fvg_ce, stop 0.3 ATR · Plan window (by 11:30) | 930 | 402 | 43.2% | 46.3% | -0.14 | -0.06 | 0.73 | -56.26 | -56.99 | -0.2 | -0.08 |
| Entry fvg_ce, stop 0.3 ATR · Midday 11:30-14:30 | 1545 | 502 | 32.5% | 50.2% | -0.03 | -0.01 | 0.93 | -15.9 | -29.74 | 0.0 | -0.07 |
| Entry fvg_ce, stop 0.3 ATR · Stocks only | 1882 | 559 | 29.7% | 48.3% | -0.05 | -0.02 | 0.89 | -28.71 | -43.47 | -0.06 | -0.04 |
| Entry fvg_ce, stop 0.3 ATR · R:R to T2 2.5+ | 2481 | 896 | 36.1% | 47.3% | -0.08 | -0.03 | 0.85 | -67.91 | -93.89 | -0.06 | -0.09 |
| Entry fvg_ce, stop 0.3 ATR · Risk 0.15%+ | 2689 | 827 | 30.8% | 49.7% | -0.0 | -0.0 | 0.99 | -1.93 | -40.93 | 0.02 | -0.02 |
| Entry fvg_ce, stop 0.3 ATR · Midday + R:R 2.5+ + risk 0.15%+ | 1043 | 352 | 33.7% | 52.3% | 0.03 | 0.01 | 1.06 | 9.48 | -16.67 | 0.09 | -0.03 |
| Entry blend, stop 0.1 ATR · All qualified | 3289 | 1184 | 36.0% | 45.6% | -0.1 | -0.04 | 0.81 | -122.55 | -140.19 | -0.09 | -0.12 |
| Entry blend, stop 0.1 ATR · Plan window (by 11:30) | 930 | 415 | 44.6% | 44.8% | -0.16 | -0.07 | 0.71 | -66.57 | -67.34 | -0.21 | -0.11 |
| Entry blend, stop 0.1 ATR · Midday 11:30-14:30 | 1545 | 525 | 34.0% | 48.4% | -0.05 | -0.02 | 0.9 | -25.89 | -40.86 | -0.06 | -0.03 |
| Entry blend, stop 0.1 ATR · Stocks only | 1882 | 583 | 31.0% | 45.6% | -0.08 | -0.03 | 0.84 | -47.92 | -57.3 | -0.13 | -0.04 |
| Entry blend, stop 0.1 ATR · R:R to T2 2.5+ | 2481 | 932 | 37.6% | 45.3% | -0.11 | -0.04 | 0.8 | -102.42 | -130.48 | -0.1 | -0.12 |
| Entry blend, stop 0.1 ATR · Risk 0.15%+ | 2689 | 864 | 32.1% | 48.1% | -0.02 | -0.01 | 0.96 | -16.2 | -61.02 | -0.0 | -0.03 |
| Entry blend, stop 0.1 ATR · Midday + R:R 2.5+ + risk 0.15%+ | 1043 | 362 | 34.7% | 48.9% | -0.02 | -0.01 | 0.95 | -8.79 | -24.13 | 0.01 | -0.06 |
| Entry blend, stop 0.3 ATR · All qualified | 3289 | 1184 | 36.0% | 48.1% | -0.08 | -0.03 | 0.83 | -99.58 | -115.02 | -0.06 | -0.11 |
| Entry blend, stop 0.3 ATR · Plan window (by 11:30) | 930 | 415 | 44.6% | 47.2% | -0.15 | -0.07 | 0.71 | -60.9 | -61.58 | -0.19 | -0.1 |
| Entry blend, stop 0.3 ATR · Midday 11:30-14:30 | 1545 | 525 | 34.0% | 51.0% | -0.03 | -0.01 | 0.94 | -13.83 | -29.81 | -0.01 | -0.04 |
| Entry blend, stop 0.3 ATR · Stocks only | 1882 | 583 | 31.0% | 48.2% | -0.07 | -0.02 | 0.85 | -39.59 | -50.19 | -0.07 | -0.06 |
| Entry blend, stop 0.3 ATR · R:R to T2 2.5+ | 2481 | 932 | 37.6% | 48.4% | -0.08 | -0.03 | 0.84 | -75.44 | -101.08 | -0.06 | -0.11 |
| Entry blend, stop 0.3 ATR · Risk 0.15%+ | 2689 | 864 | 32.1% | 50.7% | -0.0 | -0.0 | 0.99 | -3.32 | -43.44 | 0.02 | -0.03 |
| Entry blend, stop 0.3 ATR · Midday + R:R 2.5+ + risk 0.15%+ | 1043 | 362 | 34.7% | 52.2% | 0.01 | 0.0 | 1.02 | 3.57 | -17.84 | 0.08 | -0.06 |
| Entry ote_62, stop 0.1 ATR · All qualified | 3289 | 1126 | 34.2% | 43.9% | -0.09 | -0.03 | 0.85 | -96.92 | -124.9 | -0.09 | -0.09 |
| Entry ote_62, stop 0.1 ATR · Plan window (by 11:30) | 930 | 389 | 41.8% | 41.4% | -0.16 | -0.07 | 0.73 | -62.03 | -62.76 | -0.2 | -0.12 |
| Entry ote_62, stop 0.1 ATR · Midday 11:30-14:30 | 1545 | 496 | 32.1% | 46.6% | -0.03 | -0.01 | 0.95 | -13.39 | -38.99 | -0.05 | -0.01 |
| Entry ote_62, stop 0.1 ATR · Stocks only | 1882 | 553 | 29.4% | 43.8% | -0.05 | -0.02 | 0.9 | -29.99 | -47.69 | -0.08 | -0.03 |
| Entry ote_62, stop 0.1 ATR · R:R to T2 2.5+ | 2481 | 895 | 36.1% | 43.6% | -0.09 | -0.03 | 0.84 | -84.5 | -118.83 | -0.09 | -0.1 |
| Entry ote_62, stop 0.1 ATR · Risk 0.15%+ | 2689 | 809 | 30.1% | 45.7% | -0.0 | -0.0 | 0.99 | -3.15 | -58.52 | 0.01 | -0.02 |
| Entry ote_62, stop 0.1 ATR · Midday + R:R 2.5+ + risk 0.15%+ | 1043 | 344 | 33.0% | 46.8% | 0.01 | 0.0 | 1.03 | 4.29 | -22.42 | 0.0 | 0.02 |
| Entry ote_62, stop 0.3 ATR · All qualified | 3289 | 1126 | 34.2% | 46.9% | -0.07 | -0.02 | 0.87 | -74.87 | -101.52 | -0.06 | -0.08 |
| Entry ote_62, stop 0.3 ATR · Plan window (by 11:30) | 930 | 389 | 41.8% | 44.7% | -0.14 | -0.06 | 0.74 | -55.25 | -55.88 | -0.19 | -0.1 |
| Entry ote_62, stop 0.3 ATR · Midday 11:30-14:30 | 1545 | 496 | 32.1% | 49.4% | -0.01 | -0.0 | 0.98 | -4.3 | -27.85 | 0.01 | -0.03 |
| Entry ote_62, stop 0.3 ATR · Stocks only | 1882 | 553 | 29.4% | 47.2% | -0.04 | -0.01 | 0.92 | -21.87 | -42.7 | -0.03 | -0.05 |
| Entry ote_62, stop 0.3 ATR · R:R to T2 2.5+ | 2481 | 895 | 36.1% | 47.2% | -0.06 | -0.02 | 0.88 | -57.6 | -90.51 | -0.05 | -0.08 |
| Entry ote_62, stop 0.3 ATR · Risk 0.15%+ | 2689 | 809 | 30.1% | 48.9% | 0.01 | 0.0 | 1.03 | 10.46 | -39.76 | 0.04 | -0.02 |
| Entry ote_62, stop 0.3 ATR · Midday + R:R 2.5+ + risk 0.15%+ | 1043 | 344 | 33.0% | 50.3% | 0.04 | 0.01 | 1.09 | 13.4 | -15.96 | 0.09 | -0.01 |
| Entry tl_line, stop 0.1 ATR · All qualified | 3289 | 3 | 0.1% | 66.7% | -0.07 | -0.0 | 0.8 | -0.21 | -1.07 | 0.32 | -0.27 |
| Entry tl_line, stop 0.1 ATR · Plan window (by 11:30) | 930 | 1 | 0.1% | 100.0% | 0.32 | 0.0 |  | 0.32 | 0.0 |  | 0.32 |
| Entry tl_line, stop 0.1 ATR · Midday 11:30-14:30 | 1545 | 3 | 0.2% | 66.7% | -0.07 | -0.0 | 0.8 | -0.21 | -1.07 | 0.32 | -0.27 |
| Entry tl_line, stop 0.1 ATR · Stocks only | 1882 | 3 | 0.2% | 66.7% | -0.07 | -0.0 | 0.8 | -0.21 | -1.07 | 0.32 | -0.27 |
| Entry tl_line, stop 0.1 ATR · R:R to T2 2.5+ | 2481 | 3 | 0.1% | 66.7% | -0.07 | -0.0 | 0.8 | -0.21 | -1.07 | 0.32 | -0.27 |
| Entry tl_line, stop 0.1 ATR · Risk 0.15%+ | 2689 | 3 | 0.1% | 66.7% | -0.07 | -0.0 | 0.8 | -0.21 | -1.07 | 0.32 | -0.27 |
| Entry tl_line, stop 0.1 ATR · Midday + R:R 2.5+ + risk 0.15%+ | 1043 | 3 | 0.3% | 66.7% | -0.07 | -0.0 | 0.8 | -0.21 | -1.07 | 0.32 | -0.27 |
| Entry tl_line, stop 0.3 ATR · All qualified | 3289 | 3 | 0.1% | 66.7% | -0.12 | -0.0 | 0.67 | -0.35 | -1.06 | 0.29 | -0.32 |
| Entry tl_line, stop 0.3 ATR · Plan window (by 11:30) | 930 | 1 | 0.1% | 100.0% | 0.29 | 0.0 |  | 0.29 | 0.0 |  | 0.29 |
| Entry tl_line, stop 0.3 ATR · Midday 11:30-14:30 | 1545 | 3 | 0.2% | 66.7% | -0.12 | -0.0 | 0.67 | -0.35 | -1.06 | 0.29 | -0.32 |
| Entry tl_line, stop 0.3 ATR · Stocks only | 1882 | 3 | 0.2% | 66.7% | -0.12 | -0.0 | 0.67 | -0.35 | -1.06 | 0.29 | -0.32 |
| Entry tl_line, stop 0.3 ATR · R:R to T2 2.5+ | 2481 | 3 | 0.1% | 66.7% | -0.12 | -0.0 | 0.67 | -0.35 | -1.06 | 0.29 | -0.32 |
| Entry tl_line, stop 0.3 ATR · Risk 0.15%+ | 2689 | 3 | 0.1% | 66.7% | -0.12 | -0.0 | 0.67 | -0.35 | -1.06 | 0.29 | -0.32 |
| Entry tl_line, stop 0.3 ATR · Midday + R:R 2.5+ + risk 0.15%+ | 1043 | 3 | 0.3% | 66.7% | -0.12 | -0.0 | 0.67 | -0.35 | -1.06 | 0.29 | -0.32 |
| Scaled ladder_equal (fvg_edge 33%, blend 33%, ote_mid 33%) · All qualified | 3289 | 1376 | 41.8% | 51.3% | -0.08 | -0.03 | 0.82 | -113.87 | -131.08 | -0.08 | -0.08 |
| Scaled ladder_equal (fvg_edge 33%, blend 33%, ote_mid 33%) · Plan window (by 11:30) | 930 | 468 | 50.3% | 50.4% | -0.14 | -0.07 | 0.71 | -63.61 | -64.27 | -0.14 | -0.13 |
| Scaled ladder_equal (fvg_edge 33%, blend 33%, ote_mid 33%) · Midday 11:30-14:30 | 1545 | 613 | 39.7% | 54.0% | -0.04 | -0.02 | 0.9 | -26.66 | -40.48 | -0.06 | -0.03 |
| Scaled ladder_equal (fvg_edge 33%, blend 33%, ote_mid 33%) · Stocks only | 1882 | 681 | 36.2% | 51.5% | -0.06 | -0.02 | 0.85 | -43.49 | -54.53 | -0.09 | -0.04 |
| Scaled ladder_equal (fvg_edge 33%, blend 33%, ote_mid 33%) · R:R to T2 2.5+ | 2481 | 1070 | 43.1% | 50.9% | -0.09 | -0.04 | 0.81 | -97.15 | -124.48 | -0.08 | -0.1 |
| Scaled ladder_equal (fvg_edge 33%, blend 33%, ote_mid 33%) · Risk 0.15%+ | 2689 | 1010 | 37.6% | 54.0% | -0.01 | -0.01 | 0.96 | -14.63 | -60.12 | -0.0 | -0.03 |
| Scaled ladder_equal (fvg_edge 33%, blend 33%, ote_mid 33%) · Midday + R:R 2.5+ + risk 0.15%+ | 1043 | 418 | 40.1% | 54.3% | -0.02 | -0.01 | 0.96 | -6.37 | -21.93 | 0.01 | -0.04 |
| Scaled ladder_deep (fvg_edge 20%, blend 30%, ote_mid 50%) · All qualified | 3289 | 1376 | 41.8% | 51.6% | -0.08 | -0.03 | 0.82 | -112.23 | -132.45 | -0.08 | -0.09 |
| Scaled ladder_deep (fvg_edge 20%, blend 30%, ote_mid 50%) · Plan window (by 11:30) | 930 | 468 | 50.3% | 50.9% | -0.14 | -0.07 | 0.71 | -63.49 | -64.2 | -0.14 | -0.13 |
| Scaled ladder_deep (fvg_edge 20%, blend 30%, ote_mid 50%) · Midday 11:30-14:30 | 1545 | 613 | 39.7% | 54.3% | -0.04 | -0.01 | 0.91 | -22.36 | -38.06 | -0.05 | -0.02 |
| Scaled ladder_deep (fvg_edge 20%, blend 30%, ote_mid 50%) · Stocks only | 1882 | 681 | 36.2% | 52.1% | -0.05 | -0.02 | 0.87 | -36.42 | -50.6 | -0.08 | -0.03 |
| Scaled ladder_deep (fvg_edge 20%, blend 30%, ote_mid 50%) · R:R to T2 2.5+ | 2481 | 1070 | 43.1% | 50.9% | -0.09 | -0.04 | 0.82 | -94.53 | -125.72 | -0.08 | -0.1 |
| Scaled ladder_deep (fvg_edge 20%, blend 30%, ote_mid 50%) · Risk 0.15%+ | 2689 | 1010 | 37.6% | 54.4% | -0.01 | -0.0 | 0.98 | -7.98 | -57.72 | 0.0 | -0.02 |
| Scaled ladder_deep (fvg_edge 20%, blend 30%, ote_mid 50%) · Midday + R:R 2.5+ + risk 0.15%+ | 1043 | 418 | 40.1% | 54.5% | 0.0 | 0.0 | 1.0 | 0.07 | -21.89 | 0.01 | -0.01 |

## 8. Trade management (systematic, qualified, triggered)

| Method | Trades | Avg R | Win rate |
|---|---|---|---|
| Plan: half at T1, rest to T2 (gross) | 1036 | 0.1 | 43.0% |
| Plan, net of costs | 1036 | -0.1 | 41.3% |
| Full position to T1 (gross) | 1036 | 0.11 | 43.2% |
| Full position to T2 (gross) | 1036 | 0.11 | 37.6% |

## 10. v3 candidate tests (New York session, qualified, net of costs)

Confirmation entry = wait for price to reach the FVG, then enter on the first bar that closes beyond the prior 3 bars (bars used: {'1m': 2794, '5m': 138}). Runner = half at T1, rest to the close with a breakeven stop. 1st/2nd half columns are the out-of-sample check.

| Group | Setups | Triggered | Trigger rate | Win rate | Avg R | Expectancy R | Profit factor | Total R | Max DD R | 1st half avg R | 2nd half avg R |
|---|---|---|---|---|---|---|---|---|---|---|---|
| All (New York) · Current plan | 2935 | 863 | 29.4% | 42.8% | -0.07 | -0.02 | 0.88 | -61.26 | -91.11 | -0.08 | -0.06 |
| All (New York) · Runner to the close | 2935 | 863 | 29.4% | 42.8% | -0.07 | -0.02 | 0.89 | -57.45 | -88.16 | -0.05 | -0.08 |
| All (New York) · Full position to T2 | 2935 | 863 | 29.4% | 37.9% | -0.07 | -0.02 | 0.9 | -57.04 | -104.65 | -0.08 | -0.05 |
| All (New York) · Confirmation entry | 2935 | 954 | 32.5% | 52.5% | -0.09 | -0.03 | 0.76 | -88.05 | -92.0 | -0.12 | -0.06 |
| v3: 11:30-14:30 + risk 0.3%+ + FVG 0.5+ ATR · Current plan | 756 | 147 | 19.4% | 49.7% | 0.13 | 0.02 | 1.28 | 18.69 | -11.92 | 0.1 | 0.15 |
| v3: 11:30-14:30 + risk 0.3%+ + FVG 0.5+ ATR · Runner to the close | 756 | 147 | 19.4% | 49.7% | 0.11 | 0.02 | 1.25 | 16.65 | -11.87 | 0.1 | 0.13 |
| v3: 11:30-14:30 + risk 0.3%+ + FVG 0.5+ ATR · Full position to T2 | 756 | 147 | 19.4% | 46.9% | 0.15 | 0.03 | 1.28 | 21.51 | -13.33 | 0.13 | 0.16 |
| v3: 11:30-14:30 + risk 0.3%+ + FVG 0.5+ ATR · Confirmation entry | 756 | 202 | 26.7% | 58.4% | 0.05 | 0.01 | 1.19 | 10.52 | -7.51 | 0.07 | 0.03 |
| v3 + longs · Current plan | 621 | 112 | 18.0% | 54.5% | 0.25 | 0.05 | 1.56 | 28.06 | -8.18 | 0.21 | 0.29 |
| v3 + longs · Runner to the close | 621 | 112 | 18.0% | 54.5% | 0.23 | 0.04 | 1.52 | 26.03 | -8.13 | 0.21 | 0.25 |
| v3 + longs · Full position to T2 | 621 | 112 | 18.0% | 50.0% | 0.24 | 0.04 | 1.5 | 27.21 | -8.1 | 0.22 | 0.27 |
| v3 + longs · Confirmation entry | 621 | 166 | 26.7% | 60.2% | 0.09 | 0.02 | 1.32 | 14.3 | -6.21 | 0.11 | 0.07 |
| v3 + VWAP side · Current plan | 578 | 87 | 15.1% | 51.7% | 0.09 | 0.01 | 1.21 | 8.03 | -5.97 | 0.09 | 0.1 |
| v3 + VWAP side · Runner to the close | 578 | 87 | 15.1% | 51.7% | 0.07 | 0.01 | 1.15 | 5.99 | -5.97 | 0.09 | 0.05 |
| v3 + VWAP side · Full position to T2 | 578 | 87 | 15.1% | 49.4% | 0.1 | 0.01 | 1.2 | 8.61 | -8.65 | 0.04 | 0.15 |
| v3 + VWAP side · Confirmation entry | 578 | 130 | 22.5% | 54.6% | 0.03 | 0.01 | 1.12 | 4.28 | -6.91 | 0.05 | 0.02 |
| v3 + in play (open volume 1.5x+) · Current plan | 112 | 22 | 19.6% | 45.5% | 0.08 | 0.02 | 1.21 | 1.79 | -3.73 | -0.14 | 0.3 |
| v3 + in play (open volume 1.5x+) · Runner to the close | 112 | 22 | 19.6% | 45.5% | 0.08 | 0.02 | 1.21 | 1.79 | -3.73 | -0.14 | 0.3 |
| v3 + in play (open volume 1.5x+) · Full position to T2 | 112 | 22 | 19.6% | 45.5% | -0.08 | -0.02 | 0.83 | -1.79 | -4.62 | -0.18 | 0.02 |
| v3 + in play (open volume 1.5x+) · Confirmation entry | 112 | 29 | 25.9% | 62.1% | 0.06 | 0.02 | 1.2 | 1.81 | -2.61 | -0.06 | 0.17 |
| v3 + longs + VWAP side · Current plan | 490 | 71 | 14.5% | 53.5% | 0.18 | 0.03 | 1.4 | 12.59 | -5.26 | 0.15 | 0.2 |
| v3 + longs + VWAP side · Runner to the close | 490 | 71 | 14.5% | 53.5% | 0.15 | 0.02 | 1.33 | 10.56 | -5.26 | 0.15 | 0.14 |
| v3 + longs + VWAP side · Full position to T2 | 490 | 71 | 14.5% | 52.1% | 0.22 | 0.03 | 1.48 | 15.75 | -5.56 | 0.18 | 0.27 |
| v3 + longs + VWAP side · Confirmation entry | 490 | 111 | 22.7% | 55.0% | 0.04 | 0.01 | 1.15 | 4.66 | -7.31 | 0.09 | -0.01 |
| VWAP side only · Current plan | 2009 | 530 | 26.4% | 42.1% | -0.12 | -0.03 | 0.79 | -65.06 | -77.81 | -0.15 | -0.1 |
| VWAP side only · Runner to the close | 2009 | 530 | 26.4% | 42.1% | -0.12 | -0.03 | 0.8 | -64.64 | -74.19 | -0.11 | -0.13 |
| VWAP side only · Full position to T2 | 2009 | 530 | 26.4% | 38.3% | -0.12 | -0.03 | 0.82 | -62.99 | -85.9 | -0.14 | -0.09 |
| VWAP side only · Confirmation entry | 2009 | 615 | 30.6% | 51.7% | -0.11 | -0.03 | 0.72 | -64.71 | -73.94 | -0.11 | -0.1 |
| In play only · Current plan | 372 | 101 | 27.2% | 36.6% | -0.26 | -0.07 | 0.6 | -26.36 | -32.79 | -0.5 | -0.03 |
| In play only · Runner to the close | 372 | 101 | 27.2% | 36.6% | -0.27 | -0.07 | 0.58 | -27.38 | -33.9 | -0.5 | -0.05 |
| In play only · Full position to T2 | 372 | 101 | 27.2% | 31.7% | -0.38 | -0.1 | 0.48 | -38.48 | -41.15 | -0.58 | -0.19 |
| In play only · Confirmation entry | 372 | 118 | 31.7% | 53.4% | -0.11 | -0.04 | 0.72 | -13.48 | -23.63 | -0.25 | 0.03 |

## 11. Trendline retest confluence (New York session, qualified, net of costs)

Trendline = the falling line across the lower highs into the sweep (rising line across higher lows for shorts), broken by a close and not failed. Confluence = its level at the snapshot sits in the entry zone (FVG near edge to entry) within 0.25 ATR. Retest at fill = the line was within 0.3 ATR of the fill price when the order filled. Only rows recorded since Nov 4, 2026 (rerun the backtest to fill history).

| Group | Setups | Triggered | Trigger rate | Win rate | Avg R | Expectancy R | Profit factor | Total R | Max DD R | 1st half avg R | 2nd half avg R |
|---|---|---|---|---|---|---|---|---|---|---|---|
| All (New York, trendline recorded) · current plan | 22 | 16 | 72.7% | 37.5% | -0.38 | -0.28 | 0.45 | -6.12 | -7.74 | -0.66 | -0.1 |
| No trendline found/broken · current plan | 12 | 9 | 75.0% | 33.3% | -0.43 | -0.32 | 0.43 | -3.88 | -5.5 | -0.69 | -0.22 |
| Trendline found and broken · current plan | 10 | 7 | 70.0% | 42.9% | -0.32 | -0.22 | 0.48 | -2.24 | -2.24 | -0.43 | -0.24 |
| Trendline confluence at snapshot · current plan | 3 | 3 | 100.0% | 66.7% | 0.11 | 0.11 | 1.31 | 0.33 | -1.07 | 0.84 | -0.25 |
| No confluence at snapshot · current plan | 19 | 13 | 68.4% | 30.8% | -0.5 | -0.34 | 0.36 | -6.46 | -8.08 | -0.82 | -0.22 |
| Confluence, 3+ touches · current plan | 0 | 0 |  |  |  |  |  | 0.0 | 0.0 |  |  |
| Confluence + longs · current plan | 3 | 3 | 100.0% | 66.7% | 0.11 | 0.11 | 1.31 | 0.33 | -1.07 | 0.84 | -0.25 |
| Confluence + midday (11:30-14:30) · current plan | 3 | 3 | 100.0% | 66.7% | 0.11 | 0.11 | 1.31 | 0.33 | -1.07 | 0.84 | -0.25 |
| Confluence + risk 0.3%+ · current plan | 2 | 2 | 100.0% | 50.0% | -0.12 | -0.12 | 0.78 | -0.24 | -1.07 | 0.84 | -1.07 |
| Confluence + VWAP side · current plan | 1 | 1 | 100.0% | 100.0% | 0.84 | 0.84 |  | 0.84 | 0.0 |  | 0.84 |
| Confluence + longs + midday + risk 0.3%+ · current plan | 2 | 2 | 100.0% | 50.0% | -0.12 | -0.12 | 0.78 | -0.24 | -1.07 | 0.84 | -1.07 |
| Fill was a trendline retest (any setup) | 22 | 2 | 9.1% | 50.0% | -0.25 | -0.02 | 0.53 | -0.5 | -1.07 | 0.57 | -1.07 |
| Fill was a trendline retest + longs | 22 | 2 | 9.1% | 50.0% | -0.25 | -0.02 | 0.53 | -0.5 | -1.07 | 0.57 | -1.07 |
| Entry at the trendline (stop 0.1 ATR) | 3 | 3 | 100.0% | 66.7% | -0.07 | -0.07 | 0.8 | -0.21 | -1.07 | 0.32 | -0.27 |
| Entry at the trendline (stop 0.3 ATR) | 3 | 3 | 100.0% | 66.7% | -0.12 | -0.12 | 0.67 | -0.35 | -1.06 | 0.29 | -0.32 |

## 9. Automatic changes in this run

| Key | Old | New | Evidence |
|---|---|---|---|
| None |  |  |  |
