# FVG review: 2026-11-23 16:50 ET (Daily)

Sessions: 139 (2026-05-07 to 2026-11-23). Config version 3.

## 1. Strategy performance (qualified setups; results net of costs)

Costs: 0.02% of price per side. Entries allowed until 15:30 ET.

| Group | Setups | Triggered | Trigger rate | Win rate | Avg R | Expectancy R | Profit factor | Total R | Max DD R | 1st half avg R | 2nd half avg R |
|---|---|---|---|---|---|---|---|---|---|---|---|
| Live dashboard snapshots | 230 | 72 | 31.3% | 44.4% | -0.16 | -0.05 | 0.68 | -11.72 | -14.29 | -0.23 | -0.1 |
| Daily full-session replays | 420 | 161 | 38.3% | 37.3% | -0.29 | -0.11 | 0.58 | -46.07 | -54.89 | -0.24 | -0.34 |
| Backtest | 3224 | 1010 | 31.3% | 41.1% | -0.1 | -0.03 | 0.84 | -104.96 | -135.21 | -0.08 | -0.13 |
| Systematic (replays + backtest) | 3644 | 1171 | 32.1% | 40.6% | -0.13 | -0.04 | 0.8 | -151.03 | -178.32 | -0.15 | -0.11 |
| Systematic, before cost (gross) | 3644 | 1171 | 32.1% | 42.1% | 0.07 | 0.02 | 1.14 | 84.38 | -39.17 | 0.04 | 0.1 |
| Systematic, plan window only (New York, formed by 11:30) | 1031 | 402 | 39.0% | 38.6% | -0.18 | -0.07 | 0.72 | -73.08 | -74.47 | -0.27 | -0.09 |
| Live top-5 suggestions only | 160 | 49 | 30.6% | 46.9% | -0.2 | -0.06 | 0.59 | -9.99 | -11.76 | -0.33 | -0.08 |
| Your actual trades | 1 | 1 |  | 0.0% | -1.77 |  |  | -1.77 |  |  |  |
| Stocks and ETFs, New York session only | 3047 | 904 | 29.7% | 41.6% | -0.1 | -0.03 | 0.83 | -92.5 | -118.38 | -0.1 | -0.1 |
| Futures, New York session | 169 | 58 | 34.3% | 44.8% | -0.08 | -0.03 | 0.87 | -4.59 | -13.19 | 0.13 | -0.29 |
| Futures, all 24-hour sessions | 597 | 267 | 44.7% | 37.1% | -0.22 | -0.1 | 0.7 | -58.53 | -60.57 | -0.15 | -0.29 |

## 1c. Futures by session (24-hour test; qualified, net of costs)

Asia and London use their own levels: prior-day high/low, the previous session's high/low, and the session's first 30 minutes.

| Group | Setups | Triggered | Trigger rate | Win rate | Avg R | Expectancy R | Profit factor | Total R | Max DD R | 1st half avg R | 2nd half avg R |
|---|---|---|---|---|---|---|---|---|---|---|---|
| Futures, Asia session (6 PM-midnight ET) | 187 | 83 | 44.4% | 31.3% | -0.26 | -0.11 | 0.66 | -21.21 | -23.71 | -0.3 | -0.21 |
| Futures, London session (2-8 AM ET) | 241 | 126 | 52.3% | 37.3% | -0.26 | -0.14 | 0.66 | -32.73 | -38.05 | -0.33 | -0.19 |
| Futures, NY session (9:30-4:00 ET) | 169 | 58 | 34.3% | 44.8% | -0.08 | -0.03 | 0.87 | -4.59 | -13.19 | 0.13 | -0.29 |
| CL=F Asia | 24 | 14 | 58.3% | 50.0% | 0.33 | 0.19 | 1.56 | 4.6 | -3.71 | -0.12 | 0.78 |
| CL=F London | 27 | 10 | 37.0% | 40.0% | 0.09 | 0.03 | 1.15 | 0.87 | -2.21 | -0.14 | 0.31 |
| CL=F NY | 22 | 8 | 36.4% | 25.0% | -0.46 | -0.17 | 0.42 | -3.71 | -3.71 | -0.62 | -0.31 |
| ES=F Asia | 16 | 6 | 37.5% | 33.3% | -0.45 | -0.17 | 0.43 | -2.72 | -4.64 | 0.28 | -1.18 |
| ES=F London | 31 | 19 | 61.3% | 36.8% | -0.01 | -0.01 | 0.98 | -0.21 | -5.2 | -0.29 | 0.24 |
| ES=F NY | 21 | 9 | 42.9% | 66.7% | 0.64 | 0.28 | 3.37 | 5.8 | -1.41 | 1.23 | 0.18 |
| GC=F Asia | 39 | 25 | 64.1% | 24.0% | -0.1 | -0.07 | 0.85 | -2.58 | -10.46 | 0.07 | -0.27 |
| GC=F London | 17 | 6 | 35.3% | 66.7% | 0.35 | 0.12 | 2.0 | 2.09 | -1.05 | 0.05 | 0.64 |
| GC=F NY | 19 | 8 | 42.1% | 50.0% | 0.05 | 0.02 | 1.09 | 0.37 | -2.67 | 0.28 | -0.19 |
| NG=F Asia | 0 | 0 |  |  |  |  |  | 0.0 | 0.0 |  |  |
| NG=F London | 0 | 0 |  |  |  |  |  | 0.0 | 0.0 |  |  |
| NG=F NY | 1 | 1 | 100.0% | 0.0% | -1.16 | -1.16 | 0.0 | -1.16 | -1.16 |  | -1.16 |
| NQ=F Asia | 16 | 8 | 50.0% | 37.5% | -0.08 | -0.04 | 0.88 | -0.61 | -5.19 | -1.03 | 0.88 |
| NQ=F London | 25 | 11 | 44.0% | 9.1% | -0.7 | -0.31 | 0.1 | -7.74 | -7.74 | -0.88 | -0.55 |
| NQ=F NY | 14 | 4 | 28.6% | 25.0% | -0.32 | -0.09 | 0.38 | -1.29 | -2.08 | -1.01 | 0.37 |
| RTY=F Asia | 19 | 5 | 26.3% | 60.0% | 0.4 | 0.11 | 1.9 | 2.01 | -2.23 | 1.12 | -0.08 |
| RTY=F London | 35 | 24 | 68.6% | 37.5% | -0.12 | -0.08 | 0.82 | -2.77 | -10.2 | -0.43 | 0.2 |
| RTY=F NY | 16 | 2 | 12.5% | 50.0% | -0.1 | -0.01 | 0.82 | -0.19 | -1.04 | -1.04 | 0.85 |
| YM=F Asia | 21 | 6 | 28.6% | 16.7% | -0.8 | -0.23 | 0.15 | -4.81 | -5.67 | -0.51 | -1.09 |
| YM=F London | 32 | 16 | 50.0% | 56.2% | 0.31 | 0.16 | 1.64 | 4.97 | -2.29 | 0.14 | 0.48 |
| YM=F NY | 17 | 3 | 17.6% | 33.3% | 0.43 | 0.08 | 1.63 | 1.3 | -2.05 | 3.35 | -1.03 |
| ZB=F Asia | 18 | 7 | 38.9% | 28.6% | -1.07 | -0.42 | 0.05 | -7.49 | -7.73 | -0.65 | -1.38 |
| ZB=F London | 15 | 9 | 60.0% | 44.4% | -0.37 | -0.22 | 0.54 | -3.3 | -3.38 | -0.7 | -0.1 |
| ZB=F NY | 20 | 9 | 45.0% | 66.7% | 0.49 | 0.22 | 1.95 | 4.37 | -1.65 | 0.8 | 0.23 |
| ZC=F Asia | 1 | 1 | 100.0% | 0.0% | -1.71 | -1.71 | 0.0 | -1.71 | -1.71 |  | -1.71 |
| ZC=F London | 0 | 0 |  |  |  |  |  | 0.0 | 0.0 |  |  |
| ZC=F NY | 1 | 0 | 0.0% |  |  | 0.0 |  | 0.0 | 0.0 |  |  |
| ZF=F Asia | 17 | 6 | 35.3% | 16.7% | -0.85 | -0.3 | 0.13 | -5.09 | -5.09 | -1.24 | -0.46 |
| ZF=F London | 23 | 14 | 60.9% | 28.6% | -1.07 | -0.65 | 0.2 | -14.95 | -14.95 | -1.34 | -0.79 |
| ZF=F NY | 16 | 6 | 37.5% | 50.0% | -0.72 | -0.27 | 0.14 | -4.31 | -4.64 | -0.53 | -0.9 |
| ZN=F Asia | 11 | 4 | 36.4% | 25.0% | -0.49 | -0.18 | 0.37 | -1.95 | -2.63 | -1.31 | 0.34 |
| ZN=F London | 15 | 8 | 53.3% | 25.0% | -0.68 | -0.36 | 0.33 | -5.44 | -5.44 | -0.54 | -0.82 |
| ZN=F NY | 11 | 6 | 54.5% | 33.3% | -0.52 | -0.28 | 0.37 | -3.11 | -3.11 | -0.01 | -1.03 |
| ZS=F Asia | 5 | 1 | 20.0% | 0.0% | -0.85 | -0.17 | 0.0 | -0.85 | -0.85 |  | -0.85 |
| ZS=F London | 21 | 9 | 42.9% | 33.3% | -0.69 | -0.3 | 0.32 | -6.25 | -7.26 | -0.95 | -0.49 |
| ZS=F NY | 11 | 2 | 18.2% | 0.0% | -1.33 | -0.24 | 0.0 | -2.66 | -2.66 | -1.32 | -1.34 |

## 2. New York session: by asset, side, time of day, risk size (systematic, qualified)

| Group | Setups | Triggered | Trigger rate | Win rate | Avg R | Expectancy R | Profit factor | Total R | Max DD R | 1st half avg R | 2nd half avg R |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ETF | 991 | 339 | 34.2% | 40.4% | -0.19 | -0.07 | 0.72 | -65.35 | -77.79 | -0.13 | -0.25 |
| Stock | 2056 | 565 | 27.5% | 42.3% | -0.05 | -0.01 | 0.92 | -27.14 | -44.58 | -0.06 | -0.03 |
| Future | 169 | 58 | 34.3% | 44.8% | -0.08 | -0.03 | 0.87 | -4.59 | -13.19 | 0.13 | -0.29 |
| Leveraged/inverse ETFs | 142 | 44 | 31.0% | 50.0% | 0.33 | 0.1 | 1.76 | 14.65 | -6.42 | 0.77 | -0.11 |
| LONG | 2821 | 873 | 30.9% | 41.8% | -0.11 | -0.03 | 0.83 | -94.04 | -117.62 | -0.09 | -0.13 |
| SHORT | 395 | 89 | 22.5% | 41.6% | -0.03 | -0.01 | 0.92 | -3.05 | -9.63 | -0.15 | 0.08 |
| Formed 10:00-10:30 | 336 | 160 | 47.6% | 31.2% | -0.3 | -0.14 | 0.59 | -48.64 | -49.25 | -0.32 | -0.29 |
| Formed 10:30-11:30 | 645 | 226 | 35.0% | 42.9% | -0.11 | -0.04 | 0.81 | -24.41 | -33.43 | -0.24 | 0.03 |
| Formed 11:30-13:00 | 904 | 293 | 32.4% | 46.8% | -0.05 | -0.02 | 0.91 | -15.07 | -32.57 | 0.04 | -0.14 |
| Formed 13:00-14:30 | 789 | 217 | 27.5% | 39.6% | -0.1 | -0.03 | 0.84 | -21.3 | -34.2 | -0.18 | -0.02 |
| Formed 14:30-16:00 | 542 | 66 | 12.2% | 48.5% | 0.19 | 0.02 | 1.34 | 12.33 | -16.45 | 0.65 | -0.28 |
| Risk 0-0.15% of price | 675 | 326 | 48.3% | 34.0% | -0.41 | -0.2 | 0.53 | -133.27 | -136.18 | -0.37 | -0.45 |
| Risk 0.15-0.3% of price | 707 | 268 | 37.9% | 40.3% | -0.13 | -0.05 | 0.79 | -36.11 | -45.15 | -0.18 | -0.09 |
| Risk 0.3-0.6% of price | 1123 | 318 | 28.3% | 44.7% | 0.05 | 0.01 | 1.09 | 14.98 | -20.24 | 0.06 | 0.04 |
| Risk 0.6%+ | 1139 | 259 | 22.7% | 44.0% | 0.01 | 0.0 | 1.03 | 3.37 | -21.8 | 0.07 | -0.04 |

## 2b. Short guardrails (systematic; shorts use full exit at T1, breakeven at +0.5R, 60-minute time stop)

Sizing: longs 1.25% risk (cap 5.0% of account), shorts 0.5% risk (cap 2.5%). Results here are in R, before sizing.

| Group | Setups | Triggered | Trigger rate | Win rate | Avg R | Expectancy R | Profit factor | Total R | Max DD R | 1st half avg R | 2nd half avg R |
|---|---|---|---|---|---|---|---|---|---|---|---|
| Longs passing the normal filters | 3245 | 1081 | 33.3% | 40.4% | -0.14 | -0.05 | 0.79 | -149.57 | -174.71 | -0.15 | -0.13 |
| Shorts passing the normal filters (before guardrails) | 2336 | 828 | 35.4% | 27.9% | -0.18 | -0.06 | 0.64 | -148.91 | -153.4 | -0.1 | -0.26 |
| Shorts passing every guardrail (traded) | 399 | 90 | 22.6% | 42.2% | -0.02 | -0.0 | 0.96 | -1.45 | -9.63 | -0.15 | 0.11 |
| Shorts passing: bearish daily trend | 1037 | 370 | 35.7% | 29.7% | -0.2 | -0.07 | 0.62 | -72.48 | -82.87 | -0.16 | -0.24 |
| Shorts failing: bearish daily trend | 1299 | 458 | 35.3% | 26.4% | -0.17 | -0.06 | 0.66 | -76.44 | -78.31 | -0.07 | -0.26 |
| Shorts passing: PDH or 2+ level sweep | 1671 | 557 | 33.3% | 29.8% | -0.11 | -0.04 | 0.75 | -62.58 | -66.93 | -0.02 | -0.2 |
| Shorts failing: PDH or 2+ level sweep | 665 | 271 | 40.8% | 24.0% | -0.32 | -0.13 | 0.49 | -86.33 | -87.54 | -0.28 | -0.35 |
| Shorts passing: R:R to T2 3.0+ | 1720 | 611 | 35.5% | 28.3% | -0.19 | -0.07 | 0.65 | -113.43 | -118.79 | -0.08 | -0.29 |
| Shorts failing: R:R to T2 3.0+ | 616 | 217 | 35.2% | 26.7% | -0.16 | -0.06 | 0.64 | -35.49 | -38.04 | -0.16 | -0.17 |
| Shorts passing: risk 0.3%+ of price | 1258 | 361 | 28.7% | 33.2% | -0.01 | -0.0 | 0.97 | -3.36 | -25.88 | 0.05 | -0.07 |
| Shorts failing: risk 0.3%+ of price | 1078 | 467 | 43.3% | 23.8% | -0.31 | -0.14 | 0.49 | -145.55 | -146.84 | -0.28 | -0.35 |
| Shorts passing: formed 10:30 or later | 2088 | 698 | 33.4% | 27.1% | -0.2 | -0.07 | 0.62 | -140.77 | -143.82 | -0.13 | -0.28 |
| Shorts failing: formed 10:30 or later | 248 | 130 | 52.4% | 32.3% | -0.06 | -0.03 | 0.85 | -8.15 | -20.84 | 0.08 | -0.2 |
| Shorts passing: not a leveraged ETF | 2246 | 801 | 35.7% | 27.5% | -0.2 | -0.07 | 0.61 | -158.92 | -161.98 | -0.13 | -0.27 |
| Shorts failing: not a leveraged ETF | 90 | 27 | 30.0% | 40.7% | 0.37 | 0.11 | 2.24 | 10.01 | -2.49 | 0.81 | -0.03 |

## 3. Outcomes (systematic, qualified)

| Outcome | Count | Share | Avg R |
|---|---|---|---|
| Not triggered (ran to T1 first) | 2267 | 62.2% | 0.0 |
| Stop | 569 | 15.6% | -1.22 |
| EOD exit | 239 | 6.6% | 0.19 |
| Not triggered (cutoff) | 204 | 5.6% | 0.0 |
| T1 then EOD | 152 | 4.2% | 1.79 |
| T1 then breakeven | 83 | 2.3% | 0.58 |
| T1 then T2 | 81 | 2.2% | 2.0 |
| Time stop | 28 | 0.8% | 0.51 |
| Breakeven stop | 19 | 0.5% | -0.1 |
| Invalidated before entry | 1 | 0.0% | 0.0 |
| Not triggered | 1 | 0.0% | 0.0 |

## 4. Score calibration. A useful score shows results improving band by band.

| Group | Setups | Triggered | Trigger rate | Win rate | Avg R | Expectancy R | Profit factor | Total R | Max DD R | 1st half avg R | 2nd half avg R |
|---|---|---|---|---|---|---|---|---|---|---|---|
| Score 90+ | 20 | 12 | 60.0% | 75.0% | 0.92 | 0.55 | 6.01 | 11.09 | -2.22 | 1.18 | 0.67 |
| Score 75-89 | 1282 | 382 | 29.8% | 40.3% | -0.13 | -0.04 | 0.8 | -48.25 | -74.93 | -0.15 | -0.1 |
| Score 60-74 | 2023 | 643 | 31.8% | 41.2% | -0.1 | -0.03 | 0.84 | -66.87 | -77.69 | -0.01 | -0.19 |
| Score under 60 | 319 | 134 | 42.0% | 35.1% | -0.35 | -0.15 | 0.54 | -47.0 | -48.96 | -0.3 | -0.4 |

## 5. Factor attribution (all triggered systematic setups, qualified or not)

| Factor | Weight key | Weight | With | Avg R with | Without | Avg R without | Difference | Read |
|---|---|---|---|---|---|---|---|---|
| Prior-day level swept | sweep_pd | 20 | 2895 | -0.13 | 3281 | -0.16 | 0.04 | No clear effect |
| Only PM/OR level swept | sweep_other | 15 | 2585 | -0.15 | 3591 | -0.14 | -0.0 | No clear effect |
| FVG in discount/premium | zone | 10 | 2245 | -0.18 | 3931 | -0.13 | -0.05 | No clear effect |
| FVG overlaps OTE | ote | 15 | 1987 | -0.16 | 4189 | -0.14 | -0.03 | No clear effect |
| R:R to T1 of 2 or more | rr | 8 | 476 | -0.28 | 5700 | -0.13 | -0.15 | Hurts |
| HTF bias aligned | bias | 10 | 2364 | -0.14 | 3812 | -0.15 | 0.0 | No clear effect |
| Displacement volume 1.5x+ | vol | 5 | 758 | -0.11 | 5418 | -0.15 | 0.04 | No clear effect |
| Formed 10:00-11:30 | time | 5 | 2888 | -0.19 | 3288 | -0.11 | -0.08 | No clear effect |
| Trendline retest confluence | tl | 14 | 65 | 0.05 | 626 | -0.26 | 0.31 | Helps |

## 6. Filter check (systematic)

| Group | Setups | Triggered | Trigger rate | Win rate | Avg R | Expectancy R | Profit factor | Total R | Max DD R | 1st half avg R | 2nd half avg R |
|---|---|---|---|---|---|---|---|---|---|---|---|
| Passed filters | 3644 | 1171 | 32.1% | 40.6% | -0.13 | -0.04 | 0.8 | -151.03 | -178.32 | -0.15 | -0.11 |
| Filtered out | 8330 | 5005 | 60.1% | 47.6% | -0.15 | -0.09 | 0.61 | -746.2 | -746.88 | -0.11 | -0.19 |
| No OTE overlap | 6220 | 4189 | 67.3% | 51.7% | -0.14 | -0.09 | 0.61 | -572.22 | -572.89 | -0.12 | -0.15 |
| OTE overlap, R:R to T2 1.5-2 | 152 | 70 | 46.1% | 30.0% | -0.31 | -0.14 | 0.49 | -21.48 | -21.54 | -0.12 | -0.49 |
| OTE overlap, R:R to T2 2-2.5 | 1261 | 369 | 29.3% | 35.5% | -0.16 | -0.05 | 0.72 | -58.65 | -59.64 | -0.15 | -0.17 |
| OTE overlap, R:R to T2 2.5-3 | 652 | 212 | 32.5% | 37.7% | -0.04 | -0.01 | 0.93 | -8.34 | -43.27 | -0.3 | 0.22 |
| OTE overlap, R:R to T2 3+ | 3689 | 1336 | 36.2% | 34.3% | -0.18 | -0.06 | 0.71 | -236.54 | -270.48 | -0.09 | -0.26 |

## 7. Improvement tests: entry type x stop buffer x filter (net of costs)

ote_mid = current entry (middle of the FVG/OTE overlap); fvg_edge = first touch of the gap; fvg_ce = gap midpoint; blend = halfway between the gap edge and ote_mid; ote_62 = first touch of the OTE zone; tl_line = limit at the broken trendline (only setups with trendline confluence). Scaled rows are in R of the full planned position (a partial fill counts only what filled).

| Group | Setups | Triggered | Trigger rate | Win rate | Avg R | Expectancy R | Profit factor | Total R | Max DD R | 1st half avg R | 2nd half avg R |
|---|---|---|---|---|---|---|---|---|---|---|---|
| Entry ote_mid, stop 0.1 ATR · All qualified | 3644 | 1171 | 32.1% | 40.6% | -0.13 | -0.04 | 0.8 | -151.01 | -178.3 | -0.15 | -0.11 |
| Entry ote_mid, stop 0.1 ATR · Plan window (by 11:30) | 1031 | 402 | 39.0% | 38.6% | -0.18 | -0.07 | 0.72 | -73.07 | -74.47 | -0.27 | -0.09 |
| Entry ote_mid, stop 0.1 ATR · Midday 11:30-14:30 | 1693 | 510 | 30.1% | 43.7% | -0.07 | -0.02 | 0.88 | -36.36 | -52.98 | -0.04 | -0.1 |
| Entry ote_mid, stop 0.1 ATR · Stocks only | 2056 | 565 | 27.5% | 42.3% | -0.05 | -0.01 | 0.92 | -27.14 | -44.58 | -0.06 | -0.03 |
| Entry ote_mid, stop 0.1 ATR · R:R to T2 2.5+ | 2772 | 942 | 34.0% | 40.3% | -0.14 | -0.05 | 0.79 | -130.97 | -164.68 | -0.14 | -0.13 |
| Entry ote_mid, stop 0.1 ATR · Risk 0.15%+ | 2969 | 845 | 28.5% | 43.1% | -0.02 | -0.01 | 0.96 | -17.75 | -51.8 | 0.0 | -0.05 |
| Entry ote_mid, stop 0.1 ATR · Midday + R:R 2.5+ + risk 0.15%+ | 1158 | 371 | 32.0% | 44.7% | 0.0 | 0.0 | 1.0 | 0.25 | -33.85 | 0.04 | -0.04 |
| Entry ote_mid, stop 0.3 ATR · All qualified | 3644 | 1171 | 32.1% | 43.3% | -0.11 | -0.04 | 0.81 | -131.99 | -156.12 | -0.11 | -0.12 |
| Entry ote_mid, stop 0.3 ATR · Plan window (by 11:30) | 1031 | 402 | 39.0% | 41.5% | -0.17 | -0.06 | 0.71 | -66.65 | -69.61 | -0.25 | -0.08 |
| Entry ote_mid, stop 0.3 ATR · Midday 11:30-14:30 | 1693 | 510 | 30.1% | 46.5% | -0.05 | -0.02 | 0.9 | -27.44 | -45.04 | 0.0 | -0.11 |
| Entry ote_mid, stop 0.3 ATR · Stocks only | 2056 | 565 | 27.5% | 45.1% | -0.05 | -0.01 | 0.91 | -27.57 | -45.06 | -0.03 | -0.07 |
| Entry ote_mid, stop 0.3 ATR · R:R to T2 2.5+ | 2772 | 942 | 34.0% | 43.5% | -0.11 | -0.04 | 0.81 | -106.23 | -136.6 | -0.1 | -0.13 |
| Entry ote_mid, stop 0.3 ATR · Risk 0.15%+ | 2969 | 845 | 28.5% | 45.9% | -0.01 | -0.0 | 0.98 | -9.98 | -44.56 | 0.02 | -0.04 |
| Entry ote_mid, stop 0.3 ATR · Midday + R:R 2.5+ + risk 0.15%+ | 1158 | 371 | 32.0% | 48.0% | 0.02 | 0.01 | 1.04 | 7.52 | -31.46 | 0.1 | -0.06 |
| Entry fvg_edge, stop 0.1 ATR · All qualified | 3644 | 1540 | 42.3% | 49.2% | -0.11 | -0.04 | 0.77 | -162.85 | -170.24 | -0.11 | -0.11 |
| Entry fvg_edge, stop 0.1 ATR · Plan window (by 11:30) | 1031 | 515 | 50.0% | 49.1% | -0.14 | -0.07 | 0.7 | -72.27 | -75.84 | -0.18 | -0.1 |
| Entry fvg_edge, stop 0.1 ATR · Midday 11:30-14:30 | 1693 | 684 | 40.4% | 50.4% | -0.09 | -0.04 | 0.79 | -62.7 | -68.22 | -0.08 | -0.1 |
| Entry fvg_edge, stop 0.1 ATR · Stocks only | 2056 | 758 | 36.9% | 49.6% | -0.09 | -0.03 | 0.79 | -71.67 | -74.77 | -0.11 | -0.08 |
| Entry fvg_edge, stop 0.1 ATR · R:R to T2 2.5+ | 2772 | 1214 | 43.8% | 48.5% | -0.12 | -0.05 | 0.75 | -147.55 | -159.77 | -0.14 | -0.1 |
| Entry fvg_edge, stop 0.1 ATR · Risk 0.15%+ | 2969 | 1131 | 38.1% | 51.7% | -0.06 | -0.02 | 0.86 | -63.49 | -81.03 | -0.03 | -0.08 |
| Entry fvg_edge, stop 0.1 ATR · Midday + R:R 2.5+ + risk 0.15%+ | 1158 | 477 | 41.2% | 51.2% | -0.08 | -0.03 | 0.81 | -39.74 | -45.35 | -0.03 | -0.13 |
| Entry fvg_edge, stop 0.3 ATR · All qualified | 3644 | 1540 | 42.3% | 51.3% | -0.09 | -0.04 | 0.79 | -141.69 | -150.94 | -0.07 | -0.11 |
| Entry fvg_edge, stop 0.3 ATR · Plan window (by 11:30) | 1031 | 515 | 50.0% | 51.3% | -0.13 | -0.06 | 0.7 | -66.58 | -71.28 | -0.16 | -0.09 |
| Entry fvg_edge, stop 0.3 ATR · Midday 11:30-14:30 | 1693 | 684 | 40.4% | 52.5% | -0.08 | -0.03 | 0.81 | -52.38 | -58.67 | -0.04 | -0.11 |
| Entry fvg_edge, stop 0.3 ATR · Stocks only | 2056 | 758 | 36.9% | 51.8% | -0.08 | -0.03 | 0.79 | -63.23 | -67.22 | -0.07 | -0.1 |
| Entry fvg_edge, stop 0.3 ATR · R:R to T2 2.5+ | 2772 | 1214 | 43.8% | 51.1% | -0.1 | -0.04 | 0.77 | -121.31 | -135.5 | -0.1 | -0.1 |
| Entry fvg_edge, stop 0.3 ATR · Risk 0.15%+ | 2969 | 1131 | 38.1% | 53.8% | -0.04 | -0.02 | 0.89 | -49.58 | -68.8 | -0.01 | -0.08 |
| Entry fvg_edge, stop 0.3 ATR · Midday + R:R 2.5+ + risk 0.15%+ | 1158 | 477 | 41.2% | 53.7% | -0.06 | -0.03 | 0.85 | -28.96 | -38.41 | 0.02 | -0.14 |
| Entry fvg_ce, stop 0.1 ATR · All qualified | 3644 | 1285 | 35.3% | 43.3% | -0.13 | -0.05 | 0.77 | -170.68 | -180.47 | -0.14 | -0.12 |
| Entry fvg_ce, stop 0.1 ATR · Plan window (by 11:30) | 1031 | 441 | 42.8% | 42.6% | -0.17 | -0.07 | 0.71 | -73.8 | -73.8 | -0.23 | -0.1 |
| Entry fvg_ce, stop 0.1 ATR · Midday 11:30-14:30 | 1693 | 566 | 33.4% | 45.6% | -0.09 | -0.03 | 0.82 | -52.87 | -61.45 | -0.07 | -0.12 |
| Entry fvg_ce, stop 0.1 ATR · Stocks only | 2056 | 626 | 30.4% | 44.7% | -0.08 | -0.02 | 0.85 | -47.89 | -53.99 | -0.1 | -0.05 |
| Entry fvg_ce, stop 0.1 ATR · R:R to T2 2.5+ | 2772 | 1026 | 37.0% | 42.8% | -0.14 | -0.05 | 0.77 | -139.08 | -156.22 | -0.16 | -0.12 |
| Entry fvg_ce, stop 0.1 ATR · Risk 0.15%+ | 2969 | 935 | 31.5% | 45.6% | -0.05 | -0.02 | 0.9 | -45.59 | -62.81 | -0.04 | -0.06 |
| Entry fvg_ce, stop 0.1 ATR · Midday + R:R 2.5+ + risk 0.15%+ | 1158 | 405 | 35.0% | 46.2% | -0.05 | -0.02 | 0.89 | -21.64 | -32.76 | 0.01 | -0.11 |
| Entry fvg_ce, stop 0.3 ATR · All qualified | 3644 | 1285 | 35.3% | 45.9% | -0.11 | -0.04 | 0.78 | -145.7 | -156.39 | -0.11 | -0.12 |
| Entry fvg_ce, stop 0.3 ATR · Plan window (by 11:30) | 1031 | 441 | 42.8% | 45.1% | -0.15 | -0.07 | 0.71 | -67.12 | -69.17 | -0.21 | -0.09 |
| Entry fvg_ce, stop 0.3 ATR · Midday 11:30-14:30 | 1693 | 566 | 33.4% | 48.4% | -0.07 | -0.02 | 0.86 | -39.4 | -48.92 | -0.02 | -0.12 |
| Entry fvg_ce, stop 0.3 ATR · Stocks only | 2056 | 626 | 30.4% | 47.4% | -0.07 | -0.02 | 0.86 | -41.53 | -49.48 | -0.06 | -0.08 |
| Entry fvg_ce, stop 0.3 ATR · R:R to T2 2.5+ | 2772 | 1026 | 37.0% | 45.9% | -0.11 | -0.04 | 0.8 | -110.05 | -127.31 | -0.1 | -0.11 |
| Entry fvg_ce, stop 0.3 ATR · Risk 0.15%+ | 2969 | 935 | 31.5% | 48.2% | -0.03 | -0.01 | 0.93 | -31.1 | -48.82 | -0.01 | -0.06 |
| Entry fvg_ce, stop 0.3 ATR · Midday + R:R 2.5+ + risk 0.15%+ | 1158 | 405 | 35.0% | 49.6% | -0.02 | -0.01 | 0.95 | -8.89 | -30.01 | 0.08 | -0.12 |
| Entry blend, stop 0.1 ATR · All qualified | 3644 | 1332 | 36.6% | 44.7% | -0.13 | -0.05 | 0.77 | -170.98 | -183.72 | -0.12 | -0.13 |
| Entry blend, stop 0.1 ATR · Plan window (by 11:30) | 1031 | 454 | 44.0% | 43.8% | -0.17 | -0.08 | 0.69 | -78.56 | -79.59 | -0.23 | -0.12 |
| Entry blend, stop 0.1 ATR · Midday 11:30-14:30 | 1693 | 591 | 34.9% | 46.7% | -0.09 | -0.03 | 0.83 | -50.91 | -58.88 | -0.06 | -0.11 |
| Entry blend, stop 0.1 ATR · Stocks only | 2056 | 651 | 31.7% | 45.0% | -0.09 | -0.03 | 0.82 | -59.17 | -63.36 | -0.12 | -0.06 |
| Entry blend, stop 0.1 ATR · R:R to T2 2.5+ | 2772 | 1063 | 38.3% | 44.0% | -0.14 | -0.05 | 0.76 | -147.59 | -166.3 | -0.14 | -0.14 |
| Entry blend, stop 0.1 ATR · Risk 0.15%+ | 2969 | 974 | 32.8% | 46.8% | -0.05 | -0.02 | 0.9 | -47.52 | -70.01 | -0.02 | -0.08 |
| Entry blend, stop 0.1 ATR · Midday + R:R 2.5+ + risk 0.15%+ | 1158 | 416 | 35.9% | 46.4% | -0.07 | -0.02 | 0.86 | -28.43 | -35.86 | -0.0 | -0.14 |
| Entry blend, stop 0.3 ATR · All qualified | 3644 | 1332 | 36.6% | 47.1% | -0.11 | -0.04 | 0.78 | -147.02 | -160.4 | -0.09 | -0.13 |
| Entry blend, stop 0.3 ATR · Plan window (by 11:30) | 1031 | 454 | 44.0% | 46.3% | -0.16 | -0.07 | 0.69 | -71.6 | -74.0 | -0.21 | -0.1 |
| Entry blend, stop 0.3 ATR · Midday 11:30-14:30 | 1693 | 591 | 34.9% | 49.2% | -0.07 | -0.02 | 0.86 | -38.46 | -47.22 | -0.02 | -0.11 |
| Entry blend, stop 0.3 ATR · Stocks only | 2056 | 651 | 31.7% | 47.5% | -0.08 | -0.03 | 0.83 | -51.76 | -57.78 | -0.08 | -0.08 |
| Entry blend, stop 0.3 ATR · R:R to T2 2.5+ | 2772 | 1063 | 38.3% | 46.9% | -0.11 | -0.04 | 0.78 | -119.05 | -138.21 | -0.09 | -0.13 |
| Entry blend, stop 0.3 ATR · Risk 0.15%+ | 2969 | 974 | 32.8% | 49.3% | -0.03 | -0.01 | 0.92 | -33.4 | -55.78 | 0.0 | -0.07 |
| Entry blend, stop 0.3 ATR · Midday + R:R 2.5+ + risk 0.15%+ | 1158 | 416 | 35.9% | 49.5% | -0.04 | -0.01 | 0.91 | -15.75 | -32.31 | 0.06 | -0.14 |
| Entry ote_62, stop 0.1 ATR · All qualified | 3644 | 1270 | 34.9% | 43.1% | -0.11 | -0.04 | 0.81 | -139.23 | -162.89 | -0.13 | -0.09 |
| Entry ote_62, stop 0.1 ATR · Plan window (by 11:30) | 1031 | 426 | 41.3% | 40.8% | -0.18 | -0.07 | 0.71 | -74.99 | -74.99 | -0.24 | -0.11 |
| Entry ote_62, stop 0.1 ATR · Midday 11:30-14:30 | 1693 | 560 | 33.1% | 45.0% | -0.07 | -0.02 | 0.88 | -37.15 | -51.64 | -0.04 | -0.09 |
| Entry ote_62, stop 0.1 ATR · Stocks only | 2056 | 618 | 30.1% | 43.5% | -0.06 | -0.02 | 0.88 | -39.03 | -53.06 | -0.08 | -0.05 |
| Entry ote_62, stop 0.1 ATR · R:R to T2 2.5+ | 2772 | 1023 | 36.9% | 42.5% | -0.12 | -0.05 | 0.79 | -125.25 | -154.37 | -0.14 | -0.1 |
| Entry ote_62, stop 0.1 ATR · Risk 0.15%+ | 2969 | 914 | 30.8% | 44.6% | -0.03 | -0.01 | 0.93 | -31.81 | -64.69 | -0.01 | -0.06 |
| Entry ote_62, stop 0.1 ATR · Midday + R:R 2.5+ + risk 0.15%+ | 1158 | 398 | 34.4% | 45.0% | -0.03 | -0.01 | 0.93 | -13.49 | -31.63 | -0.0 | -0.06 |
| Entry ote_62, stop 0.3 ATR · All qualified | 3644 | 1270 | 34.9% | 45.8% | -0.09 | -0.03 | 0.83 | -117.86 | -140.8 | -0.09 | -0.09 |
| Entry ote_62, stop 0.3 ATR · Plan window (by 11:30) | 1031 | 426 | 41.3% | 44.1% | -0.16 | -0.06 | 0.71 | -66.58 | -68.1 | -0.23 | -0.08 |
| Entry ote_62, stop 0.3 ATR · Midday 11:30-14:30 | 1693 | 560 | 33.1% | 47.5% | -0.05 | -0.02 | 0.9 | -28.7 | -43.47 | 0.0 | -0.1 |
| Entry ote_62, stop 0.3 ATR · Stocks only | 2056 | 618 | 30.1% | 46.6% | -0.05 | -0.02 | 0.89 | -32.96 | -48.92 | -0.03 | -0.07 |
| Entry ote_62, stop 0.3 ATR · R:R to T2 2.5+ | 2772 | 1023 | 36.9% | 45.7% | -0.1 | -0.04 | 0.82 | -98.22 | -126.44 | -0.09 | -0.1 |
| Entry ote_62, stop 0.3 ATR · Risk 0.15%+ | 2969 | 914 | 30.8% | 47.6% | -0.02 | -0.01 | 0.96 | -17.92 | -49.05 | 0.01 | -0.05 |
| Entry ote_62, stop 0.3 ATR · Midday + R:R 2.5+ + risk 0.15%+ | 1158 | 398 | 34.4% | 48.0% | -0.01 | -0.0 | 0.97 | -5.15 | -30.85 | 0.06 | -0.09 |
| Entry tl_line, stop 0.1 ATR · All qualified | 3644 | 13 | 0.4% | 46.2% | -0.06 | -0.0 | 0.84 | -0.74 | -3.06 | 0.16 | -0.24 |
| Entry tl_line, stop 0.1 ATR · Plan window (by 11:30) | 1031 | 2 | 0.2% | 50.0% | 0.12 | 0.0 | 4.56 | 0.25 | -0.07 | 0.32 | -0.07 |
| Entry tl_line, stop 0.1 ATR · Midday 11:30-14:30 | 1693 | 9 | 0.5% | 44.4% | -0.34 | -0.0 | 0.31 | -3.06 | -4.06 | -0.31 | -0.37 |
| Entry tl_line, stop 0.1 ATR · Stocks only | 2056 | 7 | 0.3% | 42.9% | -0.17 | -0.0 | 0.47 | -1.18 | -2.16 | -0.07 | -0.24 |
| Entry tl_line, stop 0.1 ATR · R:R to T2 2.5+ | 2772 | 13 | 0.5% | 46.2% | -0.06 | -0.0 | 0.84 | -0.74 | -3.06 | 0.16 | -0.24 |
| Entry tl_line, stop 0.1 ATR · Risk 0.15%+ | 2969 | 13 | 0.4% | 46.2% | -0.06 | -0.0 | 0.84 | -0.74 | -3.06 | 0.16 | -0.24 |
| Entry tl_line, stop 0.1 ATR · Midday + R:R 2.5+ + risk 0.15%+ | 1158 | 9 | 0.8% | 44.4% | -0.34 | -0.0 | 0.31 | -3.06 | -4.06 | -0.31 | -0.37 |
| Entry tl_line, stop 0.3 ATR · All qualified | 3644 | 13 | 0.4% | 53.8% | -0.06 | -0.0 | 0.84 | -0.72 | -3.18 | 0.06 | -0.15 |
| Entry tl_line, stop 0.3 ATR · Plan window (by 11:30) | 1031 | 2 | 0.2% | 100.0% | 0.44 | 0.0 |  | 0.87 | 0.0 | 0.29 | 0.58 |
| Entry tl_line, stop 0.3 ATR · Midday 11:30-14:30 | 1693 | 9 | 0.5% | 44.4% | -0.37 | -0.0 | 0.26 | -3.34 | -4.19 | -0.38 | -0.37 |
| Entry tl_line, stop 0.3 ATR · Stocks only | 2056 | 7 | 0.3% | 57.1% | -0.12 | -0.0 | 0.64 | -0.81 | -2.28 | -0.12 | -0.12 |
| Entry tl_line, stop 0.3 ATR · R:R to T2 2.5+ | 2772 | 13 | 0.5% | 53.8% | -0.06 | -0.0 | 0.84 | -0.72 | -3.18 | 0.06 | -0.15 |
| Entry tl_line, stop 0.3 ATR · Risk 0.15%+ | 2969 | 13 | 0.4% | 53.8% | -0.06 | -0.0 | 0.84 | -0.72 | -3.18 | 0.06 | -0.15 |
| Entry tl_line, stop 0.3 ATR · Midday + R:R 2.5+ + risk 0.15%+ | 1158 | 9 | 0.8% | 44.4% | -0.37 | -0.0 | 0.26 | -3.34 | -4.19 | -0.38 | -0.37 |
| Scaled ladder_equal (fvg_edge 33%, blend 33%, ote_mid 33%) · All qualified | 3644 | 1540 | 42.3% | 50.4% | -0.11 | -0.04 | 0.78 | -161.88 | -176.12 | -0.1 | -0.11 |
| Scaled ladder_equal (fvg_edge 33%, blend 33%, ote_mid 33%) · Plan window (by 11:30) | 1031 | 515 | 50.0% | 49.7% | -0.14 | -0.07 | 0.7 | -74.23 | -76.21 | -0.19 | -0.1 |
| Scaled ladder_equal (fvg_edge 33%, blend 33%, ote_mid 33%) · Midday 11:30-14:30 | 1693 | 684 | 40.4% | 52.3% | -0.08 | -0.03 | 0.83 | -51.62 | -60.85 | -0.06 | -0.09 |
| Scaled ladder_equal (fvg_edge 33%, blend 33%, ote_mid 33%) · Stocks only | 2056 | 758 | 36.9% | 51.2% | -0.07 | -0.03 | 0.83 | -54.89 | -60.81 | -0.09 | -0.06 |
| Scaled ladder_equal (fvg_edge 33%, blend 33%, ote_mid 33%) · R:R to T2 2.5+ | 2772 | 1214 | 43.8% | 49.8% | -0.12 | -0.05 | 0.76 | -142.11 | -162.3 | -0.13 | -0.11 |
| Scaled ladder_equal (fvg_edge 33%, blend 33%, ote_mid 33%) · Risk 0.15%+ | 2969 | 1131 | 38.1% | 52.7% | -0.04 | -0.02 | 0.9 | -45.07 | -68.35 | -0.01 | -0.07 |
| Scaled ladder_equal (fvg_edge 33%, blend 33%, ote_mid 33%) · Midday + R:R 2.5+ + risk 0.15%+ | 1158 | 477 | 41.2% | 52.4% | -0.05 | -0.02 | 0.87 | -25.15 | -33.96 | -0.0 | -0.11 |
| Scaled ladder_deep (fvg_edge 20%, blend 30%, ote_mid 50%) · All qualified | 3644 | 1540 | 42.3% | 50.8% | -0.1 | -0.04 | 0.78 | -159.81 | -177.01 | -0.1 | -0.11 |
| Scaled ladder_deep (fvg_edge 20%, blend 30%, ote_mid 50%) · Plan window (by 11:30) | 1031 | 515 | 50.0% | 50.5% | -0.14 | -0.07 | 0.7 | -74.25 | -75.95 | -0.19 | -0.1 |
| Scaled ladder_deep (fvg_edge 20%, blend 30%, ote_mid 50%) · Midday 11:30-14:30 | 1693 | 684 | 40.4% | 52.9% | -0.07 | -0.03 | 0.84 | -47.65 | -58.57 | -0.05 | -0.09 |
| Scaled ladder_deep (fvg_edge 20%, blend 30%, ote_mid 50%) · Stocks only | 2056 | 758 | 36.9% | 52.1% | -0.06 | -0.02 | 0.85 | -47.97 | -55.99 | -0.08 | -0.05 |
| Scaled ladder_deep (fvg_edge 20%, blend 30%, ote_mid 50%) · R:R to T2 2.5+ | 2772 | 1214 | 43.8% | 50.1% | -0.11 | -0.05 | 0.77 | -139.32 | -162.82 | -0.12 | -0.11 |
| Scaled ladder_deep (fvg_edge 20%, blend 30%, ote_mid 50%) · Risk 0.15%+ | 2969 | 1131 | 38.1% | 53.4% | -0.03 | -0.01 | 0.92 | -38.1 | -63.89 | -0.01 | -0.06 |
| Scaled ladder_deep (fvg_edge 20%, blend 30%, ote_mid 50%) · Midday + R:R 2.5+ + risk 0.15%+ | 1158 | 477 | 41.2% | 53.0% | -0.04 | -0.02 | 0.91 | -19.02 | -33.88 | 0.01 | -0.09 |

## 8. Trade management (systematic, qualified, triggered)

| Method | Trades | Avg R | Win rate |
|---|---|---|---|
| Plan: half at T1, rest to T2 (gross) | 1171 | 0.07 | 42.1% |
| Plan, net of costs | 1171 | -0.13 | 40.6% |
| Full position to T1 (gross) | 1171 | 0.08 | 42.4% |
| Full position to T2 (gross) | 1171 | 0.07 | 37.0% |

## 10. v3 candidate tests (New York session, qualified, net of costs)

Confirmation entry = wait for price to reach the FVG, then enter on the first bar that closes beyond the prior 3 bars (bars used: {'1m': 3044, '5m': 169}). Runner = half at T1, rest to the close with a breakeven stop. 1st/2nd half columns are the out-of-sample check.

| Group | Setups | Triggered | Trigger rate | Win rate | Avg R | Expectancy R | Profit factor | Total R | Max DD R | 1st half avg R | 2nd half avg R |
|---|---|---|---|---|---|---|---|---|---|---|---|
| All (New York) · Current plan | 3216 | 962 | 29.9% | 41.8% | -0.1 | -0.03 | 0.84 | -97.09 | -122.81 | -0.08 | -0.12 |
| All (New York) · Runner to the close | 3216 | 962 | 29.9% | 41.8% | -0.1 | -0.03 | 0.84 | -94.53 | -122.02 | -0.06 | -0.14 |
| All (New York) · Full position to T2 | 3216 | 962 | 29.9% | 37.4% | -0.1 | -0.03 | 0.86 | -93.21 | -130.03 | -0.07 | -0.12 |
| All (New York) · Confirmation entry | 3216 | 1049 | 32.6% | 51.8% | -0.11 | -0.03 | 0.72 | -111.98 | -112.6 | -0.13 | -0.09 |
| v3: 11:30-14:30 + risk 0.3%+ + FVG 0.5+ ATR · Current plan | 840 | 173 | 20.6% | 45.7% | 0.03 | 0.01 | 1.07 | 5.85 | -21.03 | 0.09 | -0.02 |
| v3: 11:30-14:30 + risk 0.3%+ + FVG 0.5+ ATR · Runner to the close | 840 | 173 | 20.6% | 45.7% | 0.02 | 0.0 | 1.04 | 3.82 | -21.03 | 0.09 | -0.05 |
| v3: 11:30-14:30 + risk 0.3%+ + FVG 0.5+ ATR · Full position to T2 | 840 | 173 | 20.6% | 43.9% | 0.06 | 0.01 | 1.11 | 10.83 | -22.04 | 0.09 | 0.03 |
| v3: 11:30-14:30 + risk 0.3%+ + FVG 0.5+ ATR · Confirmation entry | 840 | 232 | 27.6% | 54.7% | -0.01 | -0.0 | 0.98 | -1.48 | -14.71 | 0.07 | -0.08 |
| v3 + longs · Current plan | 682 | 134 | 19.6% | 48.5% | 0.1 | 0.02 | 1.2 | 13.2 | -18.59 | 0.23 | -0.03 |
| v3 + longs · Runner to the close | 682 | 134 | 19.6% | 48.5% | 0.08 | 0.02 | 1.17 | 11.17 | -18.59 | 0.23 | -0.06 |
| v3 + longs · Full position to T2 | 682 | 134 | 19.6% | 44.8% | 0.09 | 0.02 | 1.17 | 12.35 | -20.33 | 0.2 | -0.01 |
| v3 + longs · Confirmation entry | 682 | 190 | 27.9% | 55.3% | 0.01 | 0.0 | 1.03 | 1.63 | -13.85 | 0.12 | -0.1 |
| v3 + VWAP side · Current plan | 628 | 95 | 15.1% | 49.5% | 0.04 | 0.01 | 1.1 | 4.21 | -9.78 | 0.08 | 0.01 |
| v3 + VWAP side · Runner to the close | 628 | 95 | 15.1% | 49.5% | 0.02 | 0.0 | 1.05 | 2.18 | -9.78 | 0.08 | -0.03 |
| v3 + VWAP side · Full position to T2 | 628 | 95 | 15.1% | 47.4% | 0.05 | 0.01 | 1.1 | 4.79 | -10.37 | 0.04 | 0.06 |
| v3 + VWAP side · Confirmation entry | 628 | 141 | 22.5% | 52.5% | 0.0 | 0.0 | 1.01 | 0.56 | -7.9 | 0.05 | -0.05 |
| v3 + in play (open volume 1.5x+) · Current plan | 132 | 30 | 22.7% | 40.0% | -0.05 | -0.01 | 0.9 | -1.41 | -3.78 | 0.0 | -0.1 |
| v3 + in play (open volume 1.5x+) · Runner to the close | 132 | 30 | 22.7% | 40.0% | -0.05 | -0.01 | 0.9 | -1.41 | -3.78 | 0.0 | -0.1 |
| v3 + in play (open volume 1.5x+) · Full position to T2 | 132 | 30 | 22.7% | 40.0% | -0.15 | -0.03 | 0.72 | -4.47 | -6.7 | -0.11 | -0.19 |
| v3 + in play (open volume 1.5x+) · Confirmation entry | 132 | 38 | 28.8% | 52.6% | -0.06 | -0.02 | 0.84 | -2.28 | -5.06 | 0.01 | -0.13 |
| v3 + longs + VWAP side · Current plan | 529 | 79 | 14.9% | 50.6% | 0.11 | 0.02 | 1.24 | 8.78 | -6.52 | 0.16 | 0.06 |
| v3 + longs + VWAP side · Runner to the close | 529 | 79 | 14.9% | 50.6% | 0.09 | 0.01 | 1.18 | 6.74 | -6.52 | 0.17 | 0.01 |
| v3 + longs + VWAP side · Full position to T2 | 529 | 79 | 14.9% | 49.4% | 0.15 | 0.02 | 1.32 | 11.93 | -7.1 | 0.19 | 0.11 |
| v3 + longs + VWAP side · Confirmation entry | 529 | 122 | 23.1% | 52.5% | 0.01 | 0.0 | 1.03 | 0.95 | -8.23 | 0.07 | -0.06 |
| VWAP side only · Current plan | 2200 | 581 | 26.4% | 41.8% | -0.14 | -0.04 | 0.77 | -80.24 | -80.24 | -0.16 | -0.12 |
| VWAP side only · Runner to the close | 2200 | 581 | 26.4% | 41.8% | -0.14 | -0.04 | 0.77 | -81.08 | -84.67 | -0.12 | -0.16 |
| VWAP side only · Full position to T2 | 2200 | 581 | 26.4% | 38.4% | -0.14 | -0.04 | 0.79 | -78.76 | -87.42 | -0.14 | -0.13 |
| VWAP side only · Confirmation entry | 2200 | 669 | 30.4% | 51.3% | -0.11 | -0.03 | 0.7 | -76.72 | -77.31 | -0.13 | -0.1 |
| In play only · Current plan | 428 | 123 | 28.7% | 35.8% | -0.29 | -0.08 | 0.57 | -35.18 | -38.58 | -0.42 | -0.16 |
| In play only · Runner to the close | 428 | 123 | 28.7% | 35.8% | -0.29 | -0.08 | 0.55 | -36.2 | -39.6 | -0.42 | -0.17 |
| In play only · Full position to T2 | 428 | 123 | 28.7% | 31.7% | -0.38 | -0.11 | 0.48 | -46.72 | -51.1 | -0.51 | -0.25 |
| In play only · Confirmation entry | 428 | 135 | 31.5% | 51.9% | -0.14 | -0.04 | 0.66 | -18.32 | -23.63 | -0.25 | -0.02 |

## 11. Trendline retest confluence (New York session, qualified, net of costs)

Trendline = the falling line across the lower highs into the sweep (rising line across higher lows for shorts), broken by a close and not failed. Confluence = its level at the snapshot sits in the entry zone (FVG near edge to entry) within 0.25 ATR. Retest at fill = the line was within 0.3 ATR of the fill price when the order filled. Only rows recorded since Nov 4, 2026 (rerun the backtest to fill history).

| Group | Setups | Triggered | Trigger rate | Win rate | Avg R | Expectancy R | Profit factor | Total R | Max DD R | 1st half avg R | 2nd half avg R |
|---|---|---|---|---|---|---|---|---|---|---|---|
| All (New York, trendline recorded) · current plan | 303 | 115 | 38.0% | 33.9% | -0.36 | -0.14 | 0.47 | -41.96 | -43.38 | -0.37 | -0.36 |
| No trendline found/broken · current plan | 181 | 54 | 29.8% | 35.2% | -0.37 | -0.11 | 0.47 | -20.16 | -21.35 | -0.52 | -0.23 |
| Trendline found and broken · current plan | 122 | 61 | 50.0% | 32.8% | -0.36 | -0.18 | 0.47 | -21.8 | -24.27 | -0.07 | -0.64 |
| Trendline confluence at snapshot · current plan | 23 | 13 | 56.5% | 38.5% | -0.18 | -0.1 | 0.61 | -2.38 | -5.07 | -0.37 | -0.02 |
| No confluence at snapshot · current plan | 280 | 102 | 36.4% | 33.3% | -0.39 | -0.14 | 0.46 | -39.58 | -39.71 | -0.4 | -0.38 |
| Confluence, 3+ touches · current plan | 6 | 3 | 50.0% | 100.0% | 0.77 | 0.39 |  | 2.31 | 0.0 | 0.78 | 0.77 |
| Confluence + longs · current plan | 18 | 10 | 55.6% | 50.0% | -0.11 | -0.06 | 0.77 | -1.09 | -4.02 | -0.23 | 0.02 |
| Confluence + midday (11:30-14:30) · current plan | 17 | 10 | 58.8% | 40.0% | -0.19 | -0.11 | 0.62 | -1.86 | -4.02 | -0.23 | -0.14 |
| Confluence + risk 0.3%+ · current plan | 16 | 10 | 62.5% | 30.0% | -0.25 | -0.15 | 0.51 | -2.45 | -4.71 | -0.56 | 0.07 |
| Confluence + VWAP side · current plan | 7 | 4 | 57.1% | 25.0% | -0.21 | -0.12 | 0.5 | -0.85 | -1.68 | 0.18 | -0.61 |
| Confluence + longs + midday + risk 0.3%+ · current plan | 11 | 7 | 63.6% | 42.9% | -0.17 | -0.11 | 0.68 | -1.16 | -3.67 | -0.24 | -0.11 |
| Fill was a trendline retest (any setup) | 303 | 6 | 2.0% | 50.0% | -0.07 | -0.0 | 0.84 | -0.42 | -1.88 | -0.33 | 0.19 |
| Fill was a trendline retest + longs | 240 | 6 | 2.5% | 50.0% | -0.07 | -0.0 | 0.84 | -0.42 | -1.88 | -0.33 | 0.19 |
| Entry at the trendline (stop 0.1 ATR) | 23 | 12 | 52.2% | 41.7% | -0.25 | -0.13 | 0.34 | -3.02 | -4.13 | -0.4 | -0.1 |
| Entry at the trendline (stop 0.3 ATR) | 23 | 12 | 52.2% | 50.0% | -0.22 | -0.11 | 0.42 | -2.64 | -4.25 | -0.44 | 0.0 |

## 9. Automatic changes in this run

| Key | Old | New | Evidence |
|---|---|---|---|
| None |  |  |  |
