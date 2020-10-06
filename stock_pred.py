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

investing = True

def find_potentials_alpha_vantage():
    for gainers in si.get_gainers(25):
        try:
            stock = si.get_stock_data_alpha_vantage(gainers)
            stock_name = gainers

            print(stock[0])

            potential_stocks.append([stock_name, stock])
        except ValueError as e:
            if(str(e) == "Thank you for using Alpha Vantage! Our standard API call frequency is 5 calls per minute and 500 calls per day. Please visit https://www.alphavantage.co/premium/ if you would like to target a higher API call frequency."):
                print("Over the max amount of calls", gainers)
            else:
                print("Could not invest in:", gainers)

def find_potentials_yfinance():
    for gainers in si.get_gainers(25):
        try:
            stock = si.get_stock_data_yfinance(gainers, period='200d')
            stock_name = gainers

            potential_stocks.append([stock_name, stock['Open']])
        except ValueError as e:
            print("Could not invest in:", gainers)


def SMA(days, stonk):
    s = 0
    for i in range(days):
        s += stonk[i+1]
    s = s / days
    return s


def find_investments():
    for potentials in potential_stocks:
        print(SMA(20, potentials[1]))
        if(SMA(20, potentials[1]) < SMA(5, potentials[1])):
            print("invest!", potentials[0], potentials[1][0])
            invested_stocks.append([potentials[0], potentials[1][0]])

find_potentials_yfinance()
find_investments()

while investing:
    print("Doing some research...")
    time.sleep(300)
    for i in range(len(invested_stocks)):
        bought_price = invested_stocks[i][1]
        current_price = si.get_stock_data_yfinance(gainers, period='2d')[0]

        print(current_price)

        pros_change = ((current_price[0] - bought_price) / bought_price) * 100

        print("Stock:", invested_stocks[i][0], "Bought_price:", bought_price, "Current_price:", current_price[0], "Pros_schange:", pros_change)

        if(pros_change > 2):
            print("Sold at a profit of", current_price - bought_price)
            invested_stocks.pop(i)
        elif(pros_change < -2):
            print("Sold at a change of", current_price - bought_price)
            invested_stocks.pop(i)
