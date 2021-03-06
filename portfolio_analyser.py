import yfinance as yf
from datetime import datetime, timedelta

SECONDS_IN_A_YEAR = 31536000

def get_value_growth(portfolio, startDate, endDate):
    startPrice = 0.0
    endPrice = 0.0
    for ticker in portfolio.keys():
        hist = yf.Ticker(ticker).history(start=startDate, 
                                        end=endDate)
        print(hist)
        startPrice += hist['Close'][0] * portfolio[ticker]
        div_info = hist[hist['Dividends'] != 0.0]
        endPrice += (sum(div_info['Dividends']) + hist['Close'][-1]) * portfolio[ticker]
    
    return startPrice, endPrice


def compound_annual_growth_rate(portfolio, startDate, endDate):

    startPrice, endPrice = get_value_growth(portfolio, 
                                            startDate,
                                            endDate)
    
    start = datetime.strptime(startDate, '%Y-%m-%d')
    end = datetime.strptime(endDate, '%Y-%m-%d')
    elapsedTime = divmod((end - start).total_seconds(), SECONDS_IN_A_YEAR)
    years = elapsedTime[0]+elapsedTime[1]/SECONDS_IN_A_YEAR
    print(years)
    return ((endPrice / startPrice)**(1/years)) - 1


def annual_return_rate_by_year(portfolio, year):
    return compound_annual_growth_rate(portfolio, 
                                startDate=f'{year}-01-01',
                                endDate=f'{year+1}-01-01')

portfolio = {
    'VOOG': 1,
}

print(compound_annual_growth_rate(portfolio, 
                                startDate='2020-01-01',
                                endDate='2021-01-01'))