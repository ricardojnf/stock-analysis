from yahoo_fin import stock_info as yf
from datetime import datetime, timedelta

SECONDS_IN_A_YEAR = 31536000

def get_value_growth(portfolio, startDate, endDate):
    startPrice = 0.0
    endPrice = 0.0
    for ticker in portfolio.keys():
        hist = yf.get_data(ticker, start_date=startDate, 
                                    end_date=endDate)
        
        startPrice += hist['close'][0] * portfolio[ticker]
        try:
            div_info = yf.get_dividends(ticker, start_date=startDate, 
                                    end_date=endDate)
            print(div_info)
            div_value = sum(div_info['dividend'])
            print(div_value)
        except Exception:
            div_value = 0.0

        endPrice += (div_value + hist['close'][-1]) * portfolio[ticker]
    
    return startPrice, endPrice


def compound_annual_growth_rate(portfolio, startDate, endDate):

    startPrice, endPrice = get_value_growth(portfolio, 
                                            startDate,
                                            endDate)
    
    start = datetime.strptime(startDate, '%m/%d/%Y')
    end = datetime.strptime(endDate, '%m/%d/%Y')
    elapsedTime = divmod((end - start).total_seconds(), SECONDS_IN_A_YEAR)
    years = elapsedTime[0]+elapsedTime[1]/SECONDS_IN_A_YEAR
    print(years)
    return ((endPrice / startPrice)**(1/years)) - 1


def annual_return_rate_by_year(portfolio, year):
    return compound_annual_growth_rate(portfolio, 
                                startDate=f'01/01/{year}',
                                endDate=f'01/01/{year+1}')

portfolio = {
    'VOO': 1,
}

hist = yf.get_data('VOOG', start_date=f'01/01/2020', 
                                    end_date=f'01/01/2021')
print(hist)