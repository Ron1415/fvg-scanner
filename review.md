# FVG review: 2026-11-11 17:04 ET (Daily)

Sessions: 131 (2026-05-07 to 2026-11-11). Config version 1.

## 1. Strategy performance (qualified setups; results net of costs)

Costs: 0.02% of price per side. Entries allowed until 15:30 ET.

| Group | Setups | Triggered | Trigger rate | Win rate | Avg R | Expectancy R | Profit factor | Total R | Max DD R | 1st half avg R | 2nd half avg R |
|---|---|---|---|---|---|---|---|---|---|---|---|
| Live dashboard snapshots | 116 | 30 | 25.9% | 40.0% | -0.13 | -0.03 | 0.75 | -3.84 | -6.88 | -0.04 | -0.22 |
| Daily full-session replays | 183 | 52 | 28.4% | 48.1% | -0.1 | -0.03 | 0.83 | -5.28 | -12.97 | 0.01 | -0.22 |
| Backtest | 3224 | 1010 | 31.3% | 41.1% | -0.1 | -0.03 | 0.84 | -104.96 | -135.21 | -0.08 | -0.13 |
| Systematic (replays + backtest) | 3407 | 1062 | 31.2% | 41.4% | -0.1 | -0.03 | 0.84 | -110.24 | -136.4 | -0.1 | -0.11 |
| Systematic, before cost (gross) | 3407 | 1062 | 31.2% | 43.0% | 0.1 | 0.03 | 1.19 | 105.55 | -37.49 | 0.07 | 0.13 |
| Systematic, plan window only (New York, formed by 11:30) | 956 | 369 | 38.6% | 39.0% | -0.17 | -0.07 | 0.73 | -63.01 | -63.51 | -0.25 | -0.09 |
| Live top-5 suggestions only | 77 | 20 | 26.0% | 40.0% | -0.18 | -0.05 | 0.66 | -3.67 | -4.29 | -0.19 | -0.18 |
| Your actual trades | 1 | 1 |  | 0.0% | -1.77 |  |  | -1.77 |  |  |  |
| Stocks and ETFs, New York session only | 2880 | 832 | 28.9% | 42.4% | -0.08 | -0.02 | 0.87 | -66.02 | -92.17 | -0.07 | -0.09 |
| Futures, New York session | 147 | 47 | 32.0% | 48.9% | 0.03 | 0.01 | 1.05 | 1.34 | -9.25 | 0.33 | -0.26 |
| Futures, all 24-hour sessions | 527 | 230 | 43.6% | 37.8% | -0.19 | -0.08 | 0.74 | -44.23 | -47.51 | -0.28 | -0.11 |

## 1c. Futures by session (24-hour test; qualified, net of costs)

Asia and London use their own levels: prior-day high/low, the previous session's high/low, and the session's first 30 minutes.

| Group | Setups | Triggered | Trigger rate | Win rate | Avg R | Expectancy R | Profit factor | Total R | Max DD R | 1st half avg R | 2nd half avg R |
|---|---|---|---|---|---|---|---|---|---|---|---|
| Futures, Asia session (6 PM-midnight ET) | 171 | 74 | 43.3% | 29.7% | -0.27 | -0.12 | 0.66 | -20.09 | -21.96 | -0.21 | -0.33 |
| Futures, London session (2-8 AM ET) | 209 | 109 | 52.2% | 38.5% | -0.23 | -0.12 | 0.69 | -25.48 | -38.05 | -0.64 | 0.16 |
| Futures, NY session (9:30-4:00 ET) | 147 | 47 | 32.0% | 48.9% | 0.03 | 0.01 | 1.05 | 1.34 | -9.25 | 0.33 | -0.26 |
| CL=F Asia | 21 | 11 | 52.4% | 45.5% | 0.4 | 0.21 | 1.65 | 4.39 | -2.35 | -0.11 | 0.82 |
| CL=F London | 21 | 8 | 38.1% | 50.0% | 0.38 | 0.14 | 1.81 | 3.02 | -2.21 | -0.35 | 1.1 |
| CL=F NY | 21 | 7 | 33.3% | 28.6% | -0.38 | -0.13 | 0.5 | -2.66 | -3.18 | -1.06 | 0.13 |
| ES=F Asia | 16 | 6 | 37.5% | 33.3% | -0.45 | -0.17 | 0.43 | -2.72 | -4.64 | 0.28 | -1.18 |
| ES=F London | 26 | 16 | 61.5% | 43.8% | 0.19 | 0.11 | 1.28 | 2.98 | -5.2 | -0.57 | 0.94 |
| ES=F NY | 19 | 8 | 42.1% | 75.0% | 0.85 | 0.36 | 5.84 | 6.83 | -1.41 | 1.23 | 0.48 |
| GC=F Asia | 35 | 23 | 65.7% | 26.1% | -0.06 | -0.04 | 0.91 | -1.47 | -10.46 | 0.18 | -0.29 |
| GC=F London | 16 | 6 | 37.5% | 66.7% | 0.35 | 0.13 | 2.0 | 2.09 | -1.05 | 0.05 | 0.64 |
| GC=F NY | 15 | 4 | 26.7% | 50.0% | 0.28 | 0.07 | 1.54 | 1.11 | -1.04 | 0.66 | -0.1 |
| NQ=F Asia | 14 | 7 | 50.0% | 28.6% | -0.32 | -0.16 | 0.57 | -2.21 | -5.19 | -1.04 | 0.23 |
| NQ=F London | 19 | 7 | 36.8% | 0.0% | -0.79 | -0.29 | 0.0 | -5.53 | -5.53 | -1.03 | -0.61 |
| NQ=F NY | 13 | 4 | 30.8% | 25.0% | -0.32 | -0.1 | 0.38 | -1.29 | -2.08 | -1.01 | 0.37 |
| RTY=F Asia | 19 | 5 | 26.3% | 60.0% | 0.4 | 0.11 | 1.9 | 2.01 | -2.23 | 1.12 | -0.08 |
| RTY=F London | 32 | 21 | 65.6% | 28.6% | -0.39 | -0.26 | 0.47 | -8.24 | -10.2 | -0.79 | -0.03 |
| RTY=F NY | 15 | 2 | 13.3% | 50.0% | -0.1 | -0.01 | 0.82 | -0.19 | -1.04 | -1.04 | 0.85 |
| YM=F Asia | 21 | 6 | 28.6% | 16.7% | -0.8 | -0.23 | 0.15 | -4.81 | -5.67 | -0.51 | -1.09 |
| YM=F London | 29 | 15 | 51.7% | 60.0% | 0.4 | 0.21 | 1.89 | 6.03 | -2.29 | 0.32 | 0.48 |
| YM=F NY | 15 | 2 | 13.3% | 50.0% | 1.16 | 0.15 | 3.24 | 2.31 | -1.03 | 3.35 | -1.03 |
| ZB=F Asia | 16 | 6 | 37.5% | 16.7% | -1.29 | -0.48 | 0.02 | -7.73 | -7.73 | -0.65 | -1.92 |
| ZB=F London | 13 | 8 | 61.5% | 50.0% | -0.19 | -0.11 | 0.72 | -1.49 | -3.38 | -0.7 | 0.33 |
| ZB=F NY | 16 | 7 | 43.8% | 71.4% | 0.53 | 0.23 | 2.27 | 3.72 | -1.6 | 0.58 | 0.5 |
| ZF=F Asia | 15 | 5 | 33.3% | 20.0% | -0.95 | -0.32 | 0.14 | -4.76 | -4.76 | -0.87 | -1.01 |
| ZF=F London | 19 | 12 | 63.2% | 25.0% | -1.1 | -0.7 | 0.2 | -13.21 | -13.21 | -1.84 | -0.36 |
| ZF=F NY | 14 | 6 | 42.9% | 50.0% | -0.72 | -0.31 | 0.14 | -4.31 | -4.64 | -0.53 | -0.9 |
| ZN=F Asia | 9 | 4 | 44.4% | 25.0% | -0.49 | -0.22 | 0.37 | -1.95 | -2.63 | -1.31 | 0.34 |
| ZN=F London | 13 | 7 | 53.8% | 28.6% | -0.7 | -0.38 | 0.36 | -4.88 | -4.88 | -0.59 | -0.78 |
| ZN=F NY | 8 | 5 | 62.5% | 40.0% | -0.31 | -0.19 | 0.54 | -1.53 | -1.81 | -0.77 | 0.0 |
| ZS=F Asia | 5 | 1 | 20.0% | 0.0% | -0.85 | -0.17 | 0.0 | -0.85 | -0.85 |  | -0.85 |
| ZS=F London | 21 | 9 | 42.9% | 33.3% | -0.69 | -0.3 | 0.32 | -6.25 | -7.26 | -0.95 | -0.49 |
| ZS=F NY | 11 | 2 | 18.2% | 0.0% | -1.33 | -0.24 | 0.0 | -2.66 | -2.66 | -1.32 | -1.34 |

## 2. New York session: by asset, side, time of day, risk size (systematic, qualified)

| Group | Setups | Triggered | Trigger rate | Win rate | Avg R | Expectancy R | Profit factor | Total R | Max DD R | 1st half avg R | 2nd half avg R |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ETF | 942 | 315 | 33.4% | 41.9% | -0.15 | -0.05 | 0.78 | -47.79 | -63.67 | -0.07 | -0.23 |
| Stock | 1938 | 517 | 26.7% | 42.7% | -0.04 | -0.01 | 0.94 | -18.23 | -41.36 | -0.06 | -0.01 |
| Future | 147 | 47 | 32.0% | 48.9% | 0.03 | 0.01 | 1.05 | 1.34 | -9.25 | 0.33 | -0.26 |
| Leveraged/inverse ETFs | 139 | 44 | 31.7% | 50.0% | 0.33 | 0.11 | 1.76 | 14.65 | -6.42 | 0.77 | -0.11 |
| LONG | 2677 | 797 | 29.8% | 42.8% | -0.08 | -0.02 | 0.88 | -61.85 | -87.25 | -0.08 | -0.07 |
| SHORT | 350 | 82 | 23.4% | 42.7% | -0.03 | -0.01 | 0.91 | -2.82 | -9.63 | -0.08 | 0.01 |
| Formed 10:00-10:30 | 313 | 148 | 47.3% | 31.8% | -0.27 | -0.13 | 0.63 | -40.16 | -40.16 | -0.32 | -0.22 |
| Formed 10:30-11:30 | 595 | 206 | 34.6% | 43.7% | -0.1 | -0.04 | 0.81 | -21.61 | -33.43 | -0.25 | 0.04 |
| Formed 11:30-13:00 | 846 | 267 | 31.6% | 48.7% | -0.0 | -0.0 | 0.99 | -1.08 | -18.0 | 0.03 | -0.04 |
| Formed 13:00-14:30 | 752 | 197 | 26.2% | 40.6% | -0.07 | -0.02 | 0.89 | -13.11 | -34.2 | -0.19 | 0.06 |
| Formed 14:30-16:00 | 521 | 61 | 11.7% | 47.5% | 0.19 | 0.02 | 1.32 | 11.29 | -16.45 | 0.73 | -0.34 |
| Risk 0-0.15% of price | 620 | 300 | 48.4% | 34.3% | -0.4 | -0.19 | 0.54 | -120.62 | -120.64 | -0.44 | -0.36 |
| Risk 0.15-0.3% of price | 670 | 244 | 36.4% | 41.4% | -0.09 | -0.03 | 0.86 | -21.76 | -45.15 | -0.14 | -0.04 |
| Risk 0.3-0.6% of price | 1075 | 290 | 27.0% | 45.9% | 0.07 | 0.02 | 1.14 | 20.96 | -20.24 | 0.07 | 0.08 |
| Risk 0.6%+ | 1042 | 228 | 21.9% | 45.2% | 0.05 | 0.01 | 1.1 | 11.19 | -16.61 | 0.06 | 0.03 |

## 2b. Short guardrails (systematic; shorts use full exit at T1, breakeven at +0.5R, 60-minute time stop)

Sizing: longs 1.25% risk (cap 5.0% of account), shorts 0.5% risk (cap 2.5%). Results here are in R, before sizing.

| Group | Setups | Triggered | Trigger rate | Win rate | Avg R | Expectancy R | Profit factor | Total R | Max DD R | 1st half avg R | 2nd half avg R |
|---|---|---|---|---|---|---|---|---|---|---|---|
| Longs passing the normal filters | 3056 | 980 | 32.1% | 41.3% | -0.11 | -0.04 | 0.83 | -107.42 | -132.82 | -0.11 | -0.11 |
| Shorts passing the normal filters (before guardrails) | 2211 | 790 | 35.7% | 27.6% | -0.18 | -0.06 | 0.64 | -140.28 | -143.36 | -0.08 | -0.28 |
| Shorts passing every guardrail (traded) | 351 | 82 | 23.4% | 42.7% | -0.03 | -0.01 | 0.91 | -2.82 | -9.63 | -0.08 | 0.01 |
| Shorts passing: bearish daily trend | 952 | 348 | 36.6% | 29.6% | -0.2 | -0.07 | 0.61 | -71.33 | -78.54 | -0.12 | -0.29 |
| Shorts failing: bearish daily trend | 1259 | 442 | 35.1% | 26.0% | -0.16 | -0.05 | 0.68 | -68.95 | -70.6 | -0.09 | -0.23 |
| Shorts passing: PDH or 2+ level sweep | 1582 | 533 | 33.7% | 29.5% | -0.12 | -0.04 | 0.74 | -61.73 | -66.59 | -0.04 | -0.19 |
| Shorts failing: PDH or 2+ level sweep | 629 | 257 | 40.9% | 23.7% | -0.31 | -0.12 | 0.5 | -78.55 | -79.41 | -0.29 | -0.32 |
| Shorts passing: R:R to T2 3.0+ | 1622 | 579 | 35.7% | 27.8% | -0.19 | -0.07 | 0.64 | -108.11 | -112.44 | -0.05 | -0.32 |
| Shorts failing: R:R to T2 3.0+ | 589 | 211 | 35.8% | 27.0% | -0.15 | -0.05 | 0.66 | -32.17 | -38.04 | -0.12 | -0.18 |
| Shorts passing: risk 0.3%+ of price | 1183 | 348 | 29.4% | 32.8% | -0.02 | -0.01 | 0.94 | -7.66 | -25.88 | 0.05 | -0.09 |
| Shorts failing: risk 0.3%+ of price | 1028 | 442 | 43.0% | 23.5% | -0.3 | -0.13 | 0.5 | -132.62 | -134.27 | -0.24 | -0.36 |
| Shorts passing: formed 10:30 or later | 1967 | 662 | 33.7% | 26.9% | -0.19 | -0.07 | 0.62 | -128.79 | -130.44 | -0.11 | -0.28 |
| Shorts failing: formed 10:30 or later | 244 | 128 | 52.5% | 31.2% | -0.09 | -0.05 | 0.79 | -11.49 | -20.84 | 0.1 | -0.28 |
| Shorts passing: not a leveraged ETF | 2123 | 764 | 36.0% | 27.2% | -0.19 | -0.07 | 0.61 | -148.91 | -150.56 | -0.1 | -0.29 |
| Shorts failing: not a leveraged ETF | 88 | 26 | 29.5% | 38.5% | 0.33 | 0.1 | 2.07 | 8.63 | -2.49 | 0.81 | -0.14 |

## 3. Outcomes (systematic, qualified)

| Outcome | Count | Share | Avg R |
|---|---|---|---|
| Not triggered (ran to T1 first) | 2156 | 63.3% | 0.0 |
| Stop | 506 | 14.9% | -1.22 |
| EOD exit | 214 | 6.3% | 0.19 |
| Not triggered (cutoff) | 188 | 5.5% | 0.0 |
| T1 then EOD | 142 | 4.2% | 1.82 |
| T1 then breakeven | 80 | 2.3% | 0.58 |
| T1 then T2 | 76 | 2.2% | 1.98 |
| Time stop | 27 | 0.8% | 0.47 |
| Breakeven stop | 17 | 0.5% | -0.1 |
| Invalidated before entry | 1 | 0.0% | 0.0 |

## 4. Score calibration. A useful score shows results improving band by band.

| Group | Setups | Triggered | Trigger rate | Win rate | Avg R | Expectancy R | Profit factor | Total R | Max DD R | 1st half avg R | 2nd half avg R |
|---|---|---|---|---|---|---|---|---|---|---|---|
| Score 90+ | 20 | 12 | 60.0% | 75.0% | 0.92 | 0.55 | 6.01 | 11.09 | -2.22 | 1.18 | 0.67 |
| Score 75-89 | 1258 | 370 | 29.4% | 40.3% | -0.13 | -0.04 | 0.79 | -47.69 | -74.93 | -0.14 | -0.11 |
| Score 60-74 | 1871 | 573 | 30.6% | 42.8% | -0.06 | -0.02 | 0.9 | -36.64 | -53.11 | -0.03 | -0.09 |
| Score under 60 | 258 | 107 | 41.5% | 34.6% | -0.35 | -0.14 | 0.56 | -37.0 | -39.05 | -0.54 | -0.16 |

## 5. Factor attribution (all triggered systematic setups, qualified or not)

| Factor | Weight key | Weight | With | Avg R with | Without | Avg R without | Difference | Read |
|---|---|---|---|---|---|---|---|---|
| Prior-day level swept | sweep_pd | 20 | 2688 | -0.11 | 3053 | -0.16 | 0.04 | No clear effect |
| Only PM/OR level swept | sweep_other | 15 | 2425 | -0.14 | 3316 | -0.13 | -0.01 | No clear effect |
| FVG in discount/premium | zone | 10 | 2083 | -0.16 | 3658 | -0.12 | -0.04 | No clear effect |
| FVG overlaps OTE | ote | 15 | 1839 | -0.15 | 3902 | -0.13 | -0.01 | No clear effect |
| R:R to T1 of 2 or more | rr | 10 | 439 | -0.25 | 5302 | -0.13 | -0.12 | No clear effect |
| HTF bias aligned | bias | 10 | 2210 | -0.14 | 3531 | -0.13 | -0.01 | No clear effect |
| Displacement volume 1.5x+ | vol | 5 | 700 | -0.09 | 5041 | -0.14 | 0.05 | No clear effect |
| Formed 10:00-11:30 | time | 5 | 2692 | -0.18 | 3049 | -0.1 | -0.08 | No clear effect |
| Trendline retest confluence | tl | 10 | 31 | 0.03 | 225 | -0.22 | 0.24 | Helps |

## 6. Filter check (systematic)

| Group | Setups | Triggered | Trigger rate | Win rate | Avg R | Expectancy R | Profit factor | Total R | Max DD R | 1st half avg R | 2nd half avg R |
|---|---|---|---|---|---|---|---|---|---|---|---|
| Passed filters | 3407 | 1062 | 31.2% | 41.4% | -0.1 | -0.03 | 0.84 | -110.24 | -136.4 | -0.1 | -0.11 |
| Filtered out | 7820 | 4679 | 59.8% | 47.7% | -0.14 | -0.09 | 0.62 | -676.21 | -680.02 | -0.11 | -0.18 |
| No OTE overlap | 5814 | 3902 | 67.1% | 51.9% | -0.13 | -0.09 | 0.62 | -518.33 | -521.85 | -0.11 | -0.15 |
| OTE overlap, R:R to T2 1.5-2 | 146 | 69 | 47.3% | 30.4% | -0.3 | -0.14 | 0.5 | -20.42 | -20.51 | -0.13 | -0.46 |
| OTE overlap, R:R to T2 2-2.5 | 1199 | 346 | 28.9% | 36.1% | -0.14 | -0.04 | 0.74 | -49.57 | -55.24 | -0.13 | -0.16 |
| OTE overlap, R:R to T2 2.5-3 | 617 | 198 | 32.1% | 37.9% | -0.02 | -0.0 | 0.97 | -3.01 | -43.27 | -0.26 | 0.23 |
| OTE overlap, R:R to T2 3+ | 3451 | 1226 | 35.5% | 34.5% | -0.16 | -0.06 | 0.74 | -195.12 | -228.59 | -0.06 | -0.26 |

## 7. Improvement tests: entry type x stop buffer x filter (net of costs)

ote_mid = current entry (middle of the FVG/OTE overlap); fvg_edge = first touch of the gap; fvg_ce = gap midpoint; blend = halfway between the gap edge and ote_mid; ote_62 = first touch of the OTE zone; tl_line = limit at the broken trendline (only setups with trendline confluence). Scaled rows are in R of the full planned position (a partial fill counts only what filled).

| Group | Setups | Triggered | Trigger rate | Win rate | Avg R | Expectancy R | Profit factor | Total R | Max DD R | 1st half avg R | 2nd half avg R |
|---|---|---|---|---|---|---|---|---|---|---|---|
| Entry ote_mid, stop 0.1 ATR · All qualified | 3407 | 1062 | 31.2% | 41.4% | -0.1 | -0.03 | 0.84 | -110.23 | -136.39 | -0.1 | -0.11 |
| Entry ote_mid, stop 0.1 ATR · Plan window (by 11:30) | 956 | 369 | 38.6% | 39.0% | -0.17 | -0.07 | 0.73 | -63.0 | -63.51 | -0.25 | -0.09 |
| Entry ote_mid, stop 0.1 ATR · Midday 11:30-14:30 | 1598 | 464 | 29.0% | 45.3% | -0.03 | -0.01 | 0.95 | -14.19 | -35.77 | -0.05 | -0.01 |
| Entry ote_mid, stop 0.1 ATR · Stocks only | 1938 | 517 | 26.7% | 42.7% | -0.04 | -0.01 | 0.94 | -18.23 | -41.36 | -0.06 | -0.01 |
| Entry ote_mid, stop 0.1 ATR · R:R to T2 2.5+ | 2564 | 844 | 32.9% | 41.4% | -0.11 | -0.04 | 0.83 | -92.37 | -128.51 | -0.11 | -0.11 |
| Entry ote_mid, stop 0.1 ATR · Risk 0.15%+ | 2787 | 762 | 27.3% | 44.2% | 0.01 | 0.0 | 1.03 | 10.39 | -51.41 | 0.01 | 0.01 |
| Entry ote_mid, stop 0.1 ATR · Midday + R:R 2.5+ + risk 0.15%+ | 1074 | 330 | 30.7% | 46.7% | 0.05 | 0.02 | 1.1 | 17.51 | -22.62 | 0.04 | 0.07 |
| Entry ote_mid, stop 0.3 ATR · All qualified | 3407 | 1062 | 31.2% | 44.4% | -0.09 | -0.03 | 0.85 | -91.4 | -114.56 | -0.07 | -0.1 |
| Entry ote_mid, stop 0.3 ATR · Plan window (by 11:30) | 956 | 369 | 38.6% | 42.0% | -0.16 | -0.06 | 0.73 | -57.92 | -58.0 | -0.24 | -0.08 |
| Entry ote_mid, stop 0.3 ATR · Midday 11:30-14:30 | 1598 | 464 | 29.0% | 48.3% | -0.01 | -0.0 | 0.98 | -4.96 | -26.45 | 0.0 | -0.03 |
| Entry ote_mid, stop 0.3 ATR · Stocks only | 1938 | 517 | 26.7% | 45.8% | -0.03 | -0.01 | 0.94 | -16.29 | -38.05 | -0.02 | -0.04 |
| Entry ote_mid, stop 0.3 ATR · R:R to T2 2.5+ | 2564 | 844 | 32.9% | 44.8% | -0.08 | -0.03 | 0.86 | -68.6 | -99.09 | -0.07 | -0.09 |
| Entry ote_mid, stop 0.3 ATR · Risk 0.15%+ | 2787 | 762 | 27.3% | 47.2% | 0.02 | 0.01 | 1.05 | 17.45 | -36.54 | 0.03 | 0.01 |
| Entry ote_mid, stop 0.3 ATR · Midday + R:R 2.5+ + risk 0.15%+ | 1074 | 330 | 30.7% | 50.3% | 0.08 | 0.02 | 1.16 | 25.3 | -17.07 | 0.12 | 0.04 |
| Entry fvg_edge, stop 0.1 ATR · All qualified | 3407 | 1412 | 41.4% | 50.3% | -0.08 | -0.03 | 0.82 | -117.31 | -131.96 | -0.09 | -0.08 |
| Entry fvg_edge, stop 0.1 ATR · Plan window (by 11:30) | 956 | 474 | 49.6% | 49.8% | -0.13 | -0.07 | 0.71 | -63.18 | -63.71 | -0.14 | -0.13 |
| Entry fvg_edge, stop 0.1 ATR · Midday 11:30-14:30 | 1598 | 630 | 39.4% | 51.6% | -0.06 | -0.03 | 0.85 | -40.52 | -49.53 | -0.07 | -0.05 |
| Entry fvg_edge, stop 0.1 ATR · Stocks only | 1938 | 698 | 36.0% | 49.9% | -0.09 | -0.03 | 0.8 | -60.86 | -66.33 | -0.12 | -0.06 |
| Entry fvg_edge, stop 0.1 ATR · R:R to T2 2.5+ | 2564 | 1101 | 42.9% | 49.8% | -0.1 | -0.04 | 0.8 | -106.33 | -120.87 | -0.11 | -0.08 |
| Entry fvg_edge, stop 0.1 ATR · Risk 0.15%+ | 2787 | 1035 | 37.1% | 53.0% | -0.03 | -0.01 | 0.93 | -29.51 | -67.32 | -0.01 | -0.04 |
| Entry fvg_edge, stop 0.1 ATR · Midday + R:R 2.5+ + risk 0.15%+ | 1074 | 430 | 40.0% | 52.3% | -0.05 | -0.02 | 0.88 | -22.04 | -31.79 | -0.03 | -0.08 |
| Entry fvg_edge, stop 0.3 ATR · All qualified | 3407 | 1412 | 41.4% | 52.5% | -0.07 | -0.03 | 0.84 | -96.92 | -110.47 | -0.06 | -0.08 |
| Entry fvg_edge, stop 0.3 ATR · Plan window (by 11:30) | 956 | 474 | 49.6% | 51.9% | -0.12 | -0.06 | 0.71 | -58.35 | -58.72 | -0.13 | -0.12 |
| Entry fvg_edge, stop 0.3 ATR · Midday 11:30-14:30 | 1598 | 630 | 39.4% | 53.8% | -0.05 | -0.02 | 0.88 | -30.04 | -38.6 | -0.03 | -0.06 |
| Entry fvg_edge, stop 0.3 ATR · Stocks only | 1938 | 698 | 36.0% | 52.3% | -0.07 | -0.03 | 0.82 | -51.31 | -55.94 | -0.07 | -0.07 |
| Entry fvg_edge, stop 0.3 ATR · R:R to T2 2.5+ | 2564 | 1101 | 42.9% | 52.5% | -0.07 | -0.03 | 0.83 | -81.14 | -97.18 | -0.07 | -0.07 |
| Entry fvg_edge, stop 0.3 ATR · Risk 0.15%+ | 2787 | 1035 | 37.1% | 55.3% | -0.02 | -0.01 | 0.96 | -16.67 | -52.06 | 0.01 | -0.04 |
| Entry fvg_edge, stop 0.3 ATR · Midday + R:R 2.5+ + risk 0.15%+ | 1074 | 430 | 40.0% | 55.1% | -0.03 | -0.01 | 0.93 | -10.98 | -23.34 | 0.04 | -0.09 |
| Entry fvg_ce, stop 0.1 ATR · All qualified | 3407 | 1169 | 34.3% | 44.5% | -0.11 | -0.04 | 0.81 | -128.38 | -141.55 | -0.11 | -0.11 |
| Entry fvg_ce, stop 0.1 ATR · Plan window (by 11:30) | 956 | 406 | 42.5% | 43.8% | -0.15 | -0.06 | 0.73 | -61.62 | -62.35 | -0.2 | -0.1 |
| Entry fvg_ce, stop 0.1 ATR · Midday 11:30-14:30 | 1598 | 517 | 32.4% | 47.2% | -0.06 | -0.02 | 0.88 | -31.7 | -43.33 | -0.06 | -0.06 |
| Entry fvg_ce, stop 0.1 ATR · Stocks only | 1938 | 573 | 29.6% | 45.5% | -0.07 | -0.02 | 0.87 | -37.36 | -52.09 | -0.1 | -0.03 |
| Entry fvg_ce, stop 0.1 ATR · R:R to T2 2.5+ | 2564 | 921 | 35.9% | 44.1% | -0.11 | -0.04 | 0.81 | -100.4 | -123.85 | -0.12 | -0.09 |
| Entry fvg_ce, stop 0.1 ATR · Risk 0.15%+ | 2787 | 847 | 30.4% | 47.1% | -0.02 | -0.0 | 0.97 | -13.84 | -58.75 | -0.02 | -0.01 |
| Entry fvg_ce, stop 0.1 ATR · Midday + R:R 2.5+ + risk 0.15%+ | 1074 | 362 | 33.7% | 48.3% | -0.01 | -0.0 | 0.98 | -3.84 | -24.3 | 0.01 | -0.03 |
| Entry fvg_ce, stop 0.3 ATR · All qualified | 3407 | 1169 | 34.3% | 47.1% | -0.09 | -0.03 | 0.83 | -105.23 | -117.75 | -0.08 | -0.1 |
| Entry fvg_ce, stop 0.3 ATR · Plan window (by 11:30) | 956 | 406 | 42.5% | 46.3% | -0.14 | -0.06 | 0.73 | -56.85 | -57.46 | -0.19 | -0.09 |
| Entry fvg_ce, stop 0.3 ATR · Midday 11:30-14:30 | 1598 | 517 | 32.4% | 50.1% | -0.04 | -0.01 | 0.92 | -18.75 | -30.78 | -0.0 | -0.07 |
| Entry fvg_ce, stop 0.3 ATR · Stocks only | 1938 | 573 | 29.6% | 48.3% | -0.05 | -0.02 | 0.89 | -30.56 | -43.47 | -0.05 | -0.06 |
| Entry fvg_ce, stop 0.3 ATR · R:R to T2 2.5+ | 2564 | 921 | 35.9% | 47.3% | -0.08 | -0.03 | 0.85 | -73.66 | -93.89 | -0.08 | -0.08 |
| Entry fvg_ce, stop 0.3 ATR · Risk 0.15%+ | 2787 | 847 | 30.4% | 49.8% | -0.0 | -0.0 | 1.0 | -1.68 | -40.93 | 0.01 | -0.02 |
| Entry fvg_ce, stop 0.3 ATR · Midday + R:R 2.5+ + risk 0.15%+ | 1074 | 362 | 33.7% | 51.9% | 0.02 | 0.01 | 1.05 | 8.43 | -16.67 | 0.1 | -0.05 |
| Entry blend, stop 0.1 ATR · All qualified | 3407 | 1214 | 35.6% | 45.7% | -0.11 | -0.04 | 0.81 | -127.6 | -142.65 | -0.1 | -0.11 |
| Entry blend, stop 0.1 ATR · Plan window (by 11:30) | 956 | 419 | 43.8% | 44.9% | -0.16 | -0.07 | 0.71 | -67.12 | -67.68 | -0.21 | -0.11 |
| Entry blend, stop 0.1 ATR · Midday 11:30-14:30 | 1598 | 540 | 33.8% | 48.1% | -0.05 | -0.02 | 0.89 | -28.7 | -40.86 | -0.05 | -0.05 |
| Entry blend, stop 0.1 ATR · Stocks only | 1938 | 597 | 30.8% | 45.6% | -0.08 | -0.03 | 0.83 | -49.7 | -57.3 | -0.12 | -0.05 |
| Entry blend, stop 0.1 ATR · R:R to T2 2.5+ | 2564 | 957 | 37.3% | 45.2% | -0.11 | -0.04 | 0.8 | -108.14 | -130.48 | -0.11 | -0.12 |
| Entry blend, stop 0.1 ATR · Risk 0.15%+ | 2787 | 884 | 31.7% | 48.2% | -0.02 | -0.01 | 0.96 | -15.66 | -61.02 | 0.0 | -0.04 |
| Entry blend, stop 0.1 ATR · Midday + R:R 2.5+ + risk 0.15%+ | 1074 | 372 | 34.6% | 48.4% | -0.03 | -0.01 | 0.94 | -9.76 | -24.13 | -0.0 | -0.05 |
| Entry blend, stop 0.3 ATR · All qualified | 3407 | 1214 | 35.6% | 48.2% | -0.09 | -0.03 | 0.83 | -105.34 | -119.44 | -0.07 | -0.1 |
| Entry blend, stop 0.3 ATR · Plan window (by 11:30) | 956 | 419 | 43.8% | 47.3% | -0.15 | -0.06 | 0.71 | -61.65 | -62.13 | -0.2 | -0.09 |
| Entry blend, stop 0.3 ATR · Midday 11:30-14:30 | 1598 | 540 | 33.8% | 50.7% | -0.03 | -0.01 | 0.93 | -16.94 | -29.81 | -0.0 | -0.06 |
| Entry blend, stop 0.3 ATR · Stocks only | 1938 | 597 | 30.8% | 48.1% | -0.07 | -0.02 | 0.85 | -41.7 | -50.19 | -0.07 | -0.07 |
| Entry blend, stop 0.3 ATR · R:R to T2 2.5+ | 2564 | 957 | 37.3% | 48.3% | -0.09 | -0.03 | 0.83 | -81.69 | -101.96 | -0.07 | -0.11 |
| Entry blend, stop 0.3 ATR · Risk 0.15%+ | 2787 | 884 | 31.7% | 50.7% | -0.0 | -0.0 | 0.99 | -3.58 | -43.44 | 0.03 | -0.03 |
| Entry blend, stop 0.3 ATR · Midday + R:R 2.5+ + risk 0.15%+ | 1074 | 372 | 34.6% | 51.6% | 0.01 | 0.0 | 1.01 | 2.3 | -17.84 | 0.08 | -0.07 |
| Entry ote_62, stop 0.1 ATR · All qualified | 3407 | 1157 | 34.0% | 44.2% | -0.09 | -0.03 | 0.85 | -98.74 | -127.14 | -0.09 | -0.08 |
| Entry ote_62, stop 0.1 ATR · Plan window (by 11:30) | 956 | 393 | 41.1% | 41.5% | -0.16 | -0.07 | 0.73 | -62.15 | -63.07 | -0.21 | -0.11 |
| Entry ote_62, stop 0.1 ATR · Midday 11:30-14:30 | 1598 | 512 | 32.0% | 46.7% | -0.03 | -0.01 | 0.94 | -15.21 | -38.99 | -0.07 | 0.01 |
| Entry ote_62, stop 0.1 ATR · Stocks only | 1938 | 568 | 29.3% | 44.0% | -0.05 | -0.02 | 0.9 | -29.35 | -47.69 | -0.07 | -0.03 |
| Entry ote_62, stop 0.1 ATR · R:R to T2 2.5+ | 2564 | 921 | 35.9% | 43.8% | -0.1 | -0.03 | 0.84 | -88.01 | -121.32 | -0.11 | -0.08 |
| Entry ote_62, stop 0.1 ATR · Risk 0.15%+ | 2787 | 829 | 29.7% | 46.0% | -0.0 | -0.0 | 1.0 | -1.44 | -58.52 | 0.01 | -0.01 |
| Entry ote_62, stop 0.1 ATR · Midday + R:R 2.5+ + risk 0.15%+ | 1074 | 355 | 33.1% | 46.8% | 0.01 | 0.0 | 1.02 | 3.43 | -22.42 | 0.01 | 0.01 |
| Entry ote_62, stop 0.3 ATR · All qualified | 3407 | 1157 | 34.0% | 47.1% | -0.07 | -0.02 | 0.87 | -77.86 | -104.52 | -0.06 | -0.07 |
| Entry ote_62, stop 0.3 ATR · Plan window (by 11:30) | 956 | 393 | 41.1% | 44.8% | -0.14 | -0.06 | 0.74 | -55.65 | -56.29 | -0.2 | -0.08 |
| Entry ote_62, stop 0.3 ATR · Midday 11:30-14:30 | 1598 | 512 | 32.0% | 49.4% | -0.01 | -0.0 | 0.97 | -6.43 | -27.85 | -0.02 | -0.01 |
| Entry ote_62, stop 0.3 ATR · Stocks only | 1938 | 568 | 29.3% | 47.4% | -0.04 | -0.01 | 0.92 | -21.83 | -42.7 | -0.01 | -0.06 |
| Entry ote_62, stop 0.3 ATR · R:R to T2 2.5+ | 2564 | 921 | 35.9% | 47.2% | -0.07 | -0.02 | 0.87 | -61.99 | -93.55 | -0.07 | -0.07 |
| Entry ote_62, stop 0.3 ATR · Risk 0.15%+ | 2787 | 829 | 29.7% | 49.1% | 0.01 | 0.0 | 1.03 | 11.2 | -39.76 | 0.04 | -0.01 |
| Entry ote_62, stop 0.3 ATR · Midday + R:R 2.5+ + risk 0.15%+ | 1074 | 355 | 33.1% | 50.1% | 0.03 | 0.01 | 1.08 | 12.27 | -17.37 | 0.09 | -0.02 |
| Entry tl_line, stop 0.1 ATR · All qualified | 3407 | 4 | 0.1% | 75.0% | 0.52 | 0.0 | 2.93 | 2.07 | -1.07 | 0.43 | 0.6 |
| Entry tl_line, stop 0.1 ATR · Plan window (by 11:30) | 956 | 1 | 0.1% | 100.0% | 0.32 | 0.0 |  | 0.32 | 0.0 |  | 0.32 |
| Entry tl_line, stop 0.1 ATR · Midday 11:30-14:30 | 1598 | 3 | 0.2% | 66.7% | -0.07 | -0.0 | 0.8 | -0.21 | -1.07 | 0.32 | -0.27 |
| Entry tl_line, stop 0.1 ATR · Stocks only | 1938 | 3 | 0.2% | 66.7% | -0.07 | -0.0 | 0.8 | -0.21 | -1.07 | 0.32 | -0.27 |
| Entry tl_line, stop 0.1 ATR · R:R to T2 2.5+ | 2564 | 4 | 0.2% | 75.0% | 0.52 | 0.0 | 2.93 | 2.07 | -1.07 | 0.43 | 0.6 |
| Entry tl_line, stop 0.1 ATR · Risk 0.15%+ | 2787 | 4 | 0.1% | 75.0% | 0.52 | 0.0 | 2.93 | 2.07 | -1.07 | 0.43 | 0.6 |
| Entry tl_line, stop 0.1 ATR · Midday + R:R 2.5+ + risk 0.15%+ | 1074 | 3 | 0.3% | 66.7% | -0.07 | -0.0 | 0.8 | -0.21 | -1.07 | 0.32 | -0.27 |
| Entry tl_line, stop 0.3 ATR · All qualified | 3407 | 4 | 0.1% | 75.0% | 0.39 | 0.0 | 2.48 | 1.57 | -1.06 | 0.36 | 0.43 |
| Entry tl_line, stop 0.3 ATR · Plan window (by 11:30) | 956 | 1 | 0.1% | 100.0% | 0.29 | 0.0 |  | 0.29 | 0.0 |  | 0.29 |
| Entry tl_line, stop 0.3 ATR · Midday 11:30-14:30 | 1598 | 3 | 0.2% | 66.7% | -0.12 | -0.0 | 0.67 | -0.35 | -1.06 | 0.29 | -0.32 |
| Entry tl_line, stop 0.3 ATR · Stocks only | 1938 | 3 | 0.2% | 66.7% | -0.12 | -0.0 | 0.67 | -0.35 | -1.06 | 0.29 | -0.32 |
| Entry tl_line, stop 0.3 ATR · R:R to T2 2.5+ | 2564 | 4 | 0.2% | 75.0% | 0.39 | 0.0 | 2.48 | 1.57 | -1.06 | 0.36 | 0.43 |
| Entry tl_line, stop 0.3 ATR · Risk 0.15%+ | 2787 | 4 | 0.1% | 75.0% | 0.39 | 0.0 | 2.48 | 1.57 | -1.06 | 0.36 | 0.43 |
| Entry tl_line, stop 0.3 ATR · Midday + R:R 2.5+ + risk 0.15%+ | 1074 | 3 | 0.3% | 66.7% | -0.12 | -0.0 | 0.67 | -0.35 | -1.06 | 0.29 | -0.32 |
| Scaled ladder_equal (fvg_edge 33%, blend 33%, ote_mid 33%) · All qualified | 3407 | 1412 | 41.4% | 51.4% | -0.08 | -0.03 | 0.82 | -118.35 | -133.86 | -0.08 | -0.09 |
| Scaled ladder_equal (fvg_edge 33%, blend 33%, ote_mid 33%) · Plan window (by 11:30) | 956 | 474 | 49.6% | 50.4% | -0.14 | -0.07 | 0.71 | -64.14 | -64.64 | -0.15 | -0.12 |
| Scaled ladder_equal (fvg_edge 33%, blend 33%, ote_mid 33%) · Midday 11:30-14:30 | 1598 | 630 | 39.4% | 53.8% | -0.05 | -0.02 | 0.89 | -29.44 | -41.3 | -0.05 | -0.04 |
| Scaled ladder_equal (fvg_edge 33%, blend 33%, ote_mid 33%) · Stocks only | 1938 | 698 | 36.0% | 51.6% | -0.06 | -0.02 | 0.85 | -45.06 | -54.53 | -0.1 | -0.03 |
| Scaled ladder_equal (fvg_edge 33%, blend 33%, ote_mid 33%) · R:R to T2 2.5+ | 2564 | 1101 | 42.9% | 51.0% | -0.09 | -0.04 | 0.8 | -102.21 | -124.48 | -0.09 | -0.09 |
| Scaled ladder_equal (fvg_edge 33%, blend 33%, ote_mid 33%) · Risk 0.15%+ | 2787 | 1035 | 37.1% | 54.1% | -0.01 | -0.0 | 0.97 | -13.37 | -60.12 | -0.0 | -0.02 |
| Scaled ladder_equal (fvg_edge 33%, blend 33%, ote_mid 33%) · Midday + R:R 2.5+ + risk 0.15%+ | 1074 | 430 | 40.0% | 54.2% | -0.02 | -0.01 | 0.96 | -7.25 | -21.93 | -0.0 | -0.03 |
| Scaled ladder_deep (fvg_edge 20%, blend 30%, ote_mid 50%) · All qualified | 3407 | 1412 | 41.4% | 51.8% | -0.08 | -0.03 | 0.82 | -117.04 | -135.03 | -0.07 | -0.09 |
| Scaled ladder_deep (fvg_edge 20%, blend 30%, ote_mid 50%) · Plan window (by 11:30) | 956 | 474 | 49.6% | 50.8% | -0.14 | -0.07 | 0.71 | -64.06 | -64.52 | -0.15 | -0.12 |
| Scaled ladder_deep (fvg_edge 20%, blend 30%, ote_mid 50%) · Midday 11:30-14:30 | 1598 | 630 | 39.4% | 54.3% | -0.04 | -0.02 | 0.91 | -25.48 | -38.98 | -0.05 | -0.03 |
| Scaled ladder_deep (fvg_edge 20%, blend 30%, ote_mid 50%) · Stocks only | 1938 | 698 | 36.0% | 52.3% | -0.06 | -0.02 | 0.87 | -38.44 | -50.6 | -0.09 | -0.02 |
| Scaled ladder_deep (fvg_edge 20%, blend 30%, ote_mid 50%) · R:R to T2 2.5+ | 2564 | 1101 | 42.9% | 51.1% | -0.09 | -0.04 | 0.81 | -99.85 | -125.72 | -0.09 | -0.1 |
| Scaled ladder_deep (fvg_edge 20%, blend 30%, ote_mid 50%) · Risk 0.15%+ | 2787 | 1035 | 37.1% | 54.6% | -0.01 | -0.0 | 0.98 | -7.31 | -57.72 | 0.0 | -0.02 |
| Scaled ladder_deep (fvg_edge 20%, blend 30%, ote_mid 50%) · Midday + R:R 2.5+ + risk 0.15%+ | 1074 | 430 | 40.0% | 54.7% | -0.0 | -0.0 | 0.99 | -1.19 | -21.89 | 0.0 | -0.01 |

## 8. Trade management (systematic, qualified, triggered)

| Method | Trades | Avg R | Win rate |
|---|---|---|---|
| Plan: half at T1, rest to T2 (gross) | 1062 | 0.1 | 43.0% |
| Plan, net of costs | 1062 | -0.1 | 41.4% |
| Full position to T1 (gross) | 1062 | 0.11 | 43.3% |
| Full position to T2 (gross) | 1062 | 0.1 | 37.6% |

## 10. v3 candidate tests (New York session, qualified, net of costs)

Confirmation entry = wait for price to reach the FVG, then enter on the first bar that closes beyond the prior 3 bars (bars used: {'1m': 2877, '5m': 147}). Runner = half at T1, rest to the close with a breakeven stop. 1st/2nd half columns are the out-of-sample check.

| Group | Setups | Triggered | Trigger rate | Win rate | Avg R | Expectancy R | Profit factor | Total R | Max DD R | 1st half avg R | 2nd half avg R |
|---|---|---|---|---|---|---|---|---|---|---|---|
| All (New York) · Current plan | 3027 | 879 | 29.0% | 42.8% | -0.07 | -0.02 | 0.88 | -64.67 | -91.11 | -0.08 | -0.06 |
| All (New York) · Runner to the close | 3027 | 879 | 29.0% | 42.8% | -0.07 | -0.02 | 0.89 | -60.87 | -88.78 | -0.06 | -0.08 |
| All (New York) · Full position to T2 | 3027 | 879 | 29.0% | 38.0% | -0.07 | -0.02 | 0.9 | -60.37 | -104.65 | -0.09 | -0.05 |
| All (New York) · Confirmation entry | 3027 | 977 | 32.3% | 52.2% | -0.1 | -0.03 | 0.75 | -93.38 | -95.6 | -0.11 | -0.08 |
| v3: 11:30-14:30 + risk 0.3%+ + FVG 0.5+ ATR · Current plan | 788 | 153 | 19.4% | 48.4% | 0.09 | 0.02 | 1.19 | 13.55 | -13.05 | 0.11 | 0.07 |
| v3: 11:30-14:30 + risk 0.3%+ + FVG 0.5+ ATR · Runner to the close | 788 | 153 | 19.4% | 48.4% | 0.08 | 0.01 | 1.16 | 11.51 | -13.05 | 0.11 | 0.04 |
| v3: 11:30-14:30 + risk 0.3%+ + FVG 0.5+ ATR · Full position to T2 | 788 | 153 | 19.4% | 45.8% | 0.11 | 0.02 | 1.2 | 16.37 | -15.55 | 0.11 | 0.1 |
| v3: 11:30-14:30 + risk 0.3%+ + FVG 0.5+ ATR · Confirmation entry | 788 | 211 | 26.8% | 56.9% | 0.02 | 0.01 | 1.08 | 5.1 | -8.1 | 0.07 | -0.03 |
| v3 + longs · Current plan | 643 | 117 | 18.2% | 53.0% | 0.21 | 0.04 | 1.44 | 24.0 | -8.18 | 0.2 | 0.21 |
| v3 + longs · Runner to the close | 643 | 117 | 18.2% | 53.0% | 0.19 | 0.03 | 1.41 | 21.96 | -8.13 | 0.2 | 0.17 |
| v3 + longs · Full position to T2 | 643 | 117 | 18.2% | 48.7% | 0.2 | 0.04 | 1.4 | 23.15 | -9.54 | 0.17 | 0.22 |
| v3 + longs · Confirmation entry | 643 | 172 | 26.7% | 58.1% | 0.05 | 0.01 | 1.19 | 9.44 | -6.21 | 0.12 | -0.01 |
| v3 + VWAP side · Current plan | 596 | 89 | 14.9% | 51.7% | 0.08 | 0.01 | 1.18 | 7.12 | -6.87 | 0.06 | 0.1 |
| v3 + VWAP side · Runner to the close | 596 | 89 | 14.9% | 51.7% | 0.06 | 0.01 | 1.13 | 5.08 | -6.87 | 0.06 | 0.05 |
| v3 + VWAP side · Full position to T2 | 596 | 89 | 14.9% | 49.4% | 0.09 | 0.01 | 1.17 | 7.7 | -8.65 | 0.02 | 0.15 |
| v3 + VWAP side · Confirmation entry | 596 | 133 | 22.3% | 53.4% | 0.02 | 0.0 | 1.07 | 2.51 | -6.91 | 0.06 | -0.02 |
| v3 + in play (open volume 1.5x+) · Current plan | 113 | 22 | 19.5% | 45.5% | 0.08 | 0.02 | 1.21 | 1.79 | -3.73 | -0.14 | 0.3 |
| v3 + in play (open volume 1.5x+) · Runner to the close | 113 | 22 | 19.5% | 45.5% | 0.08 | 0.02 | 1.21 | 1.79 | -3.73 | -0.14 | 0.3 |
| v3 + in play (open volume 1.5x+) · Full position to T2 | 113 | 22 | 19.5% | 45.5% | -0.08 | -0.02 | 0.83 | -1.79 | -4.62 | -0.18 | 0.02 |
| v3 + in play (open volume 1.5x+) · Confirmation entry | 113 | 30 | 26.5% | 60.0% | 0.06 | 0.01 | 1.18 | 1.66 | -2.61 | 0.02 | 0.09 |
| v3 + longs + VWAP side · Current plan | 507 | 73 | 14.4% | 53.4% | 0.16 | 0.02 | 1.36 | 11.69 | -5.26 | 0.12 | 0.2 |
| v3 + longs + VWAP side · Runner to the close | 507 | 73 | 14.4% | 53.4% | 0.13 | 0.02 | 1.3 | 9.65 | -5.26 | 0.12 | 0.14 |
| v3 + longs + VWAP side · Full position to T2 | 507 | 73 | 14.4% | 52.1% | 0.2 | 0.03 | 1.44 | 14.84 | -5.56 | 0.14 | 0.26 |
| v3 + longs + VWAP side · Confirmation entry | 507 | 114 | 22.5% | 53.5% | 0.03 | 0.01 | 1.09 | 2.9 | -7.31 | 0.09 | -0.04 |
| VWAP side only · Current plan | 2070 | 536 | 25.9% | 42.2% | -0.13 | -0.03 | 0.79 | -67.7 | -77.81 | -0.15 | -0.1 |
| VWAP side only · Runner to the close | 2070 | 536 | 25.9% | 42.2% | -0.13 | -0.03 | 0.79 | -67.29 | -74.19 | -0.12 | -0.13 |
| VWAP side only · Full position to T2 | 2070 | 536 | 25.9% | 38.4% | -0.12 | -0.03 | 0.81 | -65.49 | -85.9 | -0.15 | -0.09 |
| VWAP side only · Confirmation entry | 2070 | 625 | 30.2% | 51.4% | -0.11 | -0.03 | 0.72 | -67.55 | -73.94 | -0.11 | -0.1 |
| In play only · Current plan | 377 | 101 | 26.8% | 36.6% | -0.26 | -0.07 | 0.6 | -26.36 | -32.79 | -0.5 | -0.03 |
| In play only · Runner to the close | 377 | 101 | 26.8% | 36.6% | -0.27 | -0.07 | 0.58 | -27.38 | -33.9 | -0.5 | -0.05 |
| In play only · Full position to T2 | 377 | 101 | 26.8% | 31.7% | -0.38 | -0.1 | 0.48 | -38.48 | -41.15 | -0.58 | -0.19 |
| In play only · Confirmation entry | 377 | 119 | 31.6% | 52.9% | -0.11 | -0.04 | 0.71 | -13.63 | -23.63 | -0.25 | 0.02 |

## 11. Trendline retest confluence (New York session, qualified, net of costs)

Trendline = the falling line across the lower highs into the sweep (rising line across higher lows for shorts), broken by a close and not failed. Confluence = its level at the snapshot sits in the entry zone (FVG near edge to entry) within 0.25 ATR. Retest at fill = the line was within 0.3 ATR of the fill price when the order filled. Only rows recorded since Nov 4, 2026 (rerun the backtest to fill history).

| Group | Setups | Triggered | Trigger rate | Win rate | Avg R | Expectancy R | Profit factor | Total R | Max DD R | 1st half avg R | 2nd half avg R |
|---|---|---|---|---|---|---|---|---|---|---|---|
| All (New York, trendline recorded) · current plan | 114 | 32 | 28.1% | 40.6% | -0.3 | -0.08 | 0.53 | -9.54 | -11.39 | -0.38 | -0.21 |
| No trendline found/broken · current plan | 66 | 18 | 27.3% | 33.3% | -0.55 | -0.15 | 0.27 | -9.99 | -9.99 | -0.43 | -0.68 |
| Trendline found and broken · current plan | 48 | 14 | 29.2% | 50.0% | 0.03 | 0.01 | 1.07 | 0.45 | -2.91 | -0.32 | 0.38 |
| Trendline confluence at snapshot · current plan | 6 | 3 | 50.0% | 66.7% | 0.11 | 0.06 | 1.31 | 0.33 | -1.07 | 0.84 | -0.25 |
| No confluence at snapshot · current plan | 108 | 29 | 26.9% | 37.9% | -0.34 | -0.09 | 0.48 | -9.87 | -11.73 | -0.54 | -0.16 |
| Confluence, 3+ touches · current plan | 2 | 0 | 0.0% |  |  | 0.0 |  | 0.0 | 0.0 |  |  |
| Confluence + longs · current plan | 4 | 3 | 75.0% | 66.7% | 0.11 | 0.08 | 1.31 | 0.33 | -1.07 | 0.84 | -0.25 |
| Confluence + midday (11:30-14:30) · current plan | 6 | 3 | 50.0% | 66.7% | 0.11 | 0.06 | 1.31 | 0.33 | -1.07 | 0.84 | -0.25 |
| Confluence + risk 0.3%+ · current plan | 5 | 2 | 40.0% | 50.0% | -0.12 | -0.05 | 0.78 | -0.24 | -1.07 | 0.84 | -1.07 |
| Confluence + VWAP side · current plan | 2 | 1 | 50.0% | 100.0% | 0.84 | 0.42 |  | 0.84 | 0.0 |  | 0.84 |
| Confluence + longs + midday + risk 0.3%+ · current plan | 3 | 2 | 66.7% | 50.0% | -0.12 | -0.08 | 0.78 | -0.24 | -1.07 | 0.84 | -1.07 |
| Fill was a trendline retest (any setup) | 114 | 2 | 1.8% | 50.0% | -0.25 | -0.0 | 0.53 | -0.5 | -1.07 | 0.57 | -1.07 |
| Fill was a trendline retest + longs | 96 | 2 | 2.1% | 50.0% | -0.25 | -0.01 | 0.53 | -0.5 | -1.07 | 0.57 | -1.07 |
| Entry at the trendline (stop 0.1 ATR) | 6 | 3 | 50.0% | 66.7% | -0.07 | -0.04 | 0.8 | -0.21 | -1.07 | 0.32 | -0.27 |
| Entry at the trendline (stop 0.3 ATR) | 6 | 3 | 50.0% | 66.7% | -0.12 | -0.06 | 0.67 | -0.35 | -1.06 | 0.29 | -0.32 |

## 9. Automatic changes in this run

| Key | Old | New | Evidence |
|---|---|---|---|
| None |  |  |  |
