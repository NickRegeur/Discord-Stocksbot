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
    info = t.fast_info  # fast, but sometimes missing fields

    price = info.get("last_price")
    prev_close = info.get("previous_close")
    currency = info.get("currency", "USD")

    if price is None:
        raise ValueError(f"No price data for {symbol}")

    change = None
    change_percent = None

    if prev_close not in (None, 0) and price is not None:
        change = float(price) - float(prev_close)
        change_percent = (change / float(prev_close)) * 100

    return Quote(
        symbol=symbol,
        price=float(price),
        currency=str(currency),
        change=change,
        change_percent=change_percent,
    )



