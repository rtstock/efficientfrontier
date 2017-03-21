# -*- coding: utf-8 -*-
"""
Created on Wed Jul 29 17:31:47 2015

@author: justin.malinchak
"""

# -*- coding: utf-8 -*-
"""
Created on Wed Jul 29 17:18:11 2015

@author: justin.malinchak
"""


    
import calccovcorrmatrix
mylistofsymbols = ['MHD','YHOO','EWZ','LEO'] # ,'^RUT','^DJI','AAPL','^GSPC','^OEX','^MID'
startdate = '2009-12-31'
o = calccovcorrmatrix.perform(mylistofsymbols,startdate)
print o.CovarianceMatrix
o.permutations(10)
