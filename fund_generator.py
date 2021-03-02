import yfinance as yf
import stock_info
from collections import defaultdict
import itertools

MAX_NUMBER_STOCKS = 30

class Fund:
    def __init__(self, identifier):
        self.identifier = identifier
        self.orders = list()
        self.fund = defaultdict()

    def setFund(self, stockDict):
        self.fund = stockDict
    
    def generateDefaultFund(self):
        self.__findBestFund()

    # -------- Private Methods ---------
    def __generateCombStocks(self):
        tickers = list()
        with open('tickers_list.txt', 'r') as f:
            stocks = f.readlines()
            for stock in stocks:
                tickers.append(stock.split('\t')[0])
            
            comb = itertools.combinations(tickers, MAX_NUMBER_STOCKS)
        
        return comb

    def __findBestFund(self):
        growth = 0.0
        combs = self.__generateCombStocks()
        for comb in combs:
            startPrice = 0.0
            endPrice = 0.0
            for stock in comb:
                try:
                    hist = stock_info.get_stock_history(stock, timeRange='5y')
                    startPrice += hist.values[0][3] * (1/MAX_NUMBER_STOCKS)
                    endPrice += hist.values[-1][3] * (1/MAX_NUMBER_STOCKS)
                except Exception:
                    pass
            if endPrice - startPrice > growth:
                growth = endPrice - startPrice
                bestComb = comb
        
        print(growth)
        print(bestComb)

