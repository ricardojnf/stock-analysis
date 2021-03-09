import matplotlib.pyplot as plt


def portfolio_pie_chart(portfolio):

    plt.figure(figsize=(6,5))
    plt.title('Portfolio Pie Chart')
    plt.pie(portfolio.values(), labels=portfolio.keys(),
                autopct='%1.1f%%')
    plt.show()
    plt.close()


def plot_portfolio_evolution(portfolio):
    plt.figure(figsize=(6,5))
    plt.title('Portfolio Evolution over time')
    
    plt.show()
    plt.close()