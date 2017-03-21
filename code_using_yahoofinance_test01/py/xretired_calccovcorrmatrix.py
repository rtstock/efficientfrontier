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
        
        
        passed = 0
        for k,v in dict_of_dfs.items():
            if passed == 0:        
                df_align = v[['b_monthend','e_pctchange']]
                df_align = df_align.set_index('b_monthend')
                df_align.columns = [k]
                #sLength = len(df_align[k])
                #originalid = k
                
            else:
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
            passed = 1
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