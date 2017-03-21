# -*- coding: utf-8 -*-
"""
Created on Thu Aug 06 16:02:03 2015

@author: justin.malinchak
"""

print '--------------------'
import pandas as pd
import numpy as np, numpy.random
SymbolsList = ['WMT','NKE','T','MCD','JPM','^RUT','XOM','MSFT','YHOO','QQQ','HD','GS','BAC','LEO']


from random import randrange, shuffle

randomlist = []
uniqueflag = False
total_to_generate = 10
start_range = -100
end_range = 100

for i in xrange (1,total_to_generate+1):
    while not uniqueflag:
        randomnumber = randrange(start_range,end_range)
        if randomnumber not in randomlist and randomnumber not in (11111, 22222, 33333, 44444, 55555, 66666, 77777, 88888, 99999):
            uniqueflag = True
    randomlist.append(randomnumber)
    uniqueflag = False
shuffle(randomlist)
for x in randomlist:
    print x
