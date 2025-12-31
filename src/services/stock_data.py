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

    ticker = yf.Ticker(symbol)

    info = ticker.fast_info

    price = info.get("last_price")
    currency = info.get("currency", "USD")

    prev_close = info.get("previous_close")

    change = None
    change_percent = None
    if price is not None and prev_close not in (None, 0):
        change = price - prev_close
        change_percent = (change / prev_close) * 100

    if price is None:
        raise ValueError(f"Couldn't fetch price for symbol '{symbol}'")

    return Quote(
        symbol=symbol,
        price=float(price),
        currency=str(currency),
        change=None if change is None else float(change),
        change_percent=None if change_percent is None else float(change_percent),
    )



