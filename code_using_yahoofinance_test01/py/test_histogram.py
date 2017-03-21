# -*- coding: utf-8 -*-
"""
Created on Wed Aug 05 10:22:21 2015

@author: justin.malinchak
"""
import numpy as np
#import matplotlib.pyplot as plt

a = np.arange(5)
a = np.random.binomial(10,0.5,100)
a = np.random.normal(0,100,10)
print 'a=',a
hist, bin_edges = np.histogram(a, density=True)
print 'hist=',hist
print 'bin_edges=',bin_edges
#array([ 0.5,  0. ,  0.5,  0. ,  0. ,  0.5,  0. ,  0.5,  0. ,  0.5])
print 'hist sum=',hist.sum()
#2.4999999999999996
print 'sum of hist X diff=',np.sum(hist*np.diff(bin_edges))
#plt.hist = hist
#plt.show

import matplotlib.pylab as plt
import pandas as pd
import numpy as np
df = pd.DataFrame(np.random.randn(10,2), columns=['col1','col2'])
#df['col3'] = np.arange(len(df))**2 * 100 + 100
print df
#plt.scatter(df.col1, df.col2, s=df.col3)
plt.scatter(df.col1, df.col2, s=10)
s = '12345'
print s[:-2]