# -*- coding: utf-8 -*-
"""
Created on Tue Jul 21 14:01:52 2015

@author: justin.malinchak
"""
import os
#os.environ["FRED_API_KEY"] = "63ef8588c3a78e956fb156c8a1603152"
#print os.environ['FRED_API_KEY']

from fredapi import Fred
fred = Fred()
import pandas as pd
pd.options.display.max_colwidth = 60

#%matplotlib inline
import matplotlib.pyplot as plt
#from IPython.core.pylabtools import figsize
#figsize(20, 5)

s = fred.get_series('DSPIC96', observation_start='1960-01-01', observation_end='2015-07-01')

print s.tail()

print '------------------------'
info = fred.get_series_info('DSPIC96')
print len(info)
for k,vinfo in info.iteritems():
    print k,vinfo

df_gdp = fred.get_series_as_of_date('GDP', '2/1/2015')
print df_gdp

df_search = fred.search('income').T
print df_search