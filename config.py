"""All settings for the FVG scanner. Edit on GitHub (pencil icon) to change a rule.

Values in tuning.json (written by the weekly auto-tune) override WEIGHTS and
FILTERS. Every automatic change is logged in config_changes.json. To undo one,
edit or delete the entry in tuning.json.
"""

# ----------------------------------------------------------------- universe
UNIVERSE_SIZE = 100          # stocks/ETFs: most liquid by 20-day average dollar volume
MIN_PRICE = 5.0
INCLUDE_FUTURES = True
FUTURES_SIZE = 10            # most liquid futures by 20-day average notional volume

ETF_CANDIDATES = [
    "SPY", "QQQ", "IWM", "DIA", "TQQQ", "SQQQ", "SOXL", "SOXS", "SPXL", "SPXS", "TNA", "TZA", "UPRO", "SH",
    "PSQ", "XLF", "XLE", "XLK", "XLV", "XLI", "XLY", "XLP", "XLU", "XLC", "XLB", "XLRE", "SMH", "SOXX", "GLD",
    "SLV", "GDX", "GDXJ", "USO", "UNG", "TLT", "IEF", "HYG", "LQD", "EEM", "EFA", "FXI", "KWEB", "EWZ", "EWJ",
    "KRE", "XBI", "ARKK", "IBIT", "FBTC", "ETHA", "XOP", "XHB", "ITB", "JETS", "TSLL", "NVDL",
]
LEVERAGED_ETFS = ["TQQQ", "SQQQ", "SOXL", "SOXS", "SPXL", "SPXS", "TNA", "TZA", "UPRO", "SH", "PSQ", "TSLL", "NVDL"]
STOCK_CANDIDATES = [
    "AAPL", "MSFT", "NVDA", "AMZN", "META", "GOOGL", "TSLA", "AVGO", "AMD", "NFLX", "PLTR", "MU", "INTC", "SMCI",
    "ARM", "QCOM", "TSM", "ORCL", "CRM", "ADBE", "NOW", "UBER", "SHOP", "COIN", "MSTR", "HOOD", "SOFI", "PYPL",
    "XYZ", "BA", "DIS", "NKE", "SBUX", "MCD", "WMT", "COST", "TGT", "HD", "LOW", "JPM", "BAC", "C", "WFC", "GS",
    "MS", "SCHW", "V", "MA", "AXP", "UNH", "LLY", "JNJ", "PFE", "MRK", "ABBV", "NVO", "XOM", "CVX", "OXY", "COP",
    "SLB", "F", "GM", "RIVN", "NIO", "BABA", "PDD", "JD", "CSCO", "IBM", "MRVL", "LRCX", "AMAT", "KLAC", "ANET",
    "DELL", "CVNA", "RDDT", "APP", "CRWD", "PANW", "SNOW", "NET", "DDOG", "ZS", "T", "VZ", "TMUS", "KO", "PEP",
    "PG", "CAT", "GE", "GEV", "DE", "LMT", "RTX", "ABNB", "DASH", "SPOT", "ROKU", "AFRM", "UPST", "MARA", "RIOT",
    "CLSK", "IONQ", "RGTI", "SNAP", "PINS", "LULU", "CMG", "DKNG", "CCL", "AAL", "UAL", "DAL", "LUV", "WBD",
    "ACHR", "JOBY", "ASTS", "RKLB", "SOUN", "VRT", "ON", "TXN", "ADI", "WDC", "STX",
]
# Yahoo continuous front-month futures; mult = dollars per 1.00 of price
# Futures costs per side, in price points: 1 tick of slippage + about $2.50 commission per contract.
FUTURES_TICK = {"ES=F": 0.25, "NQ=F": 0.25, "YM=F": 1.0, "RTY=F": 0.1, "CL=F": 0.01, "NG=F": 0.001, "GC=F": 0.1,
                "SI=F": 0.005, "HG=F": 0.0005, "ZN=F": 1 / 64, "ZB=F": 1 / 32, "ZF=F": 1 / 128, "6E=F": 0.00005,
                "6J=F": 0.0000005, "ZC=F": 0.25, "ZS=F": 0.25}
FUTURES_COMMISSION = 2.50
FUTURES = {
    "ES=F": ("E-mini S&P 500", 50), "NQ=F": ("E-mini Nasdaq-100", 20), "YM=F": ("E-mini Dow", 5),
    "RTY=F": ("E-mini Russell 2000", 50), "CL=F": ("Crude Oil", 1000), "NG=F": ("Natural Gas", 10000),
    "GC=F": ("Gold", 100), "SI=F": ("Silver", 5000), "HG=F": ("Copper", 25000), "ZN=F": ("10-Year T-Note", 1000),
    "ZB=F": ("30-Year T-Bond", 1000), "ZF=F": ("5-Year T-Note", 1000), "6E=F": ("Euro FX", 125000),
    "6J=F": ("Japanese Yen", 12500000), "ZC=F": ("Corn", 50), "ZS=F": ("Soybeans", 50),
}

# ----------------------------------------------------------------- sessions (minutes after midnight, New York)
PRE_START, RTH_OPEN, OR_END, RTH_CLOSE = 240, 570, 600, 960
LIVE_WINDOW = (565, 965)        # live scans 9:25 AM - 4:05 PM ET
EOD_AFTER = 975                 # end-of-day job runs after 4:15 PM ET

# ----------------------------------------------------------------- setup rules
OTE = (0.62, 0.705, 0.79)
STOP_ATR_BUFFER = 0.1           # stop = sweep extreme - 0.1 x 5-minute ATR
WEIGHTS = {                     # Setup Score points (normalized to 0-100)
    "sweep_pd": 20, "sweep_other": 15, "mss": 15, "zone": 10, "ote": 15, "rr": 10,
    "bias": 10, "bias_neutral": 4, "vol": 5, "time": 5, "prox": 10,
}
FILTERS = {"require_ote": True, "min_rr_t1": 1.0, "min_rr_t2": 2.0, "min_score": 0}
TOP_N = 5

# ----------------------------------------------------------------- backtest / simulation
SIM = {
    "entry_start": 600,          # no fills before 10:00
    "entry_cutoff": 930,         # training mode: fills allowed until 3:30 PM (all-day evidence)
    "plan_window_end": 690,      # the original plan window (11:30) for comparison
    "eod_exit": 955,             # open positions close at 3:55 PM
    "partial_at_t1": 0.5,
    "replay_step": 5,            # replay checks every 5 minutes
    # Round-trip cost in percent of price (slippage + fees). Applied to every
    # "net" result. 0.02% per side is about 1 cent on a $50 stock.
    "cost_pct_per_side": 0.02,
}

# Side-by-side improvement tests (every simulated setup is re-run with each).
# The live rules do not change until Ron approves a winner.
TESTS = {
    # ote_mid = current (middle of the FVG/OTE overlap); fvg_edge = first touch of the gap;
    # fvg_ce = gap midpoint; blend = halfway between the gap's near edge and ote_mid (added Nov 3,
    # Ron's idea); ote_62 = first touch of the OTE zone (62% retracement)
    "entries": ["ote_mid", "fvg_edge", "fvg_ce", "blend", "ote_62"],
    "stop_buffers": [0.1, 0.3],                        # ATR beyond the sweep extreme
    # v3 tests (Nov 3): confirmation entry on 1-minute bars (Alpaca in the backtest, Yahoo for
    # the daily replay; futures fall back to 5-minute bars). Recorded as r_confirm / r_runner.
    "confirm_1m": True,
    # Candidate filters for the review (not live rules): midday window, minimum risk, minimum FVG size,
    # VWAP side, "in play" opening relative volume.
    "v3": {"window": (690, 870), "min_risk_pct": 0.3, "min_gap_atr": 0.5, "in_play_rvol": 1.5},
    # Scaled entries: several limit orders, one shared stop and targets. Weights = share of the
    # full position at each price (shallowest first). Results are in R of the full planned risk.
    "ladders": {
        "ladder_equal": [("fvg_edge", 1 / 3), ("blend", 1 / 3), ("ote_mid", 1 / 3)],
        "ladder_deep": [("fvg_edge", 0.2), ("blend", 0.3), ("ote_mid", 0.5)],
    },
}

# Futures 24-hour test (Nov 3, 2026): besides New York (9:30-4:00 ET), futures are also
# replayed in two overnight sessions. Start = minutes after midnight ET; length in minutes.
# Asia starts the evening before the trading day. Stocks and ETFs stay New York only.
SESSIONS_24H = True
FUTURES_SESSIONS = {"Asia": (18 * 60, 360), "London": (2 * 60, 360)}

# ----------------------------------------------------------------- learning
TRAINING_MODE = True
AUTO_TUNE = {                   # Ron chose auto-apply with guardrails (Nov 2, 2026)
    "enabled": True, "min_samples": 20, "delta_r": 0.15, "weight_step": 2, "max_changes": 3,
    "weight_bounds": (0, 30), "min_rr_t2_bounds": (1.5, 3.0), "min_score_bounds": (0, 80),
}
# Dashboard position sizing (Nov 3, 2026): risk up to RISK_PCT of the account per trade, but the
# whole position (all scaled entries together) is capped at MAX_POSITION_PCT of the account value.
RISK_PCT = 1.0
MAX_POSITION_PCT = 5.0
# Side sizing (Nov 3, 2026, Ron: lower risk for shorts, a bit higher for longs). Risk is a share
# of the account; the position cap is the value of all legs together as a share of the account.
SIZING = {"LONG": {"risk_pct": 1.25, "max_position_pct": 5.0},
          "SHORT": {"risk_pct": 0.5, "max_position_pct": 2.5}}

# Short guardrails: a short must pass every check below as well as the normal filters.
# Each check is recorded per setup, so the review shows shorts with and without it.
SHORT_RULES = {
    "enabled": True,
    "require_bearish_bias": True,     # daily trend down (close below a falling 20-day average)
    "require_strong_sweep": True,     # swept the prior-day high, or 2+ levels at once
    "min_rr_t2": 3.0,                 # longs: FILTERS["min_rr_t2"]
    "min_risk_pct": 0.3,              # stop at least 0.3% of price away (costs and noise)
    "not_before": 630,                # no shorts formed before 10:30 ET (New York session)
    "no_leveraged_etfs": True,
}
# Closer management for shorts: full exit at T1, stop to breakeven once the trade is +0.5R,
# and exit after 60 minutes if T1 has not been reached. Longs keep the plan in SIM.
SIDE_MGMT = {"LONG": {}, "SHORT": {"partial_at_t1": 1.0, "be_after_r": 0.5, "time_stop_min": 60}}
DASHBOARD_LADDER = "ladder_deep"   # the scaled-entry plan shown on the dashboard

# ----------------------------------------------------------------- data
# A free Alpaca account (alpaca.markets) gives years of 5-minute stock/ETF history.
# Add ALPACA_KEY_ID and ALPACA_SECRET_KEY as repository secrets to backtest 6 months.
# Without them the backtest uses Yahoo, which keeps only about 60 days of 5-minute bars.
# Futures always come from Yahoo (about 60 days).
ALPACA_FEED = "sip"
