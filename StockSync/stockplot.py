from stock_class import Stock 
from reg_class import Regression
import matplotlib.pyplot as plt


def plot(stock1: str, stock2: str, range: str):
    '''
    Plots simple regression model based on stock prices from
    indicated time range 
    '''

    x_stock = Stock(stock1, range)
    y_stock = Stock(stock2, range)
    xvals = x_stock.get_close_list()
    yvals = y_stock.get_close_list()

    regdata = Regression(xvals, yvals)
    r_squared = regdata.rs 
    #r_deviation = regdata.sd 

    # creating list of y values of regression function
    y_reg = [regdata.b1*x + regdata.b0 for x in xvals]

    plt.figure(figsize = (15,5))
    plt.plot(xvals, yvals, marker = 'o', linestyle = 'None')
    plt.plot(xvals, y_reg, color = 'orange')
    plt.xlabel(x_stock.ticker)
    plt.ylabel(y_stock.ticker)
    plt.title(x_stock.ticker + "/" + y_stock.ticker + " Price Linear Regression Model")

    # Legend for metrics
    # plt.legend(loc = 'upper right')

    plt.subplots_adjust(right = 0.70)
    
    metrics_text = (
        'Regression Model Characteristics:\n'
        f'\n'
        f'Model Function: {regdata}\n'
        f'R-squared Coefficient: {r_squared}\n'
    )

    plt.text(
        x = max(xvals) + ((max(xvals) - min(xvals))/11.5),
        y = (max(yvals) + min(yvals)) / 2,
        s = metrics_text,
        fontsize = 10,
        bbox = dict(facecolor = 'lightgray', alpha = 0.5)
    )

    plt.show()



    