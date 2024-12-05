import yfinance as yf
from .models import Currency, ExchangeRate


def update_currencies():
    codes = ["USD", "EUR", "PLN", "SGD", "JPY", "GBP"]
    for code in codes:
        Currency.objects.get_or_create(code=code)


def update_exchange_rate(base_currency, quote_currency):
    pair = f"{base_currency}{quote_currency}=X"
    ticker = yf.Ticker(pair)
    data = ticker.history(period="1d")

    if not data.empty:
        price = data['Close'][-1]
        ExchangeRate.objects.update_or_create(
            currency_pair=f"{base_currency}{quote_currency}",
            defaults={'exchange_rate': price}
        )
