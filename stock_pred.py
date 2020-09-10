# -*- coding: utf-8 -*-
"""
Created on Tue Aug 25 13:30:53 2020

@author: Vagard Stenberg
"""

import stock_info as si
import time

stock_name = ""

for gainers in si.get_gainers(25):
    try:
        stock = si.get_stock_data(gainers)
        stock_name = gainers
        break;
    except:
        print("Could not invest in:", gainers)

if(stock.empty):
    print("Found no stocks at this time... shutting down...")
    exit()

buying_price = []

money = 10000

def SMA(days):
    s = 0
    for i in range(days):
        s += stock[i+1]
    s = s / days
    return s

if(SMA(200) < SMA(50)):
    print("invest!", stock_name, stock[0])
    buying_price = stock[0]
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
    
print("SMA 200:", SMA(200))
print("SMA 50:", SMA(50))