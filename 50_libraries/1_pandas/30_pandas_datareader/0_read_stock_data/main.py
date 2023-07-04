from datetime import datetime
import pandas_datareader.data as web

qkey = "73JMr-Fhopzju62Q3Nvz"

start = datetime(1990, 1, 1)
end = datetime(2020, 3, 7)

symbol = "WIKI/TSLA"
tesla = web.DataReader(symbol, "quandl", start, end, api_key=qkey)

print(tesla)

