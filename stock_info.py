import yfinance as yf

def get_stock_info(symbol):
    '''
    Returns basic info about the stock requested

    Parameters
    ----------
    symbol : str
        Symbol representing the stock in the stock market

    Returns
    -------
    list
        A list of the basic info about the stock
    '''

    key_info = ['shortName', 'sector', 'previousClose', 
                'exDividendDate', 'dividendYield']
    st_info = yf.Ticker(symbol).info
    return [st_info[key] for key in key_info]


def get_stock_history(symbol, timeRange='max', dividendInfo=False,
                        stockSplit=False):
    '''
    Returns basic info about the stock requested

    Parameters
    ----------
    symbol : str
        Symbol representing the stock in the stock market
    
    period : str
        Time range of the information.
        Valid periods: 1d,5d,1mo,3mo,6mo,1y,2y,5y,10y,ytd,max
    
    dividendInfo : bool
        Indicates if we want to filter only the dates where it was paid
        dividends

    Returns
    -------
    Pandas DataFrame
        A data frame containing historical information about the price values
        of the stock
    '''

    st_hist = yf.Ticker(symbol).history(period=timeRange)

    if dividendInfo:
        st_div_hist = st_hist['Dividends'] != 0.0
        print(st_div_hist)
    if stockSplit:
        st_split_hist = st_hist['Stock Splits'] != 0.0
    
    try:
        st_hist = st_hist[st_div_hist | st_split_hist]
    except UnboundLocalError:
        pass
    
    return st_hist
