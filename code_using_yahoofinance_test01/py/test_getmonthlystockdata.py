# -*- coding: utf-8 -*-
"""
Created on Wed Jul 29 09:25:32 2015

@author: justin.malinchak
"""
import datetime
import pandas as pd
from pandas import DataFrame
from pandas.io.data import DataReader
symbols_list = ['AAPL', 'TSLA', 'YHOO','GOOG', 'MSFT','ALTR','WDC','KLAC']

symbols=[]
for ticker in symbols_list: 
    r = DataReader(ticker, "yahoo", 
                   start=datetime.datetime(2014, 12, 30))
    # add a symbol column
    r['Symbol'] = ticker 
    symbols.append(r)
# concatenate all the dfs
df = pd.concat(symbols)
#define cell with the columns that i need
cell= df[['Symbol','Open','High','Low','Adj Close','Volume']]
#changing sort of Symbol (ascending) and Date(descending) setting Symbol as first column and changing date format
cell.reset_index().sort(['Symbol', 'Date'], ascending=[1,0]).set_index('Symbol').to_csv('stock.csv', date_format='%Y-%m-%d')

print cell
