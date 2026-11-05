"""Settings for the trendline-break 1-minute model (tl1m.py), the same rules as the TradingView
indicator FVG_1m_Trendlines.pine. Long AND short (the short side is the long side mirrored).
Edit on GitHub (pencil icon); then run the workflow with mode `tl1m`.
"""

# ----------------------------------------------------------------- trendlines (indicator: "Trendlines")
PIVOT_K = 2            # swing strength: bars each side
MIN_TOUCH = 2          # swing points on the line (the two anchors count)
TOL_ATR = 0.10         # touch / poke-through tolerance, x 1-minute ATR
MIN_GAP_BARS = 3       # bars between the two anchor points
CONFIRM_CLOSES = 1     # closes beyond the line to confirm a break
BREAK_MARGIN_ATR = 0.0 # the break close must clear the line by this much
MAX_PIVOTS = 8         # swing points considered

# ----------------------------------------------------------------- FVGs (indicator: "Fair value gaps")
MIN_GAP_PCT = 0.02     # FVG height, % of price
MAX_EXT_BARS = 30      # a gap expires after 30 bars
HL_BEFORE, HL_AFTER = 5, 15   # setup FVGs: formed up to 5 bars before / 15 bars after the break

# ----------------------------------------------------------------- trade (indicator: "Trade preview")
RULES = {"vwap": True, "orb": True, "daily": False, "fib": True, "trendline": False}
FIB_ZONE = (0.45, 0.70)
TL_PAD_ATR = 0.25
MAX_WAIT_BARS = 30
STOP_ATR = 0.10
MIN_RISK_PCT = 0.20
TARGET_R = 4.0
PARTIAL = 0.5
FIRST_FILL, LAST_FILL, EOD_EXIT = 630, 900, 955   # minutes after midnight New York
OR_END = 585
TICK = 0.01            # a limit fills only if price trades 1 tick through it
COST_PCT_PER_SIDE = 0.02
SLIP_PER_SHARE = 0.01  # realistic cost: limit orders free, $0.01/share on market exits

# ----------------------------------------------------------------- backtest
SPLIT_DATE = "2026-09-01"      # choose on sessions before, confirm on sessions after
ALLOW_ETFS = ["SPY"]           # stocks plus these ETFs
# Each run is the core with some settings changed. "stop": fvg (below the FVG) / swing (below the swing
# low of the new move) / close2 (no stop order: exit on 2 closes beyond the swing low; breakeven stop
# after 2 closes beyond the recent high).
RUNS = {
    "core": {},
    "stop below the swing low": {"stop": "swing"},
    "2-close exit, no initial stop": {"stop": "close2"},
    "target 3R": {"target_r": 3.0},
    "trendline retest required": {"trendline": True},
    "without VWAP": {"vwap": False},
    "without opening range": {"orb": False},
    "without Fibonacci": {"fib": False},
}
CHARTS = 24                    # sample trade charts (losers and winners) -> site/tl_charts/
