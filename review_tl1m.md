# Trendline-break 1-minute model review: 2026-11-04 20:30 ET

Data: Alpaca 1-minute (SIP), 2026-05-07 to 2026-11-03, 74 symbols (stocks plus SPY). Same rules as FVG_1m_Trendlines.pine. Rules on: vwap, orb, fib. Realistic cost = limit orders free, $0.01/share on market exits; standard cost = 0.02% per side.

## 1. Runs (each changes one thing from the core)

| Group | Trades | Win rate | Avg R (realistic cost) | Avg R (standard cost) | Profit factor | Total R | Max DD R | Design avg R (to Aug) | Confirm avg R (Sep on) |
|---|---|---|---|---|---|---|---|---|---|
| core · both sides | 9642 | 16.4% | -0.06 | -0.24 | 0.91 | -577.94 | -752.89 | -0.06 (n=6340) | -0.06 (n=3302) |
| core · long | 4933 | 16.4% | -0.07 | -0.25 | 0.89 | -342.30 | -442.34 | -0.05 (n=3242) | -0.11 (n=1691) |
| core · short | 4709 | 16.5% | -0.05 | -0.23 | 0.92 | -235.65 | -443.00 | -0.08 (n=3098) | -0.00 (n=1611) |
| stop below the swing low · both sides | 8968 | 16.3% | -0.05 | -0.19 | 0.91 | -452.86 | -653.40 | -0.06 (n=5860) | -0.04 (n=3108) |
| stop below the swing low · long | 4584 | 16.6% | -0.06 | -0.19 | 0.90 | -260.27 | -345.81 | -0.03 (n=3000) | -0.10 (n=1584) |
| stop below the swing low · short | 4384 | 16.0% | -0.04 | -0.18 | 0.92 | -192.58 | -392.73 | -0.08 (n=2860) | 0.02 (n=1524) |
| 2-close exit, no initial stop · both sides | 8699 | 18.9% | -0.08 | -0.22 | 0.88 | -678.03 | -867.44 | -0.09 (n=5677) | -0.06 (n=3022) |
| 2-close exit, no initial stop · long | 4449 | 18.7% | -0.09 | -0.23 | 0.86 | -401.16 | -476.12 | -0.07 (n=2909) | -0.14 (n=1540) |
| 2-close exit, no initial stop · short | 4250 | 19.2% | -0.07 | -0.20 | 0.90 | -276.88 | -510.28 | -0.11 (n=2768) | 0.02 (n=1482) |
| target 3R · both sides | 9657 | 20.3% | -0.07 | -0.24 | 0.89 | -653.10 | -810.34 | -0.07 (n=6351) | -0.06 (n=3306) |
| target 3R · long | 4939 | 20.2% | -0.08 | -0.25 | 0.88 | -376.84 | -446.59 | -0.06 (n=3247) | -0.11 (n=1692) |
| target 3R · short | 4718 | 20.3% | -0.06 | -0.23 | 0.91 | -276.26 | -465.38 | -0.08 (n=3104) | -0.02 (n=1614) |
| trendline retest required · both sides | 2597 | 15.2% | -0.06 | -0.24 | 0.90 | -155.58 | -231.45 | -0.09 (n=1713) | -0.01 (n=884) |
| trendline retest required · long | 1337 | 15.1% | -0.07 | -0.25 | 0.88 | -94.52 | -150.26 | -0.10 (n=913) | -0.00 (n=424) |
| trendline retest required · short | 1260 | 15.4% | -0.05 | -0.22 | 0.92 | -61.06 | -108.60 | -0.07 (n=800) | -0.02 (n=460) |
| without VWAP · both sides | 14652 | 15.9% | -0.07 | -0.25 | 0.88 | -1089.32 | -1158.20 | -0.07 (n=9717) | -0.09 (n=4935) |
| without VWAP · long | 7502 | 15.6% | -0.10 | -0.27 | 0.84 | -742.22 | -839.99 | -0.09 (n=4969) | -0.12 (n=2533) |
| without VWAP · short | 7150 | 16.3% | -0.05 | -0.22 | 0.92 | -347.10 | -522.95 | -0.05 (n=4748) | -0.05 (n=2402) |
| without opening range · both sides | 13642 | 16.3% | -0.07 | -0.24 | 0.89 | -915.36 | -1103.71 | -0.06 (n=8875) | -0.07 (n=4767) |
| without opening range · long | 6877 | 16.0% | -0.09 | -0.26 | 0.86 | -606.71 | -718.48 | -0.08 (n=4509) | -0.11 (n=2368) |
| without opening range · short | 6765 | 16.6% | -0.05 | -0.22 | 0.93 | -308.65 | -495.98 | -0.05 (n=4366) | -0.04 (n=2399) |
| without Fibonacci · both sides | 14615 | 15.6% | -0.06 | -0.23 | 0.91 | -832.88 | -1095.55 | -0.07 (n=9672) | -0.02 (n=4943) |
| without Fibonacci · long | 7484 | 15.6% | -0.07 | -0.25 | 0.88 | -537.94 | -616.22 | -0.07 (n=4947) | -0.08 (n=2537) |
| without Fibonacci · short | 7131 | 15.7% | -0.04 | -0.22 | 0.93 | -294.95 | -622.71 | -0.08 (n=4725) | 0.04 (n=2406) |

## 2. How the core trades end

| Exit | Trades | Avg R |
|---|---|---|
| 4R then breakeven | 565 | 1.99 |
| 4R then close | 785 | 5.16 |
| breakeven | 2117 | -0.03 |
| close | 254 | 1.57 |
| stop | 5504 | -1.03 |
| stop on the fill bar | 417 | -1.04 |

## 3. The losing trades (5939 of 9642; breakevens excluded)

| Pattern | Losers | Share |
|---|---|---|
| Stopped on the fill bar | 417 | 7% |
| Stopped within 5 bars of the fill | 2346 | 40% |
| Was +1R or better first, then stopped | 1152 | 19% |
| Never better than +0.5R | 3574 | 60% |

Average best point reached by losers: 0.55R. Winners: 1586, of which 1350 reached 4R.

## 4. What separates winners from losers (core, realistic cost; quartiles of each measure)

| Measure | Quartile range | Trades | Win rate | Avg R | Design avg R | Confirm avg R |
|---|---|---|---|---|---|---|
| Stop distance, % of price | (0.0444322361821002, 0.199999999999996] | 2411 | 16.1% | -0.10 | -0.08 | -0.14 |
| Stop distance, % of price | (0.199999999999996, 0.2] | 2421 | 16.3% | -0.08 | -0.10 | -0.05 |
| Stop distance, % of price | (0.2, 0.200000000000004] | 2405 | 17.0% | 0.01 | 0.02 | -0.03 |
| Stop distance, % of price | (0.200000000000004, 0.861698467663766] | 2405 | 16.4% | -0.06 | -0.09 | -0.01 |
| FVG height, x ATR | (0.0464, 0.37] | 2411 | 16.3% | -0.10 | -0.12 | -0.05 |
| FVG height, x ATR | (0.37, 0.593] | 2410 | 15.9% | -0.06 | -0.08 | -0.03 |
| FVG height, x ATR | (0.593, 0.911] | 2410 | 17.7% | 0.02 | 0.07 | -0.07 |
| FVG height, x ATR | (0.911, 5.623] | 2411 | 15.9% | -0.10 | -0.11 | -0.07 |
| Retracement of the FVG midpoint | (0.449, 0.5] | 2411 | 16.5% | -0.01 | 0.03 | -0.08 |
| Retracement of the FVG midpoint | (0.5, 0.547] | 2410 | 17.1% | -0.07 | -0.08 | -0.03 |
| Retracement of the FVG midpoint | (0.547, 0.603] | 2410 | 15.6% | -0.09 | -0.11 | -0.04 |
| Retracement of the FVG midpoint | (0.603, 0.7] | 2411 | 16.7% | -0.08 | -0.08 | -0.07 |
| Trendline touches | (1.999, 6.0] | 9642 | 16.4% | -0.06 | -0.06 | -0.06 |
| Trendline steepness, ATR per bar | (-0.00099286, 0.0728] | 2411 | 18.5% | 0.00 | -0.01 | 0.02 |
| Trendline steepness, ATR per bar | (0.0728, 0.15] | 2410 | 15.8% | -0.11 | -0.10 | -0.13 |
| Trendline steepness, ATR per bar | (0.15, 0.244] | 2410 | 16.1% | -0.08 | -0.09 | -0.06 |
| Trendline steepness, ATR per bar | (0.244, 1.34] | 2411 | 15.4% | -0.05 | -0.05 | -0.06 |
| Trendline length, bars | (5.999, 11.0] | 3009 | 16.5% | -0.03 | -0.03 | -0.02 |
| Trendline length, bars | (11.0, 14.0] | 1892 | 16.0% | -0.10 | -0.09 | -0.13 |
| Trendline length, bars | (14.0, 20.0] | 2629 | 16.6% | -0.07 | -0.10 | -0.01 |
| Trendline length, bars | (20.0, 74.0] | 2112 | 16.6% | -0.06 | -0.04 | -0.10 |
| Break candle body, x ATR | (-0.001, 0.468] | 2411 | 16.2% | -0.08 | -0.11 | -0.03 |
| Break candle body, x ATR | (0.468, 0.825] | 2410 | 16.8% | -0.07 | -0.06 | -0.08 |
| Break candle body, x ATR | (0.825, 1.232] | 2410 | 16.3% | -0.02 | 0.00 | -0.08 |
| Break candle body, x ATR | (1.232, 5.887] | 2411 | 16.5% | -0.07 | -0.08 | -0.05 |
| Break close beyond the line, x ATR | (-0.0009999999999256001, 0.213] | 2411 | 16.9% | -0.03 | -0.04 | 0.00 |
| Break close beyond the line, x ATR | (0.213, 0.473] | 2410 | 15.8% | -0.11 | -0.12 | -0.10 |
| Break close beyond the line, x ATR | (0.473, 0.857] | 2410 | 17.1% | -0.01 | -0.02 | 0.01 |
| Break close beyond the line, x ATR | (0.857, 5.19] | 2411 | 16.0% | -0.09 | -0.07 | -0.14 |
| Size of the new move, x ATR | (1.4240000000000002, 3.49] | 2411 | 14.5% | -0.08 | -0.10 | -0.02 |
| Size of the new move, x ATR | (3.49, 4.495] | 2410 | 15.9% | -0.05 | -0.05 | -0.04 |
| Size of the new move, x ATR | (4.495, 5.794] | 2410 | 17.4% | -0.03 | -0.06 | 0.04 |
| Size of the new move, x ATR | (5.794, 16.209] | 2411 | 18.0% | -0.09 | -0.03 | -0.19 |
| Bars from break to fill | (0.999, 5.0] | 2752 | 13.5% | -0.13 | -0.14 | -0.11 |
| Bars from break to fill | (5.0, 9.0] | 2110 | 17.1% | -0.02 | -0.00 | -0.06 |
| Bars from break to fill | (9.0, 16.0] | 2466 | 17.5% | -0.01 | -0.07 | 0.11 |
| Bars from break to fill | (16.0, 31.0] | 2314 | 18.2% | -0.07 | -0.02 | -0.16 |
| Entry distance from VWAP, x ATR | (0.0, 2.306] | 2411 | 16.5% | -0.05 | -0.02 | -0.11 |
| Entry distance from VWAP, x ATR | (2.306, 4.722] | 2410 | 16.7% | -0.08 | -0.13 | 0.00 |
| Entry distance from VWAP, x ATR | (4.722, 8.105] | 2410 | 15.9% | -0.05 | -0.05 | -0.04 |
| Entry distance from VWAP, x ATR | (8.105, 45.491] | 2411 | 16.6% | -0.06 | -0.05 | -0.08 |
| Fill time (minutes after midnight) | (629.999, 685.0] | 2445 | 17.4% | -0.04 | -0.06 | 0.01 |
| Fill time (minutes after midnight) | (685.0, 749.0] | 2389 | 16.3% | -0.04 | -0.05 | -0.03 |
| Fill time (minutes after midnight) | (749.0, 822.0] | 2423 | 16.3% | -0.06 | -0.03 | -0.12 |
| Fill time (minutes after midnight) | (822.0, 899.0] | 2385 | 15.8% | -0.10 | -0.11 | -0.09 |

## 5. Candidate stricter entries (core baseline: design -0.06R, confirm -0.06R)

A rule is worth adopting only if it beats the baseline in BOTH periods with a reasonable number of trades.

| Rule | Trades kept | Win rate | Avg R | Design avg R | Confirm avg R | Beats baseline in both? |
|---|---|---|---|---|---|---|
| Trendline with 3+ touches | 1091 | 16.2% | -0.08 | -0.10 | -0.04 | no |
| FVG at least 0.5 ATR tall | 5796 | 16.5% | -0.05 | -0.04 | -0.08 | no |
| Midpoint at 50-61.8% exactly | 5304 | 16.1% | -0.09 | -0.10 | -0.06 | no |
| Break candle body at least 1 ATR | 3680 | 16.6% | -0.04 | -0.02 | -0.09 | no |
| Break close at least 0.25 ATR beyond the line | 6848 | 16.3% | -0.07 | -0.06 | -0.07 | no |
| Fill within 10 bars of the break | 5312 | 15.2% | -0.08 | -0.08 | -0.06 | no |
| Stop at least 0.30% of price | 37 | 5.4% | -0.77 | -0.83 | -0.38 | no |
| New move at least 3 ATR | 8416 | 16.9% | -0.05 | -0.05 | -0.05 | yes |
| Entry within 2 ATR of VWAP | 2110 | 16.5% | -0.06 | -0.04 | -0.10 | no |
| Fill before 13:00 | 5904 | 16.7% | -0.04 | -0.05 | -0.02 | yes |
| Trendline not steeper than 0.5 ATR per bar | 9461 | 16.5% | -0.06 | -0.06 | -0.06 | no |

## 6. By symbol (core, top and bottom 8 by total R)

| Symbol | Trades | Avg R | Total R |
|---|---|---|---|
| PANW | 170 | 0.32 | 54.45 |
| TMUS | 141 | 0.34 | 47.38 |
| ORCL | 148 | 0.27 | 39.49 |
| STX | 139 | 0.25 | 34.54 |
| KLAC | 151 | 0.22 | 32.53 |
| DELL | 186 | 0.14 | 25.39 |
| WMT | 82 | 0.29 | 23.71 |
| HOOD | 161 | 0.14 | 22.99 |
| MSTR | 177 | -0.18 | -32.56 |
| MRVL | 181 | -0.18 | -33.13 |
| CSCO | 100 | -0.35 | -34.64 |
| C | 111 | -0.42 | -46.66 |
| INTC | 172 | -0.30 | -51.67 |
| TXN | 189 | -0.29 | -54.71 |
| RKLB | 155 | -0.40 | -62.25 |
| SMCI | 141 | -0.52 | -72.66 |

## 7. Core setups reached but not taken, by blocking rule

| Rule | Setups |
|---|---|
| vwap | 38689 |
| orb | 38805 |
| daily | 0 |
| fib | 29860 |
| trendline | 0 |
| time | 10350 |

Charts of sample losers and winners: site/tl_charts/ (GitHub Pages: /tl_charts/).
