"""Settings for the 1-minute FVG model (fvg1m.py). Long only. Edit on GitHub (pencil icon).

The setup, in order (Ron, Nov 4, 2026):
  1. Up-trend bias: daily trend up, price above VWAP, and the 15-minute opening range broken upward.
  2. Break of market structure on the 1-minute chart: a close above the last lower high.
  3. A bullish fair value gap in the move up.
  4. Pullback into the FVG midpoint, which sits at the 50-61.8% Fibonacci retracement and on the
     broken (falling) trendline.
  5. Stop just below the FVG; first target 4R; stop to breakeven once price closes above the recent
     high; let the rest ride to the next untouched 15-minute FVG (a price magnet) or the close.
"""

# ----------------------------------------------------------------- rules (True = required)
RULES = {
    "daily_up": True,      # prior close above a rising 20-day average
    "vwap": True,          # entry above the session VWAP
    "orb": True,           # a 1-minute close above the 9:30-9:45 opening-range high earlier today
    "fib": True,           # FVG midpoint at the 50-61.8% retracement of the move (with tolerance)
    "trendline": True,     # the broken falling trendline runs through the FVG at the moment of entry
}

# ----------------------------------------------------------------- session (minutes after midnight, New York)
OPEN, OR_END = 570, 585          # 15-minute opening range: 9:30-9:45
ENTRY_START, ENTRY_END = 585, 900  # orders may fill 9:45 AM - 3:00 PM
EOD_EXIT = 955                   # anything open is sold at 3:55 PM

# ----------------------------------------------------------------- structure
PIVOT_K = 3                      # a swing high needs 3 lower highs on each side (1-minute bars)
MAX_WAIT_BARS = 30               # cancel the order if no pullback fills within 30 minutes of the break
MAX_TRADES_PER_DAY = 2           # per symbol; one position at a time
MIN_GAP_PCT = 0.02               # FVG must be at least 0.02% of price tall
FIB_ZONE = (0.45, 0.70)          # 50% and 61.8%, with a little tolerance either side
TL_PAD_ATR = 0.25                # trendline may sit up to 0.25 x 1-minute ATR outside the FVG
TL_TOL_ATR = 0.10                # closes may poke 0.1 ATR through the line before it is "broken"

# ----------------------------------------------------------------- risk and exits
STOP_ATR = 0.10                  # stop = FVG bottom - 0.1 x 1-minute ATR ...
MIN_RISK_PCT = 0.20              # ... widened to at least 0.20% of price (costs eat tiny stops)
TARGET_R = 4.0                   # first target and minimum reward:risk
PARTIAL_AT_TARGET = 0.5          # sell half at 4R; the rest rides
MAGNET_DAYS = 2                  # 15-minute FVGs from today and the prior 2 sessions are magnets
COST_PCT_PER_SIDE = 0.02         # slippage + fees, percent of price per side

# ----------------------------------------------------------------- backtest
# Each run switches one rule off so the review shows what every rule adds.
RUNS = {
    "core": {},
    "without daily trend": {"daily_up": False},
    "without VWAP": {"vwap": False},
    "without opening range": {"orb": False},
    "without Fibonacci": {"fib": False},
    "without trendline": {"trendline": False},
    "structure + FVG only": {"daily_up": False, "vwap": False, "orb": False, "fib": False, "trendline": False},
}
EXCLUDE = ["TQQQ", "SQQQ", "SOXL", "SOXS", "SPXL", "SPXS", "TNA", "TZA", "UPRO", "SH", "PSQ", "TSLL", "NVDL"]
