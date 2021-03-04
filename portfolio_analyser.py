import yfinance as yf
import stock_info
from datetime import datetime, timedelta

def calculate_year_growth_rate(portfolio, year):

    startDate = f"{year}-01-01"
    now = datetime.now()
    currYear = now.year
    if year == currYear:
        endDate = f"{currYear}-{now.month}-{now.day}"
    else:
        endDate = f"{year}-12-31"
    
    startPrice = 0.0
    endPrice = 0.0
    for ticker in portfolio.keys():
        hist = yf.Ticker(ticker).history(start=startDate, 
                                        end=endDate)
        startPrice += hist.values[0][3] * portfolio[ticker]

        div_info = hist[hist['Dividends'] != 0.0]
        endPrice += (sum(div_info['Dividends']) + hist.values[-1][3]) * portfolio[ticker]
    
    return ((endPrice - startPrice) / startPrice) * 100.0


def calculate_yearly_growth_rate(portfolio, timeRange):
    
    if timeRange[-1] != 'y':
        raise Exception('Time range should be in years. Example: \'5y\'')
    
    growth = 1
    currYear = datetime.now().year
    startYear = currYear - int(timeRange[:-1])
    for y in range(startYear, currYear):
        print(calculate_year_growth_rate(portfolio, y))
        growth *= 1 + (calculate_year_growth_rate(portfolio, y) / 100)

    return (pow(growth, 1 / int(timeRange[:-1])) - 1 ) * 100.0


portfolio = {
    'VOOG': 1,
}

print(calculate_yearly_growth_rate(portfolio, '5y'))
