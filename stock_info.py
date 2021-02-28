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

print(get_stock_info('AMZN'))