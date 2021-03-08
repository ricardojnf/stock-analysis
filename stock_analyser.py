from yahoo_fin import stock_info as yf
from datetime import datetime, timedelta

SECONDS_IN_A_YEAR = 31536000

def get_value_growth(ticker, startDate, endDate=None):

    if not endDate:
        now = datetime.now()
        endDate = f'{now.month}/{now.day}/{now.year}'

    hist = yf.get_data(ticker, start_date=startDate, 
                                end_date=endDate)
    startPrice = hist['close'][0]
    endPrice = hist['close'][-1]
    
    return startPrice, endPrice


def growth_rate(ticker, startDate, endDate=None):
    if not endDate:
        now = datetime.now()
        endDate = f'{now.month}/{now.day}/{now.year}'
    
    startPrice, endPrice = get_value_growth(ticker, 
                                            startDate,
                                            endDate)
    return (endPrice / startPrice) - 1


def compound_annual_growth_rate(ticker, startDate, endDate=None):

    if not endDate:
        now = datetime.now()
        endDate = f'{now.month}/{now.day}/{now.year}'

    startPrice, endPrice = get_value_growth(ticker, 
                                            startDate,
                                            endDate)
    
    start = datetime.strptime(startDate, '%m/%d/%Y')
    end = datetime.strptime(endDate, '%m/%d/%Y')
    elapsedTime = divmod((end - start).total_seconds(), SECONDS_IN_A_YEAR)
    years = elapsedTime[0]+elapsedTime[1]/SECONDS_IN_A_YEAR
    print(years)

    return ((endPrice / startPrice)**(1/years)) - 1


def annual_return_rate_by_year(ticker, year):
    return compound_annual_growth_rate(ticker, 
                                startDate=f'01/01/{year}',
                                endDate=f'01/01/{year+1}')


def get_PE_ratio(ticker):

    info = yf.get_analysts_info(ticker)['Earnings History']
    date = info.columns[-1]
    eps = sum(map(float, info.loc[1][1:]))
    st_info = yf.get_data(ticker, start_date=date)
    share_price = st_info['close'][-1]

    return share_price / eps


def get_price_at_date(ticker, date):
    to_date = datetime.strptime(date, '%m/%d/%Y')
    hist = yf.get_data(ticker, 
            start_date=f'{to_date.month}/{to_date.day}/{to_date.year}',
            end_date=f'{to_date.month}/{to_date.day + 1}/{to_date.year}')
    
    return hist['close'][0]

