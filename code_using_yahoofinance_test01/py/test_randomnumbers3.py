# -*- coding: utf-8 -*-
"""
Created on Thu Aug 06 15:46:23 2015

@author: justin.malinchak
"""

SymbolsList = ['WMT','NKE','T','MCD','JPM','^RUT','XOM','MSFT','YHOO','QQQ','HD','GS','BAC','LEO']
import random

#for i in xrange(5):
#    print '%04.3f' % random.uniform(-1, 1)
    


def myfunc(n):
    for i in range(n):
        yield random.uniform(-0.1, 0.1)

import numpy as np
import pandas as pd
ls_02 = np.fromiter(myfunc(len(SymbolsList)), dtype=float)
#ls_02 = numpy.random.normal(mu, sigma,len(SymbolsList))

print ls_02
ar_02 = np.array(ls_02)
ar_02 /= ar_02.sum()
#print ar_02.sum()
fractions_series = pd.Series(ar_02, index=SymbolsList)
print fractions_series
t = reduce(lambda x,y:x+y,fractions_series)
print t

#print numpy.random.beta(1, 2, size=10)
#print numpy.random.exponential(scale=20.0, size=10)
#print np.random.standard_cauchy(size=10)
