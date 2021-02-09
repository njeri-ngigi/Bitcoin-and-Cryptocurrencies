import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from datetime import datetime

BITCOIN_PATH = "/Users/njeringigi/Downloads/archive/bitcoin_price.csv"
ETHEREUM_PATH = "/Users/njeringigi/Downloads/archive/ethereum_price.csv"
BITCOIN_CASH_PATH = "/Users/njeringigi/Downloads/archive/bitcoin_cash_price.csv"
LITECOIN_PATH = "/Users/njeringigi/Downloads/archive/litecoin_price.csv"

def open_file_and_plot_graph(path):
    col_list = ["Date", "Close"]
    data = pd.read_csv(path, usecols=col_list)
    
    price = list(data.Close)
    dates = list(data.Date)
    
    fdates = [datetime.strptime(d, '%b %d, %Y') for d in dates]
    xdates = mdates.date2num(fdates)
    
    
    return price, xdates
    
btc_price, btc_dates = open_file_and_plot_graph(BITCOIN_PATH)
eth_price, eth_dates = open_file_and_plot_graph(ETHEREUM_PATH)
btc_cash_price, btc_cash_dates = open_file_and_plot_graph(BITCOIN_CASH_PATH)
ltc_price, ltc_dates = open_file_and_plot_graph(LITECOIN_PATH)
    
years = mdates.YearLocator()   # every year
months = mdates.MonthLocator()  # every month
years_fmt = mdates.DateFormatter('%Y')

formatter = mdates.DateFormatter('%Y')
figure, axes = plt.subplots()
axes.xaxis.set_major_formatter(formatter)
plt.setp(axes.get_xticklabels(), rotation = 15) 
axes.plot(btc_dates, btc_price, label = "Bitcoin")
axes.plot(eth_dates, eth_price, label = "Ethereum") 
axes.plot(btc_cash_dates, btc_cash_price, label = "Bitcoin Cash") 
axes.plot(ltc_dates, ltc_price, label = "Litecoin") 
axes.set_xlabel("Years between 2013-2018")
axes.set_ylabel("Price Per Unit in $")
axes.legend()
axes.xaxis.set_major_locator(years)
axes.xaxis.set_major_formatter(years_fmt)
axes.xaxis.set_minor_locator(months)

fig = plt.gcf()
fig.set_size_inches(18.5, 10.5)
fig.savefig('test2png.png', dpi=100)

plt.title("A graph showing the variation of prices of 4 cryptocurrencies from the year 2013 to 2018")
plt.show() 

