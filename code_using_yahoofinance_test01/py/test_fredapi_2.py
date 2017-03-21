# -*- coding: utf-8 -*-
"""
Created on Tue Jul 21 14:40:39 2015

@author: justin.malinchak
"""

from fredapi import Fred
fred = Fred()
#s = fred.get_series('DSPIC96', observation_start='1960-01-01', observation_end='2015-07-01')
#print s

df_homesales = fred.search_by_release(291, limit=50, order_by='popularity', sort_order='desc')
print df_homesales['title']
df = {}
df['s1'] = fred.get_series('HOSMEDUSM052N')
df['s2'] = fred.get_series('HOSMEDUSNEM052N')
df['s3'] = fred.get_series('HOSMEDUSSOM052N')
import pandas as pd
df = pd.DataFrame(df)
df.plot()
print df['s1']

