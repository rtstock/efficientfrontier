# -*- coding: utf-8 -*-
"""
Created on Wed Aug 05 15:06:10 2015

@author: justin.malinchak
"""
#import random
#def constrained_sum_sample_pos(n, total):
#    """Return a randomly chosen list of n positive integers summing to total.
#    Each such list is equally likely to occur."""
#    
#    dividers = random.sample(xrange(-100, total), n - 1)
#    return [a - b for a, b in zip(dividers + [total], [0] + dividers)]

def constrained_sum_sample_pos(n, minimum,maximum,total):
    """Return a randomly chosen list of n positive integers summing to total.
    Each such list is equally likely to occur."""
    import random    
    if minimum < 0:
        dividers = sorted(random.sample(xrange(minimum, total), n - 1))
    else:
        dividers = sorted(random.sample(xrange(minimum, total), n - 1))
    print 'dividers',dividers
    return [a - b for a, b in zip(dividers + [maximum], [0] + dividers)]

SymbolsList = ['WMT','NKE','T','MCD','JPM','^RUT','XOM','MSFT','YHOO','QQQ','HD','GS','BAC','LEO']

from random import shuffle
shuffle(SymbolsList)
mymin = -20
mymax = 20
int_list = constrained_sum_sample_pos(len(SymbolsList),mymin,mymax,100) 
#print int_list
fractions_list = [float(x)/float(100) for x in int_list]
#t = reduce(lambda x,y:x+y,s)

import pandas as pd

fractions_series = pd.Series(fractions_list, index=SymbolsList)
print fractions_series
t = reduce(lambda x,y:x+y,fractions_series)
print t


print '--------------------'
import numpy as np, numpy.random
fractions_list = np.random.dirichlet(np.ones(len(SymbolsList)),size=1)
print fractions_list
fractions_series = pd.Series(fractions_list[0], index=SymbolsList)
print fractions_series
t = reduce(lambda x,y:x+y,fractions_series)
print t
mu, sigma = 0, 1 # mean and standard deviation
#a = np.random.normal(mu,sigma,size=len(SymbolsList))
ls_01 = np.random.randint(0,100,len(SymbolsList))

print ls_01
ls_02 = [float(i) for i in ls_01]
print ls_02
ar_02 = numpy.array(ls_02)
print ar_02

print ar_02.sum()
#a = np.random.random(len(SymbolsList))
ar_02 /= ar_02.sum()
print ar_02.sum()
fractions_series = pd.Series(ar_02, index=SymbolsList)
print fractions_series
t = reduce(lambda x,y:x+y,fractions_series)
#print t

#print fractions_series
#t = reduce(lambda x,y:x+y,fractions_series)
