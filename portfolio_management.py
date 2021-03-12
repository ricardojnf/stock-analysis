from yahoo_fin import stock_info as yf
from collections import defaultdict
from datetime import datetime
import pandas as pd
import stock_analyser as sa
import plot_lib as pl

class Portfolio:

    def __init__(self):
        self.orders = defaultdict(list)
        self.portfolio = {}


    def get_portfolio_distribution(self):
        pl.portfolio_pie_chart(self.portfolio)


    def visualize_value_growth(self, start_date=None):
        date_range, invested_money, value_money = self.__portfolio_over_time__()
        pl.plot_portfolio_evolution(date_range, invested_money, value_money)
    

    def add_buy_order(self, ticker, nShares, date):
        to_date = datetime.strptime(date, '%m/%d/%Y')
        
        self.orders[to_date].append((ticker, nShares, 'buy'))

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
        self.orders[to_date].append((ticker, nShares, 'sell'))
    

    ###########################################################################
    #######################    PRIVATE METHODS    #############################
    ###########################################################################

    def __portfolio_over_time__(self, start_date=None):

        if not start_date:
            start_date = sorted(list(self.orders.keys()))[0]
        
        date_range = pd.date_range(start_date, datetime.today(), freq='D')
        portf = {}

        invested_money = [0]*len(date_range)
        value_money = [0]*len(date_range)

        for i in range(len(date_range)):
            if i > 0:
                invested_money[i] = invested_money[i-1]
            if date_range[i] in self.orders.keys():
                for tup in self.orders[date_range[i]]:
                    mult = 1
                    if tup[2] == 'sell':
                        mult = -1
                    if tup[0] in portf.keys():
                        portf[tup[0]] += tup[1]*mult
                    else:
                        portf[tup[0]] = tup[1]*mult
                    invested_money[i] += sa.get_price_at_date(tup[0], 
                                        date_range[i]) * tup[1] * mult
                
            for key, value in portf.items():
                try:
                    price = sa.get_price_at_date(key, 
                                        date_range[i]) * value
                except Exception:
                    price = value_money[i-1]
                value_money[i] += price

        return date_range, invested_money, value_money

        

test = Portfolio()
test.add_buy_order('VOO', 20, '03/06/2019')
test.add_buy_order('VOOG', 20, '03/06/2019')
test.add_buy_order('MSFT', 20, '03/06/2019')
test.add_buy_order('AAPL', 20, '03/06/2019')
test.add_buy_order('AMZN', 20, '03/06/2019')
test.get_portfolio_distribution()