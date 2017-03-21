# -*- coding: utf-8 -*-
"""
Created on Tue Jul 28 16:16:39 2015

@author: justin.malinchak
"""

def constrained_sum_sample_pos(n, total):
    """Return a randomly chosen list of n positive integers summing to total.
    Each such list is equally likely to occur."""
    import random
    dividers = sorted(random.sample(xrange(1, total), n - 1))
    return [a - b for a, b in zip(dividers + [total], [0] + dividers)]
#print constrained_sum_sample_pos(5,100)    

import operator
def sumproduct(*lists):
    return sum(reduce(operator.mul, data) for data in zip(*lists))

import numpy as np
import pandas as pd
import math as mth
class perform:

    #DataFrameResult
    def set_MonthlyReturnsDataframe(self,MonthlyReturnsDataframe):
        self._MonthlyReturnsDataframe = MonthlyReturnsDataframe
    def get_MonthlyReturnsDataframe(self):
        return self._MonthlyReturnsDataframe
    MonthlyReturnsDataframe = property(get_MonthlyReturnsDataframe, set_MonthlyReturnsDataframe)

    def set_CovarianceMatrix(self,CovarianceMatrix):
        self._CovarianceMatrix = CovarianceMatrix
    def get_CovarianceMatrix(self):
        return self._CovarianceMatrix
    CovarianceMatrix = property(get_CovarianceMatrix, set_CovarianceMatrix)

    def set_CorrelationMatrix(self,CorrelationMatrix):
        self._CorrelationMatrix = CorrelationMatrix
    def get_CorrelationMatrix(self):
        return self._CorrelationMatrix
    CorrelationMatrix = property(get_CorrelationMatrix, set_CorrelationMatrix)

    def set_AnnualizedReturnsSeries(self,AnnualizedReturnsSeries):
        self._AnnualizedReturnsSeries = AnnualizedReturnsSeries
    def get_AnnualizedReturnsSeries(self):
        return self._AnnualizedReturnsSeries
    AnnualizedReturnsSeries = property(get_AnnualizedReturnsSeries, set_AnnualizedReturnsSeries)

    def set_SymbolsList(self,SymbolsList):
        self._SymbolsList = SymbolsList
    def get_SymbolsList(self):
        return self._SymbolsList
    SymbolsList = property(get_SymbolsList, set_SymbolsList)

    def set_StartDateString(self,StartDateString):
        self._StartDateString = StartDateString
    def get_StartDateString(self):
        return self._StartDateString
    StartDateString = property(get_StartDateString, set_StartDateString)

    def __init__(self,
                     list_of_symbols 
                     ,  startdate_string = '2005-01-01'
                     ,  showresults = 0):
        print('Initialized class builddataframeofrefdateminusd2tod1stockpricechanges')
        self.SymbolsList = list_of_symbols
        self.StartDateString = startdate_string
        self.MonthlyReturnsDataframe = self._buildmonthlyreturnsdataframe()
        self.CovarianceMatrix = self._cov()
        self.CorrelationMatrix = self._corr()
        #if showresults == 1:
        #    print('showresults=' + str(showresults) + ' builddataframeofrefdateminusd2tod1stockpricechanges')
        
        #self.build(list_of_symbols,showresults)
    
#    def set_DataFrameResult(self,DataFrameResult):
#        self._DataFrameResult = DataFrameResult
#    def get_DataFrameResult(self):
#        return self._DataFrameResult
#    DataFrameResult = property(get_DataFrameResult, set_DataFrameResult)   




    def _buildmonthlyreturnsdataframe(self,
                 showresults = 0):

        #'^GSmr   ^OEX    ^VIX    ^OEX    ^MID   ^RUT   ^DJI
        
        import pullreturns as pr
        dict_of_dfs = {}
        
        mysymbolslist = self.SymbolsList # list_of_symbols #['^GSPC','^DJI','^MID','^OEX','AAPL','LEO']
        ser_annual = pd.Series()
        for symbol in mysymbolslist:
            o = pr.perform(symbol,self.StartDateString)
            df = o.MonthlyReturnsDataframe
            dict_of_dfs[symbol] = df
            annualizedreturn = o.annualizedreturns()
            ser_annual = ser_annual.set_value(symbol, annualizedreturn)
        if not showresults == 0:
            print '----- ser_annual -----'
            print ser_annual 
        self.AnnualizedReturnsSeries = ser_annual 
        
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
        #import pandas as pd
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
        #self.MonthlyReturnsDataframe = df_align
        return df_align


    def _cov(self,
                 ):

        #'^GSmr   ^OEX    ^VIX    ^OEX    ^MID   ^RUT   ^DJI
        
#        import numpy as np
#        import pandas as pd

        df_align = self.MonthlyReturnsDataframe #monthlyreturns(list_of_symbols)
        
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
        


    def _corr(self,
                 ):

        #'^GSmr   ^OEX    ^VIX    ^OEX    ^MID   ^RUT   ^DJI
        
#        import numpy as np
#        import pandas as pd

#        print '----------------------------------------------------'
#        print '                 monthly returns'
#        print '----------------------------------------------------'

        df_align = self.MonthlyReturnsDataframe #self.monthlyreturns(list_of_symbols)
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

#    def seedweightseries(self,
#
#                     ):
#        import pandas as pd
#        index = self.SymbolsList
#        ser_seed = pd.Series(float(1)/float(len(index)), index=index)
#        
#        return ser_seed

    def equalweightseries(self,

                     ):
        
        index = self.SymbolsList
        ser_seed = pd.Series(float(1)/float(len(index)), index=index)
        
        return ser_seed


    def randomweightseries(self,
                     ):
        int_list = constrained_sum_sample_pos(len(self.SymbolsList),100) 
        fractions_list = [float(x)/float(100) for x in int_list]
        #t = reduce(lambda x,y:x+y,s)
        
        fractions_series = pd.Series(fractions_list, index=self.SymbolsList)
        return fractions_series

#    def portfolioreturnrandomweights(self,):
#        return sumproduct(self.randomweightseries(),self.AnnualizedReturnsSeries)
#
#    def portfolioreturnequalweights(self,):
#        return sumproduct(self.equalweightseries(),self.AnnualizedReturnsSeries)

#    def portfoliostandarddeviationrandomweights(self,):
#        #df = pd.DataFrame({'a' : [4,1,3], 'b' : [5,2,4]},index=[1,2,3])
#        df = self.CovarianceMatrix
#        #s = pd.Series([0.6,0.4],index=['a','b'])
#        s = self.randomweightseries()
#        s1 = df.dot(s)
#        s2 = s1.dot(s.T)
#        return s2
#
#
#    def portfoliostandarddeviationequalweights(self,):
#        #df = pd.DataFrame({'a' : [4,1,3], 'b' : [5,2,4]},index=[1,2,3])
#        df = self.CovarianceMatrix
#        #s = pd.Series([0.6,0.4],index=['a','b'])
#        s = self.equalweightseries()
#        s1 = df.dot(s)
#        s2 = s1.dot(s.T)
#        return s2

    def portfolioriskreturnrandomweight(self,):
        #df = pd.DataFrame({'a' : [4,1,3], 'b' : [5,2,4]},index=[1,2,3])

        #s = pd.Series([0.6,0.4],index=['a','b'])
        rws = self.randomweightseries()
        portfolioreturn = sumproduct(rws,self.AnnualizedReturnsSeries)
        df = self.CovarianceMatrix
        s1 = df.dot(rws)
        portfoliovariance = s1.dot(rws.T)
        portfoliostandarddeviation = mth.sqrt(portfoliovariance)
        data = [rws,portfolioreturn,portfoliostandarddeviation]
        index = ['randomweightseries','portfolioreturn','portfoliostandarddeviation']
        returnseries = pd.Series(data, index=index)
        return returnseries

    def permutations(self,howmany):    
        print '---------------------------------------'
        print 'permutations '
        print '---------------------------------------'
        for i in range(howmany):
            permutation_series = self.portfolioriskreturnrandomweight()
            print '---------------------'
            print '---portfolio weights'
            print '---------------------'
            for idx in permutation_series['randomweightseries'].iteritems():
                print idx
            print '---portfolioreturn',permutation_series['portfolioreturn']
            print '---portfoliostandarddeviation',permutation_series['portfoliostandarddeviation']
        return 1
if __name__=='__main__':
    o = perform(['^GSPC','^DJI','^OEX','GLD','^RUT','^IXIC'],'2009-12-31') # '^GSPC','^OEX','^MID','^RUT','^DJI'
    
    MonthlyReturnsDataframe = o.MonthlyReturnsDataframe
    randomweightseries = o.randomweightseries()
    equalweightsseries = o.equalweightseries()
    AnnualizedReturnsSeries = o.AnnualizedReturnsSeries
    #portfolioreturnrandomweights = o.portfolioreturnrandomweights()
    #portfolioreturnequalweights = o.portfolioreturnequalweights()
    #portfoliostandarddeviationrandomweights = o.portfoliostandarddeviationrandomweights()
    #portfoliostandarddeviationequalweights = o.portfoliostandarddeviationequalweights()
    print '----- MonthlyReturnsDataframe -----'
    print MonthlyReturnsDataframe    
    print '----- randomweightseries -----'
    print randomweightseries
    print '----- equalweightsseries -----'
    print equalweightsseries

    print '----- AnnualizedReturnsSeries -----'
    print AnnualizedReturnsSeries
    
#    print '----- portfolioreturnequalweights -----'
#    print o.portfolioreturnequalweights
#    print '----- portfoliostandarddeviationequalweights -----'
#    print o.portfoliostandarddeviationequalweights    
    
    print '---------------------------------------'
    print 'permutations '
    print '---------------------------------------'
    print 'ok here is the data'
    for i in range(3):
        permutation_series = o.portfolioriskreturnrandomweight()
        print '---------------------'
        print '---portfolio weights'
        print '---------------------'
        for idx in permutation_series['randomweightseries'].iteritems():
            print idx
        print '---portfolioreturn',permutation_series['portfolioreturn']
        print '---portfoliostandarddeviation',permutation_series['portfoliostandarddeviation']
            #print j,permutation_series['randomweightseries'].iloc[j],permutation_series['randomweightseries'][j].index
            #print randweight


#    print '----- portfolioreturnrandomweights -----'
#    print o.portfolioreturnrandomweights()
#    print o.portfolioreturnrandomweights()
#    print o.portfolioreturnrandomweights()
#    print o.portfolioreturnrandomweights()
#    
#    print '----- portfoliostandarddeviationrandomweights -----'    
#    print o.portfoliostandarddeviationrandomweights()
#    print o.portfoliostandarddeviationrandomweights()
#    print o.portfoliostandarddeviationrandomweights()
#    print o.portfoliostandarddeviationrandomweights()
    

    print 'there was no method from chosen library calccovcorrmatrix  ***************************************'