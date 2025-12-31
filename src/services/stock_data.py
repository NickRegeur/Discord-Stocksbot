from dataclasses import dataclass
import yfinance as yf


@dataclass
class Quote:
    symbol: str
    price: float
    currency: str
    change: float | None
    change_percent: float | None


def get_quote(symbol: str) -> Quote:
    symbol = symbol.upper().strip()

    t = yf.Ticker(symbol)
    info = t.fast_info

    price = info.get("last_price")
    prev_close = info.get("previous_close")
    currency = info.get("currency", "USD")

    # ---- fallback if fast_info is empty/missing ----
    if price is None or prev_close is None:
        hist = t.history(period="2d", interval="1d")  # 2 closes = last + previous
        if hist is None or hist.empty or "Close" not in hist:
            raise ValueError(f"No price data for {symbol}")

        closes = hist["Close"].dropna()
        if len(closes) == 0:
            raise ValueError(f"No price data for {symbol}")

        price = float(closes.iloc[-1])
        prev_close = float(closes.iloc[-2]) if len(closes) >= 2 else None
    # ----------------------------------------------

    if price is None:
        raise ValueError(f"No price data for {symbol}")

    change = None
    change_percent = None

    if prev_close not in (None, 0):
        change = float(price) - float(prev_close)
        change_percent = (change / float(prev_close)) * 100

    return Quote(
        symbol=symbol,
        price=float(price),
        currency=str(currency),
        change=change,
        change_percent=change_percent,
    )



