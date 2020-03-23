from datetime import datetime
import pandas_datareader.data as web


class DataReader:
    qkey = "73JMr-Fhopzju62Q3Nvz"

    def get_stock_data(self, ticker, start=datetime(1990, 1, 1), end=datetime.now()):
        symbol = f"WIKI/{ticker}"
        return web.DataReader(symbol, "quandl", start, end, api_key=self.qkey)
