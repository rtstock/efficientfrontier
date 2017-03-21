# -*- coding: utf-8 -*-
"""
Created on Wed Aug 05 15:06:10 2015

@author: justin.malinchak
"""




print '--------------------'
import pandas as pd
import numpy as np, numpy.random
SymbolsList = ['WMT','NKE','T','MCD','JPM','^RUT','XOM','MSFT','YHOO','QQQ','HD','GS','BAC','LEO']

import random
min = 0.0
max = 1.0
A = 500.0
B = 100.0

def generate(n):
    C = [min + i*(max-min)/(n+1) for i in range(1, n+1)]
    Y = [0]
    for i in range(1,n-1):
        # This line should be changed in order to always get positive numbers
        # It should be relatively easy to figure out some good random generator
        Y.append(random.random())
    val = A - C[0]*B
    for i in range(1, n-1):
        val -= Y[i] * (C[i] - C[0])
    val /= (C[n-1] - C[0])
    Y.append(val)
    val = B
    for i in range(1, n):
        val -= Y[i]
    Y[0] = val
    result = []
    for i in range(0, n):
        result.append([ Y[i]*C[i], Y[i] ])
    return result

print generate(10)