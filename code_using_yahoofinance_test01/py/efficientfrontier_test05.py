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

    #DataFrameResult
    def set_ReturnsDataframe(self,ReturnsDataframe):
        self._ReturnsDataframe = ReturnsDataframe
    def get_ReturnsDataframe(self):
        return self._ReturnsDataframe
    ReturnsDataframe = property(get_ReturnsDataframe, set_ReturnsDataframe)

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


    def set_MonthlyOrDaily(self,MonthlyOrDaily):
        self._MonthlyOrDaily = MonthlyOrDaily
    def get_MonthlyOrDaily(self):
        return self._MonthlyOrDaily
    MonthlyOrDaily = property(get_MonthlyOrDaily, set_MonthlyOrDaily)

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
                     ,  monthlyordaily='monthly'
                     ,  pctchangeorlogreturn = 'pctchange'
                     ,  showresults = 0):
        print('Initialized class builddataframeofrefdateminusd2tod1stockpricechanges')
        from random import shuffle
        shuffle(list_of_symbols)
        self.SymbolsList = list_of_symbols
        self.StartDateString = startdate_string
        self.MonthlyOrDaily = monthlyordaily
        self.PctChangeOrLogReturn = pctchangeorlogreturn
        self.ReturnsDataframe = self.returnsdataframe()
        #self.BottomConstraint = bottomconstraint
        #self.TopConstraint = topconstraint
        #self.MonthlyReturnsDataframe = self.monthlyreturnsdataframe()
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




#    def monthlyreturnsdataframe(self,
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
#        df_largest = pd.DataFrame(index=index, columns=columns)
#        df_largest = df_largest.fillna(0) # with 0s rather than NaNs
#        #print df_largest
#        #while len(dict_of_dfs_bysize) < len(dict_of_dfs):
#        keyoflargestdf = ''
#        for k,v in dict_of_dfs.items():
#            if len(v) > len(df_largest):
#                df_largest = v
#                keyoflargestdf = k
#                #break
#        
#        df_align = df_largest[['b_periodend','e_pctchange']]
#        df_align = df_align.set_index('b_periodend')
#        df_align.columns = [keyoflargestdf]
#        df_align.sort_index
#        #print df_align
#        #print df_largest
#
##            if passed == 0:        
##                df_align = v[['b_periodend','e_pctchange']]
##                df_align = df_align.set_index('b_periodend')
##                df_align.columns = [k]
##                df_align.sort_index
##                #sLength = len(df_align[k])
##                #originalid = k
##                
##            else:
#
#             
#        for k,v in dict_of_dfs.items():
#            if not k == keyoflargestdf:
#                df_new = v[['b_periodend','e_pctchange']]
#                df_new = df_new.set_index('b_periodend')
#                df_new.columns = [k]
#                df_new.sort_index
#                #print df_new
#                #df_align[k] = df_new.loc[k].shape[0]
#                #print df_new
#                #df_align[k] = pd.Series(df_new, index=df_align.index)
#                #df_align[k] = df_align[originalid].map(lambda x: df_new[k])
#                df_align[k] = df_new[k]
#        if showresults == 1:
#            print '----------------------------------------------------'
#            print '                 monthly returns'
#            print '----------------------------------------------------'
#            print df_align
#        #self.MonthlyReturnsDataframe = df_align
#        return df_align

    def returnsdataframe(self
                 , showresults = 0):

        #'^GSmr   ^OEX    ^VIX    ^OEX    ^MID   ^RUT   ^DJI
        if self.MonthlyOrDaily == 'daily':
            import pullreturnsdaily as pr
        else:
            import pullreturnsmonthly as pr
        dict_of_dfs = {}

        # Build the annualized returns series
        mysymbolslist = self.SymbolsList # list_of_symbols #['^GSPC','^DJI','^MID','^OEX','AAPL','LEO']
        ser_annual = pd.Series()
        for symbol in mysymbolslist:
            o = pr.perform(symbol,self.StartDateString)
            df = o.ReturnsDataframe
            dict_of_dfs[symbol] = df
            annualizedreturn = o.annualizedreturn()
            ser_annual = ser_annual.set_value(symbol, annualizedreturn)
        if not showresults == 0:
            print '----- ser_annual -----'
            print ser_annual
        print '1111111111111111111111111111111111111111111111111111111111111'
        self.AnnualizedReturnsSeries = ser_annual 
        

  
#        mysymbolslist = self.SymbolsList # list_of_symbols #['^GSPC','^DJI','^MID','^OEX','AAPL','LEO']
#        #ser_annual = pd.Series()
#        for symbol in mysymbolslist:
#            o = pr.perform(symbol,self.StartDateString)
#            df = o.ReturnsDataframe
#            dict_of_dfs[symbol] = df
            
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
        
        
        df_align = df_largest[['b_periodend','e_'+ self.PctChangeOrLogReturn]]
        df_align = df_align.set_index('b_periodend')
        df_align.columns = [keyoflargestdf]
        df_align.sort_index
        #print df_align
        #print df_largest

#            if passed == 0:        
#                df_align = v[['b_periodend','e_pctchange']]
#                df_align = df_align.set_index('b_periodend')
#                df_align.columns = [k]
#                df_align.sort_index
#                #sLength = len(df_align[k])
#                #originalid = k
#                
#            else:

             
        for k,v in dict_of_dfs.items():
            if not k == keyoflargestdf:
                df_new = v[['b_periodend','e_' + self.PctChangeOrLogReturn]]
                df_new = df_new.set_index('b_periodend')
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
            print '                 returns'
            print '----------------------------------------------------'
            print df_align
        #self.MonthlyReturnsDataframe = df_align
        return df_align





    def covariancematrix(self
#            , monthlyordaily='monthly'
#            , pctchangeorlogreturn = 'pctchange'
                 ):

        #'^GSmr   ^OEX    ^VIX    ^OEX    ^MID   ^RUT   ^DJI
        
#        import numpy as np
#        import pandas as pd

        #df_align = self.MonthlyReturnsDataframe #monthlyreturns(list_of_symbols)
        #df_align = self.returnsdataframe(monthlyordaily)
        #df_align = self.returnsdataframe(monthlyordaily,pctchangeorlogreturn)
        df_align = self.ReturnsDataframe
        df_align = df_align.dropna()
        
        
        covmatrix_array = np.cov(df_align,None,0)
        #good np.savetxt("cov.csv", covmatrix_array, delimiter=",", fmt='%s')
        
        rows = np.array(list(df_align))[: np.newaxis]
        #str_data = np.char.mod("%10.6f", df_align)
        
        #print str_data
        #print rows
        #print list(df_align)
        
        
        dfcovariancematrix = pd.DataFrame(covmatrix_array, index=rows, columns=list(df_align))
#        if monthlyordaily == 'daily':
#            for i in range(len(dfcovariancematrix)):
#                print dfcovariancematrix.iloc[i] 
#                
        return dfcovariancematrix
#        print '----------------------------------------------------'
#        print '                 covariance matrix'
#        print '----------------------------------------------------'
#        print dfcovariancematrix
#        dfcovariancematrix.to_csv('cov1.csv',columns=(list(df_align)))
        


    def correlationmatrix(self
#            , monthlyordaily='monthly'
#            , pctchangeorlogreturn = 'pctchange'
                 ):

        #'^GSmr   ^OEX    ^VIX    ^OEX    ^MID   ^RUT   ^DJI
        
#        import numpy as np
#        import pandas as pd

#        print '----------------------------------------------------'
#        print '                 monthly returns'
#        print '----------------------------------------------------'

        #df_align = self.MonthlyReturnsDataframe #self.monthlyreturns(list_of_symbols)
        #df_align = self.returnsdataframe(monthlyordaily,pctchangeorlogreturn)
        df_align = self.ReturnsDataframe
        df_align = df_align.dropna()
        
        rows = np.array(list(df_align))[: np.newaxis]

        #print rows
        
        corrmatrix_array = np.corrcoef(df_align.T.values.tolist())
        #print corrmatrix_array
        
        dfcorrelationmatrix = pd.DataFrame(corrmatrix_array, index=rows, columns=list(df_align))
#        print '----------------------------------------------------'
#        print '                 correlation matrix'
#        print '----------------------------------------------------'
        
        #print dfcorrelationmatrix
        #dfcorrelationmatrix.to_csv('corr1.csv',columns=(list(df_align)))
        
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
        print 'wwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwww'
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
        print 'pppppppppppppppppppppppppppppppppppppppppppp'
        rws = self.randomweightseries()
        print self.AnnualizedReturnsSeries
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
    o = perform(['^GSPC','^DJI','^OEX','^RUT'],'2009-12-31') # '^GSPC','^OEX','^MID','^RUT','^DJI'
    #print o.returnsdataframe('daily','logreturn')
    #print o.correlationmatrix('monthly','logreturn')
    #print o.covariancematrix('monthly','logreturn')
    
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

              ^GSPC          ^OEX          ^DJI          ^RUT
^GSPC  9.709136e-05  9.330074e-05  8.714657e-05  0.0001244121
^OEX   9.330074e-05  9.046865e-05  8.441669e-05   0.000117338
^DJI   8.714657e-05  8.441669e-05  8.211599e-05  0.0001087609
^RUT   0.0001244121   0.000117338  0.0001087609  0.0001854829

'''
       
#    MonthlyReturnsDataframe = o.MonthlyReturnsDataframe
#    randomweightseries = o.randomweightseries()
#    equalweightsseries = o.equalweightseries()
#    AnnualizedReturnsSeries = o.AnnualizedReturnsSeries
#    #portfolioreturnrandomweights = o.portfolioreturnrandomweights()
#    #portfolioreturnequalweights = o.portfolioreturnequalweights()
#    #portfoliostandarddeviationrandomweights = o.portfoliostandarddeviationrandomweights()
#    #portfoliostandarddeviationequalweights = o.portfoliostandarddeviationequalweights()
#    print '----- MonthlyReturnsDataframe -----'
#    print MonthlyReturnsDataframe    
#    print '----- randomweightseries -----'
#    print randomweightseries
#    print '----- equalweightsseries -----'
#    print equalweightsseries
#
#    print '----- AnnualizedReturnsSeries -----'
#    print AnnualizedReturnsSeries
#    
##    print '----- portfolioreturnequalweights -----'
##    print o.portfolioreturnequalweights
##    print '----- portfoliostandarddeviationequalweights -----'
##    print o.portfoliostandarddeviationequalweights    
#    
#    print '---------------------------------------'
#    print 'permutations '
#    print '---------------------------------------'
#    print 'ok here is the data'
#    for i in range(3):
#        permutation_series = o.portfolioriskreturnrandomweight()
#        print '---------------------'
#        print '---portfolio weights'
#        print '---------------------'
#        for idx in permutation_series['randomweightseries'].iteritems():
#            print idx
#        print '---portfolioreturn',permutation_series['portfolioreturn']
#        print '---portfoliostandarddeviation',permutation_series['portfoliostandarddeviation']
#            #print j,permutation_series['randomweightseries'].iloc[j],permutation_series['randomweightseries'][j].index
#            #print randweight
#
#
##    print '----- portfolioreturnrandomweights -----'
##    print o.portfolioreturnrandomweights()
##    print o.portfolioreturnrandomweights()
##    print o.portfolioreturnrandomweights()
##    print o.portfolioreturnrandomweights()
##    
##    print '----- portfoliostandarddeviationrandomweights -----'    
##    print o.portfoliostandarddeviationrandomweights()
##    print o.portfoliostandarddeviationrandomweights()
##    print o.portfoliostandarddeviationrandomweights()
##    print o.portfoliostandarddeviationrandomweights()
#    
#
#    print 'there was no method from chosen library calccovcorrmatrix  ***************************************'