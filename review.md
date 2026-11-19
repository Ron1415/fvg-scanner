# FVG review: 2026-11-19 16:48 ET (Daily)

Sessions: 137 (2026-05-07 to 2026-11-19). Config version 2.

## 1. Strategy performance (qualified setups; results net of costs)

Costs: 0.02% of price per side. Entries allowed until 15:30 ET.

| Group | Setups | Triggered | Trigger rate | Win rate | Avg R | Expectancy R | Profit factor | Total R | Max DD R | 1st half avg R | 2nd half avg R |
|---|---|---|---|---|---|---|---|---|---|---|---|
| Live dashboard snapshots | 197 | 63 | 32.0% | 44.4% | -0.14 | -0.04 | 0.74 | -8.62 | -13.26 | -0.16 | -0.11 |
| Daily full-session replays | 349 | 129 | 37.0% | 41.1% | -0.23 | -0.08 | 0.64 | -29.58 | -35.41 | -0.17 | -0.29 |
| Backtest | 3224 | 1010 | 31.3% | 41.1% | -0.1 | -0.03 | 0.84 | -104.96 | -135.21 | -0.08 | -0.13 |
| Systematic (replays + backtest) | 3573 | 1139 | 31.9% | 41.1% | -0.12 | -0.04 | 0.81 | -134.54 | -158.84 | -0.13 | -0.1 |
| Systematic, before cost (gross) | 3573 | 1139 | 31.9% | 42.7% | 0.09 | 0.03 | 1.17 | 97.94 | -37.49 | 0.05 | 0.12 |
| Systematic, plan window only (New York, formed by 11:30) | 1012 | 396 | 39.1% | 38.9% | -0.17 | -0.07 | 0.73 | -69.24 | -74.47 | -0.27 | -0.08 |
| Live top-5 suggestions only | 132 | 43 | 32.6% | 44.2% | -0.23 | -0.08 | 0.57 | -10.08 | -11.76 | -0.23 | -0.24 |
| Your actual trades | 1 | 1 |  | 0.0% | -1.77 |  |  | -1.77 |  |  |  |
| Stocks and ETFs, New York session only | 2998 | 883 | 29.5% | 42.1% | -0.09 | -0.03 | 0.85 | -79.52 | -103.83 | -0.08 | -0.1 |
| Futures, New York session | 159 | 54 | 34.0% | 46.3% | -0.04 | -0.01 | 0.93 | -2.24 | -13.14 | 0.16 | -0.24 |
| Futures, all 24-hour sessions | 575 | 256 | 44.5% | 37.5% | -0.21 | -0.1 | 0.71 | -55.02 | -58.38 | -0.18 | -0.25 |

## 1c. Futures by session (24-hour test; qualified, net of costs)

Asia and London use their own levels: prior-day high/low, the previous session's high/low, and the session's first 30 minutes.

| Group | Setups | Triggered | Trigger rate | Win rate | Avg R | Expectancy R | Profit factor | Total R | Max DD R | 1st half avg R | 2nd half avg R |
|---|---|---|---|---|---|---|---|---|---|---|---|
| Futures, Asia session (6 PM-midnight ET) | 185 | 81 | 43.8% | 30.9% | -0.26 | -0.12 | 0.65 | -21.39 | -23.71 | -0.28 | -0.25 |
| Futures, London session (2-8 AM ET) | 231 | 121 | 52.4% | 38.0% | -0.26 | -0.14 | 0.66 | -31.38 | -38.05 | -0.39 | -0.13 |
| Futures, NY session (9:30-4:00 ET) | 159 | 54 | 34.0% | 46.3% | -0.04 | -0.01 | 0.93 | -2.24 | -13.14 | 0.16 | -0.24 |
| CL=F Asia | 22 | 12 | 54.5% | 50.0% | 0.37 | 0.2 | 1.65 | 4.41 | -2.35 | -0.27 | 1.01 |
| CL=F London | 26 | 10 | 38.5% | 40.0% | 0.09 | 0.03 | 1.15 | 0.87 | -2.21 | -0.14 | 0.31 |
| CL=F NY | 21 | 7 | 33.3% | 28.6% | -0.38 | -0.13 | 0.5 | -2.66 | -3.18 | -1.06 | 0.13 |
| ES=F Asia | 16 | 6 | 37.5% | 33.3% | -0.45 | -0.17 | 0.43 | -2.72 | -4.64 | 0.28 | -1.18 |
| ES=F London | 29 | 17 | 58.6% | 41.2% | 0.11 | 0.07 | 1.16 | 1.91 | -5.2 | -0.57 | 0.72 |
| ES=F NY | 19 | 8 | 42.1% | 75.0% | 0.85 | 0.36 | 5.84 | 6.83 | -1.41 | 1.23 | 0.48 |
| GC=F Asia | 39 | 25 | 64.1% | 24.0% | -0.1 | -0.07 | 0.85 | -2.58 | -10.46 | 0.07 | -0.27 |
| GC=F London | 16 | 6 | 37.5% | 66.7% | 0.35 | 0.13 | 2.0 | 2.09 | -1.05 | 0.05 | 0.64 |
| GC=F NY | 18 | 7 | 38.9% | 42.9% | -0.07 | -0.03 | 0.87 | -0.52 | -2.67 | 0.72 | -0.67 |
| NQ=F Asia | 16 | 8 | 50.0% | 37.5% | -0.08 | -0.04 | 0.88 | -0.61 | -5.19 | -1.03 | 0.88 |
| NQ=F London | 23 | 9 | 39.1% | 11.1% | -0.63 | -0.25 | 0.13 | -5.71 | -6.56 | -1.03 | -0.32 |
| NQ=F NY | 14 | 4 | 28.6% | 25.0% | -0.32 | -0.09 | 0.38 | -1.29 | -2.08 | -1.01 | 0.37 |
| RTY=F Asia | 19 | 5 | 26.3% | 60.0% | 0.4 | 0.11 | 1.9 | 2.01 | -2.23 | 1.12 | -0.08 |
| RTY=F London | 34 | 23 | 67.6% | 34.8% | -0.24 | -0.16 | 0.64 | -5.57 | -10.2 | -0.54 | 0.03 |
| RTY=F NY | 15 | 2 | 13.3% | 50.0% | -0.1 | -0.01 | 0.82 | -0.19 | -1.04 | -1.04 | 0.85 |
| YM=F Asia | 21 | 6 | 28.6% | 16.7% | -0.8 | -0.23 | 0.15 | -4.81 | -5.67 | -0.51 | -1.09 |
| YM=F London | 32 | 16 | 50.0% | 56.2% | 0.31 | 0.16 | 1.64 | 4.97 | -2.29 | 0.14 | 0.48 |
| YM=F NY | 16 | 3 | 18.8% | 33.3% | 0.43 | 0.08 | 1.63 | 1.3 | -2.05 | 3.35 | -1.03 |
| ZB=F Asia | 18 | 7 | 38.9% | 28.6% | -1.07 | -0.42 | 0.05 | -7.49 | -7.73 | -0.65 | -1.38 |
| ZB=F London | 14 | 9 | 64.3% | 44.4% | -0.37 | -0.24 | 0.54 | -3.3 | -3.38 | -0.7 | -0.1 |
| ZB=F NY | 19 | 9 | 47.4% | 66.7% | 0.49 | 0.23 | 1.95 | 4.37 | -1.65 | 0.8 | 0.23 |
| ZC=F Asia | 1 | 1 | 100.0% | 0.0% | -1.71 | -1.71 | 0.0 | -1.71 | -1.71 |  | -1.71 |
| ZC=F London | 0 | 0 |  |  |  |  |  | 0.0 | 0.0 |  |  |
| ZC=F NY | 1 | 0 | 0.0% |  |  | 0.0 |  | 0.0 | 0.0 |  |  |
| ZF=F Asia | 17 | 6 | 35.3% | 16.7% | -0.85 | -0.3 | 0.13 | -5.09 | -5.09 | -1.24 | -0.46 |
| ZF=F London | 22 | 14 | 63.6% | 28.6% | -1.07 | -0.68 | 0.2 | -14.95 | -14.95 | -1.34 | -0.79 |
| ZF=F NY | 15 | 6 | 40.0% | 50.0% | -0.72 | -0.29 | 0.14 | -4.31 | -4.64 | -0.53 | -0.9 |
| ZN=F Asia | 11 | 4 | 36.4% | 25.0% | -0.49 | -0.18 | 0.37 | -1.95 | -2.63 | -1.31 | 0.34 |
| ZN=F London | 14 | 8 | 57.1% | 25.0% | -0.68 | -0.39 | 0.33 | -5.44 | -5.44 | -0.54 | -0.82 |
| ZN=F NY | 10 | 6 | 60.0% | 33.3% | -0.52 | -0.31 | 0.37 | -3.11 | -3.11 | -0.01 | -1.03 |
| ZS=F Asia | 5 | 1 | 20.0% | 0.0% | -0.85 | -0.17 | 0.0 | -0.85 | -0.85 |  | -0.85 |
| ZS=F London | 21 | 9 | 42.9% | 33.3% | -0.69 | -0.3 | 0.32 | -6.25 | -7.26 | -0.95 | -0.49 |
| ZS=F NY | 11 | 2 | 18.2% | 0.0% | -1.33 | -0.24 | 0.0 | -2.66 | -2.66 | -1.32 | -1.34 |

## 2. New York session: by asset, side, time of day, risk size (systematic, qualified)

| Group | Setups | Triggered | Trigger rate | Win rate | Avg R | Expectancy R | Profit factor | Total R | Max DD R | 1st half avg R | 2nd half avg R |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ETF | 974 | 334 | 34.3% | 40.7% | -0.19 | -0.06 | 0.73 | -62.53 | -74.96 | -0.11 | -0.26 |
| Stock | 2024 | 549 | 27.1% | 43.0% | -0.03 | -0.01 | 0.94 | -16.99 | -41.36 | -0.07 | 0.01 |
| Future | 159 | 54 | 34.0% | 46.3% | -0.04 | -0.01 | 0.93 | -2.24 | -13.14 | 0.16 | -0.24 |
| Leveraged/inverse ETFs | 141 | 44 | 31.2% | 50.0% | 0.33 | 0.1 | 1.76 | 14.65 | -6.42 | 0.77 | -0.11 |
| LONG | 2783 | 851 | 30.6% | 42.4% | -0.09 | -0.03 | 0.86 | -77.33 | -100.87 | -0.09 | -0.09 |
| SHORT | 374 | 86 | 23.0% | 41.9% | -0.05 | -0.01 | 0.88 | -4.44 | -9.63 | -0.12 | 0.02 |
| Formed 10:00-10:30 | 328 | 155 | 47.3% | 31.6% | -0.29 | -0.14 | 0.61 | -44.91 | -46.38 | -0.29 | -0.29 |
| Formed 10:30-11:30 | 634 | 225 | 35.5% | 43.1% | -0.11 | -0.04 | 0.81 | -24.3 | -33.43 | -0.25 | 0.03 |
| Formed 11:30-13:00 | 891 | 289 | 32.4% | 47.1% | -0.05 | -0.02 | 0.91 | -14.34 | -31.26 | 0.04 | -0.14 |
| Formed 13:00-14:30 | 769 | 203 | 26.4% | 41.4% | -0.05 | -0.01 | 0.92 | -9.9 | -34.2 | -0.21 | 0.11 |
| Formed 14:30-16:00 | 535 | 65 | 12.1% | 47.7% | 0.18 | 0.02 | 1.32 | 11.69 | -16.45 | 0.69 | -0.32 |
| Risk 0-0.15% of price | 665 | 323 | 48.6% | 34.1% | -0.41 | -0.2 | 0.53 | -133.62 | -136.18 | -0.39 | -0.44 |
| Risk 0.15-0.3% of price | 693 | 258 | 37.2% | 41.5% | -0.1 | -0.04 | 0.84 | -26.85 | -45.15 | -0.17 | -0.04 |
| Risk 0.3-0.6% of price | 1107 | 309 | 27.9% | 45.0% | 0.05 | 0.01 | 1.1 | 16.4 | -20.24 | 0.09 | 0.02 |
| Risk 0.6%+ | 1108 | 249 | 22.5% | 45.0% | 0.04 | 0.01 | 1.08 | 9.53 | -16.61 | 0.1 | -0.02 |

## 2b. Short guardrails (systematic; shorts use full exit at T1, breakeven at +0.5R, 60-minute time stop)

Sizing: longs 1.25% risk (cap 5.0% of account), shorts 0.5% risk (cap 2.5%). Results here are in R, before sizing.

| Group | Setups | Triggered | Trigger rate | Win rate | Avg R | Expectancy R | Profit factor | Total R | Max DD R | 1st half avg R | 2nd half avg R |
|---|---|---|---|---|---|---|---|---|---|---|---|
| Longs passing the normal filters | 3195 | 1052 | 32.9% | 41.0% | -0.13 | -0.04 | 0.81 | -131.7 | -155.24 | -0.14 | -0.11 |
| Shorts passing the normal filters (before guardrails) | 2293 | 815 | 35.5% | 27.9% | -0.18 | -0.06 | 0.64 | -146.91 | -152.98 | -0.09 | -0.27 |
| Shorts passing every guardrail (traded) | 378 | 87 | 23.0% | 42.5% | -0.03 | -0.01 | 0.92 | -2.84 | -9.63 | -0.12 | 0.06 |
| Shorts passing: bearish daily trend | 1005 | 363 | 36.1% | 30.0% | -0.2 | -0.07 | 0.62 | -71.02 | -82.87 | -0.14 | -0.25 |
| Shorts failing: bearish daily trend | 1288 | 452 | 35.1% | 26.1% | -0.17 | -0.06 | 0.66 | -75.89 | -75.89 | -0.09 | -0.24 |
| Shorts passing: PDH or 2+ level sweep | 1633 | 546 | 33.4% | 29.7% | -0.11 | -0.04 | 0.75 | -62.49 | -66.93 | -0.04 | -0.19 |
| Shorts failing: PDH or 2+ level sweep | 660 | 269 | 40.8% | 24.2% | -0.31 | -0.13 | 0.49 | -84.43 | -87.54 | -0.28 | -0.35 |
| Shorts passing: R:R to T2 3.0+ | 1682 | 599 | 35.6% | 28.4% | -0.19 | -0.07 | 0.65 | -111.05 | -118.38 | -0.06 | -0.31 |
| Shorts failing: R:R to T2 3.0+ | 611 | 216 | 35.4% | 26.4% | -0.17 | -0.06 | 0.64 | -35.86 | -38.04 | -0.16 | -0.17 |
| Shorts passing: risk 0.3%+ of price | 1231 | 356 | 28.9% | 32.9% | -0.02 | -0.01 | 0.95 | -6.51 | -25.88 | 0.05 | -0.08 |
| Shorts failing: risk 0.3%+ of price | 1062 | 459 | 43.2% | 24.0% | -0.31 | -0.13 | 0.5 | -140.41 | -142.88 | -0.28 | -0.33 |
| Shorts passing: formed 10:30 or later | 2045 | 685 | 33.5% | 27.0% | -0.2 | -0.07 | 0.61 | -138.77 | -141.11 | -0.13 | -0.28 |
| Shorts failing: formed 10:30 or later | 248 | 130 | 52.4% | 32.3% | -0.06 | -0.03 | 0.85 | -8.15 | -20.84 | 0.08 | -0.2 |
| Shorts passing: not a leveraged ETF | 2204 | 789 | 35.8% | 27.5% | -0.2 | -0.07 | 0.62 | -155.55 | -160.19 | -0.13 | -0.27 |
| Shorts failing: not a leveraged ETF | 89 | 26 | 29.2% | 38.5% | 0.33 | 0.1 | 2.07 | 8.63 | -2.49 | 0.81 | -0.14 |

## 3. Outcomes (systematic, qualified)

| Outcome | Count | Share | Avg R |
|---|---|---|---|
| Not triggered (ran to T1 first) | 2230 | 62.4% | 0.0 |
| Stop | 546 | 15.3% | -1.22 |
| EOD exit | 236 | 6.6% | 0.19 |
| Not triggered (cutoff) | 202 | 5.7% | 0.0 |
| T1 then EOD | 150 | 4.2% | 1.79 |
| T1 then breakeven | 82 | 2.3% | 0.58 |
| T1 then T2 | 80 | 2.2% | 1.99 |
| Time stop | 28 | 0.8% | 0.51 |
| Breakeven stop | 17 | 0.5% | -0.1 |
| Invalidated before entry | 1 | 0.0% | 0.0 |
| Not triggered | 1 | 0.0% | 0.0 |

## 4. Score calibration. A useful score shows results improving band by band.

| Group | Setups | Triggered | Trigger rate | Win rate | Avg R | Expectancy R | Profit factor | Total R | Max DD R | 1st half avg R | 2nd half avg R |
|---|---|---|---|---|---|---|---|---|---|---|---|
| Score 90+ | 20 | 12 | 60.0% | 75.0% | 0.92 | 0.55 | 6.01 | 11.09 | -2.22 | 1.18 | 0.67 |
| Score 75-89 | 1276 | 377 | 29.5% | 40.3% | -0.13 | -0.04 | 0.79 | -48.54 | -74.93 | -0.13 | -0.13 |
| Score 60-74 | 1979 | 623 | 31.5% | 42.1% | -0.09 | -0.03 | 0.86 | -53.65 | -62.2 | -0.03 | -0.14 |
| Score under 60 | 298 | 127 | 42.6% | 35.4% | -0.34 | -0.15 | 0.55 | -43.44 | -45.33 | -0.28 | -0.41 |

## 5. Factor attribution (all triggered systematic setups, qualified or not)

| Factor | Weight key | Weight | With | Avg R with | Without | Avg R without | Difference | Read |
|---|---|---|---|---|---|---|---|---|
| Prior-day level swept | sweep_pd | 20 | 2809 | -0.11 | 3222 | -0.16 | 0.05 | No clear effect |
| Only PM/OR level swept | sweep_other | 15 | 2551 | -0.15 | 3480 | -0.13 | -0.01 | No clear effect |
| FVG in discount/premium | zone | 10 | 2198 | -0.17 | 3833 | -0.12 | -0.05 | No clear effect |
| FVG overlaps OTE | ote | 15 | 1942 | -0.16 | 4089 | -0.13 | -0.02 | No clear effect |
| R:R to T1 of 2 or more | rr | 10 | 468 | -0.29 | 5563 | -0.13 | -0.16 | Hurts |
| HTF bias aligned | bias | 10 | 2323 | -0.14 | 3708 | -0.14 | -0.0 | No clear effect |
| Displacement volume 1.5x+ | vol | 5 | 743 | -0.1 | 5288 | -0.14 | 0.04 | No clear effect |
| Formed 10:00-11:30 | time | 5 | 2834 | -0.18 | 3197 | -0.1 | -0.08 | No clear effect |
| Trendline retest confluence | tl | 12 | 49 | 0.08 | 497 | -0.21 | 0.3 | Helps |

## 6. Filter check (systematic)

| Group | Setups | Triggered | Trigger rate | Win rate | Avg R | Expectancy R | Profit factor | Total R | Max DD R | 1st half avg R | 2nd half avg R |
|---|---|---|---|---|---|---|---|---|---|---|---|
| Passed filters | 3573 | 1139 | 31.9% | 41.1% | -0.12 | -0.04 | 0.81 | -134.54 | -158.84 | -0.13 | -0.1 |
| Filtered out | 8168 | 4892 | 59.9% | 47.8% | -0.14 | -0.09 | 0.62 | -705.91 | -707.37 | -0.12 | -0.17 |
| No OTE overlap | 6088 | 4089 | 67.2% | 52.0% | -0.13 | -0.09 | 0.62 | -537.44 | -537.85 | -0.12 | -0.14 |
| OTE overlap, R:R to T2 1.5-2 | 151 | 69 | 45.7% | 30.4% | -0.3 | -0.14 | 0.5 | -20.42 | -20.51 | -0.13 | -0.46 |
| OTE overlap, R:R to T2 2-2.5 | 1238 | 363 | 29.3% | 35.5% | -0.16 | -0.05 | 0.72 | -56.52 | -59.56 | -0.14 | -0.18 |
| OTE overlap, R:R to T2 2.5-3 | 647 | 212 | 32.8% | 37.7% | -0.04 | -0.01 | 0.93 | -8.34 | -43.27 | -0.3 | 0.22 |
| OTE overlap, R:R to T2 3+ | 3617 | 1298 | 35.9% | 34.7% | -0.17 | -0.06 | 0.72 | -217.72 | -249.53 | -0.08 | -0.25 |

## 7. Improvement tests: entry type x stop buffer x filter (net of costs)

ote_mid = current entry (middle of the FVG/OTE overlap); fvg_edge = first touch of the gap; fvg_ce = gap midpoint; blend = halfway between the gap edge and ote_mid; ote_62 = first touch of the OTE zone; tl_line = limit at the broken trendline (only setups with trendline confluence). Scaled rows are in R of the full planned position (a partial fill counts only what filled).

| Group | Setups | Triggered | Trigger rate | Win rate | Avg R | Expectancy R | Profit factor | Total R | Max DD R | 1st half avg R | 2nd half avg R |
|---|---|---|---|---|---|---|---|---|---|---|---|
| Entry ote_mid, stop 0.1 ATR · All qualified | 3573 | 1139 | 31.9% | 41.1% | -0.12 | -0.04 | 0.81 | -134.53 | -158.83 | -0.13 | -0.1 |
| Entry ote_mid, stop 0.1 ATR · Plan window (by 11:30) | 1012 | 396 | 39.1% | 38.9% | -0.17 | -0.07 | 0.73 | -69.23 | -74.47 | -0.27 | -0.08 |
| Entry ote_mid, stop 0.1 ATR · Midday 11:30-14:30 | 1660 | 492 | 29.6% | 44.7% | -0.05 | -0.01 | 0.92 | -24.23 | -40.57 | -0.05 | -0.05 |
| Entry ote_mid, stop 0.1 ATR · Stocks only | 2024 | 549 | 27.1% | 43.0% | -0.03 | -0.01 | 0.94 | -16.99 | -41.36 | -0.07 | 0.01 |
| Entry ote_mid, stop 0.1 ATR · R:R to T2 2.5+ | 2714 | 913 | 33.6% | 41.0% | -0.13 | -0.04 | 0.8 | -115.92 | -147.26 | -0.13 | -0.12 |
| Entry ote_mid, stop 0.1 ATR · Risk 0.15%+ | 2908 | 816 | 28.1% | 43.9% | -0.0 | -0.0 | 1.0 | -0.92 | -51.41 | 0.02 | -0.02 |
| Entry ote_mid, stop 0.1 ATR · Midday + R:R 2.5+ + risk 0.15%+ | 1128 | 353 | 31.3% | 46.2% | 0.04 | 0.01 | 1.07 | 12.38 | -22.62 | 0.04 | 0.03 |
| Entry ote_mid, stop 0.3 ATR · All qualified | 3573 | 1139 | 31.9% | 43.8% | -0.1 | -0.03 | 0.82 | -118.2 | -139.8 | -0.09 | -0.11 |
| Entry ote_mid, stop 0.3 ATR · Plan window (by 11:30) | 1012 | 396 | 39.1% | 41.7% | -0.17 | -0.06 | 0.71 | -65.54 | -69.61 | -0.25 | -0.08 |
| Entry ote_mid, stop 0.3 ATR · Midday 11:30-14:30 | 1660 | 492 | 29.6% | 47.6% | -0.03 | -0.01 | 0.94 | -15.83 | -32.71 | 0.0 | -0.06 |
| Entry ote_mid, stop 0.3 ATR · Stocks only | 2024 | 549 | 27.1% | 45.9% | -0.03 | -0.01 | 0.94 | -17.3 | -38.05 | -0.03 | -0.04 |
| Entry ote_mid, stop 0.3 ATR · R:R to T2 2.5+ | 2714 | 913 | 33.6% | 44.1% | -0.1 | -0.03 | 0.82 | -93.94 | -122.31 | -0.08 | -0.12 |
| Entry ote_mid, stop 0.3 ATR · Risk 0.15%+ | 2908 | 816 | 28.1% | 46.7% | 0.0 | 0.0 | 1.01 | 3.81 | -36.54 | 0.03 | -0.02 |
| Entry ote_mid, stop 0.3 ATR · Midday + R:R 2.5+ + risk 0.15%+ | 1128 | 353 | 31.3% | 49.6% | 0.05 | 0.02 | 1.11 | 19.13 | -19.12 | 0.11 | 0.0 |
| Entry fvg_edge, stop 0.1 ATR · All qualified | 3573 | 1506 | 42.1% | 49.5% | -0.1 | -0.04 | 0.79 | -145.15 | -151.88 | -0.1 | -0.09 |
| Entry fvg_edge, stop 0.1 ATR · Plan window (by 11:30) | 1012 | 508 | 50.2% | 49.2% | -0.14 | -0.07 | 0.71 | -68.88 | -75.84 | -0.17 | -0.1 |
| Entry fvg_edge, stop 0.1 ATR · Midday 11:30-14:30 | 1660 | 665 | 40.1% | 51.0% | -0.08 | -0.03 | 0.82 | -51.22 | -56.74 | -0.08 | -0.07 |
| Entry fvg_edge, stop 0.1 ATR · Stocks only | 2024 | 740 | 36.6% | 49.9% | -0.08 | -0.03 | 0.81 | -62.44 | -66.33 | -0.1 | -0.07 |
| Entry fvg_edge, stop 0.1 ATR · R:R to T2 2.5+ | 2714 | 1184 | 43.6% | 48.8% | -0.11 | -0.05 | 0.77 | -131.31 | -143.45 | -0.13 | -0.09 |
| Entry fvg_edge, stop 0.1 ATR · Risk 0.15%+ | 2908 | 1100 | 37.8% | 52.2% | -0.04 | -0.02 | 0.9 | -46.33 | -67.32 | -0.03 | -0.05 |
| Entry fvg_edge, stop 0.1 ATR · Midday + R:R 2.5+ + risk 0.15%+ | 1128 | 458 | 40.6% | 52.0% | -0.06 | -0.03 | 0.85 | -28.26 | -33.87 | -0.04 | -0.08 |
| Entry fvg_edge, stop 0.3 ATR · All qualified | 3573 | 1506 | 42.1% | 51.5% | -0.08 | -0.04 | 0.8 | -126.28 | -134.68 | -0.07 | -0.1 |
| Entry fvg_edge, stop 0.3 ATR · Plan window (by 11:30) | 1012 | 508 | 50.2% | 51.2% | -0.13 | -0.06 | 0.7 | -65.28 | -71.28 | -0.16 | -0.1 |
| Entry fvg_edge, stop 0.3 ATR · Midday 11:30-14:30 | 1660 | 665 | 40.1% | 53.1% | -0.06 | -0.02 | 0.85 | -41.17 | -47.46 | -0.05 | -0.08 |
| Entry fvg_edge, stop 0.3 ATR · Stocks only | 2024 | 740 | 36.6% | 52.2% | -0.07 | -0.03 | 0.82 | -54.25 | -57.44 | -0.06 | -0.09 |
| Entry fvg_edge, stop 0.3 ATR · R:R to T2 2.5+ | 2714 | 1184 | 43.6% | 51.4% | -0.09 | -0.04 | 0.79 | -107.41 | -121.26 | -0.09 | -0.09 |
| Entry fvg_edge, stop 0.3 ATR · Risk 0.15%+ | 2908 | 1100 | 37.8% | 54.3% | -0.03 | -0.01 | 0.92 | -34.76 | -53.12 | -0.01 | -0.05 |
| Entry fvg_edge, stop 0.3 ATR · Midday + R:R 2.5+ + risk 0.15%+ | 1128 | 458 | 40.6% | 54.6% | -0.04 | -0.02 | 0.9 | -17.75 | -27.2 | 0.02 | -0.09 |
| Entry fvg_ce, stop 0.1 ATR · All qualified | 3573 | 1253 | 35.1% | 43.9% | -0.12 | -0.04 | 0.79 | -152.36 | -162.15 | -0.13 | -0.11 |
| Entry fvg_ce, stop 0.1 ATR · Plan window (by 11:30) | 1012 | 435 | 43.0% | 43.0% | -0.16 | -0.07 | 0.72 | -69.09 | -73.8 | -0.23 | -0.09 |
| Entry fvg_ce, stop 0.1 ATR · Midday 11:30-14:30 | 1660 | 548 | 33.0% | 46.7% | -0.07 | -0.02 | 0.86 | -39.57 | -48.15 | -0.07 | -0.08 |
| Entry fvg_ce, stop 0.1 ATR · Stocks only | 2024 | 610 | 30.1% | 45.6% | -0.06 | -0.02 | 0.89 | -34.95 | -52.09 | -0.1 | -0.01 |
| Entry fvg_ce, stop 0.1 ATR · R:R to T2 2.5+ | 2714 | 997 | 36.7% | 43.4% | -0.12 | -0.05 | 0.79 | -122.45 | -139.59 | -0.15 | -0.1 |
| Entry fvg_ce, stop 0.1 ATR · Risk 0.15%+ | 2908 | 906 | 31.2% | 46.5% | -0.03 | -0.01 | 0.94 | -25.84 | -58.75 | -0.03 | -0.03 |
| Entry fvg_ce, stop 0.1 ATR · Midday + R:R 2.5+ + risk 0.15%+ | 1128 | 387 | 34.3% | 47.8% | -0.02 | -0.01 | 0.96 | -8.34 | -24.3 | -0.0 | -0.04 |
| Entry fvg_ce, stop 0.3 ATR · All qualified | 3573 | 1253 | 35.1% | 46.4% | -0.1 | -0.04 | 0.8 | -131.43 | -141.06 | -0.09 | -0.12 |
| Entry fvg_ce, stop 0.3 ATR · Plan window (by 11:30) | 1012 | 435 | 43.0% | 45.3% | -0.15 | -0.06 | 0.71 | -65.46 | -69.17 | -0.21 | -0.09 |
| Entry fvg_ce, stop 0.3 ATR · Midday 11:30-14:30 | 1660 | 548 | 33.0% | 49.5% | -0.05 | -0.02 | 0.89 | -27.5 | -36.88 | -0.01 | -0.09 |
| Entry fvg_ce, stop 0.3 ATR · Stocks only | 2024 | 610 | 30.1% | 48.2% | -0.05 | -0.01 | 0.89 | -30.25 | -43.47 | -0.06 | -0.04 |
| Entry fvg_ce, stop 0.3 ATR · R:R to T2 2.5+ | 2714 | 997 | 36.7% | 46.4% | -0.1 | -0.04 | 0.81 | -97.51 | -114.03 | -0.09 | -0.1 |
| Entry fvg_ce, stop 0.3 ATR · Risk 0.15%+ | 2908 | 906 | 31.2% | 49.0% | -0.02 | -0.01 | 0.96 | -15.72 | -40.93 | -0.0 | -0.03 |
| Entry fvg_ce, stop 0.3 ATR · Midday + R:R 2.5+ + risk 0.15%+ | 1128 | 387 | 34.3% | 51.2% | 0.01 | 0.0 | 1.02 | 3.02 | -17.97 | 0.07 | -0.06 |
| Entry blend, stop 0.1 ATR · All qualified | 3573 | 1300 | 36.4% | 45.2% | -0.12 | -0.04 | 0.79 | -152.83 | -164.99 | -0.12 | -0.12 |
| Entry blend, stop 0.1 ATR · Plan window (by 11:30) | 1012 | 448 | 44.3% | 44.0% | -0.17 | -0.07 | 0.7 | -75.32 | -79.16 | -0.22 | -0.11 |
| Entry blend, stop 0.1 ATR · Midday 11:30-14:30 | 1660 | 573 | 34.5% | 47.8% | -0.06 | -0.02 | 0.87 | -36.63 | -44.6 | -0.06 | -0.07 |
| Entry blend, stop 0.1 ATR · Stocks only | 2024 | 635 | 31.4% | 45.7% | -0.08 | -0.02 | 0.85 | -47.69 | -57.3 | -0.11 | -0.04 |
| Entry blend, stop 0.1 ATR · R:R to T2 2.5+ | 2714 | 1034 | 38.1% | 44.6% | -0.13 | -0.05 | 0.77 | -131.18 | -149.61 | -0.14 | -0.12 |
| Entry blend, stop 0.1 ATR · Risk 0.15%+ | 2908 | 945 | 32.5% | 47.6% | -0.03 | -0.01 | 0.94 | -28.25 | -61.02 | -0.01 | -0.05 |
| Entry blend, stop 0.1 ATR · Midday + R:R 2.5+ + risk 0.15%+ | 1128 | 398 | 35.3% | 48.0% | -0.04 | -0.01 | 0.92 | -14.15 | -24.13 | -0.01 | -0.06 |
| Entry blend, stop 0.3 ATR · All qualified | 3573 | 1300 | 36.4% | 47.5% | -0.1 | -0.04 | 0.8 | -132.53 | -144.16 | -0.08 | -0.12 |
| Entry blend, stop 0.3 ATR · Plan window (by 11:30) | 1012 | 448 | 44.3% | 46.2% | -0.16 | -0.07 | 0.69 | -70.88 | -73.89 | -0.21 | -0.11 |
| Entry blend, stop 0.3 ATR · Midday 11:30-14:30 | 1660 | 573 | 34.5% | 50.3% | -0.04 | -0.02 | 0.9 | -25.66 | -34.42 | -0.01 | -0.08 |
| Entry blend, stop 0.3 ATR · Stocks only | 2024 | 635 | 31.4% | 48.0% | -0.07 | -0.02 | 0.86 | -41.65 | -50.19 | -0.07 | -0.06 |
| Entry blend, stop 0.3 ATR · R:R to T2 2.5+ | 2714 | 1034 | 38.1% | 47.4% | -0.1 | -0.04 | 0.8 | -106.33 | -124.0 | -0.09 | -0.12 |
| Entry blend, stop 0.3 ATR · Risk 0.15%+ | 2908 | 945 | 32.5% | 49.9% | -0.02 | -0.01 | 0.96 | -18.05 | -43.44 | 0.01 | -0.05 |
| Entry blend, stop 0.3 ATR · Midday + R:R 2.5+ + risk 0.15%+ | 1128 | 398 | 35.3% | 51.0% | -0.01 | -0.0 | 0.98 | -2.95 | -19.51 | 0.06 | -0.07 |
| Entry ote_62, stop 0.1 ATR · All qualified | 3573 | 1238 | 34.6% | 43.6% | -0.1 | -0.03 | 0.83 | -120.46 | -142.52 | -0.12 | -0.07 |
| Entry ote_62, stop 0.1 ATR · Plan window (by 11:30) | 1012 | 420 | 41.5% | 41.2% | -0.17 | -0.07 | 0.72 | -70.49 | -73.74 | -0.24 | -0.1 |
| Entry ote_62, stop 0.1 ATR · Midday 11:30-14:30 | 1660 | 542 | 32.7% | 45.9% | -0.04 | -0.01 | 0.92 | -24.15 | -38.99 | -0.07 | -0.02 |
| Entry ote_62, stop 0.1 ATR · Stocks only | 2024 | 602 | 29.7% | 44.2% | -0.05 | -0.01 | 0.91 | -28.0 | -47.69 | -0.08 | -0.02 |
| Entry ote_62, stop 0.1 ATR · R:R to T2 2.5+ | 2714 | 994 | 36.6% | 43.2% | -0.11 | -0.04 | 0.82 | -108.06 | -136.04 | -0.13 | -0.08 |
| Entry ote_62, stop 0.1 ATR · Risk 0.15%+ | 2908 | 885 | 30.4% | 45.4% | -0.02 | -0.0 | 0.97 | -13.37 | -58.52 | -0.0 | -0.03 |
| Entry ote_62, stop 0.1 ATR · Midday + R:R 2.5+ + risk 0.15%+ | 1128 | 380 | 33.7% | 46.3% | -0.0 | -0.0 | 1.0 | -0.49 | -22.42 | 0.02 | -0.02 |
| Entry ote_62, stop 0.3 ATR · All qualified | 3573 | 1238 | 34.6% | 46.4% | -0.08 | -0.03 | 0.84 | -102.19 | -123.17 | -0.08 | -0.08 |
| Entry ote_62, stop 0.3 ATR · Plan window (by 11:30) | 1012 | 420 | 41.5% | 44.3% | -0.15 | -0.06 | 0.72 | -64.98 | -67.48 | -0.22 | -0.09 |
| Entry ote_62, stop 0.3 ATR · Midday 11:30-14:30 | 1660 | 542 | 32.7% | 48.5% | -0.03 | -0.01 | 0.94 | -16.28 | -30.86 | -0.02 | -0.04 |
| Entry ote_62, stop 0.3 ATR · Stocks only | 2024 | 602 | 29.7% | 47.3% | -0.04 | -0.01 | 0.92 | -22.54 | -42.7 | -0.03 | -0.05 |
| Entry ote_62, stop 0.3 ATR · R:R to T2 2.5+ | 2714 | 994 | 36.6% | 46.4% | -0.08 | -0.03 | 0.84 | -84.16 | -110.84 | -0.08 | -0.09 |
| Entry ote_62, stop 0.3 ATR · Risk 0.15%+ | 2908 | 885 | 30.4% | 48.4% | -0.0 | -0.0 | 0.99 | -2.77 | -39.76 | 0.02 | -0.03 |
| Entry ote_62, stop 0.3 ATR · Midday + R:R 2.5+ + risk 0.15%+ | 1128 | 380 | 33.7% | 49.5% | 0.02 | 0.01 | 1.04 | 7.26 | -18.24 | 0.08 | -0.05 |
| Entry tl_line, stop 0.1 ATR · All qualified | 3573 | 7 | 0.2% | 42.9% | -0.02 | -0.0 | 0.96 | -0.13 | -2.2 | -0.07 | 0.02 |
| Entry tl_line, stop 0.1 ATR · Plan window (by 11:30) | 1012 | 1 | 0.1% | 100.0% | 0.32 | 0.0 |  | 0.32 | 0.0 |  | 0.32 |
| Entry tl_line, stop 0.1 ATR · Midday 11:30-14:30 | 1660 | 5 | 0.3% | 40.0% | -0.47 | -0.0 | 0.27 | -2.34 | -3.2 | 0.43 | -1.07 |
| Entry tl_line, stop 0.1 ATR · Stocks only | 2024 | 5 | 0.2% | 40.0% | -0.26 | -0.0 | 0.4 | -1.3 | -2.16 | 0.43 | -0.72 |
| Entry tl_line, stop 0.1 ATR · R:R to T2 2.5+ | 2714 | 7 | 0.3% | 42.9% | -0.02 | -0.0 | 0.96 | -0.13 | -2.2 | -0.07 | 0.02 |
| Entry tl_line, stop 0.1 ATR · Risk 0.15%+ | 2908 | 7 | 0.2% | 42.9% | -0.02 | -0.0 | 0.96 | -0.13 | -2.2 | -0.07 | 0.02 |
| Entry tl_line, stop 0.1 ATR · Midday + R:R 2.5+ + risk 0.15%+ | 1128 | 5 | 0.4% | 40.0% | -0.47 | -0.0 | 0.27 | -2.34 | -3.2 | 0.43 | -1.07 |
| Entry tl_line, stop 0.3 ATR · All qualified | 3573 | 7 | 0.2% | 42.9% | -0.11 | -0.0 | 0.78 | -0.75 | -2.32 | -0.12 | -0.1 |
| Entry tl_line, stop 0.3 ATR · Plan window (by 11:30) | 1012 | 1 | 0.1% | 100.0% | 0.29 | 0.0 |  | 0.29 | 0.0 |  | 0.29 |
| Entry tl_line, stop 0.3 ATR · Midday 11:30-14:30 | 1660 | 5 | 0.3% | 40.0% | -0.52 | -0.0 | 0.22 | -2.6 | -3.32 | 0.36 | -1.11 |
| Entry tl_line, stop 0.3 ATR · Stocks only | 2024 | 5 | 0.2% | 40.0% | -0.31 | -0.0 | 0.31 | -1.57 | -2.28 | 0.36 | -0.76 |
| Entry tl_line, stop 0.3 ATR · R:R to T2 2.5+ | 2714 | 7 | 0.3% | 42.9% | -0.11 | -0.0 | 0.78 | -0.75 | -2.32 | -0.12 | -0.1 |
| Entry tl_line, stop 0.3 ATR · Risk 0.15%+ | 2908 | 7 | 0.2% | 42.9% | -0.11 | -0.0 | 0.78 | -0.75 | -2.32 | -0.12 | -0.1 |
| Entry tl_line, stop 0.3 ATR · Midday + R:R 2.5+ + risk 0.15%+ | 1128 | 5 | 0.4% | 40.0% | -0.52 | -0.0 | 0.22 | -2.6 | -3.32 | 0.36 | -1.11 |
| Scaled ladder_equal (fvg_edge 33%, blend 33%, ote_mid 33%) · All qualified | 3573 | 1506 | 42.1% | 50.8% | -0.1 | -0.04 | 0.79 | -144.34 | -157.31 | -0.1 | -0.1 |
| Scaled ladder_equal (fvg_edge 33%, blend 33%, ote_mid 33%) · Plan window (by 11:30) | 1012 | 508 | 50.2% | 49.8% | -0.14 | -0.07 | 0.71 | -70.81 | -76.21 | -0.18 | -0.1 |
| Scaled ladder_equal (fvg_edge 33%, blend 33%, ote_mid 33%) · Midday 11:30-14:30 | 1660 | 665 | 40.1% | 53.2% | -0.06 | -0.02 | 0.86 | -39.01 | -48.24 | -0.07 | -0.05 |
| Scaled ladder_equal (fvg_edge 33%, blend 33%, ote_mid 33%) · Stocks only | 2024 | 740 | 36.6% | 51.6% | -0.06 | -0.02 | 0.86 | -44.64 | -54.53 | -0.08 | -0.04 |
| Scaled ladder_equal (fvg_edge 33%, blend 33%, ote_mid 33%) · R:R to T2 2.5+ | 2714 | 1184 | 43.6% | 50.3% | -0.11 | -0.05 | 0.78 | -126.11 | -145.53 | -0.12 | -0.1 |
| Scaled ladder_equal (fvg_edge 33%, blend 33%, ote_mid 33%) · Risk 0.15%+ | 2908 | 1100 | 37.8% | 53.4% | -0.02 | -0.01 | 0.94 | -27.29 | -60.12 | -0.02 | -0.03 |
| Scaled ladder_equal (fvg_edge 33%, blend 33%, ote_mid 33%) · Midday + R:R 2.5+ + risk 0.15%+ | 1128 | 458 | 40.6% | 53.7% | -0.03 | -0.01 | 0.93 | -12.54 | -21.93 | -0.01 | -0.04 |
| Scaled ladder_deep (fvg_edge 20%, blend 30%, ote_mid 50%) · All qualified | 3573 | 1506 | 42.1% | 51.3% | -0.09 | -0.04 | 0.8 | -142.48 | -158.03 | -0.09 | -0.1 |
| Scaled ladder_deep (fvg_edge 20%, blend 30%, ote_mid 50%) · Plan window (by 11:30) | 1012 | 508 | 50.2% | 50.6% | -0.14 | -0.07 | 0.71 | -70.77 | -75.95 | -0.18 | -0.1 |
| Scaled ladder_deep (fvg_edge 20%, blend 30%, ote_mid 50%) · Midday 11:30-14:30 | 1660 | 665 | 40.1% | 53.8% | -0.05 | -0.02 | 0.88 | -34.98 | -45.89 | -0.06 | -0.04 |
| Scaled ladder_deep (fvg_edge 20%, blend 30%, ote_mid 50%) · Stocks only | 2024 | 740 | 36.6% | 52.6% | -0.05 | -0.02 | 0.88 | -37.61 | -50.6 | -0.07 | -0.03 |
| Scaled ladder_deep (fvg_edge 20%, blend 30%, ote_mid 50%) · R:R to T2 2.5+ | 2714 | 1184 | 43.6% | 50.7% | -0.1 | -0.05 | 0.78 | -123.51 | -145.89 | -0.11 | -0.1 |
| Scaled ladder_deep (fvg_edge 20%, blend 30%, ote_mid 50%) · Risk 0.15%+ | 2908 | 1100 | 37.8% | 54.1% | -0.02 | -0.01 | 0.95 | -20.41 | -57.72 | -0.01 | -0.02 |
| Scaled ladder_deep (fvg_edge 20%, blend 30%, ote_mid 50%) · Midday + R:R 2.5+ + risk 0.15%+ | 1128 | 458 | 40.6% | 54.4% | -0.01 | -0.01 | 0.97 | -6.34 | -21.89 | -0.0 | -0.02 |

## 8. Trade management (systematic, qualified, triggered)

| Method | Trades | Avg R | Win rate |
|---|---|---|---|
| Plan: half at T1, rest to T2 (gross) | 1139 | 0.09 | 42.7% |
| Plan, net of costs | 1139 | -0.12 | 41.1% |
| Full position to T1 (gross) | 1139 | 0.1 | 42.9% |
| Full position to T2 (gross) | 1139 | 0.08 | 37.4% |

## 10. v3 candidate tests (New York session, qualified, net of costs)

Confirmation entry = wait for price to reach the FVG, then enter on the first bar that closes beyond the prior 3 bars (bars used: {'1m': 2995, '5m': 159}). Runner = half at T1, rest to the close with a breakeven stop. 1st/2nd half columns are the out-of-sample check.

| Group | Setups | Triggered | Trigger rate | Win rate | Avg R | Expectancy R | Profit factor | Total R | Max DD R | 1st half avg R | 2nd half avg R |
|---|---|---|---|---|---|---|---|---|---|---|---|
| All (New York) · Current plan | 3157 | 937 | 29.7% | 42.4% | -0.09 | -0.03 | 0.86 | -81.76 | -106.07 | -0.09 | -0.09 |
| All (New York) · Runner to the close | 3157 | 937 | 29.7% | 42.4% | -0.08 | -0.03 | 0.86 | -79.21 | -105.27 | -0.06 | -0.11 |
| All (New York) · Full position to T2 | 3157 | 937 | 29.7% | 37.9% | -0.08 | -0.02 | 0.88 | -75.75 | -112.51 | -0.09 | -0.07 |
| All (New York) · Confirmation entry | 3157 | 1033 | 32.7% | 52.0% | -0.1 | -0.03 | 0.74 | -105.0 | -105.0 | -0.12 | -0.09 |
| v3: 11:30-14:30 + risk 0.3%+ + FVG 0.5+ ATR · Current plan | 820 | 163 | 19.9% | 46.6% | 0.06 | 0.01 | 1.11 | 9.03 | -17.56 | 0.08 | 0.04 |
| v3: 11:30-14:30 + risk 0.3%+ + FVG 0.5+ ATR · Runner to the close | 820 | 163 | 19.9% | 46.6% | 0.04 | 0.01 | 1.09 | 6.99 | -17.56 | 0.08 | 0.01 |
| v3: 11:30-14:30 + risk 0.3%+ + FVG 0.5+ ATR · Full position to T2 | 820 | 163 | 19.9% | 44.2% | 0.08 | 0.02 | 1.15 | 13.34 | -18.57 | 0.08 | 0.08 |
| v3: 11:30-14:30 + risk 0.3%+ + FVG 0.5+ ATR · Confirmation entry | 820 | 224 | 27.3% | 56.2% | 0.01 | 0.0 | 1.04 | 2.9 | -9.81 | 0.06 | -0.03 |
| v3 + longs · Current plan | 669 | 126 | 18.8% | 50.0% | 0.14 | 0.03 | 1.29 | 17.88 | -13.91 | 0.23 | 0.06 |
| v3 + longs · Runner to the close | 669 | 126 | 18.8% | 50.0% | 0.13 | 0.02 | 1.26 | 15.85 | -13.91 | 0.23 | 0.02 |
| v3 + longs · Full position to T2 | 669 | 126 | 18.8% | 46.0% | 0.14 | 0.03 | 1.26 | 17.03 | -15.65 | 0.2 | 0.07 |
| v3 + longs · Confirmation entry | 669 | 184 | 27.5% | 57.1% | 0.03 | 0.01 | 1.11 | 6.17 | -9.31 | 0.12 | -0.05 |
| v3 + VWAP side · Current plan | 618 | 94 | 15.2% | 50.0% | 0.06 | 0.01 | 1.12 | 5.26 | -8.73 | 0.08 | 0.03 |
| v3 + VWAP side · Runner to the close | 618 | 94 | 15.2% | 50.0% | 0.03 | 0.01 | 1.08 | 3.23 | -8.73 | 0.08 | -0.01 |
| v3 + VWAP side · Full position to T2 | 618 | 94 | 15.2% | 47.9% | 0.06 | 0.01 | 1.12 | 5.85 | -9.31 | 0.04 | 0.09 |
| v3 + VWAP side · Confirmation entry | 618 | 141 | 22.8% | 52.5% | 0.0 | 0.0 | 1.01 | 0.56 | -7.9 | 0.05 | -0.05 |
| v3 + in play (open volume 1.5x+) · Current plan | 121 | 24 | 19.8% | 41.7% | 0.02 | 0.0 | 1.04 | 0.41 | -3.73 | -0.22 | 0.25 |
| v3 + in play (open volume 1.5x+) · Runner to the close | 121 | 24 | 19.8% | 41.7% | 0.02 | 0.0 | 1.04 | 0.41 | -3.73 | -0.22 | 0.25 |
| v3 + in play (open volume 1.5x+) · Full position to T2 | 121 | 24 | 19.8% | 41.7% | -0.13 | -0.03 | 0.73 | -3.17 | -4.62 | -0.25 | -0.01 |
| v3 + in play (open volume 1.5x+) · Confirmation entry | 121 | 33 | 27.3% | 57.6% | 0.02 | 0.0 | 1.05 | 0.58 | -2.61 | 0.11 | -0.07 |
| v3 + longs + VWAP side · Current plan | 524 | 78 | 14.9% | 51.3% | 0.13 | 0.02 | 1.28 | 9.83 | -5.47 | 0.16 | 0.09 |
| v3 + longs + VWAP side · Runner to the close | 524 | 78 | 14.9% | 51.3% | 0.1 | 0.01 | 1.22 | 7.79 | -5.47 | 0.17 | 0.03 |
| v3 + longs + VWAP side · Full position to T2 | 524 | 78 | 14.9% | 50.0% | 0.17 | 0.02 | 1.36 | 12.98 | -6.05 | 0.19 | 0.14 |
| v3 + longs + VWAP side · Confirmation entry | 524 | 122 | 23.3% | 52.5% | 0.01 | 0.0 | 1.03 | 0.95 | -8.23 | 0.07 | -0.06 |
| VWAP side only · Current plan | 2164 | 574 | 26.5% | 42.2% | -0.13 | -0.03 | 0.78 | -75.35 | -80.01 | -0.17 | -0.09 |
| VWAP side only · Runner to the close | 2164 | 574 | 26.5% | 42.2% | -0.13 | -0.04 | 0.78 | -76.19 | -83.34 | -0.13 | -0.13 |
| VWAP side only · Full position to T2 | 2164 | 574 | 26.5% | 38.7% | -0.13 | -0.03 | 0.8 | -72.87 | -86.37 | -0.15 | -0.1 |
| VWAP side only · Confirmation entry | 2164 | 665 | 30.7% | 51.1% | -0.11 | -0.04 | 0.7 | -75.99 | -77.31 | -0.13 | -0.1 |
| In play only · Current plan | 395 | 109 | 27.6% | 37.6% | -0.24 | -0.07 | 0.62 | -26.24 | -32.79 | -0.52 | 0.03 |
| In play only · Runner to the close | 395 | 109 | 27.6% | 37.6% | -0.25 | -0.07 | 0.61 | -27.26 | -33.9 | -0.52 | 0.01 |
| In play only · Full position to T2 | 395 | 109 | 27.6% | 33.0% | -0.35 | -0.1 | 0.51 | -38.3 | -41.15 | -0.6 | -0.11 |
| In play only · Confirmation entry | 395 | 126 | 31.9% | 52.4% | -0.12 | -0.04 | 0.71 | -14.61 | -23.63 | -0.26 | 0.02 |

## 11. Trendline retest confluence (New York session, qualified, net of costs)

Trendline = the falling line across the lower highs into the sweep (rising line across higher lows for shorts), broken by a close and not failed. Confluence = its level at the snapshot sits in the entry zone (FVG near edge to entry) within 0.25 ATR. Retest at fill = the line was within 0.3 ATR of the fill price when the order filled. Only rows recorded since Nov 4, 2026 (rerun the backtest to fill history).

| Group | Setups | Triggered | Trigger rate | Win rate | Avg R | Expectancy R | Profit factor | Total R | Max DD R | 1st half avg R | 2nd half avg R |
|---|---|---|---|---|---|---|---|---|---|---|---|
| All (New York, trendline recorded) · current plan | 244 | 90 | 36.9% | 37.8% | -0.3 | -0.11 | 0.55 | -26.63 | -26.63 | -0.31 | -0.28 |
| No trendline found/broken · current plan | 145 | 47 | 32.4% | 36.2% | -0.36 | -0.12 | 0.48 | -17.02 | -18.73 | -0.55 | -0.18 |
| Trendline found and broken · current plan | 99 | 43 | 43.4% | 39.5% | -0.22 | -0.1 | 0.64 | -9.61 | -11.86 | -0.01 | -0.43 |
| Trendline confluence at snapshot · current plan | 15 | 7 | 46.7% | 28.6% | -0.47 | -0.22 | 0.3 | -3.31 | -4.71 | 0.11 | -0.91 |
| No confluence at snapshot · current plan | 229 | 83 | 36.2% | 38.6% | -0.28 | -0.1 | 0.57 | -23.32 | -23.32 | -0.31 | -0.25 |
| Confluence, 3+ touches · current plan | 2 | 0 | 0.0% |  |  | 0.0 |  | 0.0 | 0.0 |  |  |
| Confluence + longs · current plan | 12 | 6 | 50.0% | 33.3% | -0.38 | -0.19 | 0.38 | -2.26 | -3.67 | 0.11 | -0.87 |
| Confluence + midday (11:30-14:30) · current plan | 12 | 6 | 50.0% | 33.3% | -0.38 | -0.19 | 0.38 | -2.26 | -3.67 | 0.11 | -0.87 |
| Confluence + risk 0.3%+ · current plan | 12 | 6 | 50.0% | 16.7% | -0.65 | -0.32 | 0.18 | -3.88 | -4.71 | -0.24 | -1.06 |
| Confluence + VWAP side · current plan | 6 | 3 | 50.0% | 33.3% | -0.24 | -0.12 | 0.53 | -0.73 | -1.56 | 0.84 | -0.78 |
| Confluence + longs + midday + risk 0.3%+ · current plan | 9 | 5 | 55.6% | 20.0% | -0.57 | -0.31 | 0.23 | -2.83 | -3.67 | -0.12 | -0.87 |
| Fill was a trendline retest (any setup) | 244 | 3 | 1.2% | 33.3% | -0.33 | -0.0 | 0.36 | -1.0 | -1.57 | 0.57 | -0.79 |
| Fill was a trendline retest + longs | 202 | 3 | 1.5% | 33.3% | -0.33 | -0.0 | 0.36 | -1.0 | -1.57 | 0.57 | -0.79 |
| Entry at the trendline (stop 0.1 ATR) | 15 | 6 | 40.0% | 33.3% | -0.4 | -0.16 | 0.26 | -2.41 | -3.27 | -0.07 | -0.73 |
| Entry at the trendline (stop 0.3 ATR) | 15 | 6 | 40.0% | 33.3% | -0.44 | -0.18 | 0.21 | -2.66 | -3.38 | -0.12 | -0.77 |

## 9. Automatic changes in this run

| Key | Old | New | Evidence |
|---|---|---|---|
| None |  |  |  |
