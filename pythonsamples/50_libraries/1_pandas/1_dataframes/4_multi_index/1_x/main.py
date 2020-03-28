import pandas as pd

multi = pd.MultiIndex(names=["ticker", "localSymbol"])

data = pd.DataFrame(
    data=None,
    index=multi,
    columns=["bidSize", "bid", "ask", "askSize", "high", "low", "close"],
)

print(data)
