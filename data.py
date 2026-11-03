"""Price data: Yahoo Finance (yfinance) for live scans, daily bars, futures and the
last ~60 days of 5-minute bars; Alpaca (free account) for 6+ months of 5-minute
stock/ETF history when ALPACA_KEY_ID / ALPACA_SECRET_KEY are set.

Every intraday series is returned as a list of engine.Bar in New York time.
"""
from __future__ import annotations

import datetime as dt
import gzip
import logging
import os
import pickle
import time
from pathlib import Path
from zoneinfo import ZoneInfo

import pandas as pd

import config as C
from engine import Bar

NY = ZoneInfo("America/New_York")
ROOT = Path(__file__).resolve().parent
CACHE = ROOT / "cache"
log = logging.getLogger("data")


def _to_bars(df: pd.DataFrame) -> list:
    if df is None or df.empty:
        return []
    df = df.dropna(subset=["Open", "High", "Low", "Close"])
    idx = df.index
    if idx.tz is None:
        idx = idx.tz_localize("UTC")
    idx = idx.tz_convert(NY)
    out = []
    for t, o, h, l, c, v in zip(idx, df["Open"], df["High"], df["Low"], df["Close"],
                                df["Volume"] if "Volume" in df else [0] * len(df)):
        out.append(Bar(int(t.timestamp()), t.strftime("%Y-%m-%d"), t.hour * 60 + t.minute,
                       float(o), float(h), float(l), float(c), float(v or 0)))
    return out


def _split(raw: pd.DataFrame, tickers: list[str]) -> dict:
    out = {}
    if raw is None or raw.empty:
        return out
    if isinstance(raw.columns, pd.MultiIndex):
        lv0 = set(raw.columns.get_level_values(0))
        for t in tickers:
            if t in lv0:
                out[t] = raw[t]
    elif len(tickers) == 1:
        out[tickers[0]] = raw
    return out


def yahoo_intraday(tickers: list[str], period="5d", interval="5m") -> dict[str, list]:
    import yfinance as yf
    out = {}
    for i in range(0, len(tickers), 40):
        batch = tickers[i:i + 40]
        try:
            raw = yf.download(batch, period=period, interval=interval, prepost=True, group_by="ticker",
                              auto_adjust=False, progress=False, threads=True)
        except Exception as e:   # network hiccup: skip the batch, keep going
            log.warning("Yahoo intraday batch failed: %s", e)
            continue
        for t, df in _split(raw, batch).items():
            bars = _to_bars(df)
            if bars:
                out[t] = bars
    return out


def yahoo_daily(tickers: list[str], period="1y") -> dict[str, pd.DataFrame]:
    """Completed daily bars: DataFrame with date index (str), Close, Volume."""
    import yfinance as yf
    out = {}
    for i in range(0, len(tickers), 60):
        batch = tickers[i:i + 60]
        try:
            raw = yf.download(batch, period=period, interval="1d", group_by="ticker", auto_adjust=False,
                              progress=False, threads=True)
        except Exception as e:
            log.warning("Yahoo daily batch failed: %s", e)
            continue
        for t, df in _split(raw, batch).items():
            df = df.dropna(subset=["Close"])
            if df.empty:
                continue
            df = df.copy()
            df.index = [d.strftime("%Y-%m-%d") for d in df.index]
            out[t] = df[["Close", "Volume"]]
    return out


# ----------------------------------------------------------------- Alpaca (6+ months of 5-minute bars)
def alpaca_enabled() -> bool:
    return bool(os.environ.get("ALPACA_KEY_ID", "").strip() and os.environ.get("ALPACA_SECRET_KEY", "").strip())


def alpaca_5m(ticker: str, start: dt.date, end: dt.date) -> list:
    """5-minute bars incl. extended hours from Alpaca's market-data API (split-adjusted)."""
    import requests
    cache = CACHE / f"alpaca_{ticker}_{start}_{end}.pkl.gz"
    if cache.exists():
        return pickle.loads(gzip.decompress(cache.read_bytes()))
    # .strip(): a key pasted into GitHub secrets with a trailing Enter breaks the request header
    hdr = {"APCA-API-KEY-ID": os.environ["ALPACA_KEY_ID"].strip(), "APCA-API-SECRET-KEY": os.environ["ALPACA_SECRET_KEY"].strip()}
    params = {"timeframe": "5Min", "start": f"{start}T00:00:00Z", "end": f"{end}T23:59:00Z", "limit": 10000,
              "adjustment": "split", "feed": C.ALPACA_FEED, "sort": "asc"}
    rows, token = [], None
    url = f"https://data.alpaca.markets/v2/stocks/{ticker}/bars"
    for _ in range(100):
        if token:
            params["page_token"] = token
        for attempt in range(4):
            r = requests.get(url, headers=hdr, params=params, timeout=30)
            if r.status_code == 429:
                time.sleep(5 * (attempt + 1)); continue
            break
        if r.status_code != 200:
            log.warning("Alpaca %s: HTTP %s %s", ticker, r.status_code, r.text[:200])
            return []
        j = r.json()
        rows += j.get("bars") or []
        token = j.get("next_page_token")
        if not token:
            break
        time.sleep(0.35)          # stay under 200 requests per minute
    out = []
    for b in rows:
        t = pd.Timestamp(b["t"]).tz_convert(NY)
        out.append(Bar(int(t.timestamp()), t.strftime("%Y-%m-%d"), t.hour * 60 + t.minute,
                       float(b["o"]), float(b["h"]), float(b["l"]), float(b["c"]), float(b.get("v") or 0)))
    CACHE.mkdir(exist_ok=True)
    cache.write_bytes(gzip.compress(pickle.dumps(out)))
    return out
