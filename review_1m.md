# 1-minute FVG model review: 2026-11-04 17:54 ET
Data: Alpaca 1-minute (SIP), 2026-05-07 to 2026-11-03, 96 symbols. Long only. Results in R, net of 0.02% per side.

## 1. Each rule switched off in turn (current plan: half at 4R, rest to the 15-minute magnet)

| Group | Trades | Win rate | Avg R | Profit factor | Total R | Max DD R | 1st half avg R | 2nd half avg R |
|---|---|---|---|---|---|---|---|---|
| core | 667 | 17.4% | -0.13 | 0.82 | -84.76 | -112.65 | -0.12 | -0.13 |
| without daily trend | 1645 | 15.8% | -0.25 | 0.66 | -407.82 | -428.44 | -0.19 | -0.30 |
| without VWAP | 991 | 16.0% | -0.20 | 0.72 | -199.46 | -219.24 | -0.22 | -0.18 |
| without opening range | 983 | 16.1% | -0.20 | 0.72 | -198.38 | -218.72 | -0.19 | -0.21 |
| without Fibonacci | 1034 | 14.8% | -0.24 | 0.67 | -245.06 | -251.57 | -0.22 | -0.25 |
| without trendline | 2383 | 17.7% | -0.18 | 0.75 | -433.67 | -444.38 | -0.14 | -0.22 |
| structure + FVG only | 20031 | 16.0% | -0.19 | 0.73 | -3900.52 | -3907.44 | -0.17 | -0.22 |

## 2. Core model: exit methods

| Group | Trades | Win rate | Avg R | Profit factor | Total R | Max DD R | 1st half avg R | 2nd half avg R |
|---|---|---|---|---|---|---|---|---|
| Half at 4R, rest to the 15-minute magnet (plan) | 667 | 17.4% | -0.13 | 0.82 | -84.76 | -112.65 | -0.12 | -0.13 |
| Everything at 4R | 667 | 17.4% | -0.14 | 0.81 | -91.67 | -114.84 | -0.13 | -0.14 |
| Half at 4R, rest held to the close | 667 | 17.4% | -0.13 | 0.82 | -83.44 | -111.37 | -0.13 | -0.12 |

## 3. Core model: by entry time, risk size, room to the first magnet

| Group | Trades | Win rate | Avg R | Profit factor | Total R | Max DD R | 1st half avg R | 2nd half avg R |
|---|---|---|---|---|---|---|---|---|
| Filled 9:45-10:30 | 68 | 14.7% | -0.40 | 0.53 | -27.35 | -35.40 | -0.24 | -0.57 |
| Filled 10:30-12:00 | 199 | 19.1% | -0.05 | 0.93 | -9.60 | -41.77 | 0.18 | -0.27 |
| Filled 12:00-15:00 | 400 | 17.0% | -0.12 | 0.83 | -47.81 | -80.16 | -0.22 | -0.02 |
| Risk 0.20-0.35% of price | 667 | 17.4% | -0.13 | 0.82 | -84.76 | -112.65 | -0.12 | -0.13 |
| Risk 0.35%+ of price | 0 | | | | | | | |
| A 15-minute magnet sits before 4R | 77 | 14.3% | -0.30 | 0.57 | -22.78 | -32.72 | -0.05 | -0.54 |
| Clear path to 4R | 590 | 17.8% | -0.11 | 0.85 | -61.98 | -80.40 | -0.14 | -0.07 |
| Trendline with 3+ touches | 166 | 16.9% | -0.21 | 0.72 | -34.88 | -47.97 | -0.34 | -0.08 |

## 4. Core model: exits and costs

| Exit | Trades |
|---|---|
| Stop | 364 |
| Breakeven | 180 |
| 4R then close | 53 |
| Close | 33 |
| 4R then breakeven | 31 |
| 4R then magnet | 6 |

Average cost per trade: 0.20R. Trades reaching 4R: 13.5%. Median risk: 0.20% of price.

## 5. Core model by symbol (top and bottom 8 by total R)

| Symbol | Trades | Avg R | Total R |
|---|---|---|---|
| RTX | 11 | 1.24 | 13.62 |
| IBM | 12 | 1.07 | 12.86 |
| C | 3 | 3.75 | 11.25 |
| PANW | 14 | 0.71 | 9.89 |
| SNOW | 16 | 0.61 | 9.73 |
| DELL | 16 | 0.57 | 9.06 |
| WMT | 6 | 1.47 | 8.82 |
| NOW | 8 | 0.98 | 7.80 |
| IBIT | 10 | -0.70 | -7.00 |
| JNJ | 10 | -0.70 | -7.00 |
| SOXX | 10 | -0.70 | -7.00 |
| MA | 11 | -0.65 | -7.20 |
| SMH | 9 | -0.98 | -8.80 |
| COIN | 8 | -1.19 | -9.56 |
| DIA | 14 | -0.69 | -9.70 |
| AMAT | 11 | -0.92 | -10.17 |

How to read this: a rule earns its place when switching it off (section 1) lowers the average R in BOTH halves. Fewer than about 100 core trades is too small a sample to trust.
