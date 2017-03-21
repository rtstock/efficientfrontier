# -*- coding: utf-8 -*-
"""
Created on Tue Jul 28 16:16:39 2015

@author: justin.malinchak
"""

class perform:
    
    def __init__(self,):
        print('Initialized class builddataframeofrefdateminusd2tod1stockpricechanges')
        #if showresults == 1:
        #    print('showresults=' + str(showresults) + ' builddataframeofrefdateminusd2tod1stockpricechanges')
        
        #self.build(list_of_symbols,showresults)
    
#    def set_DataFrameResult(self,DataFrameResult):
#        self._DataFrameResult = DataFrameResult
#    def get_DataFrameResult(self):
#        return self._DataFrameResult
#    DataFrameResult = property(get_DataFrameResult, set_DataFrameResult)   

    #DataFrameResult
#    def set_DataFrameMonthlyReturns(self,DataFrameMonthlyReturns):
#        self._DataFrameMonthlyReturns = DataFrameMonthlyReturns
#    def get_DataFrameMonthlyReturns(self):
#        return self._DataFrameMonthlyReturns
#    DataFrameMonthlyReturns = property(get_DataFrameMonthlyReturns, set_DataFrameMonthlyReturns)



    def monthlyreturns(self,
                     list_of_symbols ,
                     startdate_string = '2005-01-01',
                     showresults = 0
                 ):

        #'^GSmr   ^OEX    ^VIX    ^OEX    ^MID   ^RUT   ^DJI
        
        import pullreturns as pr
        dict_of_dfs = {}
        
        mysymbolslist = list_of_symbols #['^GSPC','^DJI','^MID','^OEX','AAPL','LEO']
        
        for symbol in mysymbolslist:
            df = pr.monthlyreturnsusingyahoosymbol(symbol,startdate_string)
            dict_of_dfs[symbol] = df
        
        #df = pr.monthlyreturnsusingyahoosymbol('^GSPC','2005-01-01')
        #dict_of_dfs['^GSPC'] = df
        #
        #df = pr.monthlyreturnsusingyahoosymbol('^DJI','2005-01-01')
        #dict_of_dfs['^DJI'] = df
        #
        #df = pr.monthlyreturnsusingyahoosymbol('^MID','2005-01-01')
        #dict_of_dfs['^MID'] = df
        #
        #df = pr.monthlyreturnsusingyahoosymbol('^VIX','2005-01-01')
        #dict_of_dfs['^VIX'] = df
        
        
        #passed = 0
        #import datetime
        import pandas as pd
        #import numpy as np
        
        #todays_date = datetime.datetime.now().date()
        #index = pd.date_range(todays_date-datetime.timedelta(10), periods=10, freq='D')
        index = ['X']
        columns = ['A','B', 'C']
        df_largest = pd.DataFrame(index=index, columns=columns)
        df_largest = df_largest.fillna(0) # with 0s rather than NaNs
        #print df_largest
        #while len(dict_of_dfs_bysize) < len(dict_of_dfs):
        keyoflargestdf = ''
        for k,v in dict_of_dfs.items():
            if len(v) > len(df_largest):
                df_largest = v
                keyoflargestdf = k
                #break
        
        df_align = df_largest[['b_monthend','e_pctchange']]
        df_align = df_align.set_index('b_monthend')
        df_align.columns = [keyoflargestdf]
        df_align.sort_index
        #print df_align
        #print df_largest

#            if passed == 0:        
#                df_align = v[['b_monthend','e_pctchange']]
#                df_align = df_align.set_index('b_monthend')
#                df_align.columns = [k]
#                df_align.sort_index
#                #sLength = len(df_align[k])
#                #originalid = k
#                
#            else:

             
        for k,v in dict_of_dfs.items():
            if not k == keyoflargestdf:
                df_new = v[['b_monthend','e_pctchange']]
                df_new = df_new.set_index('b_monthend')
                df_new.columns = [k]
                df_new.sort_index
                #print df_new
                #df_align[k] = df_new.loc[k].shape[0]
                #print df_new
                #df_align[k] = pd.Series(df_new, index=df_align.index)
                #df_align[k] = df_align[originalid].map(lambda x: df_new[k])
                df_align[k] = df_new[k]
        if showresults == 1:
            print '----------------------------------------------------'
            print '                 monthly returns'
            print '----------------------------------------------------'
            print df_align
        #self.DataFrameMonthlyReturns = df_align
        return df_align


    def cov(self,
                     list_of_symbols ,
                     startdate_string = '',
                     showresults = 0
                 ):

        #'^GSmr   ^OEX    ^VIX    ^OEX    ^MID   ^RUT   ^DJI
        
        import numpy as np
        import pandas as pd

        df_align = self.monthlyreturns(list_of_symbols)
        
        df_align = df_align.dropna()
        
        
        covmatrix_array = np.cov(df_align,None,0)
        #good np.savetxt("cov.csv", covmatrix_array, delimiter=",", fmt='%s')
        
        rows = np.array(list(df_align))[: np.newaxis]
        #str_data = np.char.mod("%10.6f", df_align)
        
        #print str_data
        #print rows
        #print list(df_align)
        
        
        df_cov = pd.DataFrame(covmatrix_array, index=rows, columns=list(df_align))
        return df_cov
#        print '----------------------------------------------------'
#        print '                 covariance matrix'
#        print '----------------------------------------------------'
#        print df_cov
#        df_cov.to_csv('cov1.csv',columns=(list(df_align)))
        


    def corr(self,
                     list_of_symbols ,
                     startdate_string = '',
                     showresults = 0
                 ):

        #'^GSmr   ^OEX    ^VIX    ^OEX    ^MID   ^RUT   ^DJI
        
        import numpy as np
        import pandas as pd

#        print '----------------------------------------------------'
#        print '                 monthly returns'
#        print '----------------------------------------------------'

        df_align = self.monthlyreturns(list_of_symbols)
        df_align = df_align.dropna()
        
        rows = np.array(list(df_align))[: np.newaxis]

        #print rows
        
        corrmatrix_array = np.corrcoef(df_align.T.values.tolist())
        #print corrmatrix_array
        
        df_corr = pd.DataFrame(corrmatrix_array, index=rows, columns=list(df_align))
#        print '----------------------------------------------------'
#        print '                 correlation matrix'
#        print '----------------------------------------------------'
        
        #print df_corr
        #df_corr.to_csv('corr1.csv',columns=(list(df_align)))
        
        return df_corr
        #print '222',sqrt(float(9))
        
        
        #numpyMatrix = df_align.as_matrix()
        #print numpyMatrix
        #print numpyMatrix.dtype
        ##print 'sqrt',sqrt(float(9))
        
        
        
        #with open('cov1.csv', 'w') as f:
        #    df_cov.to_csv(f,columns=())
            
        
        #    np.savetxt(f, np.hstack((rows, str_data)), delimiter=",", fmt='%s')
        #np.savetxt(f, np.hstack((rows, str_data)), delimiter=', ', fmt='%s')
        #print np.cov(df_01)
        #2014-09-30  -0.01551384  -0.06188098
        
        
        #if __name__=='__main__':
        #    df = monthlyreturnsusingyahoosymbol('^GDAXI')
        #    print df
        #    print 'there was no method from library mydata chosen'

#    def seedweights(self,
#                         list_of_symbols ,
#                         #startdate_string = '',
#                         showresults = 0
#                     ):
#        import pandas as pd
#        columns = list_of_symbols
#        index = ['values']
#        df_seed = pd.DataFrame(index=index, columns=columns)
#        df_seed = df_seed.fillna(float(1)/len(columns))
#        return df_seed

#s = Series(data, index=index)

    def seedweightseries(self,
                         list_of_symbols ,
                         #startdate_string = '',
                         #showresults = 0
                     ):
        import pandas as pd
        index = list_of_symbols
        ser_seed = pd.Series(float(1)/float(len(index)), index=index)
        
        return ser_seed


if __name__=='__main__':
    o = perform()
    
    #df = o.monthlyreturns(['^GSPC','^OEX','^MID','^RUT','^DJI'],'2009-12-31')
    ser = o.seedweightseries(['^GSPC','^OEX','^MID','^RUT','^DJI'])
    print ser
    print 'there was no method from library mydata chosen'