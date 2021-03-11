import matplotlib.pyplot as plt
from yahoo_fin import stock_info as yf

def portfolio_pie_chart(portfolio):

    plt.figure(figsize=(6,5))
    plt.title('Portfolio Pie Chart')
    plt.pie(portfolio.values(), labels=portfolio.keys(),
                autopct='%1.1f%%')
    plt.show()
    plt.close()


def plot_portfolio_evolution(timestamps, invested_money, value_money):
    
    plt.figure(figsize=(6,5))
    plt.title('Portfolio Evolution over time')
    plt.plot(timestamps, invested_money, label='Invested Money')
    plt.plot(timestamps, value_money, label='Portfolio Value')
    plt.xticks(rotation=45)
    plt.show()
    plt.close()