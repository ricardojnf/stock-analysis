import yfinance as yf
import stock_info

f = open('tickers_list.txt', 'r')
lines = f.readlines()
wr = open('ticker_list.txt', 'w')
arr = list()
for l in lines:
    try:
        hist = stock_info.get_stock_history(l.split('\t')[0], timeRange='5y')
        print(hist.values[0][3])
        wr.writelines(l)
    except Exception:
        print("NOT FOUND")
        pass
