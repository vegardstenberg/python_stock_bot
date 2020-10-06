# -*- coding: utf-8 -*-
"""
Created on Fri Aug  7 19:30:58 2020

@author: Vegard Hansen Stenberg
"""

from bs4 import BeautifulSoup
from requests import get
#from rtstock.stock import Stock
from alpha_vantage.timeseries import TimeSeries
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import datetime
import time
import yfinance as yf

def get_stock_data_yfinance(ticker, period,columns=['Open']):
    obj = yf.Ticker(ticker)
    data = obj.history(period=period)[columns]
    return data.iloc[::-1]

def get_gainers(num):
    url = "https://finance.yahoo.com/gainers?guce_referrer=aHR0cHM6Ly93d3cuZ29vZ2xlLmNvbS8&guce_referrer_sig=AQAAAFuJ0IVKv_Tf8WcVSCR8AzIQueCWedQJ8YZq54QeRZ4zOFIceLyuDev9O0ZtzjGuvPi_mBA0EzVc9pIHExQTM2khJo7QDrC5zNk2gloM8IrhuaQayF2C_DL5Sa95ldMUUYJAQZDSvh-Vo94Kg_G4Xd7DAL8roImPYIjwgAqIYOEN&_guc_consent_skip=1596822014"
    response = get(url)

    soup = BeautifulSoup(response.text, 'lxml')

    tickers = soup.find_all('a', class_='Fw(600) C($linkColor)')
    name = soup.find_all('td', class_='Va(m) Ta(start) Px(10px) Fz(s)')

    gainers_tickers = []

    print("Todays Gainers:")
    for i in range(num):
        print("Symbol:", tickers[i].text, "Name:", name[i].text)
        gainers_tickers.append(tickers[i].text)

    return gainers_tickers

def get_stock_data_alpha_vantage(ticker):
    alpha_key = "ZPMRPROK30QKNPIG"
    timeseries = TimeSeries(key=alpha_key, output_format='pandas')
    data, meta_data = timeseries.get_intraday(symbol=ticker, interval='1min', outputsize='full')

    return data['4. close']
