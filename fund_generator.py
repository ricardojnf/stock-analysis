import yfinance as yf
import stock_info
from collections import defaultdict
import itertools

def calculate_yearly_growth_rate(portfolio, timeRange):
    
    startPrice = 0.0
    endPrice = 0.0
    try:
        for ticker in portfolio.keys():
            hist = stock_info.get_stock_history(ticker, timeRange)
            print(hist)
            stock_time_range = hist.index[-1].year - hist.index[0].year
            if stock_time_range < int(timeRange[:-1]):
                raise Exception("Time range not possible")
            startPrice += hist.values[0][3] * portfolio[ticker]
            endPrice += hist.values[-1][3] * portfolio[ticker]
    except Exception as e:
        print(e)
        print(f"Recalculating for {stock_time_range}y")
        return calculate_yearly_growth_rate(portfolio, f"{stock_time_range}y")
    
    return (((endPrice - startPrice) / startPrice) * 100) / stock_time_range

portfolio = {
    'VOO': 1
}

print(calculate_yearly_growth_rate(portfolio, '3y'))

