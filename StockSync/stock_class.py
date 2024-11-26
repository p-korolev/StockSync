import yfinance as yf

class Stock:
    def __init__(self, ticker: str, range: str):
        '''
        Creates stock object under ticker name and retrieves info
        based on time range indicated
        '''  
        self.ticker = ticker 
        self.range = range
        load = yf.Ticker(self.ticker)
        self.history = load.history(period = range)

    def get_info(self):
        print(self.history)

    def get_open_list(self):
        return list(self.history["Open"])

    def get_close_list(self):
        return list(self.history["Close"]) 

    def get_vol_list(self):
        return list(self.history["Volume"])
    

