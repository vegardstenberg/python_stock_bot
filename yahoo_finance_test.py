import yfinance as yf


def get_stock_data_yfinance(ticker, period,columns=['Open']):
    obj = yf.Ticker(ticker)
    data = obj.history(period=period)[columns]
    return data.iloc[::-1]



import pandas as pd
from alpha_vantage.timeseries import TimeSeries
from alpha_vantage.foreignexchange import ForeignExchange
import matplotlib.pyplot as plt

api_key = 'ZPMRPROK30QKNPIG'
ts = TimeSeries(key=api_key, output_format='pandas')
fx = ForeignExchange(key=api_key, output_format='pandas')

def get_price(ticker,columns=['05. price','07. latest trading day']):
    '''
    Returns a DataFrame of prices for ticker on Alpha Vantage API
    '''
    data, meta_data= ts.get_quote_endpoint(ticker)
    data.reset_index(inplace=True)
    data = data[columns]
    data.columns = ['price', 'date']
    data.set_index('date', inplace=True)
    return data

print(get_stock_data_yfinance("AAPL", period='2d')['Open'][0])
