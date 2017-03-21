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


    
import efficientfrontier as ef
o = ef.perform(['^GSPC','^DJI','^OEX','GLD','^RUT','^IXIC'],'2009-12-31') # '^GSPC','^OEX','^MID','^RUT','^DJI'
df = o.permutationstodataframe(50)
for index, row in df.iterrows():
    print '-----'
    print index
    print '-----'
    print 'random weights:'
    randomweightseries = row['value']['randomweightseries']
    #print index,randomweightseries
    for idx in randomweightseries.iteritems():
        print '  ',idx[0],idx[1]
    
    print 'portfolioreturn=',row['value']['portfolioreturn']
    print 'portfoliostandarddeviation=',row['value']['portfoliostandarddeviation'] 
