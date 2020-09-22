# -*- coding: utf-8 -*-
"""
Created on Tue Aug 25 13:30:53 2020

@author: Vagard Stenberg
"""

import stock_info as si
import time

stock_name = ""
stock = 0

potential_stocks = []
invested_stocks = []

for gainers in si.get_gainers(25):
    try:
        stock = si.get_stock_data(gainers)
        stock_name = gainers

        print(stock[0])

        potential_stocks.append([stock_name, stock])
    except ValueError as e:
        if(str(e) == "Thank you for using Alpha Vantage! Our standard API call frequency is 5 calls per minute and 500 calls per day. Please visit https://www.alphavantage.co/premium/ if you would like to target a higher API call frequency."):
            print("Over the max amount of calls")
            #potential_stocks.append[[gainers, si.get_stock_data[gainers]]]

        print("Could not invest in:", gainers)

potential_stocks.append([stock_name, stock[0]])

if(stock.empty):
    print("Found no stocks at this time... shutting down...")
    exit()

buying_price = []

money = 10000

def SMA(days, stonk):
    s = 0
    for i in range(days):
        s += stonk[i+1]
    s = s / days
    return s

for potentials in potential_stocks:
    if(SMA(200, potentials[1]) < SMA(50, potentials[1])):
        print("invest!", potentials[0], potentials[1][0])
        invested_stocks.append(potentials[0], potentials[1][0])

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

print(potential_stocks)

print(stock[0])
print(gainers)
print("SMA 200:", SMA(200))
print("SMA 50:", SMA(50))
