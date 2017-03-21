# -*- coding: utf-8 -*-
"""
Created on Mon Aug 03 14:35:49 2015

@author: justin.malinchak
"""
import pandas as pd
df = pd.DataFrame({'a' : [4,1,3], 'b' : [5,2,4]},index=[1,2,3])
s = pd.Series([0.6,0.4],index=['a','b'])
df_00 = df.dot(s)
print df
print '--------'
print df_00