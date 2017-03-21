# -*- coding: utf-8 -*-
"""
Created on Tue Jul 28 16:16:39 2015

@author: justin.malinchak
"""

## Before allowing negatives
#def constrained_sum_sample_pos(n, total):
#    """Return a randomly chosen list of n positive integers summing to total.
#    Each such list is equally likely to occur."""
#    import random
#    dividers = sorted(random.sample(xrange(1, total), n - 1))
#    return [a - b for a, b in zip(dividers + [total], [0] + dividers)]

## after allowing negatives
#def constrained_sum_sample_pos(n, total):
#    """Return a randomly chosen list of n positive integers summing to total.
#    Each such list is equally likely to occur."""
#    import random    
#    dividers = random.sample(xrange(-100, total), n - 1)
#    return [a - b for a, b in zip(dividers + [total], [0] + dividers)]
 


#def constrained_sum_sample_pos(n, minimum,maximum):
#    """Return a randomly chosen list of n positive integers summing to total.
#    Each such list is equally likely to occur."""
#    import random    
#    if minimum < 0:
#        dividers = random.sample(xrange(minimum, maximum), n - 1)
#    else:
#        dividers = sorted(random.sample(xrange(minimum, maximum), n - 1))
#    return [a - b for a, b in zip(dividers + [maximum], [0] + dividers)]

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

import operator
def sumproduct(*lists):
    return sum(reduce(operator.mul, data) for data in zip(*lists))

import numpy as np
import pandas as pd
import math as mth
class perform:

#    #DataFrameResult
    def set_ReturnsDataframe(self,ReturnsDataframe):
        self._ReturnsDataframe = ReturnsDataframe
    def get_ReturnsDataframe(self):
        return self._ReturnsDataframe
    ReturnsDataframe = property(get_ReturnsDataframe, set_ReturnsDataframe)

#
    def set_PriceHistoryDataframe(self,PriceHistoryDataframe):
        self._PriceHistoryDataframe = PriceHistoryDataframe
    def get_PriceHistoryDataframe(self):
        return self._PriceHistoryDataframe
    PriceHistoryDataframe = property(get_PriceHistoryDataframe, set_PriceHistoryDataframe)

#    def setCovarianceMatrix(self,CovarianceMatrix):
#        self.CovarianceMatrix = CovarianceMatrix
#    def getCovarianceMatrix(self):
#        return self._CovarianceMatrix
#    CovarianceMatrix = property(getCovarianceMatrix, setCovarianceMatrix)
#
#    def setCorrelationMatrix(self,CorrelationMatrix):
#        self.CorrelationMatrix = CorrelationMatrix
#    def getCorrelationMatrix(self):
#        return self._CorrelationMatrix
#    CorrelationMatrix = property(getCorrelationMatrix, setCorrelationMatrix)

#    def set_AnnualizedReturnsSeries(self,AnnualizedReturnsSeries):
#        self._AnnualizedReturnsSeries = AnnualizedReturnsSeries
#    def get_AnnualizedReturnsSeries(self):
#        return self._AnnualizedReturnsSeries
#    AnnualizedReturnsSeries = property(get_AnnualizedReturnsSeries, set_AnnualizedReturnsSeries)

    def set_SymbolsList(self,SymbolsList):
        self._SymbolsList = SymbolsList
    def get_SymbolsList(self):
        return self._SymbolsList
    SymbolsList = property(get_SymbolsList, set_SymbolsList)


    def set_Period(self,Period):
        self._Period = Period
    def get_Period(self):
        return self._Period
    Period = property(get_Period, set_Period)

    def set_PctChangeOrLogReturn(self,PctChangeOrLogReturn):
        self._PctChangeOrLogReturn = PctChangeOrLogReturn
    def get_PctChangeOrLogReturn(self):
        return self._PctChangeOrLogReturn
    PctChangeOrLogReturn = property(get_PctChangeOrLogReturn, set_PctChangeOrLogReturn)



    def set_BottomConstraint(self,BottomConstraint):
        self._BottomConstraint = BottomConstraint
    def get_BottomConstraint(self):
        return self._BottomConstraint
    BottomConstraint = property(get_BottomConstraint, set_BottomConstraint)

    def set_TopConstraint(self,TopConstraint):
        self._TopConstraint = TopConstraint
    def get_TopConstraint(self):
        return self._TopConstraint
    TopConstraint = property(get_TopConstraint, set_TopConstraint)


    def set_StartDateString(self,StartDateString):
        self._StartDateString = StartDateString
    def get_StartDateString(self):
        return self._StartDateString
    StartDateString = property(get_StartDateString, set_StartDateString)

    def __init__(self,
                     list_of_symbols 
                     ,  startdate_string = '2005-01-01'
                     ,  period='monthly'
                     ,  pctchangeorlogreturn = 'pctchange'
                     ,  showresults = 0):
        print('Initialized class efficientfrontier')
        from random import shuffle
        shuffle(list_of_symbols)
        self.SymbolsList = list_of_symbols
        self.StartDateString = startdate_string
        self.Period = period
        self.PctChangeOrLogReturn = pctchangeorlogreturn
        #self.ReturnsDataframe = self.compilereturnsdataframe()
        self.compilehistoricaldataframes()
        #self.BottomConstraint = bottomconstraint
        #self.TopConstraint = topconstraint
        #self.MonthlyReturnsDataframe = self.monthlycompilereturnsdataframe()
        #self.CovarianceMatrix = self.covariancematrix()
        #self.CorrelationMatrix = self.correlationmatrix()
        #if showresults == 1:
        #    print('showresults=' + str(showresults) + ' builddataframeofrefdateminusd2tod1stockpricechanges')
        
        #self.build(list_of_symbols,showresults)
    
#    def set_DataFrameResult(self,DataFrameResult):
#        self._DataFrameResult = DataFrameResult
#    def get_DataFrameResult(self):
#        return self._DataFrameResult
#    DataFrameResult = property(get_DataFrameResult, set_DataFrameResult)   




#    def monthlycompilereturnsdataframe(self,
#                 showresults = 0):
#
#        #'^GSmr   ^OEX    ^VIX    ^OEX    ^MID   ^RUT   ^DJI
#        
#        import pullreturnsmonthly as pr
#        dict_of_dfs = {}
#        
#        mysymbolslist = self.SymbolsList # list_of_symbols #['^GSPC','^DJI','^MID','^OEX','AAPL','LEO']
#        #ser_annual = pd.Series()
#        for symbol in mysymbolslist:
#            o = pr.perform(symbol,self.StartDateString)
#            df = o.ReturnsDataframe
#            dict_of_dfs[symbol] = df
#        index = ['X']
#        columns = ['A','B', 'C']
#        df_largestofreturns = pd.DataFrame(index=index, columns=columns)
#        df_largestofreturns = df_largestofreturns.fillna(0) # with 0s rather than NaNs
#        #print df_largestofreturns
#        #while len(dict_of_dfs_bysize) < len(dict_of_dfs):
#        keyoflargestreturnsdf = ''
#        for k,v in dict_of_dfs.items():
#            if len(v) > len(df_largestofreturns):
#                df_largestofreturns = v
#                keyoflargestreturnsdf = k
#                #break
#        
#        df_alignedreturns = df_largestofreturns[['b_periodend','e_pctchange']]
#        df_alignedreturns = df_alignedreturns.set_index('b_periodend')
#        df_alignedreturns.columns = [keyoflargestreturnsdf]
#        df_alignedreturns.sort_index
#        #print df_alignedreturns
#        #print df_largestofreturns
#
##            if passed == 0:        
##                df_alignedreturns = v[['b_periodend','e_pctchange']]
##                df_alignedreturns = df_alignedreturns.set_index('b_periodend')
##                df_alignedreturns.columns = [k]
##                df_alignedreturns.sort_index
##                #sLength = len(df_alignedreturns[k])
##                #originalid = k
##                
##            else:
#
#             
#        for k,v in dict_of_dfs.items():
#            if not k == keyoflargestreturnsdf:
#                df_new = v[['b_periodend','e_pctchange']]
#                df_new = df_new.set_index('b_periodend')
#                df_new.columns = [k]
#                df_new.sort_index
#                #print df_new
#                #df_alignedreturns[k] = df_new.loc[k].shape[0]
#                #print df_new
#                #df_alignedreturns[k] = pd.Series(df_new, index=df_alignedreturns.index)
#                #df_alignedreturns[k] = df_alignedreturns[originalid].map(lambda x: df_new[k])
#                df_alignedreturns[k] = df_new[k]
#        if showresults == 1:
#            print '----------------------------------------------------'
#            print '                 monthly returns'
#            print '----------------------------------------------------'
#            print df_alignedreturns
#        #self.MonthlyReturnsDataframe = df_alignedreturns
#        return df_alignedreturns
#rrrrr
    def pricehistorydataframe(self
                    , period = 'monthly' # or daily
                 , showresults = 0):

        #'^GSmr   ^OEX    ^VIX    ^OEX    ^MID   ^RUT   ^DJI
        import pullreturnsbyperiod as pr
#        if self.Period == 'daily':
#            import pullreturnsdaily as pr
#        else:
#            import pullreturnsmonthly as pr
        dict_of_dfs = {}
        print 'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx'
        # Build the annualized returns series
        mysymbolslist = self.SymbolsList # list_of_symbols #['^GSPC','^DJI','^MID','^OEX','AAPL','LEO']
        #ser_annual = pd.Series()
        for symbol in mysymbolslist:
            o = pr.perform(symbol,self.StartDateString,period)
            df = o.PriceHistoryDataframe
            dict_of_dfs[symbol] = df
            #annualizedreturn = o.annualizedreturn()
            #ser_annual = ser_annual.set_value(symbol, annualizedreturn)
#        if not showresults == 0:
#            print '----- ser_annual -----'
#            print ser_annual
        #print 'returns dataframe ready'
        #self.AnnualizedReturnsSeries = ser_annual 
        

  
#        mysymbolslist = self.SymbolsList # list_of_symbols #['^GSPC','^DJI','^MID','^OEX','AAPL','LEO']
#        #ser_annual = pd.Series()
#        for symbol in mysymbolslist:
#            o = pr.perform(symbol,self.StartDateString)
#            df = o.ReturnsDataframe
#            dict_of_dfs[symbol] = df
            
        index = ['X']
        columns = ['A','B', 'C']
        df_largestofreturns = pd.DataFrame(index=index, columns=columns)
        df_largestofreturns = df_largestofreturns.fillna(0) # with 0s rather than NaNs
        #print df_largestofreturns
        #while len(dict_of_dfs_bysize) < len(dict_of_dfs):
        keyoflargestreturnsdf = ''
        for k,v in dict_of_dfs.items():
            if len(v) > len(df_largestofreturns):
                df_largestofreturns = v
                keyoflargestreturnsdf = k
                break
        print '^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^', keyoflargestreturnsdf
        
        df_alignedreturns = df_largestofreturns[['e_adjclose']]
        #print df_alignedreturns
        df_alignedreturns.columns = [keyoflargestreturnsdf]
        #df_alignedreturns = df_alignedreturns.set_index('b_periodend')
        #print df_alignedreturns
        
        df_alignedreturns.sort_index
        #print df_alignedreturns
        

#            if passed == 0:        
#                df_alignedreturns = v[['b_periodend','e_pctchange']]
#                df_alignedreturns = df_alignedreturns.set_index('b_periodend')
#                df_alignedreturns.columns = [k]
#                df_alignedreturns.sort_index
#                #sLength = len(df_alignedreturns[k])
#                #originalid = k
#                
#            else:

             
        for k,v in dict_of_dfs.items():
            if not k == keyoflargestreturnsdf:
                df_new = v[['e_adjclose']]
                #print '----------------v--------------------'
                #print v

                #print '----------------df_new--------------------'
                #print df_new
                #df_new = df_new.set_index('b_periodend')
                df_new.columns = [k]
                #print df_new
                df_new.sort_index
                #print 'made it here'
                #print df_new
                #df_alignedreturns[k] = df_new.loc[k].shape[0]
                #print df_new
                #df_alignedreturns[k] = pd.Series(df_new, index=df_alignedreturns.index)
                #df_alignedreturns[k] = df_alignedreturns[originalid].map(lambda x: df_new[k])
                df_alignedreturns[k] = df_new#[k]
        if showresults == 1:
            print '----------------------------------------------------'
            print '                 stockhistory'
            print '----------------------------------------------------'
            print '------------------------------df_alignedreturns -------------------------'
            print df_alignedreturns
        #self.MonthlyReturnsDataframe = df_alignedreturns
        return df_alignedreturns




    def compilereturnsdataframe(self
                 , showresults = 0):

        #'^GSmr   ^OEX    ^VIX    ^OEX    ^MID   ^RUT   ^DJI
#        if self.Period == 'daily':
#            import pullreturnsdaily as pr
#        else:
#            import pullreturnsmonthly as pr
        import pullreturnsbyperiod as pr
        dict_of_df_pricehistory = {}
        dict_of_df_returns = {}
        # Build the annualized returns series
        mysymbolslist = self.SymbolsList # list_of_symbols #['^GSPC','^DJI','^MID','^OEX','AAPL','LEO']
        ser_annual = pd.Series()
        for symbol in mysymbolslist:
            o = pr.perform(symbol,self.StartDateString,self.Period)
            #print o.ReturnsDataframe[['e_'+ self.PctChangeOrLogReturn]]
            #df_pricehistorydataframe = o.PriceHistoryDataframe
            #dfcompilereturnsdataframe = o.ReturnsDataframe
            dict_of_df_pricehistory[symbol] = o.PriceHistoryDataframe
            dict_of_df_returns[symbol] = o.ReturnsDataframe
            annualizedreturn = o.annualizedreturn()
            ser_annual = ser_annual.set_value(symbol, annualizedreturn)
        
        self.AnnualizedReturnsSeries = ser_annual 
        
        #mysymbolslist = self.SymbolsList # list_of_symbols #['^GSPC','^DJI','^MID','^OEX','AAPL','LEO']
        #ser_annual = pd.Series()
#        for symbol in mysymbolslist:
#            df_pricehistory = dict_of_df_pricehistory[symbol]
#            df_returns = dict_of_df_returns[symbol]
#            o = pr.perform(symbol,self.StartDateString)
#            df = o.ReturnsDataframe
#            dict_of_dfs[symbol] = df
            
        index = ['X']
        columns = ['A','B', 'C']
        df_largestofreturns = pd.DataFrame(index=index, columns=columns)
        df_largestofreturns = df_largestofreturns.fillna(0) # with 0s rather than NaNs
        #print df_largestofreturns
        #while len(dict_of_dfs_bysize) < len(dict_of_dfs):
        keyoflargestreturnsdf = ''
        for k,v in dict_of_df_returns.items():
            if len(v) > len(df_largestofreturns):
                df_largestofreturns = v
                keyoflargestreturnsdf = k
                #break
        #wwwwww
#        print df_largestofreturns
#        print keyoflargestreturnsdf
        
        df_alignedreturns = df_largestofreturns[['e_'+ self.PctChangeOrLogReturn]]
        #df_alignedreturns = df_alignedreturns.set_index('b_periodend')
        df_alignedreturns.columns = [keyoflargestreturnsdf]
        df_alignedreturns.sort_index
        #print df_alignedreturns
        #print df_largestofreturns
#
#            if passed == 0:        
#                df_alignedreturns = v[['b_periodend','e_pctchange']]
#                df_alignedreturns = df_alignedreturns.set_index('b_periodend')
#                df_alignedreturns.columns = [k]
#                df_alignedreturns.sort_index
#                #sLength = len(df_alignedreturns[k])
#                #originalid = k
#                
#            else:

             
        for k,v in dict_of_df_returns.items():
            if not k == keyoflargestreturnsdf:
                df_new = v[['e_' + self.PctChangeOrLogReturn]]
                #df_new = df_new.set_index('b_periodend')
                df_new.columns = [k]
                df_new.sort_index
                #print df_new
                #df_alignedreturns[k] = df_new.loc[k].shape[0]
                #print df_new
                #df_alignedreturns[k] = pd.Series(df_new, index=df_alignedreturns.index)
                #df_alignedreturns[k] = df_alignedreturns[originalid].map(lambda x: df_new[k])
                df_alignedreturns[k] = df_new[k]
        if showresults == 1:
            print '----------------------------------------------------'
            print '                 returns'
            print '----------------------------------------------------'
            print df_alignedreturns

        #print df_alignedreturns
        
        #self.MonthlyReturnsDataframe = df_alignedreturns
        return df_alignedreturns



    def compilehistoricaldataframes(self
                 , showresults = 0):

        #'^GSmr   ^OEX    ^VIX    ^OEX    ^MID   ^RUT   ^DJI
#        if self.Period == 'daily':
#            import pullreturnsdaily as pr
#        else:
#            import pullreturnsmonthly as pr
        import pullreturnsbyperiod as pr
        dict_of_df_pricehistory = {}
        dict_of_df_returns = {}
        # Build the annualized returns series
        mysymbolslist = self.SymbolsList # list_of_symbols #['^GSPC','^DJI','^MID','^OEX','AAPL','LEO']
        ser_annual = pd.Series()
        for symbol in mysymbolslist:
            o = pr.perform(symbol,self.StartDateString,self.Period)
            dict_of_df_pricehistory[symbol] = o.PriceHistoryDataframe
            dict_of_df_returns[symbol] = o.ReturnsDataframe
            annualizedreturn = o.annualizedreturn()
            ser_annual = ser_annual.set_value(symbol, annualizedreturn)
        
        self.AnnualizedReturnsSeries = ser_annual 
        

        index = ['X']
        columns = ['A','B', 'C']
        
        # ----------------------------------------------------------------------
        df_largestofreturns = pd.DataFrame(index=index, columns=columns)
        df_largestofreturns = df_largestofreturns.fillna(0) # with 0s rather than NaNs
        keyoflargestreturnsdf = ''
        for k,v in dict_of_df_returns.items():
            if len(v) > len(df_largestofreturns):
                df_largestofreturns = v
                keyoflargestreturnsdf = k

        df_alignedreturns = df_largestofreturns[['e_'+ self.PctChangeOrLogReturn]]
        df_alignedreturns.columns = [keyoflargestreturnsdf]
        df_alignedreturns.sort_index
             
        for k,v in dict_of_df_returns.items():
            if not k == keyoflargestreturnsdf:
                df_new = v[['e_' + self.PctChangeOrLogReturn]]
                df_new.columns = [k]
                df_new.sort_index
                df_alignedreturns[k] = df_new[k]
        self.ReturnsDataframe = df_alignedreturns
        
        # ----------------------------------------------------------------------
        df_largestofpricehistory = pd.DataFrame(index=index, columns=columns)
        df_largestofpricehistory = df_largestofpricehistory.fillna(0) # with 0s rather than NaNs
        keyoflargestpricehistorydf = ''
        for k,v in dict_of_df_pricehistory.items():
            if len(v) > len(df_largestofpricehistory):
                df_largestofpricehistory = v
                keyoflargestpricehistorydf = k

        df_alignedpricehistory = df_largestofpricehistory[['e_adjclose']]
        df_alignedpricehistory.columns = [keyoflargestpricehistorydf]
        df_alignedpricehistory.sort_index
             
        for k,v in dict_of_df_pricehistory.items():
            if not k == keyoflargestpricehistorydf:
                df_new = v[['e_adjclose']]
                df_new.columns = [k]
                df_new.sort_index
                df_alignedpricehistory[k] = df_new[k]

        self.PriceHistoryDataframe = df_alignedpricehistory
        # ----------------------------------------------------------------------




    def covariancematrix(self
#            , period='monthly'
#            , pctchangeorlogreturn = 'pctchange'
                 ):

        #'^GSmr   ^OEX    ^VIX    ^OEX    ^MID   ^RUT   ^DJI
        
#        import numpy as np
#        import pandas as pd

        #df_alignedreturns = self.MonthlyReturnsDataframe #monthlyreturns(list_of_symbols)
        #df_alignedreturns = self.compilereturnsdataframe(period)
        #df_alignedreturns = self.compilereturnsdataframe(period,pctchangeorlogreturn)
        df_alignedreturns = self.ReturnsDataframe
        df_alignedreturns = df_alignedreturns.dropna()
        
        
        covmatrix_array = np.cov(df_alignedreturns,None,0)
        #good np.savetxt("cov.csv", covmatrix_array, delimiter=",", fmt='%s')
        
        rows = np.array(list(df_alignedreturns))[: np.newaxis]
        #str_data = np.char.mod("%10.6f", df_alignedreturns)
        
        #print str_data
        #print rows
        #print list(df_alignedreturns)
        
        
        df_covariancematrix = pd.DataFrame(covmatrix_array, index=rows, columns=list(df_alignedreturns))
#        if period == 'daily':
#            for i in range(len(df_covariancematrix)):
#                print df_covariancematrix.iloc[i] 
#                
        return df_covariancematrix
#        print '----------------------------------------------------'
#        print '                 covariance matrix'
#        print '----------------------------------------------------'
#        print df_covariancematrix
#        df_covariancematrix.to_csv('cov1.csv',columns=(list(df_alignedreturns)))
        


    def correlationmatrix(self
#            , period='monthly'
#            , pctchangeorlogreturn = 'pctchange'
                 ):

        #'^GSmr   ^OEX    ^VIX    ^OEX    ^MID   ^RUT   ^DJI
        
#        import numpy as np
#        import pandas as pd

#        print '----------------------------------------------------'
#        print '                 monthly returns'
#        print '----------------------------------------------------'

        #df_alignedreturns = self.MonthlyReturnsDataframe #self.monthlyreturns(list_of_symbols)
        #df_alignedreturns = self.compilereturnsdataframe(period,pctchangeorlogreturn)
        df_alignedreturns = self.ReturnsDataframe
        df_alignedreturns = df_alignedreturns.dropna()
        print '------------------- df_alignedreturns -------------------'
        print df_alignedreturns
        rows = np.array(list(df_alignedreturns))[: np.newaxis]

        #print rows
        
        corrmatrix_array = np.corrcoef(df_alignedreturns.T.values.tolist())
        #print corrmatrix_array
        
        dfcorrelationmatrix = pd.DataFrame(corrmatrix_array, index=rows, columns=list(df_alignedreturns))
#        print '----------------------------------------------------'
#        print '                 correlation matrix'
#        print '----------------------------------------------------'
        
        #print dfcorrelationmatrix
        #dfcorrelationmatrix.to_csv('corr1.csv',columns=(list(df_alignedreturns)))
        
        return dfcorrelationmatrix
        #print '222',sqrt(float(9))

    def equalweightseries(self,

                     ):
        
        index = self.SymbolsList
        ser_seed = pd.Series(float(1)/float(len(index)), index=index)
        
        return ser_seed


    def randomweightseries(self, 
                     ):
        #mysymbolslist = self.SymbolsList #['WMT','BAC','JPM','AAPL','GOOG']

        #int_list = constrained_sum_sample_pos(len(self.SymbolsList),100) 
        #print 'wwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwww'
        int_list = constrained_sum_sample_nonneg(len(self.SymbolsList),100) 
        
        fractions_list = [float(x)/float(100) for x in int_list]
        #sums them all to test
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
        #print 'pppppppppppppppppppppppppppppppppppppppppppp'
        rws = self.randomweightseries()
        #print self.AnnualizedReturnsSeries
        portfolioreturn = sumproduct(rws,self.AnnualizedReturnsSeries)
        df = self.covariancematrix()
        s1 = df.dot(rws)
        portfoliovariance = s1.dot(rws.T)
        portfoliostandarddeviation = mth.sqrt(portfoliovariance)
        data = [rws,portfolioreturn,portfoliostandarddeviation]
        index = ['randomweightseries','portfolioreturn','portfoliostandarddeviation']
        returnseries = pd.Series(data, index=index)
        #print 'returnseries',data
        return returnseries

#    def testpermutations(self,howmany):    
#        print '---------------------------------------'
#        print 'permutations '
#        print '---------------------------------------'
#        for i in range(howmany):
#            permutation_series = self.portfolioriskreturnrandomweight()
#            print '---------------------'
#            print '---portfolio weights'
#            print '---------------------'
#            for idx in permutation_series['randomweightseries'].iteritems():
#                print idx
#            print '---portfolioreturn',permutation_series['portfolioreturn']
#            print '---portfoliostandarddeviation',permutation_series['portfoliostandarddeviation']
#        return 1

    def permutationstodataframe(self,howmany):    
#        print '---------------------------------------'
#        print 'permutations '
#        print '---------------------------------------'
        dict_permutations = {}
        for i in range(howmany):
            #print 'qqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqq'
            #print self.portfolioriskreturnrandomweight
            permutation_series = self.portfolioriskreturnrandomweight()
            #for idx in permutation_series['randomweightseries'].iteritems():
            #    print idx
            #randomweightseries = permutation_series['randomweightseries']
            #portfolioreturn = permutation_series['portfolioreturn']
            
            #portfoliostandarddeviation = permutation_series['portfoliostandarddeviation']
            #print i,portfolioreturn,portfoliostandarddeviation 
            dict_permutations[len(dict_permutations)] = permutation_series #randomweightseries,portfolioreturn,portfoliostandarddeviation
        df = pd.DataFrame(dict_permutations.items(), columns=['key','value']) # 'portfolioreturn','portfoliostandarddeviation','weight'
        df = df.set_index('key',drop=True)
        #df = df['value']
        #df = pd.DataFrame(dict_permutations)
        #df = df.T.stack().reset_index()   
#        df = pd.DataFrame([
#            [col1,col2] for col1, d in dict_permutations.items() for col2 in d.items()
#        ])  
#        df = pd.DataFrame([
#            [col1,col2] for col1, d in dict_permutations.items() for col2 in d
#        ])
        #df.columns = 'weight','portfolioreturn','portfoliostandarddeviation'
        return df

if __name__=='__main__':
    o = perform(['^GSPC','^DJI','^OEX','^RUT']
                ,  startdate_string = '2005-01-01'
                ,  period='daily'
                ,  pctchangeorlogreturn = 'pctchange') 
    # '^GSPC','^OEX','^MID','^RUT','^DJI'
    #print o.ReturnsDataframe
    print o.PriceHistoryDataframe
    print o.correlationmatrix()
    print o.covariancematrix()


'''    
    df = o.permutationstodataframe(10)
    print df
    for index, row in df.iterrows():
        print '-----'
        print index,row
        print '-----'
        print 'random weights:'
        randomweightseries = row['value']['randomweightseries']
        #print index,randomweightseries
        for idx in randomweightseries.iteritems():
            print '  ',idx[0],idx[1]
        
        print 'portfolioreturn=',row['value']['portfolioreturn']
        print 'portfoliostandarddeviation=',row['value']['portfoliostandarddeviation'] 
'''
     
  