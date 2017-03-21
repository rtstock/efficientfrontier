# -*- coding: utf-8 -*-
"""
Created on Thu Aug 06 16:23:02 2015

@author: justin.malinchak
"""

# Before allowing negatives
def constrained_sum_sample_pos(n, total):
    """Return a randomly chosen list of n positive integers summing to total.
    Each such list is equally likely to occur."""
    import random
    dividers = sorted(random.sample(xrange(1, total), n - 1))
    return [a - b for a, b in zip(dividers + [total], [0] + dividers)]

def constrained_sum_sample_nonneg(n, total):
    """Return a randomly chosen list of n nonnegative integers summing to total.
    Each such list is equally likely to occur."""

    return [x - 1 for x in constrained_sum_sample_pos(n, total + n)]

def constrained_sum_sample_posneg(n, minimum,maximum,total):
    """Return a randomly chosen list of n positive integers summing to total.
    Each such list is equally likely to occur."""
    import numpy as np
    a = np.random.randint(minimum,maximum,n)
    print a
    return a.sum()
    
#fractions_series = pd.Series(ar_02, index=SymbolsList)
#print fractions_series
#t = reduce(lambda x,y:x+y,fractions_series)
#print t

print constrained_sum_sample_nonneg(5,100)
print constrained_sum_sample_posneg(15,-20,20,100)