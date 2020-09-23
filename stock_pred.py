# -*- coding: utf-8 -*-
"""
Created on Tue Aug 25 13:30:53 2020

@author: Vegard Hansen Stenberg
"""

import stock_info as si
import time

stock_name = ""
stock = 0

potential_stocks = []
invested_stocks = []

money = 10000

for gainers in si.get_gainers(25):
    try:
        stock = si.get_stock_data(gainers)
        stock_name = gainers

        print(stock[0])

        potential_stocks.append([stock_name, stock])
    except ValueError as e:
        if(str(e) == "Thank you for using Alpha Vantage! Our standard API call frequency is 5 calls per minute and 500 calls per day. Please visit https://www.alphavantage.co/premium/ if you would like to target a higher API call frequency."):
            print("Over the max amount of calls", gainers)
        else:
            print("Could not invest in:", gainers)

if(stock.empty):
    print("Found no stocks at this time... shutting down...")
    exit()

def SMA(days, stonk):
    s = 0
    for i in range(days):
        s += stonk[i+1]
    s = s / days
    return s

print(potential_stocks)
print(potential_stocks[0][1][0])
for potentials in potential_stocks:
    print("SMA 20", SMA(20, potentials[1]))
    print("SMA 5", SMA(5, potentials[1]))
    if(SMA(20, potentials[1]) < SMA(5, potentials[1])):
        print("invest!", potentials[0], potentials[1][0])
        invested_stocks.append([potentials[0], potentials[1][0]])
print(invested_stocks)

"""
while True:
    stock = si.get_stock_data(stock_name)
    price = stock[0]
    if ((price - buying_price) / buying_price) * 100 > 2:
        print("Sold at a profit of", price - buying_price)
        buying_price = 0
        break;
    elif(SMA(200) > SMA(50) and buying_price != 0):
        print("Sold at a loss of", buying_price - stock[0])
        buying_price = 0
        break;
    time.sleep(600)
"""
