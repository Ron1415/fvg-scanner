# 1-minute FVG model review (version 3): 2026-11-04 20:23 ET

Data: Alpaca 1-minute (SIP), 2026-05-07 to 2026-11-03, 74 symbols (stocks plus SPY). Long only. Avg R is net of the standard cost (0.02% per side). Realistic cost = limit orders free, $0.01/share on stops and the close. Fills 10:30-15:00; a limit fills only if price trades $0.01 through it.

## 1. Exit and target variants (half at the target, rest to the 15-minute magnet)

| Group | Trades | Win rate | Avg R | Profit factor | Total R | Max DD R | Design avg R (to Aug) | Confirm avg R (Sep on) | Avg R, realistic cost |
|---|---|---|---|---|---|---|---|---|---|
| Close-confirmed exits, 4R (core v3) | 426 | 18.1% | -0.14 | 0.82 | -60.34 | -100.39 | -0.21 (n=311) | 0.04 (n=115) | 0.01 |
| Close-confirmed exits, 3R | 426 | 21.1% | -0.18 | 0.77 | -74.94 | -108.39 | -0.23 (n=311) | -0.04 (n=115) | -0.02 |
| Stop below the FVG, 4R (v2) | 431 | 18.3% | -0.11 | 0.86 | -45.90 | -71.97 | -0.16 (n=315) | 0.03 (n=116) | 0.07 |

**Chosen on May-August: Stop below the FVG, 4R (v2)** (-0.16R, n=315). Confirmation from September: 0.03R (n=116). The out-of-sample check FAILS (both periods must be above zero after the standard cost).

## 2. Each rule switched off in turn (core v3: close-confirmed exits, 4R)

| Group | Trades | Win rate | Avg R | Profit factor | Total R | Max DD R | Design avg R (to Aug) | Confirm avg R (Sep on) | Avg R, realistic cost |
|---|---|---|---|---|---|---|---|---|---|
| Close-confirmed exits, 4R (core v3) | 426 | 18.1% | -0.14 | 0.82 | -60.34 | -100.39 | -0.21 (n=311) | 0.04 (n=115) | 0.01 |
| without daily trend | 1047 | 17.1% | -0.21 | 0.74 | -215.15 | -229.51 | -0.18 (n=698) | -0.25 (n=349) | -0.05 |
| without VWAP | 660 | 17.9% | -0.19 | 0.76 | -124.41 | -152.39 | -0.20 (n=474) | -0.16 (n=186) | -0.03 |
| without opening range | 614 | 17.4% | -0.17 | 0.78 | -106.38 | -149.02 | -0.22 (n=447) | -0.04 (n=167) | -0.02 |
| without Fibonacci | 656 | 16.5% | -0.19 | 0.75 | -125.44 | -154.72 | -0.22 (n=479) | -0.12 (n=177) | -0.04 |
| without trendline | 1570 | 19.1% | -0.17 | 0.77 | -268.06 | -318.28 | -0.17 (n=1151) | -0.17 (n=419) | -0.03 |

## 3. Stop below the FVG, 4R (v2): exit methods

| Group | Trades | Win rate | Avg R | Profit factor | Total R | Max DD R | Design avg R (to Aug) | Confirm avg R (Sep on) | Avg R, realistic cost |
|---|---|---|---|---|---|---|---|---|---|
| Half at the target, rest to the 15-minute magnet (plan) | 431 | 18.3% | -0.11 | 0.86 | -45.90 | -71.97 | -0.16 (n=315) | 0.03 (n=116) | 0.07 |
| Everything at the target | 431 | 18.3% | -0.10 | 0.86 | -43.50 | -63.10 | -0.16 (n=315) | 0.05 (n=116) |  |
| Half at the target, rest held to the close | 431 | 18.3% | -0.11 | 0.85 | -47.14 | -73.20 | -0.16 (n=315) | 0.03 (n=116) |  |
| Plan, before any cost | 431 | 18.6% | 0.09 | 1.16 | 40.42 | -26.08 | 0.04 (n=315) | 0.23 (n=116) |  |

## 4. Stop below the FVG, 4R (v2): by symbol type, entry time, risk size, room to the first magnet

| Group | Trades | Win rate | Avg R | Profit factor | Total R | Max DD R | Design avg R (to Aug) | Confirm avg R (Sep on) | Avg R, realistic cost |
|---|---|---|---|---|---|---|---|---|---|
| SPY | 7 | 28.6% | -0.35 | 0.36 | -2.43 | -3.80 | -0.21 (n=5) | -0.70 (n=2) | -0.15 |
| Stocks | 424 | 18.2% | -0.10 | 0.86 | -43.48 | -69.74 | -0.16 (n=310) | 0.04 (n=114) | 0.08 |
| Filled 10:30-12:00 | 137 | 22.6% | 0.01 | 1.02 | 1.76 | -28.69 | 0.03 (n=103) | -0.03 (n=34) | 0.19 |
| Filled 12:00-15:00 | 294 | 16.3% | -0.16 | 0.78 | -47.67 | -65.68 | -0.25 (n=212) | 0.05 (n=82) | 0.02 |
| Risk under 0.35% of price | 431 | 18.3% | -0.11 | 0.86 | -45.90 | -71.97 | -0.16 (n=315) | 0.03 (n=116) | 0.07 |
| Risk 0.35%+ of price | 0 | | | | | | | | |
| A 15-minute magnet sits before the target | 40 | 12.5% | -0.37 | 0.50 | -14.64 | -17.72 | -0.53 (n=31) | 0.21 (n=9) | -0.19 |
| Clear path to the target | 391 | 18.9% | -0.08 | 0.89 | -31.26 | -57.17 | -0.12 (n=284) | 0.01 (n=107) | 0.10 |

## 5. Stop below the FVG, 4R (v2): exits and costs

| Exit | Trades |
|---|---|
| Stop | 248 |
| Breakeven | 101 |
| Target then close | 42 |
| Target then breakeven | 24 |
| Close | 14 |
| Target then magnet | 2 |

Standard cost: 0.20R per trade. Realistic cost: 0.02R. Trades reaching the target: 15.8%. Median risk: 0.20% of price.

Losing trades: average -0.91R, worst -1.34R; 0.0% lost more than 1.5R (no stop order until the breakeven stop is set).

## 6. Stop below the FVG, 4R (v2) by symbol (top and bottom 8 by total R)

| Symbol | Trades | Avg R | Total R |
|---|---|---|---|
| RTX | 9 | 1.67 | 15.02 |
| IBM | 12 | 1.07 | 12.86 |
| PANW | 12 | 1.02 | 12.29 |
| DELL | 14 | 0.82 | 11.42 |
| NOW | 7 | 1.29 | 9.00 |
| C | 2 | 2.67 | 5.35 |
| KLAC | 12 | 0.38 | 4.51 |
| CAT | 2 | 1.62 | 3.24 |
| ABBV | 6 | -0.89 | -5.33 |
| SHOP | 8 | -0.70 | -5.60 |
| MA | 10 | -0.60 | -6.00 |
| MRK | 5 | -1.20 | -6.00 |
| AMD | 6 | -1.03 | -6.20 |
| JNJ | 9 | -0.76 | -6.80 |
| COIN | 7 | -1.19 | -8.36 |
| LLY | 12 | -0.78 | -9.42 |

How to read this: the variant is chosen on May-August only; September onward is the honest test. A rule earns its place when switching it off (section 2) lowers the average R in both periods.
