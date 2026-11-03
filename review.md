# FVG review: 2026-11-03 18:49 ET (Backtest)

Sessions: 49 (2026-08-26 to 2026-11-03). Config version 1.

## 1. Strategy performance (qualified setups; results net of costs)

Costs: 0.02% of price per side. Entries allowed until 15:30 ET.

| Group | Setups | Triggered | Trigger rate | Win rate | Avg R | Expectancy R | Profit factor | Total R | Max DD R | 1st half avg R | 2nd half avg R |
|---|---|---|---|---|---|---|---|---|---|---|---|
| Live dashboard snapshots | 28 | 7 | 25.0% | 42.9% | -0.06 | -0.01 | 0.92 | -0.4 | -4.34 | -0.56 | 0.32 |
| Daily full-session replays | 50 | 14 | 28.0% | 14.3% | -0.87 | -0.24 | 0.16 | -12.22 | -13.92 | -1.17 | -0.58 |
| Backtest | 477 | 210 | 44.0% | 31.9% | -0.57 | -0.25 | 0.44 | -119.03 | -119.6 | -0.68 | -0.45 |
| Systematic (replays + backtest) | 527 | 224 | 42.5% | 30.8% | -0.59 | -0.25 | 0.42 | -131.25 | -133.52 | -0.69 | -0.48 |
| Systematic, before cost (gross) | 527 | 224 | 42.5% | 38.4% | 0.04 | 0.02 | 1.07 | 8.37 | -19.83 | 0.05 | 0.03 |
| Systematic, plan window only (New York, formed by 11:30) | 79 | 39 | 49.4% | 25.6% | -0.48 | -0.24 | 0.45 | -18.74 | -19.9 | -0.06 | -0.88 |
| Live top-5 suggestions only | 17 | 4 | 23.5% | 25.0% | -0.4 | -0.09 | 0.54 | -1.61 | -3.49 | -1.13 | 0.32 |
| Your actual trades | 1 | 1 |  | 0.0% | -1.77 |  |  | -1.77 |  |  |  |
| Stocks and ETFs, New York session only | 50 | 14 | 28.0% | 14.3% | -0.87 | -0.24 | 0.16 | -12.22 | -13.92 | -1.17 | -0.58 |
| Futures, New York session | 134 | 45 | 33.6% | 42.2% | -0.12 | -0.04 | 0.83 | -5.26 | -11.28 | 0.19 | -0.41 |
| Futures, all 24-hour sessions | 477 | 210 | 44.0% | 31.9% | -0.57 | -0.25 | 0.44 | -119.03 | -119.6 | -0.68 | -0.45 |

## 1c. Futures by session (24-hour test; qualified, net of costs)

Asia and London use their own levels: prior-day high/low, the previous session's high/low, and the session's first 30 minutes.

| Group | Setups | Triggered | Trigger rate | Win rate | Avg R | Expectancy R | Profit factor | Total R | Max DD R | 1st half avg R | 2nd half avg R |
|---|---|---|---|---|---|---|---|---|---|---|---|
| Futures, Asia session (6 PM-midnight ET) | 161 | 70 | 43.5% | 25.7% | -0.69 | -0.3 | 0.37 | -48.29 | -48.86 | -0.63 | -0.75 |
| Futures, London session (2-8 AM ET) | 182 | 95 | 52.2% | 31.6% | -0.69 | -0.36 | 0.37 | -65.48 | -65.48 | -1.15 | -0.24 |
| Futures, NY session (9:30-4:00 ET) | 134 | 45 | 33.6% | 42.2% | -0.12 | -0.04 | 0.83 | -5.26 | -11.28 | 0.19 | -0.41 |
| CL=F Asia | 22 | 12 | 54.5% | 50.0% | 0.36 | 0.2 | 1.6 | 4.32 | -2.54 | -0.32 | 1.04 |
| CL=F London | 20 | 8 | 40.0% | 50.0% | 0.33 | 0.13 | 1.68 | 2.65 | -2.29 | -0.39 | 1.05 |
| CL=F NY | 20 | 7 | 35.0% | 28.6% | -0.41 | -0.14 | 0.48 | -2.89 | -3.26 | -1.09 | 0.09 |
| ES=F Asia | 15 | 6 | 40.0% | 16.7% | -1.13 | -0.45 | 0.15 | -6.79 | -8.02 | -0.31 | -1.95 |
| ES=F London | 19 | 12 | 63.2% | 25.0% | -0.88 | -0.55 | 0.33 | -10.53 | -12.86 | -2.11 | 0.36 |
| ES=F NY | 17 | 8 | 47.1% | 62.5% | 0.59 | 0.28 | 3.33 | 4.71 | -1.87 | 0.89 | 0.29 |
| GC=F Asia | 33 | 22 | 66.7% | 27.3% | -0.4 | -0.27 | 0.58 | -8.77 | -14.02 | -0.18 | -0.62 |
| GC=F London | 15 | 6 | 40.0% | 50.0% | 0.08 | 0.03 | 1.18 | 0.48 | -1.47 | -0.2 | 0.36 |
| GC=F NY | 14 | 4 | 28.6% | 50.0% | 0.1 | 0.03 | 1.16 | 0.4 | -1.24 | 0.45 | -0.25 |
| NQ=F Asia | 13 | 7 | 53.8% | 14.3% | -1.23 | -0.66 | 0.06 | -8.64 | -9.21 | -1.61 | -0.95 |
| NQ=F London | 16 | 7 | 43.8% | 14.3% | -0.68 | -0.3 | 0.28 | -4.75 | -5.15 | -0.31 | -0.95 |
| NQ=F NY | 11 | 4 | 36.4% | 25.0% | -0.5 | -0.18 | 0.22 | -2.02 | -2.6 | -1.21 | 0.2 |
| RTY=F Asia | 18 | 4 | 22.2% | 25.0% | -0.52 | -0.12 | 0.36 | -2.1 | -2.87 | 0.39 | -1.44 |
| RTY=F London | 28 | 20 | 71.4% | 25.0% | -0.86 | -0.61 | 0.23 | -17.11 | -17.11 | -1.28 | -0.43 |
| RTY=F NY | 14 | 2 | 14.3% | 50.0% | -0.22 | -0.03 | 0.63 | -0.43 | -1.17 | -1.17 | 0.74 |
| YM=F Asia | 19 | 6 | 31.6% | 0.0% | -1.75 | -0.55 | 0.0 | -10.53 | -10.53 | -1.69 | -1.82 |
| YM=F London | 26 | 13 | 50.0% | 46.2% | -0.27 | -0.14 | 0.69 | -3.56 | -5.76 | -0.52 | -0.06 |
| YM=F NY | 14 | 2 | 14.3% | 50.0% | 0.8 | 0.11 | 2.29 | 1.6 | -1.23 | 2.83 | -1.23 |
| ZB=F Asia | 14 | 5 | 35.7% | 40.0% | -0.82 | -0.29 | 0.17 | -4.09 | -4.09 | -0.53 | -1.01 |
| ZB=F London | 11 | 6 | 54.5% | 50.0% | -0.09 | -0.05 | 0.87 | -0.51 | -2.41 | -0.1 | -0.07 |
| ZB=F NY | 14 | 6 | 42.9% | 66.7% | 0.81 | 0.35 | 2.87 | 4.86 | -1.39 | 0.84 | 0.78 |
| ZF=F Asia | 14 | 4 | 28.6% | 0.0% | -2.26 | -0.65 | 0.0 | -9.03 | -9.03 | -2.82 | -1.7 |
| ZF=F London | 19 | 12 | 63.2% | 16.7% | -1.94 | -1.23 | 0.09 | -23.31 | -23.31 | -2.83 | -1.06 |
| ZF=F NY | 13 | 6 | 46.2% | 16.7% | -1.37 | -0.63 | 0.01 | -8.24 | -8.29 | -1.39 | -1.35 |
| ZN=F Asia | 9 | 4 | 44.4% | 25.0% | -0.67 | -0.3 | 0.27 | -2.66 | -3.07 | -1.53 | 0.2 |
| ZN=F London | 11 | 6 | 54.5% | 33.3% | -0.59 | -0.32 | 0.41 | -3.55 | -3.68 | -0.72 | -0.46 |
| ZN=F NY | 7 | 5 | 71.4% | 40.0% | -0.4 | -0.29 | 0.44 | -2.0 | -2.0 | -0.9 | -0.06 |
| ZS=F Asia | 4 | 0 | 0.0% |  |  | 0.0 |  | 0.0 | 0.0 |  |  |
| ZS=F London | 17 | 5 | 29.4% | 20.0% | -1.06 | -0.31 | 0.07 | -5.28 | -5.28 | -1.29 | -0.9 |
| ZS=F NY | 10 | 1 | 10.0% | 0.0% | -1.26 | -0.13 | 0.0 | -1.26 | -1.26 |  | -1.26 |

## 2. New York session: by asset, side, time of day, risk size (systematic, qualified)

| Group | Setups | Triggered | Trigger rate | Win rate | Avg R | Expectancy R | Profit factor | Total R | Max DD R | 1st half avg R | 2nd half avg R |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ETF | 23 | 10 | 43.5% | 0.0% | -1.21 | -0.53 | 0.0 | -12.1 | -12.1 | -1.06 | -1.36 |
| Stock | 27 | 4 | 14.8% | 50.0% | -0.03 | -0.0 | 0.95 | -0.13 | -1.82 | -0.29 | 0.23 |
| Future | 134 | 45 | 33.6% | 42.2% | -0.12 | -0.04 | 0.83 | -5.26 | -11.28 | 0.19 | -0.41 |
| Leveraged/inverse ETFs | 6 | 2 | 33.3% | 0.0% | -1.02 | -0.34 | 0.0 | -2.04 | -2.04 | -1.02 | -1.02 |
| LONG | 138 | 47 | 34.1% | 36.2% | -0.24 | -0.08 | 0.68 | -11.05 | -14.58 | 0.08 | -0.53 |
| SHORT | 46 | 12 | 26.1% | 33.3% | -0.54 | -0.14 | 0.37 | -6.44 | -9.58 | -0.59 | -0.48 |
| Formed 10:00-10:30 | 25 | 16 | 64.0% | 18.8% | -0.49 | -0.31 | 0.39 | -7.79 | -7.79 | -0.08 | -0.9 |
| Formed 10:30-11:30 | 47 | 23 | 48.9% | 30.4% | -0.48 | -0.23 | 0.49 | -10.96 | -12.72 | -0.04 | -0.87 |
| Formed 11:30-13:00 | 55 | 15 | 27.3% | 53.3% | -0.11 | -0.03 | 0.83 | -1.6 | -3.09 | -0.08 | -0.13 |
| Formed 13:00-14:30 | 35 | 4 | 11.4% | 75.0% | 0.89 | 0.1 | 3.87 | 3.54 | -1.24 | 1.54 | 0.23 |
| Formed 14:30-16:00 | 22 | 1 | 4.5% | 0.0% | -0.69 | -0.03 | 0.0 | -0.69 | -0.69 |  | -0.69 |
| Risk 0-0.15% of price | 323 | 162 | 50.2% | 29.6% | -0.73 | -0.37 | 0.36 | -118.3 | -120.0 | -0.76 | -0.7 |
| Risk 0.15-0.3% of price | 113 | 43 | 38.1% | 30.2% | -0.26 | -0.1 | 0.62 | -11.26 | -14.63 | -0.51 | -0.02 |
| Risk 0.3-0.6% of price | 60 | 15 | 25.0% | 46.7% | 0.05 | 0.01 | 1.09 | 0.71 | -3.31 | 0.18 | -0.07 |
| Risk 0.6%+ | 31 | 4 | 12.9% | 25.0% | -0.6 | -0.08 | 0.23 | -2.4 | -3.1 | -0.16 | -1.04 |

## 2b. Short guardrails (systematic; shorts use full exit at T1, breakeven at +0.5R, 60-minute time stop)

Sizing: longs 1.25% risk (cap 5.0% of account), shorts 0.5% risk (cap 2.5%). Results here are in R, before sizing.

| Group | Setups | Triggered | Trigger rate | Win rate | Avg R | Expectancy R | Profit factor | Total R | Max DD R | 1st half avg R | 2nd half avg R |
|---|---|---|---|---|---|---|---|---|---|---|---|
| Longs passing the normal filters | 480 | 212 | 44.2% | 30.7% | -0.59 | -0.26 | 0.42 | -124.81 | -125.39 | -0.7 | -0.48 |
| Shorts passing the normal filters (before guardrails) | 352 | 163 | 46.3% | 22.7% | -0.74 | -0.34 | 0.25 | -119.98 | -120.14 | -0.83 | -0.64 |
| Shorts passing every guardrail (traded) | 47 | 12 | 25.5% | 33.3% | -0.54 | -0.14 | 0.37 | -6.44 | -9.58 | -0.59 | -0.48 |
| Shorts passing: bearish daily trend | 160 | 84 | 52.5% | 22.6% | -0.83 | -0.44 | 0.23 | -69.93 | -69.93 | -0.95 | -0.71 |
| Shorts failing: bearish daily trend | 192 | 79 | 41.1% | 22.8% | -0.63 | -0.26 | 0.27 | -50.05 | -50.35 | -0.76 | -0.51 |
| Shorts passing: PDH or 2+ level sweep | 142 | 61 | 43.0% | 24.6% | -0.49 | -0.21 | 0.33 | -29.68 | -29.68 | -0.48 | -0.49 |
| Shorts failing: PDH or 2+ level sweep | 210 | 102 | 48.6% | 21.6% | -0.89 | -0.43 | 0.22 | -90.3 | -90.6 | -1.04 | -0.73 |
| Shorts passing: R:R to T2 3.0+ | 214 | 109 | 50.9% | 23.9% | -0.8 | -0.41 | 0.23 | -87.37 | -87.53 | -0.79 | -0.81 |
| Shorts failing: R:R to T2 3.0+ | 138 | 54 | 39.1% | 20.4% | -0.6 | -0.24 | 0.3 | -32.61 | -34.0 | -0.92 | -0.29 |
| Shorts passing: risk 0.3%+ of price | 28 | 9 | 32.1% | 33.3% | -0.03 | -0.01 | 0.93 | -0.25 | -2.61 | 0.27 | -0.26 |
| Shorts failing: risk 0.3%+ of price | 324 | 154 | 47.5% | 22.1% | -0.78 | -0.37 | 0.23 | -119.73 | -119.89 | -0.84 | -0.72 |
| Shorts passing: formed 10:30 or later | 295 | 141 | 47.8% | 23.4% | -0.74 | -0.36 | 0.25 | -104.93 | -105.08 | -0.87 | -0.62 |
| Shorts failing: formed 10:30 or later | 57 | 22 | 38.6% | 18.2% | -0.68 | -0.26 | 0.23 | -15.05 | -16.75 | -0.49 | -0.88 |
| Shorts passing: not a leveraged ETF | 314 | 153 | 48.7% | 22.9% | -0.73 | -0.36 | 0.25 | -112.1 | -112.26 | -0.83 | -0.64 |
| Shorts failing: not a leveraged ETF | 38 | 10 | 26.3% | 20.0% | -0.79 | -0.21 | 0.22 | -7.88 | -9.58 | -1.27 | -0.31 |

## 3. Outcomes (systematic, qualified)

| Outcome | Count | Share | Avg R |
|---|---|---|---|
| Not triggered (ran to T1 first) | 277 | 52.6% | 0.0 |
| Stop | 122 | 23.1% | -1.66 |
| EOD exit | 29 | 5.5% | -0.38 |
| Not triggered (cutoff) | 26 | 4.9% | 0.0 |
| T1 then T2 | 26 | 4.9% | 1.65 |
| T1 then breakeven | 25 | 4.7% | -0.07 |
| T1 then EOD | 20 | 3.8% | 1.95 |
| Time stop | 2 | 0.4% | 0.72 |

## 4. Score calibration. A useful score shows results improving band by band.

| Group | Setups | Triggered | Trigger rate | Win rate | Avg R | Expectancy R | Profit factor | Total R | Max DD R | 1st half avg R | 2nd half avg R |
|---|---|---|---|---|---|---|---|---|---|---|---|
| Score 90+ | 2 | 1 | 50.0% | 100.0% | 0.43 | 0.22 |  | 0.43 | 0.0 |  | 0.43 |
| Score 75-89 | 148 | 60 | 40.5% | 28.3% | -0.58 | -0.24 | 0.41 | -35.0 | -35.0 | -0.8 | -0.37 |
| Score 60-74 | 314 | 122 | 38.9% | 32.8% | -0.5 | -0.2 | 0.47 | -61.28 | -62.98 | -0.21 | -0.8 |
| Score under 60 | 63 | 41 | 65.1% | 26.8% | -0.86 | -0.56 | 0.32 | -35.4 | -37.62 | -1.04 | -0.7 |

## 5. Factor attribution (all triggered systematic setups, qualified or not)

| Factor | Weight key | Weight | With | Avg R with | Without | Avg R without | Difference | Read |
|---|---|---|---|---|---|---|---|---|
| Prior-day level swept | sweep_pd | 20 | 267 | -0.41 | 685 | -0.56 | 0.14 | No clear effect |
| Only PM/OR level swept | sweep_other | 15 | 516 | -0.51 | 436 | -0.53 | 0.02 | No clear effect |
| FVG in discount/premium | zone | 10 | 403 | -0.66 | 549 | -0.41 | -0.25 | Hurts |
| FVG overlaps OTE | ote | 15 | 383 | -0.67 | 569 | -0.41 | -0.25 | Hurts |
| R:R to T1 of 2 or more | rr | 10 | 136 | -0.96 | 816 | -0.44 | -0.52 | Hurts |
| HTF bias aligned | bias | 10 | 365 | -0.54 | 587 | -0.5 | -0.03 | No clear effect |
| Displacement volume 1.5x+ | vol | 5 | 300 | -0.46 | 652 | -0.54 | 0.08 | No clear effect |
| Formed 10:00-11:30 | time | 5 | 487 | -0.64 | 465 | -0.39 | -0.26 | Hurts |

## 6. Filter check (systematic)

| Group | Setups | Triggered | Trigger rate | Win rate | Avg R | Expectancy R | Profit factor | Total R | Max DD R | 1st half avg R | 2nd half avg R |
|---|---|---|---|---|---|---|---|---|---|---|---|
| Passed filters | 527 | 224 | 42.5% | 30.8% | -0.59 | -0.25 | 0.42 | -131.25 | -133.52 | -0.69 | -0.48 |
| Filtered out | 1090 | 728 | 66.8% | 35.2% | -0.5 | -0.33 | 0.25 | -360.43 | -360.43 | -0.52 | -0.47 |
| No OTE overlap | 765 | 569 | 74.4% | 39.2% | -0.41 | -0.31 | 0.26 | -235.73 | -235.73 | -0.44 | -0.39 |
| OTE overlap, R:R to T2 1.5-2 | 20 | 8 | 40.0% | 0.0% | -1.39 | -0.56 | 0.0 | -11.15 | -11.15 | -1.17 | -1.61 |
| OTE overlap, R:R to T2 2-2.5 | 182 | 81 | 44.5% | 25.9% | -0.59 | -0.26 | 0.37 | -47.41 | -47.41 | -0.9 | -0.28 |
| OTE overlap, R:R to T2 2.5-3 | 124 | 50 | 40.3% | 46.0% | -0.03 | -0.01 | 0.96 | -1.26 | -16.52 | -0.03 | -0.02 |
| OTE overlap, R:R to T2 3+ | 526 | 244 | 46.4% | 23.8% | -0.8 | -0.37 | 0.26 | -196.12 | -197.43 | -0.81 | -0.8 |

## 7. Improvement tests: entry type x stop buffer x filter (net of costs)

ote_mid = current entry (middle of the FVG/OTE overlap); fvg_edge = first touch of the gap; fvg_ce = gap midpoint; blend = halfway between the gap edge and ote_mid; ote_62 = first touch of the OTE zone. Scaled rows are in R of the full planned position (a partial fill counts only what filled).

| Group | Setups | Triggered | Trigger rate | Win rate | Avg R | Expectancy R | Profit factor | Total R | Max DD R | 1st half avg R | 2nd half avg R |
|---|---|---|---|---|---|---|---|---|---|---|---|
| Entry ote_mid, stop 0.1 ATR · All qualified | 527 | 210 | 39.8% | 31.9% | -0.57 | -0.23 | 0.44 | -119.02 | -119.59 | -0.68 | -0.45 |
| Entry ote_mid, stop 0.1 ATR · Plan window (by 11:30) | 79 | 30 | 38.0% | 33.3% | -0.27 | -0.1 | 0.66 | -8.09 | -9.25 | -0.11 | -0.43 |
| Entry ote_mid, stop 0.1 ATR · Midday 11:30-14:30 | 90 | 14 | 15.6% | 64.3% | 0.25 | 0.04 | 1.54 | 3.52 | -2.56 | 0.08 | 0.42 |
| Entry ote_mid, stop 0.1 ATR · R:R to T2 2.5+ | 401 | 154 | 38.4% | 31.2% | -0.62 | -0.24 | 0.41 | -95.32 | -95.89 | -0.76 | -0.47 |
| Entry ote_mid, stop 0.1 ATR · Risk 0.15%+ | 204 | 53 | 26.0% | 37.7% | -0.09 | -0.02 | 0.85 | -4.64 | -11.18 | -0.23 | 0.05 |
| Entry ote_mid, stop 0.1 ATR · Midday + R:R 2.5+ + risk 0.15%+ | 42 | 3 | 7.1% | 66.7% | 0.06 | 0.0 | 1.14 | 0.18 | -1.26 | -1.26 | 0.72 |
| Entry ote_mid, stop 0.3 ATR · All qualified | 527 | 210 | 39.8% | 34.3% | -0.48 | -0.19 | 0.46 | -100.52 | -101.05 | -0.58 | -0.38 |
| Entry ote_mid, stop 0.3 ATR · Plan window (by 11:30) | 79 | 30 | 38.0% | 40.0% | -0.15 | -0.06 | 0.77 | -4.52 | -6.44 | -0.03 | -0.27 |
| Entry ote_mid, stop 0.3 ATR · Midday 11:30-14:30 | 90 | 14 | 15.6% | 64.3% | 0.23 | 0.04 | 1.52 | 3.17 | -2.31 | 0.06 | 0.39 |
| Entry ote_mid, stop 0.3 ATR · R:R to T2 2.5+ | 401 | 154 | 38.4% | 34.4% | -0.5 | -0.19 | 0.45 | -77.65 | -78.18 | -0.63 | -0.38 |
| Entry ote_mid, stop 0.3 ATR · Risk 0.15%+ | 204 | 53 | 26.0% | 43.4% | 0.05 | 0.01 | 1.1 | 2.79 | -5.33 | -0.01 | 0.11 |
| Entry ote_mid, stop 0.3 ATR · Midday + R:R 2.5+ + risk 0.15%+ | 42 | 3 | 7.1% | 66.7% | 0.03 | 0.0 | 1.08 | 0.1 | -1.24 | -1.24 | 0.67 |
| Entry fvg_edge, stop 0.1 ATR · All qualified | 527 | 263 | 49.9% | 44.5% | -0.29 | -0.14 | 0.55 | -75.06 | -80.55 | -0.44 | -0.14 |
| Entry fvg_edge, stop 0.1 ATR · Plan window (by 11:30) | 79 | 35 | 44.3% | 45.7% | -0.24 | -0.11 | 0.58 | -8.51 | -9.37 | -0.12 | -0.36 |
| Entry fvg_edge, stop 0.1 ATR · Midday 11:30-14:30 | 90 | 28 | 31.1% | 71.4% | 0.21 | 0.07 | 2.07 | 5.86 | -2.25 | 0.16 | 0.26 |
| Entry fvg_edge, stop 0.1 ATR · R:R to T2 2.5+ | 401 | 195 | 48.6% | 43.6% | -0.31 | -0.15 | 0.53 | -59.92 | -62.26 | -0.45 | -0.17 |
| Entry fvg_edge, stop 0.1 ATR · Risk 0.15%+ | 204 | 72 | 35.3% | 52.8% | -0.04 | -0.01 | 0.91 | -2.68 | -7.72 | -0.12 | 0.05 |
| Entry fvg_edge, stop 0.1 ATR · Midday + R:R 2.5+ + risk 0.15%+ | 42 | 7 | 16.7% | 85.7% | 0.02 | 0.0 | 1.1 | 0.12 | -1.23 | -0.32 | 0.27 |
| Entry fvg_edge, stop 0.3 ATR · All qualified | 527 | 263 | 49.9% | 46.4% | -0.24 | -0.12 | 0.57 | -64.27 | -68.73 | -0.38 | -0.11 |
| Entry fvg_edge, stop 0.3 ATR · Plan window (by 11:30) | 79 | 35 | 44.3% | 51.4% | -0.17 | -0.08 | 0.65 | -5.96 | -6.64 | -0.07 | -0.26 |
| Entry fvg_edge, stop 0.3 ATR · Midday 11:30-14:30 | 90 | 28 | 31.1% | 71.4% | 0.19 | 0.06 | 1.99 | 5.19 | -2.11 | 0.13 | 0.24 |
| Entry fvg_edge, stop 0.3 ATR · R:R to T2 2.5+ | 401 | 195 | 48.6% | 46.2% | -0.25 | -0.12 | 0.57 | -49.2 | -50.94 | -0.38 | -0.13 |
| Entry fvg_edge, stop 0.3 ATR · Risk 0.15%+ | 204 | 72 | 35.3% | 56.9% | 0.03 | 0.01 | 1.1 | 2.49 | -3.7 | -0.0 | 0.07 |
| Entry fvg_edge, stop 0.3 ATR · Midday + R:R 2.5+ + risk 0.15%+ | 42 | 7 | 16.7% | 85.7% | 0.01 | 0.0 | 1.05 | 0.06 | -1.21 | -0.32 | 0.25 |
| Entry fvg_ce, stop 0.1 ATR · All qualified | 527 | 223 | 42.3% | 36.3% | -0.47 | -0.2 | 0.47 | -105.82 | -108.32 | -0.62 | -0.33 |
| Entry fvg_ce, stop 0.1 ATR · Plan window (by 11:30) | 79 | 30 | 38.0% | 40.0% | -0.23 | -0.09 | 0.67 | -7.04 | -8.72 | -0.1 | -0.37 |
| Entry fvg_ce, stop 0.1 ATR · Midday 11:30-14:30 | 90 | 17 | 18.9% | 64.7% | 0.1 | 0.02 | 1.25 | 1.7 | -2.63 | 0.27 | -0.05 |
| Entry fvg_ce, stop 0.1 ATR · R:R to T2 2.5+ | 401 | 165 | 41.1% | 36.4% | -0.49 | -0.2 | 0.47 | -80.65 | -83.42 | -0.64 | -0.34 |
| Entry fvg_ce, stop 0.1 ATR · Risk 0.15%+ | 204 | 57 | 27.9% | 45.6% | -0.01 | -0.0 | 0.99 | -0.45 | -7.78 | -0.14 | 0.12 |
| Entry fvg_ce, stop 0.1 ATR · Midday + R:R 2.5+ + risk 0.15%+ | 42 | 3 | 7.1% | 66.7% | -0.19 | -0.01 | 0.55 | -0.56 | -1.25 | -1.25 | 0.34 |
| Entry fvg_ce, stop 0.3 ATR · All qualified | 527 | 223 | 42.3% | 38.6% | -0.4 | -0.17 | 0.49 | -90.3 | -92.75 | -0.53 | -0.28 |
| Entry fvg_ce, stop 0.3 ATR · Plan window (by 11:30) | 79 | 30 | 38.0% | 46.7% | -0.12 | -0.05 | 0.79 | -3.74 | -5.45 | -0.02 | -0.23 |
| Entry fvg_ce, stop 0.3 ATR · Midday 11:30-14:30 | 90 | 17 | 18.9% | 64.7% | 0.09 | 0.02 | 1.26 | 1.61 | -2.4 | 0.25 | -0.04 |
| Entry fvg_ce, stop 0.3 ATR · R:R to T2 2.5+ | 401 | 165 | 41.1% | 39.4% | -0.4 | -0.16 | 0.51 | -65.94 | -68.65 | -0.53 | -0.27 |
| Entry fvg_ce, stop 0.3 ATR · Risk 0.15%+ | 204 | 57 | 27.9% | 50.9% | 0.1 | 0.03 | 1.21 | 5.56 | -4.15 | 0.04 | 0.16 |
| Entry fvg_ce, stop 0.3 ATR · Midday + R:R 2.5+ + risk 0.15%+ | 42 | 3 | 7.1% | 66.7% | -0.19 | -0.01 | 0.53 | -0.58 | -1.22 | -1.22 | 0.32 |
| Entry blend, stop 0.1 ATR · All qualified | 527 | 228 | 43.3% | 38.6% | -0.44 | -0.19 | 0.47 | -100.6 | -102.85 | -0.58 | -0.31 |
| Entry blend, stop 0.1 ATR · Plan window (by 11:30) | 79 | 31 | 39.2% | 45.2% | -0.19 | -0.08 | 0.71 | -5.96 | -7.21 | -0.14 | -0.24 |
| Entry blend, stop 0.1 ATR · Midday 11:30-14:30 | 90 | 21 | 23.3% | 71.4% | 0.2 | 0.05 | 1.65 | 4.21 | -2.49 | 0.26 | 0.15 |
| Entry blend, stop 0.1 ATR · R:R to T2 2.5+ | 401 | 169 | 42.1% | 37.9% | -0.48 | -0.2 | 0.45 | -80.82 | -83.43 | -0.62 | -0.34 |
| Entry blend, stop 0.1 ATR · Risk 0.15%+ | 204 | 59 | 28.9% | 49.2% | -0.0 | -0.0 | 1.0 | -0.15 | -8.12 | -0.22 | 0.21 |
| Entry blend, stop 0.1 ATR · Midday + R:R 2.5+ + risk 0.15%+ | 42 | 4 | 9.5% | 75.0% | -0.01 | -0.0 | 0.98 | -0.03 | -1.25 | -0.47 | 0.46 |
| Entry blend, stop 0.3 ATR · All qualified | 527 | 228 | 43.3% | 40.8% | -0.38 | -0.16 | 0.49 | -85.97 | -88.2 | -0.5 | -0.25 |
| Entry blend, stop 0.3 ATR · Plan window (by 11:30) | 79 | 31 | 39.2% | 51.6% | -0.09 | -0.04 | 0.84 | -2.9 | -4.99 | -0.05 | -0.13 |
| Entry blend, stop 0.3 ATR · Midday 11:30-14:30 | 90 | 21 | 23.3% | 71.4% | 0.18 | 0.04 | 1.64 | 3.87 | -2.28 | 0.23 | 0.14 |
| Entry blend, stop 0.3 ATR · R:R to T2 2.5+ | 401 | 169 | 42.1% | 40.8% | -0.39 | -0.17 | 0.49 | -66.6 | -69.16 | -0.51 | -0.28 |
| Entry blend, stop 0.3 ATR · Risk 0.15%+ | 204 | 59 | 28.9% | 54.2% | 0.1 | 0.03 | 1.23 | 5.85 | -4.19 | -0.05 | 0.24 |
| Entry blend, stop 0.3 ATR · Midday + R:R 2.5+ + risk 0.15%+ | 42 | 4 | 9.5% | 75.0% | -0.02 | -0.0 | 0.94 | -0.07 | -1.22 | -0.47 | 0.44 |
| Entry ote_62, stop 0.1 ATR · All qualified | 527 | 225 | 42.7% | 38.2% | -0.4 | -0.17 | 0.52 | -91.04 | -91.58 | -0.56 | -0.25 |
| Entry ote_62, stop 0.1 ATR · Plan window (by 11:30) | 79 | 31 | 39.2% | 41.9% | -0.14 | -0.06 | 0.79 | -4.45 | -6.53 | -0.08 | -0.2 |
| Entry ote_62, stop 0.1 ATR · Midday 11:30-14:30 | 90 | 19 | 21.1% | 68.4% | 0.42 | 0.09 | 2.27 | 7.9 | -2.48 | 0.71 | 0.15 |
| Entry ote_62, stop 0.1 ATR · R:R to T2 2.5+ | 401 | 167 | 41.6% | 38.3% | -0.44 | -0.18 | 0.49 | -73.61 | -74.15 | -0.67 | -0.22 |
| Entry ote_62, stop 0.1 ATR · Risk 0.15%+ | 204 | 56 | 27.5% | 44.6% | -0.0 | -0.0 | 1.0 | -0.05 | -8.56 | -0.24 | 0.23 |
| Entry ote_62, stop 0.1 ATR · Midday + R:R 2.5+ + risk 0.15%+ | 42 | 3 | 7.1% | 66.7% | -0.05 | -0.0 | 0.88 | -0.15 | -1.26 | -1.26 | 0.56 |
| Entry ote_62, stop 0.3 ATR · All qualified | 527 | 225 | 42.7% | 40.4% | -0.34 | -0.15 | 0.55 | -76.49 | -76.98 | -0.48 | -0.2 |
| Entry ote_62, stop 0.3 ATR · Plan window (by 11:30) | 79 | 31 | 39.2% | 48.4% | -0.04 | -0.02 | 0.92 | -1.37 | -5.39 | 0.01 | -0.09 |
| Entry ote_62, stop 0.3 ATR · Midday 11:30-14:30 | 90 | 19 | 21.1% | 68.4% | 0.37 | 0.08 | 2.21 | 7.07 | -2.27 | 0.63 | 0.14 |
| Entry ote_62, stop 0.3 ATR · R:R to T2 2.5+ | 401 | 167 | 41.6% | 41.3% | -0.36 | -0.15 | 0.53 | -59.34 | -59.83 | -0.55 | -0.16 |
| Entry ote_62, stop 0.3 ATR · Risk 0.15%+ | 204 | 56 | 27.5% | 50.0% | 0.12 | 0.03 | 1.26 | 6.58 | -3.94 | -0.03 | 0.27 |
| Entry ote_62, stop 0.3 ATR · Midday + R:R 2.5+ + risk 0.15%+ | 42 | 3 | 7.1% | 66.7% | -0.07 | -0.0 | 0.84 | -0.2 | -1.24 | -1.24 | 0.52 |
| Scaled ladder_equal (fvg_edge 33%, blend 33%, ote_mid 33%) · All qualified | 527 | 263 | 49.9% | 43.0% | -0.36 | -0.18 | 0.47 | -95.36 | -96.9 | -0.49 | -0.24 |
| Scaled ladder_equal (fvg_edge 33%, blend 33%, ote_mid 33%) · Plan window (by 11:30) | 79 | 35 | 44.3% | 48.6% | -0.21 | -0.1 | 0.64 | -7.52 | -8.17 | -0.05 | -0.37 |
| Scaled ladder_equal (fvg_edge 33%, blend 33%, ote_mid 33%) · Midday 11:30-14:30 | 90 | 28 | 31.1% | 78.6% | 0.16 | 0.05 | 1.76 | 4.49 | -2.37 | 0.16 | 0.16 |
| Scaled ladder_equal (fvg_edge 33%, blend 33%, ote_mid 33%) · R:R to T2 2.5+ | 401 | 195 | 48.6% | 42.1% | -0.39 | -0.19 | 0.46 | -76.25 | -77.79 | -0.5 | -0.29 |
| Scaled ladder_equal (fvg_edge 33%, blend 33%, ote_mid 33%) · Risk 0.15%+ | 204 | 72 | 35.3% | 52.8% | -0.03 | -0.01 | 0.92 | -2.23 | -8.6 | -0.14 | 0.08 |
| Scaled ladder_equal (fvg_edge 33%, blend 33%, ote_mid 33%) · Midday + R:R 2.5+ + risk 0.15%+ | 42 | 7 | 16.7% | 85.7% | 0.01 | 0.0 | 1.08 | 0.09 | -1.25 | -0.28 | 0.24 |
| Scaled ladder_deep (fvg_edge 20%, blend 30%, ote_mid 50%) · All qualified | 527 | 263 | 49.9% | 42.6% | -0.39 | -0.19 | 0.46 | -101.81 | -103.16 | -0.5 | -0.27 |
| Scaled ladder_deep (fvg_edge 20%, blend 30%, ote_mid 50%) · Plan window (by 11:30) | 79 | 35 | 44.3% | 48.6% | -0.21 | -0.09 | 0.64 | -7.48 | -7.91 | -0.03 | -0.38 |
| Scaled ladder_deep (fvg_edge 20%, blend 30%, ote_mid 50%) · Midday 11:30-14:30 | 90 | 28 | 31.1% | 78.6% | 0.15 | 0.05 | 1.68 | 4.14 | -2.41 | 0.17 | 0.13 |
| Scaled ladder_deep (fvg_edge 20%, blend 30%, ote_mid 50%) · R:R to T2 2.5+ | 401 | 195 | 48.6% | 42.1% | -0.42 | -0.2 | 0.44 | -81.41 | -82.75 | -0.51 | -0.32 |
| Scaled ladder_deep (fvg_edge 20%, blend 30%, ote_mid 50%) · Risk 0.15%+ | 204 | 72 | 35.3% | 52.8% | -0.04 | -0.01 | 0.91 | -2.57 | -9.08 | -0.15 | 0.07 |
| Scaled ladder_deep (fvg_edge 20%, blend 30%, ote_mid 50%) · Midday + R:R 2.5+ + risk 0.15%+ | 42 | 7 | 16.7% | 85.7% | 0.02 | 0.0 | 1.1 | 0.12 | -1.25 | -0.26 | 0.23 |

## 8. Trade management (systematic, qualified, triggered)

| Method | Trades | Avg R | Win rate |
|---|---|---|---|
| Plan: half at T1, rest to T2 (gross) | 224 | 0.04 | 38.4% |
| Plan, net of costs | 224 | -0.59 | 30.8% |
| Full position to T1 (gross) | 224 | 0.06 | 38.4% |
| Full position to T2 (gross) | 224 | 0.02 | 29.9% |

## 9. Automatic changes in this run

| Key | Old | New | Evidence |
|---|---|---|---|
| None |  |  |  |
