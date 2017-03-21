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

class perform:
    
    def __init__(self,
                     list_of_symbols 
                     ,  startdate_string = '2005-01-01'
                     ,  iterations = 10
                     ):
                         
        self._setup(list_of_symbols 
                     ,  startdate_string
                     ,  iterations
                     )

    def _setup(self,list_of_symbols 
                     ,  startdate_string
                     ,  iterations
                     ):
        
        import efficientfrontier as ef   
        
        o = ef.perform(list_of_symbols,startdate_string) # '^GSPC','^OEX','^MID','^RUT','^DJI'
        df = o.permutationstodataframe(iterations)
        for index, row in df.iterrows():
            print '----------'
            print index
            print '-----'
            print 'random weights:'
            randomweightseries = row['value']['randomweightseries']
            #print index,randomweightseries
            for idx in randomweightseries.iteritems():
                print '  ',idx[0],idx[1]
            
            print 'portfolioreturn=',row['value']['portfolioreturn']
            print 'portfoliostandarddeviation=',row['value']['portfoliostandarddeviation'] 

if __name__=='__main__':
    o = perform(['^GSPC','^DJI','^OEX','GLD','^RUT','^IXIC'],'2009-12-31',5) # '^GSPC','^OEX','^MID','^RUT','^DJI'
    