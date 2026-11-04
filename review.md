# FVG review: 2026-11-03 19:31 ET (Backtest)

Sessions: 125 (2026-05-07 to 2026-11-03). Config version 1.

## 1. Strategy performance (qualified setups; results net of costs)

Costs: 0.02% of price per side. Entries allowed until 15:30 ET.

| Group | Setups | Triggered | Trigger rate | Win rate | Avg R | Expectancy R | Profit factor | Total R | Max DD R | 1st half avg R | 2nd half avg R |
|---|---|---|---|---|---|---|---|---|---|---|---|
| Live dashboard snapshots | 28 | 7 | 25.0% | 42.9% | -0.06 | -0.01 | 0.92 | -0.4 | -4.34 | -0.56 | 0.32 |
| Daily full-session replays | 3 | 0 | 0.0% |  |  | 0.0 |  | 0.0 | 0.0 |  |  |
| Backtest | 3224 | 1010 | 31.3% | 41.1% | -0.1 | -0.03 | 0.84 | -104.96 | -135.21 | -0.08 | -0.13 |
| Systematic (replays + backtest) | 3227 | 1010 | 31.3% | 41.1% | -0.1 | -0.03 | 0.84 | -104.96 | -135.21 | -0.08 | -0.13 |
| Systematic, before cost (gross) | 3227 | 1010 | 31.3% | 42.8% | 0.1 | 0.03 | 1.19 | 99.73 | -37.49 | 0.09 | 0.1 |
| Systematic, plan window only (New York, formed by 11:30) | 904 | 354 | 39.2% | 39.0% | -0.17 | -0.07 | 0.74 | -58.78 | -63.51 | -0.24 | -0.09 |
| Live top-5 suggestions only | 17 | 4 | 23.5% | 25.0% | -0.4 | -0.09 | 0.54 | -1.61 | -3.49 | -1.13 | 0.32 |
| Your actual trades | 1 | 1 |  | 0.0% | -1.77 |  |  | -1.77 |  |  |  |
| Stocks and ETFs, New York session only | 2749 | 798 | 29.0% | 42.4% | -0.07 | -0.02 | 0.88 | -59.53 | -91.99 | -0.07 | -0.08 |
| Futures, New York session | 134 | 45 | 33.6% | 48.9% | 0.06 | 0.02 | 1.1 | 2.58 | -9.25 | 0.39 | -0.26 |
| Futures, all 24-hour sessions | 478 | 212 | 44.4% | 36.3% | -0.21 | -0.1 | 0.71 | -45.43 | -46.07 | -0.28 | -0.15 |

## 1c. Futures by session (24-hour test; qualified, net of costs)

Asia and London use their own levels: prior-day high/low, the previous session's high/low, and the session's first 30 minutes.

| Group | Setups | Triggered | Trigger rate | Win rate | Avg R | Expectancy R | Profit factor | Total R | Max DD R | 1st half avg R | 2nd half avg R |
|---|---|---|---|---|---|---|---|---|---|---|---|
| Futures, Asia session (6 PM-midnight ET) | 159 | 68 | 42.8% | 29.4% | -0.28 | -0.12 | 0.65 | -18.77 | -19.47 | -0.24 | -0.31 |
| Futures, London session (2-8 AM ET) | 185 | 99 | 53.5% | 35.4% | -0.3 | -0.16 | 0.63 | -29.24 | -38.05 | -0.68 | 0.09 |
| Futures, NY session (9:30-4:00 ET) | 134 | 45 | 33.6% | 48.9% | 0.06 | 0.02 | 1.1 | 2.58 | -9.25 | 0.39 | -0.26 |
| CL=F Asia | 21 | 11 | 52.4% | 45.5% | 0.4 | 0.21 | 1.65 | 4.39 | -2.35 | -0.11 | 0.82 |
| CL=F London | 19 | 8 | 42.1% | 50.0% | 0.38 | 0.16 | 1.81 | 3.02 | -2.21 | -0.35 | 1.1 |
| CL=F NY | 20 | 7 | 35.0% | 28.6% | -0.38 | -0.13 | 0.5 | -2.66 | -3.18 | -1.06 | 0.13 |
| ES=F Asia | 15 | 6 | 40.0% | 33.3% | -0.45 | -0.18 | 0.43 | -2.72 | -4.64 | 0.28 | -1.18 |
| ES=F London | 21 | 14 | 66.7% | 42.9% | 0.07 | 0.05 | 1.1 | 0.98 | -5.2 | -0.5 | 0.64 |
| ES=F NY | 17 | 8 | 47.1% | 75.0% | 0.85 | 0.4 | 5.84 | 6.83 | -1.41 | 1.23 | 0.48 |
| GC=F Asia | 32 | 21 | 65.6% | 23.8% | -0.11 | -0.07 | 0.85 | -2.28 | -10.46 | 0.31 | -0.49 |
| GC=F London | 15 | 6 | 40.0% | 66.7% | 0.35 | 0.14 | 2.0 | 2.09 | -1.05 | 0.05 | 0.64 |
| GC=F NY | 14 | 4 | 28.6% | 50.0% | 0.28 | 0.08 | 1.54 | 1.11 | -1.04 | 0.66 | -0.1 |
| NQ=F Asia | 12 | 6 | 50.0% | 16.7% | -0.74 | -0.37 | 0.15 | -4.41 | -5.19 | -1.04 | -0.43 |
| NQ=F London | 16 | 7 | 43.8% | 0.0% | -0.79 | -0.35 | 0.0 | -5.53 | -5.53 | -1.03 | -0.61 |
| NQ=F NY | 11 | 4 | 36.4% | 25.0% | -0.32 | -0.12 | 0.38 | -1.29 | -2.08 | -1.01 | 0.37 |
| RTY=F Asia | 19 | 5 | 26.3% | 60.0% | 0.4 | 0.11 | 1.9 | 2.01 | -2.23 | 1.12 | -0.08 |
| RTY=F London | 28 | 20 | 71.4% | 25.0% | -0.44 | -0.32 | 0.43 | -8.9 | -10.2 | -0.79 | -0.1 |
| RTY=F NY | 14 | 2 | 14.3% | 50.0% | -0.1 | -0.01 | 0.82 | -0.19 | -1.04 | -1.04 | 0.85 |
| YM=F Asia | 19 | 6 | 31.6% | 16.7% | -0.8 | -0.25 | 0.15 | -4.81 | -5.67 | -0.51 | -1.09 |
| YM=F London | 27 | 14 | 51.9% | 57.1% | 0.38 | 0.2 | 1.78 | 5.29 | -2.29 | 0.32 | 0.44 |
| YM=F NY | 14 | 2 | 14.3% | 50.0% | 1.16 | 0.17 | 3.24 | 2.31 | -1.03 | 3.35 | -1.03 |
| ZB=F Asia | 14 | 5 | 35.7% | 20.0% | -1.21 | -0.43 | 0.02 | -6.04 | -6.04 | -0.93 | -1.4 |
| ZB=F London | 11 | 6 | 54.5% | 33.3% | -0.41 | -0.22 | 0.54 | -2.43 | -3.38 | -0.39 | -0.42 |
| ZB=F NY | 14 | 6 | 42.9% | 66.7% | 0.6 | 0.26 | 2.23 | 3.62 | -1.6 | 0.58 | 0.63 |
| ZF=F Asia | 14 | 4 | 28.6% | 25.0% | -0.74 | -0.21 | 0.21 | -2.96 | -3.73 | -0.87 | -0.61 |
| ZF=F London | 19 | 12 | 63.2% | 25.0% | -1.1 | -0.7 | 0.2 | -13.21 | -13.21 | -1.84 | -0.36 |
| ZF=F NY | 13 | 6 | 46.2% | 50.0% | -0.72 | -0.33 | 0.14 | -4.31 | -4.64 | -0.53 | -0.9 |
| ZN=F Asia | 9 | 4 | 44.4% | 25.0% | -0.49 | -0.22 | 0.37 | -1.95 | -2.63 | -1.31 | 0.34 |
| ZN=F London | 12 | 7 | 58.3% | 28.6% | -0.7 | -0.41 | 0.36 | -4.88 | -4.88 | -0.59 | -0.78 |
| ZN=F NY | 7 | 5 | 71.4% | 40.0% | -0.31 | -0.22 | 0.54 | -1.53 | -1.81 | -0.77 | 0.0 |
| ZS=F Asia | 4 | 0 | 0.0% |  |  | 0.0 |  | 0.0 | 0.0 |  |  |
| ZS=F London | 17 | 5 | 29.4% | 20.0% | -1.13 | -0.33 | 0.05 | -5.67 | -5.67 | -1.33 | -1.0 |
| ZS=F NY | 10 | 1 | 10.0% | 0.0% | -1.32 | -0.13 | 0.0 | -1.32 | -1.32 |  | -1.32 |

## 2. New York session: by asset, side, time of day, risk size (systematic, qualified)

| Group | Setups | Triggered | Trigger rate | Win rate | Avg R | Expectancy R | Profit factor | Total R | Max DD R | 1st half avg R | 2nd half avg R |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ETF | 896 | 309 | 34.5% | 41.4% | -0.16 | -0.06 | 0.76 | -49.73 | -63.47 | -0.06 | -0.26 |
| Stock | 1853 | 489 | 26.4% | 42.9% | -0.02 | -0.01 | 0.96 | -9.8 | -41.36 | -0.07 | 0.03 |
| Future | 134 | 45 | 33.6% | 48.9% | 0.06 | 0.02 | 1.1 | 2.58 | -9.25 | 0.39 | -0.26 |
| Leveraged/inverse ETFs | 133 | 44 | 33.1% | 50.0% | 0.33 | 0.11 | 1.76 | 14.65 | -6.42 | 0.77 | -0.11 |
| LONG | 2559 | 769 | 30.1% | 42.9% | -0.07 | -0.02 | 0.89 | -51.03 | -85.82 | -0.07 | -0.07 |
| SHORT | 324 | 74 | 22.8% | 40.5% | -0.08 | -0.02 | 0.8 | -5.92 | -9.63 | -0.07 | -0.09 |
| Formed 10:00-10:30 | 301 | 145 | 48.2% | 32.4% | -0.25 | -0.12 | 0.65 | -36.37 | -37.77 | -0.32 | -0.19 |
| Formed 10:30-11:30 | 559 | 197 | 35.2% | 43.1% | -0.11 | -0.04 | 0.8 | -22.61 | -33.43 | -0.22 | -0.01 |
| Formed 11:30-13:00 | 803 | 254 | 31.6% | 49.2% | 0.02 | 0.01 | 1.04 | 5.42 | -13.55 | 0.05 | -0.01 |
| Formed 13:00-14:30 | 720 | 191 | 26.5% | 40.3% | -0.07 | -0.02 | 0.88 | -14.25 | -34.2 | -0.2 | 0.05 |
| Formed 14:30-16:00 | 500 | 56 | 11.2% | 46.4% | 0.19 | 0.02 | 1.33 | 10.85 | -16.45 | 0.66 | -0.27 |
| Risk 0-0.15% of price | 590 | 284 | 48.1% | 33.5% | -0.41 | -0.2 | 0.53 | -117.3 | -117.37 | -0.51 | -0.32 |
| Risk 0.15-0.3% of price | 643 | 239 | 37.2% | 41.4% | -0.09 | -0.03 | 0.86 | -20.49 | -45.15 | -0.15 | -0.03 |
| Risk 0.3-0.6% of price | 1019 | 279 | 27.4% | 45.5% | 0.06 | 0.02 | 1.12 | 17.37 | -20.24 | 0.06 | 0.06 |
| Risk 0.6%+ | 975 | 208 | 21.3% | 45.2% | 0.07 | 0.02 | 1.16 | 15.46 | -13.25 | 0.1 | 0.05 |

## 2b. Short guardrails (systematic; shorts use full exit at T1, breakeven at +0.5R, 60-minute time stop)

Sizing: longs 1.25% risk (cap 5.0% of account), shorts 0.5% risk (cap 2.5%). Results here are in R, before sizing.

| Group | Setups | Triggered | Trigger rate | Win rate | Avg R | Expectancy R | Profit factor | Total R | Max DD R | 1st half avg R | 2nd half avg R |
|---|---|---|---|---|---|---|---|---|---|---|---|
| Longs passing the normal filters | 2902 | 936 | 32.3% | 41.1% | -0.11 | -0.03 | 0.84 | -99.04 | -129.84 | -0.09 | -0.12 |
| Shorts passing the normal filters (before guardrails) | 2080 | 733 | 35.2% | 27.4% | -0.17 | -0.06 | 0.65 | -128.08 | -130.61 | -0.07 | -0.28 |
| Shorts passing every guardrail (traded) | 325 | 74 | 22.8% | 40.5% | -0.08 | -0.02 | 0.8 | -5.92 | -9.63 | -0.07 | -0.09 |
| Shorts passing: bearish daily trend | 893 | 328 | 36.7% | 29.3% | -0.2 | -0.08 | 0.6 | -67.17 | -74.37 | -0.11 | -0.3 |
| Shorts failing: bearish daily trend | 1187 | 405 | 34.1% | 25.9% | -0.15 | -0.05 | 0.68 | -60.91 | -62.26 | -0.08 | -0.22 |
| Shorts passing: PDH or 2+ level sweep | 1486 | 493 | 33.2% | 29.0% | -0.12 | -0.04 | 0.74 | -57.42 | -59.94 | -0.04 | -0.2 |
| Shorts failing: PDH or 2+ level sweep | 594 | 240 | 40.4% | 24.2% | -0.29 | -0.12 | 0.51 | -70.66 | -73.01 | -0.27 | -0.32 |
| Shorts passing: R:R to T2 3.0+ | 1518 | 533 | 35.1% | 27.4% | -0.18 | -0.06 | 0.64 | -97.52 | -101.67 | -0.08 | -0.29 |
| Shorts failing: R:R to T2 3.0+ | 562 | 200 | 35.6% | 27.5% | -0.15 | -0.05 | 0.67 | -30.56 | -38.04 | -0.08 | -0.23 |
| Shorts passing: risk 0.3%+ of price | 1120 | 329 | 29.4% | 31.6% | -0.04 | -0.01 | 0.9 | -12.81 | -24.94 | 0.06 | -0.14 |
| Shorts failing: risk 0.3%+ of price | 960 | 404 | 42.1% | 24.0% | -0.29 | -0.12 | 0.52 | -115.26 | -116.43 | -0.23 | -0.34 |
| Shorts passing: formed 10:30 or later | 1842 | 610 | 33.1% | 26.7% | -0.19 | -0.06 | 0.62 | -116.67 | -117.77 | -0.1 | -0.28 |
| Shorts failing: formed 10:30 or later | 238 | 123 | 51.7% | 30.9% | -0.09 | -0.05 | 0.78 | -11.41 | -19.89 | 0.14 | -0.32 |
| Shorts passing: not a leveraged ETF | 1994 | 707 | 35.5% | 27.0% | -0.19 | -0.07 | 0.61 | -136.71 | -137.87 | -0.1 | -0.29 |
| Shorts failing: not a leveraged ETF | 86 | 26 | 30.2% | 38.5% | 0.33 | 0.1 | 2.07 | 8.63 | -2.49 | 0.81 | -0.14 |

## 3. Outcomes (systematic, qualified)

| Outcome | Count | Share | Avg R |
|---|---|---|---|
| Not triggered (ran to T1 first) | 2039 | 63.2% | 0.0 |
| Stop | 486 | 15.1% | -1.22 |
| EOD exit | 202 | 6.3% | 0.21 |
| Not triggered (cutoff) | 178 | 5.5% | 0.0 |
| T1 then EOD | 138 | 4.3% | 1.83 |
| T1 then breakeven | 72 | 2.2% | 0.58 |
| T1 then T2 | 72 | 2.2% | 1.98 |
| Time stop | 24 | 0.7% | 0.44 |
| Breakeven stop | 16 | 0.5% | -0.1 |

## 4. Score calibration. A useful score shows results improving band by band.

| Group | Setups | Triggered | Trigger rate | Win rate | Avg R | Expectancy R | Profit factor | Total R | Max DD R | 1st half avg R | 2nd half avg R |
|---|---|---|---|---|---|---|---|---|---|---|---|
| Score 90+ | 20 | 12 | 60.0% | 75.0% | 0.92 | 0.55 | 6.01 | 11.09 | -2.22 | 1.18 | 0.67 |
| Score 75-89 | 1231 | 365 | 29.7% | 39.7% | -0.14 | -0.04 | 0.79 | -49.52 | -74.93 | -0.14 | -0.13 |
| Score 60-74 | 1763 | 540 | 30.6% | 42.4% | -0.07 | -0.02 | 0.9 | -35.1 | -53.11 | -0.01 | -0.12 |
| Score under 60 | 213 | 93 | 43.7% | 34.4% | -0.34 | -0.15 | 0.58 | -31.42 | -34.07 | -0.63 | -0.05 |

## 5. Factor attribution (all triggered systematic setups, qualified or not)

| Factor | Weight key | Weight | With | Avg R with | Without | Avg R without | Difference | Read |
|---|---|---|---|---|---|---|---|---|
| Prior-day level swept | sweep_pd | 20 | 2551 | -0.11 | 2889 | -0.15 | 0.04 | No clear effect |
| Only PM/OR level swept | sweep_other | 15 | 2295 | -0.13 | 3145 | -0.14 | 0.0 | No clear effect |
| FVG in discount/premium | zone | 10 | 1971 | -0.16 | 3469 | -0.12 | -0.05 | No clear effect |
| FVG overlaps OTE | ote | 15 | 1734 | -0.14 | 3706 | -0.13 | -0.01 | No clear effect |
| R:R to T1 of 2 or more | rr | 10 | 407 | -0.26 | 5033 | -0.13 | -0.14 | No clear effect |
| HTF bias aligned | bias | 10 | 2077 | -0.14 | 3363 | -0.13 | -0.01 | No clear effect |
| Displacement volume 1.5x+ | vol | 5 | 652 | -0.1 | 4788 | -0.14 | 0.04 | No clear effect |
| Formed 10:00-11:30 | time | 5 | 2545 | -0.18 | 2895 | -0.09 | -0.09 | No clear effect |

## 6. Filter check (systematic)

| Group | Setups | Triggered | Trigger rate | Win rate | Avg R | Expectancy R | Profit factor | Total R | Max DD R | 1st half avg R | 2nd half avg R |
|---|---|---|---|---|---|---|---|---|---|---|---|
| Passed filters | 3227 | 1010 | 31.3% | 41.1% | -0.1 | -0.03 | 0.84 | -104.96 | -135.21 | -0.08 | -0.13 |
| Filtered out | 7391 | 4430 | 59.9% | 47.8% | -0.14 | -0.09 | 0.62 | -631.68 | -631.89 | -0.1 | -0.18 |
| No OTE overlap | 5497 | 3706 | 67.4% | 52.1% | -0.13 | -0.09 | 0.62 | -490.11 | -490.33 | -0.11 | -0.16 |
| OTE overlap, R:R to T2 1.5-2 | 139 | 65 | 46.8% | 29.2% | -0.3 | -0.14 | 0.5 | -19.41 | -19.76 | -0.24 | -0.36 |
| OTE overlap, R:R to T2 2-2.5 | 1138 | 334 | 29.3% | 36.5% | -0.13 | -0.04 | 0.76 | -44.59 | -55.24 | -0.11 | -0.16 |
| OTE overlap, R:R to T2 2.5-3 | 582 | 185 | 31.8% | 37.8% | -0.01 | -0.0 | 0.98 | -1.74 | -43.27 | -0.23 | 0.21 |
| OTE overlap, R:R to T2 3+ | 3262 | 1150 | 35.3% | 34.3% | -0.16 | -0.06 | 0.74 | -180.78 | -218.32 | -0.05 | -0.26 |

## 7. Improvement tests: entry type x stop buffer x filter (net of costs)

ote_mid = current entry (middle of the FVG/OTE overlap); fvg_edge = first touch of the gap; fvg_ce = gap midpoint; blend = halfway between the gap edge and ote_mid; ote_62 = first touch of the OTE zone. Scaled rows are in R of the full planned position (a partial fill counts only what filled).

| Group | Setups | Triggered | Trigger rate | Win rate | Avg R | Expectancy R | Profit factor | Total R | Max DD R | 1st half avg R | 2nd half avg R |
|---|---|---|---|---|---|---|---|---|---|---|---|
| Entry ote_mid, stop 0.1 ATR · All qualified | 3227 | 1010 | 31.3% | 41.1% | -0.1 | -0.03 | 0.84 | -104.95 | -135.19 | -0.08 | -0.13 |
| Entry ote_mid, stop 0.1 ATR · Plan window (by 11:30) | 904 | 354 | 39.2% | 39.0% | -0.17 | -0.07 | 0.74 | -58.77 | -63.51 | -0.24 | -0.09 |
| Entry ote_mid, stop 0.1 ATR · Midday 11:30-14:30 | 1523 | 445 | 29.2% | 45.4% | -0.02 | -0.01 | 0.97 | -8.82 | -35.77 | -0.04 | 0.0 |
| Entry ote_mid, stop 0.1 ATR · Stocks only | 1853 | 489 | 26.4% | 42.9% | -0.02 | -0.01 | 0.96 | -9.8 | -41.36 | -0.07 | 0.03 |
| Entry ote_mid, stop 0.1 ATR · R:R to T2 2.5+ | 2431 | 799 | 32.9% | 40.8% | -0.11 | -0.04 | 0.82 | -91.6 | -128.51 | -0.07 | -0.15 |
| Entry ote_mid, stop 0.1 ATR · Risk 0.15%+ | 2637 | 726 | 27.5% | 44.1% | 0.02 | 0.0 | 1.03 | 12.35 | -51.41 | 0.02 | 0.02 |
| Entry ote_mid, stop 0.1 ATR · Midday + R:R 2.5+ + risk 0.15%+ | 1027 | 316 | 30.8% | 46.8% | 0.06 | 0.02 | 1.12 | 19.99 | -22.62 | 0.05 | 0.08 |
| Entry ote_mid, stop 0.3 ATR · All qualified | 3227 | 1010 | 31.3% | 44.2% | -0.08 | -0.03 | 0.86 | -84.09 | -111.22 | -0.06 | -0.11 |
| Entry ote_mid, stop 0.3 ATR · Plan window (by 11:30) | 904 | 354 | 39.2% | 42.1% | -0.15 | -0.06 | 0.74 | -53.41 | -57.39 | -0.23 | -0.08 |
| Entry ote_mid, stop 0.3 ATR · Midday 11:30-14:30 | 1523 | 445 | 29.2% | 48.5% | 0.0 | 0.0 | 1.0 | 0.75 | -26.45 | 0.01 | -0.01 |
| Entry ote_mid, stop 0.3 ATR · Stocks only | 1853 | 489 | 26.4% | 46.2% | -0.02 | -0.0 | 0.97 | -7.36 | -38.05 | -0.03 | -0.0 |
| Entry ote_mid, stop 0.3 ATR · R:R to T2 2.5+ | 2431 | 799 | 32.9% | 44.4% | -0.08 | -0.03 | 0.86 | -65.7 | -98.84 | -0.04 | -0.12 |
| Entry ote_mid, stop 0.3 ATR · Risk 0.15%+ | 2637 | 726 | 27.5% | 47.2% | 0.03 | 0.01 | 1.06 | 20.99 | -36.54 | 0.04 | 0.02 |
| Entry ote_mid, stop 0.3 ATR · Midday + R:R 2.5+ + risk 0.15%+ | 1027 | 316 | 30.8% | 50.6% | 0.09 | 0.03 | 1.19 | 28.23 | -17.07 | 0.12 | 0.06 |
| Entry fvg_edge, stop 0.1 ATR · All qualified | 3227 | 1345 | 41.7% | 50.4% | -0.08 | -0.03 | 0.82 | -109.46 | -131.96 | -0.09 | -0.07 |
| Entry fvg_edge, stop 0.1 ATR · Plan window (by 11:30) | 904 | 452 | 50.0% | 50.2% | -0.13 | -0.06 | 0.72 | -57.79 | -60.07 | -0.12 | -0.13 |
| Entry fvg_edge, stop 0.1 ATR · Midday 11:30-14:30 | 1523 | 605 | 39.7% | 51.7% | -0.06 | -0.02 | 0.86 | -37.59 | -48.04 | -0.07 | -0.05 |
| Entry fvg_edge, stop 0.1 ATR · Stocks only | 1853 | 661 | 35.7% | 49.9% | -0.08 | -0.03 | 0.81 | -54.51 | -65.85 | -0.11 | -0.05 |
| Entry fvg_edge, stop 0.1 ATR · R:R to T2 2.5+ | 2431 | 1044 | 42.9% | 49.8% | -0.1 | -0.04 | 0.8 | -101.52 | -120.22 | -0.11 | -0.08 |
| Entry fvg_edge, stop 0.1 ATR · Risk 0.15%+ | 2637 | 985 | 37.4% | 53.0% | -0.03 | -0.01 | 0.93 | -28.64 | -67.32 | -0.01 | -0.05 |
| Entry fvg_edge, stop 0.1 ATR · Midday + R:R 2.5+ + risk 0.15%+ | 1027 | 411 | 40.0% | 52.1% | -0.05 | -0.02 | 0.87 | -22.23 | -31.79 | -0.02 | -0.09 |
| Entry fvg_edge, stop 0.3 ATR · All qualified | 3227 | 1345 | 41.7% | 52.7% | -0.06 | -0.03 | 0.84 | -86.96 | -110.47 | -0.06 | -0.06 |
| Entry fvg_edge, stop 0.3 ATR · Plan window (by 11:30) | 904 | 452 | 50.0% | 52.4% | -0.12 | -0.06 | 0.72 | -52.85 | -54.08 | -0.11 | -0.12 |
| Entry fvg_edge, stop 0.3 ATR · Midday 11:30-14:30 | 1523 | 605 | 39.7% | 54.0% | -0.04 | -0.02 | 0.89 | -25.77 | -36.33 | -0.04 | -0.05 |
| Entry fvg_edge, stop 0.3 ATR · Stocks only | 1853 | 661 | 35.7% | 52.5% | -0.07 | -0.02 | 0.84 | -43.59 | -54.94 | -0.08 | -0.05 |
| Entry fvg_edge, stop 0.3 ATR · R:R to T2 2.5+ | 2431 | 1044 | 42.9% | 52.7% | -0.07 | -0.03 | 0.83 | -74.34 | -95.31 | -0.07 | -0.07 |
| Entry fvg_edge, stop 0.3 ATR · Risk 0.15%+ | 2637 | 985 | 37.4% | 55.3% | -0.01 | -0.01 | 0.96 | -13.7 | -52.06 | 0.01 | -0.04 |
| Entry fvg_edge, stop 0.3 ATR · Midday + R:R 2.5+ + risk 0.15%+ | 1027 | 411 | 40.0% | 55.0% | -0.02 | -0.01 | 0.94 | -9.74 | -22.64 | 0.03 | -0.08 |
| Entry fvg_ce, stop 0.1 ATR · All qualified | 3227 | 1109 | 34.4% | 43.9% | -0.11 | -0.04 | 0.8 | -124.29 | -140.72 | -0.11 | -0.11 |
| Entry fvg_ce, stop 0.1 ATR · Plan window (by 11:30) | 904 | 387 | 42.8% | 43.7% | -0.15 | -0.06 | 0.73 | -58.36 | -61.99 | -0.18 | -0.12 |
| Entry fvg_ce, stop 0.1 ATR · Midday 11:30-14:30 | 1523 | 494 | 32.4% | 46.8% | -0.06 | -0.02 | 0.89 | -29.13 | -43.12 | -0.07 | -0.05 |
| Entry fvg_ce, stop 0.1 ATR · Stocks only | 1853 | 540 | 29.1% | 45.2% | -0.06 | -0.02 | 0.88 | -32.47 | -52.09 | -0.1 | -0.02 |
| Entry fvg_ce, stop 0.1 ATR · R:R to T2 2.5+ | 2431 | 870 | 35.8% | 43.3% | -0.12 | -0.04 | 0.8 | -100.07 | -123.85 | -0.11 | -0.12 |
| Entry fvg_ce, stop 0.1 ATR · Risk 0.15%+ | 2637 | 803 | 30.5% | 46.6% | -0.02 | -0.01 | 0.96 | -14.75 | -58.75 | -0.02 | -0.02 |
| Entry fvg_ce, stop 0.1 ATR · Midday + R:R 2.5+ + risk 0.15%+ | 1027 | 345 | 33.6% | 47.8% | -0.01 | -0.0 | 0.97 | -4.18 | -24.3 | 0.02 | -0.04 |
| Entry fvg_ce, stop 0.3 ATR · All qualified | 3227 | 1109 | 34.4% | 46.7% | -0.09 | -0.03 | 0.83 | -99.43 | -114.78 | -0.08 | -0.1 |
| Entry fvg_ce, stop 0.3 ATR · Plan window (by 11:30) | 904 | 387 | 42.8% | 46.3% | -0.14 | -0.06 | 0.73 | -53.18 | -55.05 | -0.17 | -0.1 |
| Entry fvg_ce, stop 0.3 ATR · Midday 11:30-14:30 | 1523 | 494 | 32.4% | 49.8% | -0.03 | -0.01 | 0.93 | -15.78 | -29.74 | -0.01 | -0.06 |
| Entry fvg_ce, stop 0.3 ATR · Stocks only | 1853 | 540 | 29.1% | 48.1% | -0.05 | -0.01 | 0.9 | -25.04 | -43.47 | -0.05 | -0.04 |
| Entry fvg_ce, stop 0.3 ATR · R:R to T2 2.5+ | 2431 | 870 | 35.8% | 46.8% | -0.08 | -0.03 | 0.84 | -71.66 | -93.89 | -0.07 | -0.1 |
| Entry fvg_ce, stop 0.3 ATR · Risk 0.15%+ | 2637 | 803 | 30.5% | 49.4% | -0.0 | -0.0 | 1.0 | -1.08 | -40.93 | 0.01 | -0.02 |
| Entry fvg_ce, stop 0.3 ATR · Midday + R:R 2.5+ + risk 0.15%+ | 1027 | 345 | 33.6% | 51.6% | 0.02 | 0.01 | 1.06 | 8.59 | -16.67 | 0.08 | -0.03 |
| Entry blend, stop 0.1 ATR · All qualified | 3227 | 1154 | 35.8% | 45.3% | -0.11 | -0.04 | 0.81 | -121.3 | -140.19 | -0.1 | -0.11 |
| Entry blend, stop 0.1 ATR · Plan window (by 11:30) | 904 | 400 | 44.2% | 44.8% | -0.16 | -0.07 | 0.71 | -62.62 | -66.1 | -0.18 | -0.13 |
| Entry blend, stop 0.1 ATR · Midday 11:30-14:30 | 1523 | 517 | 33.9% | 48.0% | -0.05 | -0.02 | 0.9 | -25.74 | -40.86 | -0.06 | -0.04 |
| Entry blend, stop 0.1 ATR · Stocks only | 1853 | 564 | 30.4% | 45.4% | -0.08 | -0.02 | 0.85 | -43.4 | -57.3 | -0.12 | -0.03 |
| Entry blend, stop 0.1 ATR · R:R to T2 2.5+ | 2431 | 906 | 37.3% | 44.7% | -0.12 | -0.04 | 0.79 | -105.78 | -130.48 | -0.1 | -0.13 |
| Entry blend, stop 0.1 ATR · Risk 0.15%+ | 2637 | 840 | 31.9% | 47.9% | -0.02 | -0.01 | 0.96 | -14.71 | -61.02 | 0.0 | -0.04 |
| Entry blend, stop 0.1 ATR · Midday + R:R 2.5+ + risk 0.15%+ | 1027 | 355 | 34.6% | 48.2% | -0.03 | -0.01 | 0.94 | -9.74 | -24.13 | 0.01 | -0.06 |
| Entry blend, stop 0.3 ATR · All qualified | 3227 | 1154 | 35.8% | 47.9% | -0.08 | -0.03 | 0.83 | -97.67 | -115.02 | -0.07 | -0.1 |
| Entry blend, stop 0.3 ATR · Plan window (by 11:30) | 904 | 400 | 44.2% | 47.2% | -0.14 | -0.06 | 0.72 | -56.95 | -59.08 | -0.17 | -0.11 |
| Entry blend, stop 0.3 ATR · Midday 11:30-14:30 | 1523 | 517 | 33.9% | 50.7% | -0.03 | -0.01 | 0.94 | -13.63 | -29.81 | -0.0 | -0.05 |
| Entry blend, stop 0.3 ATR · Stocks only | 1853 | 564 | 30.4% | 48.0% | -0.06 | -0.02 | 0.87 | -34.99 | -50.19 | -0.07 | -0.05 |
| Entry blend, stop 0.3 ATR · R:R to T2 2.5+ | 2431 | 906 | 37.3% | 47.9% | -0.09 | -0.03 | 0.83 | -77.98 | -101.08 | -0.06 | -0.11 |
| Entry blend, stop 0.3 ATR · Risk 0.15%+ | 2637 | 840 | 31.9% | 50.5% | -0.0 | -0.0 | 1.0 | -1.42 | -43.44 | 0.02 | -0.03 |
| Entry blend, stop 0.3 ATR · Midday + R:R 2.5+ + risk 0.15%+ | 1027 | 355 | 34.6% | 51.5% | 0.01 | 0.0 | 1.02 | 2.76 | -17.84 | 0.07 | -0.05 |
| Entry ote_62, stop 0.1 ATR · All qualified | 3227 | 1100 | 34.1% | 43.9% | -0.09 | -0.03 | 0.85 | -93.69 | -124.9 | -0.09 | -0.08 |
| Entry ote_62, stop 0.1 ATR · Plan window (by 11:30) | 904 | 377 | 41.7% | 41.9% | -0.15 | -0.06 | 0.75 | -55.86 | -58.85 | -0.2 | -0.1 |
| Entry ote_62, stop 0.1 ATR · Midday 11:30-14:30 | 1523 | 490 | 32.2% | 46.5% | -0.02 | -0.01 | 0.95 | -11.99 | -38.99 | -0.05 | 0.01 |
| Entry ote_62, stop 0.1 ATR · Stocks only | 1853 | 536 | 28.9% | 44.2% | -0.04 | -0.01 | 0.92 | -22.12 | -47.69 | -0.07 | -0.01 |
| Entry ote_62, stop 0.1 ATR · R:R to T2 2.5+ | 2431 | 873 | 35.9% | 43.4% | -0.1 | -0.04 | 0.83 | -85.9 | -118.83 | -0.08 | -0.11 |
| Entry ote_62, stop 0.1 ATR · Risk 0.15%+ | 2637 | 789 | 29.9% | 45.9% | 0.0 | 0.0 | 1.0 | 1.01 | -58.52 | 0.01 | -0.01 |
| Entry ote_62, stop 0.1 ATR · Midday + R:R 2.5+ + risk 0.15%+ | 1027 | 339 | 33.0% | 46.6% | 0.01 | 0.0 | 1.03 | 4.58 | -22.42 | 0.03 | 0.0 |
| Entry ote_62, stop 0.3 ATR · All qualified | 3227 | 1100 | 34.1% | 46.8% | -0.07 | -0.02 | 0.87 | -72.38 | -101.52 | -0.06 | -0.07 |
| Entry ote_62, stop 0.3 ATR · Plan window (by 11:30) | 904 | 377 | 41.7% | 44.8% | -0.13 | -0.06 | 0.75 | -50.69 | -54.34 | -0.19 | -0.08 |
| Entry ote_62, stop 0.3 ATR · Midday 11:30-14:30 | 1523 | 490 | 32.2% | 49.4% | -0.01 | -0.0 | 0.99 | -2.86 | -27.85 | 0.0 | -0.01 |
| Entry ote_62, stop 0.3 ATR · Stocks only | 1853 | 536 | 28.9% | 47.4% | -0.03 | -0.01 | 0.94 | -15.52 | -42.7 | -0.02 | -0.04 |
| Entry ote_62, stop 0.3 ATR · R:R to T2 2.5+ | 2431 | 873 | 35.9% | 46.8% | -0.07 | -0.02 | 0.87 | -59.55 | -90.51 | -0.04 | -0.09 |
| Entry ote_62, stop 0.3 ATR · Risk 0.15%+ | 2637 | 789 | 29.9% | 48.9% | 0.02 | 0.01 | 1.04 | 13.54 | -39.76 | 0.04 | -0.0 |
| Entry ote_62, stop 0.3 ATR · Midday + R:R 2.5+ + risk 0.15%+ | 1027 | 339 | 33.0% | 50.1% | 0.04 | 0.01 | 1.09 | 13.83 | -15.96 | 0.1 | -0.02 |
| Scaled ladder_equal (fvg_edge 33%, blend 33%, ote_mid 33%) · All qualified | 3227 | 1345 | 41.7% | 51.2% | -0.08 | -0.03 | 0.82 | -111.8 | -131.08 | -0.08 | -0.09 |
| Scaled ladder_equal (fvg_edge 33%, blend 33%, ote_mid 33%) · Plan window (by 11:30) | 904 | 452 | 50.0% | 50.4% | -0.13 | -0.07 | 0.72 | -59.43 | -62.28 | -0.13 | -0.13 |
| Scaled ladder_equal (fvg_edge 33%, blend 33%, ote_mid 33%) · Midday 11:30-14:30 | 1523 | 605 | 39.7% | 53.9% | -0.04 | -0.02 | 0.9 | -25.9 | -40.48 | -0.06 | -0.03 |
| Scaled ladder_equal (fvg_edge 33%, blend 33%, ote_mid 33%) · Stocks only | 1853 | 661 | 35.7% | 51.6% | -0.06 | -0.02 | 0.86 | -38.29 | -54.53 | -0.08 | -0.03 |
| Scaled ladder_equal (fvg_edge 33%, blend 33%, ote_mid 33%) · R:R to T2 2.5+ | 2431 | 1044 | 42.9% | 50.7% | -0.1 | -0.04 | 0.8 | -99.37 | -124.48 | -0.09 | -0.1 |
| Scaled ladder_equal (fvg_edge 33%, blend 33%, ote_mid 33%) · Risk 0.15%+ | 2637 | 985 | 37.4% | 53.9% | -0.01 | -0.0 | 0.97 | -12.39 | -60.12 | 0.01 | -0.03 |
| Scaled ladder_equal (fvg_edge 33%, blend 33%, ote_mid 33%) · Midday + R:R 2.5+ + risk 0.15%+ | 1027 | 411 | 40.0% | 54.0% | -0.02 | -0.01 | 0.96 | -6.7 | -21.93 | 0.01 | -0.04 |
| Scaled ladder_deep (fvg_edge 20%, blend 30%, ote_mid 50%) · All qualified | 3227 | 1345 | 41.7% | 51.5% | -0.08 | -0.03 | 0.82 | -110.88 | -132.45 | -0.07 | -0.09 |
| Scaled ladder_deep (fvg_edge 20%, blend 30%, ote_mid 50%) · Plan window (by 11:30) | 904 | 452 | 50.0% | 50.9% | -0.13 | -0.07 | 0.72 | -59.52 | -62.43 | -0.14 | -0.13 |
| Scaled ladder_deep (fvg_edge 20%, blend 30%, ote_mid 50%) · Midday 11:30-14:30 | 1523 | 605 | 39.7% | 54.2% | -0.04 | -0.01 | 0.92 | -21.57 | -38.06 | -0.05 | -0.02 |
| Scaled ladder_deep (fvg_edge 20%, blend 30%, ote_mid 50%) · Stocks only | 1853 | 661 | 35.7% | 52.2% | -0.05 | -0.02 | 0.89 | -31.35 | -50.6 | -0.07 | -0.02 |
| Scaled ladder_deep (fvg_edge 20%, blend 30%, ote_mid 50%) · R:R to T2 2.5+ | 2431 | 1044 | 42.9% | 50.7% | -0.09 | -0.04 | 0.81 | -97.62 | -125.72 | -0.08 | -0.1 |
| Scaled ladder_deep (fvg_edge 20%, blend 30%, ote_mid 50%) · Risk 0.15%+ | 2637 | 985 | 37.4% | 54.3% | -0.01 | -0.0 | 0.98 | -6.17 | -57.72 | 0.01 | -0.02 |
| Scaled ladder_deep (fvg_edge 20%, blend 30%, ote_mid 50%) · Midday + R:R 2.5+ + risk 0.15%+ | 1027 | 411 | 40.0% | 54.3% | -0.0 | -0.0 | 1.0 | -0.23 | -21.89 | 0.02 | -0.02 |

## 8. Trade management (systematic, qualified, triggered)

| Method | Trades | Avg R | Win rate |
|---|---|---|---|
| Plan: half at T1, rest to T2 (gross) | 1010 | 0.1 | 42.8% |
| Plan, net of costs | 1010 | -0.1 | 41.1% |
| Full position to T1 (gross) | 1010 | 0.11 | 43.2% |
| Full position to T2 (gross) | 1010 | 0.1 | 37.6% |

## 10. v3 candidate tests (New York session, qualified, net of costs)

Confirmation entry = wait for price to reach the FVG, then enter on the first bar that closes beyond the prior 3 bars (bars used: {'1m': 2746, '5m': 134}). Runner = half at T1, rest to the close with a breakeven stop. 1st/2nd half columns are the out-of-sample check.

| Group | Setups | Triggered | Trigger rate | Win rate | Avg R | Expectancy R | Profit factor | Total R | Max DD R | 1st half avg R | 2nd half avg R |
|---|---|---|---|---|---|---|---|---|---|---|---|
| All (New York) · Current plan | 2883 | 843 | 29.2% | 42.7% | -0.07 | -0.02 | 0.89 | -56.95 | -91.11 | -0.07 | -0.06 |
| All (New York) · Runner to the close | 2883 | 843 | 29.2% | 42.7% | -0.06 | -0.02 | 0.9 | -53.14 | -88.16 | -0.04 | -0.08 |
| All (New York) · Full position to T2 | 2883 | 843 | 29.2% | 38.1% | -0.06 | -0.02 | 0.91 | -48.83 | -104.65 | -0.07 | -0.04 |
| All (New York) · Confirmation entry | 2883 | 932 | 32.3% | 52.8% | -0.09 | -0.03 | 0.76 | -83.5 | -92.0 | -0.13 | -0.05 |
| v3: 11:30-14:30 + risk 0.3%+ + FVG 0.5+ ATR · Current plan | 744 | 142 | 19.1% | 50.0% | 0.14 | 0.03 | 1.32 | 20.48 | -11.92 | 0.12 | 0.17 |
| v3: 11:30-14:30 + risk 0.3%+ + FVG 0.5+ ATR · Runner to the close | 744 | 142 | 19.1% | 50.0% | 0.13 | 0.02 | 1.29 | 18.44 | -11.87 | 0.12 | 0.14 |
| v3: 11:30-14:30 + risk 0.3%+ + FVG 0.5+ ATR · Full position to T2 | 744 | 142 | 19.1% | 47.2% | 0.17 | 0.03 | 1.32 | 23.88 | -13.33 | 0.14 | 0.2 |
| v3: 11:30-14:30 + risk 0.3%+ + FVG 0.5+ ATR · Confirmation entry | 744 | 196 | 26.3% | 58.2% | 0.06 | 0.01 | 1.2 | 10.89 | -7.51 | 0.07 | 0.04 |
| v3 + longs · Current plan | 609 | 107 | 17.6% | 55.1% | 0.28 | 0.05 | 1.64 | 29.85 | -8.18 | 0.22 | 0.34 |
| v3 + longs · Runner to the close | 609 | 107 | 17.6% | 55.1% | 0.26 | 0.05 | 1.6 | 27.82 | -8.13 | 0.22 | 0.3 |
| v3 + longs · Full position to T2 | 609 | 107 | 17.6% | 50.5% | 0.28 | 0.05 | 1.58 | 29.59 | -8.1 | 0.22 | 0.33 |
| v3 + longs · Confirmation entry | 609 | 160 | 26.3% | 60.0% | 0.09 | 0.02 | 1.34 | 14.68 | -6.21 | 0.12 | 0.06 |
| v3 + VWAP side · Current plan | 569 | 84 | 14.8% | 52.4% | 0.11 | 0.02 | 1.26 | 9.53 | -5.89 | 0.08 | 0.15 |
| v3 + VWAP side · Runner to the close | 569 | 84 | 14.8% | 52.4% | 0.09 | 0.01 | 1.21 | 7.49 | -5.85 | 0.08 | 0.1 |
| v3 + VWAP side · Full position to T2 | 569 | 84 | 14.8% | 50.0% | 0.13 | 0.02 | 1.26 | 10.7 | -8.65 | 0.02 | 0.23 |
| v3 + VWAP side · Confirmation entry | 569 | 126 | 22.1% | 54.8% | 0.04 | 0.01 | 1.15 | 5.28 | -6.91 | 0.05 | 0.03 |
| v3 + in play (open volume 1.5x+) · Current plan | 110 | 21 | 19.1% | 42.9% | 0.05 | 0.01 | 1.11 | 0.95 | -3.73 | -0.1 | 0.18 |
| v3 + in play (open volume 1.5x+) · Runner to the close | 110 | 21 | 19.1% | 42.9% | 0.05 | 0.01 | 1.11 | 0.95 | -3.73 | -0.1 | 0.18 |
| v3 + in play (open volume 1.5x+) · Full position to T2 | 110 | 21 | 19.1% | 42.9% | -0.1 | -0.02 | 0.8 | -2.05 | -4.62 | -0.1 | -0.1 |
| v3 + in play (open volume 1.5x+) · Confirmation entry | 110 | 27 | 24.5% | 59.3% | 0.05 | 0.01 | 1.15 | 1.39 | -2.61 | 0.02 | 0.08 |
| v3 + longs + VWAP side · Current plan | 481 | 68 | 14.1% | 54.4% | 0.21 | 0.03 | 1.48 | 14.1 | -5.26 | 0.14 | 0.28 |
| v3 + longs + VWAP side · Runner to the close | 481 | 68 | 14.1% | 54.4% | 0.18 | 0.03 | 1.41 | 12.06 | -5.26 | 0.14 | 0.22 |
| v3 + longs + VWAP side · Full position to T2 | 481 | 68 | 14.1% | 52.9% | 0.26 | 0.04 | 1.59 | 17.83 | -5.56 | 0.16 | 0.36 |
| v3 + longs + VWAP side · Confirmation entry | 481 | 107 | 22.2% | 55.1% | 0.05 | 0.01 | 1.19 | 5.67 | -7.31 | 0.08 | 0.03 |
| VWAP side only · Current plan | 1973 | 521 | 26.4% | 42.2% | -0.12 | -0.03 | 0.81 | -60.11 | -77.81 | -0.13 | -0.1 |
| VWAP side only · Runner to the close | 1973 | 521 | 26.4% | 42.2% | -0.11 | -0.03 | 0.81 | -59.7 | -74.19 | -0.09 | -0.14 |
| VWAP side only · Full position to T2 | 1973 | 521 | 26.4% | 38.6% | -0.11 | -0.03 | 0.83 | -55.59 | -85.9 | -0.13 | -0.09 |
| VWAP side only · Confirmation entry | 1973 | 602 | 30.5% | 52.2% | -0.1 | -0.03 | 0.73 | -61.43 | -73.94 | -0.12 | -0.08 |
| In play only · Current plan | 355 | 94 | 26.5% | 34.0% | -0.29 | -0.08 | 0.57 | -27.51 | -32.79 | -0.46 | -0.13 |
| In play only · Runner to the close | 355 | 94 | 26.5% | 34.0% | -0.3 | -0.08 | 0.55 | -28.52 | -33.9 | -0.46 | -0.15 |
| In play only · Full position to T2 | 355 | 94 | 26.5% | 30.9% | -0.38 | -0.1 | 0.49 | -35.41 | -41.0 | -0.53 | -0.22 |
| In play only · Confirmation entry | 355 | 110 | 31.0% | 54.5% | -0.11 | -0.03 | 0.74 | -11.83 | -23.63 | -0.23 | 0.02 |

## 9. Automatic changes in this run

| Key | Old | New | Evidence |
|---|---|---|---|
| None |  |  |  |
