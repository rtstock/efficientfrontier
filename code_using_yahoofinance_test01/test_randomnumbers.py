# -*- coding: utf-8 -*-
"""
Created on Mon Aug 03 16:06:48 2015

@author: justin.malinchak
"""

def constrained_sum_sample_pos(n, total):
    """Return a randomly chosen list of n positive integers summing to total.
    Each such list is equally likely to occur."""
    import random
    dividers = sorted(random.sample(xrange(1, total), n - 1))
    return [a - b for a, b in zip(dividers + [total], [0] + dividers)]

ser_seed = constrained_sum_sample_pos(5,100)    
print ser_seed
s = [float(x)/float(100) for x in ser_seed]
t = reduce(lambda x,y:x+y,s)
print s
print t