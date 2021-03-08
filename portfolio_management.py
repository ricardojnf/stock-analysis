from yahoo_fin import stock_info as yf
from collections import defaultdict
from datetime import datetime
import stock_analyser as sa

class Portfolio:

    def __init__(self):
        self.orders = defaultdict(list)
        self.portfolio = {}
    

    def add_buy_order(self, ticker, nShares, date):
        to_date = datetime.strptime(date, '%m/%d/%Y')
        share_price = sa.get_price_at_date(ticker, date)
        self.orders[to_date].append((ticker, nShares * share_price, 'buy'))

        if ticker in self.portfolio:
            self.portfolio[ticker] += nShares
        else:
            self.portfolio[ticker] = nShares
    

    def add_sell_order(self, ticker, nShares, date):
        if ticker in self.portfolio and self.portfolio[ticker] >= nShares:
            self.portfolio[ticker] -= nShares
        else:
            raise Exception(f'Cannot sell {ticker} shares, not enough shares to sell')

        to_date = datetime.strptime(date, '%m/%d/%Y')
        share_price = sa.get_price_at_date(ticker, date)
        self.orders[to_date].append((ticker, nShares * share_price, 'sell'))
        

