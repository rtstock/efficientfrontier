import pullreturns
import config
import mytools
import os
import pandas as pd
import shutil
import numpy as np
import sys

class perform:
    def __init__(self):
        print 'class initialized...'
        
    def set_Symbols(self,Symbols):
        self._Symbol = Symbols
    def get_Symbols(self):
        return self._Symbols
    Symbols = property(get_Symbols, set_Symbols)

    def set_StartDateString(self,StartDateString):
        self._StartDateString = StartDateString
    def get_StartDateString(self):
        return self._StartDateString
    StartDateString = property(get_StartDateString, set_StartDateString)

    def set_Period(self,Period):
        self._Period = Period
    def get_Period(self):
        return self._Period
    Period = property(get_Period, set_Period)

    def set_Source(self,Source):
        self._Source = Source
    def get_Source(self):
        return self._Source
    Source = property(get_Source, set_Source)
    
    def set_StockHistoryDataframe(self,StockHistoryDataframe):
        self._StockHistoryDataframe = StockHistoryDataframe
    def get_StockHistoryDataframe(self):
        return self._StockHistoryDataframe
    StockHistoryDataframe = property(get_StockHistoryDataframe, set_StockHistoryDataframe)

    def set_ReturnsDataframe(self,ReturnsDataframe):
        self._ReturnsDataframe = ReturnsDataframe
    def get_ReturnsDataframe(self):
        return self._ReturnsDataframe
    ReturnsDataframe = property(get_ReturnsDataframe, set_ReturnsDataframe)

    def set_CorrelationMatrix(self,CorrelationMatrix):
        self._CorrelationMatrix = CorrelationMatrix
    def get_CorrelationMatrix(self):
        return self._CorrelationMatrix
    CorrelationMatrix = property(get_CorrelationMatrix, set_CorrelationMatrix)

    

        
    #def getlistofsymbols(self,):
    #    import pullsp500weightsassymbols as pw
    #    mydict = pw.execute()
    #    mylist = []
    #    for k,v in mydict.items():
    #        print k,v
    #        mylist.append(v['Name'])
    #    return mylist
                
        

    def getlistofsymbols_fromdatabase(self, period='2016-08-08'):
        
        
        rows_weights = []        

        rows_weights.append(['a_symbol','b_weight'])
        
        import pyodbc
        import datetime
        import calendar
        import config
        cnxn = pyodbc.connect(config.localdatabaseconnectstring)
        cursor = cnxn.cursor()
        s_sql = 'select Ticker, DataValue from vWeightsOfIndexes where Period = (select max(Period) from vWeightsOfIndexes)'
        print s_sql
        cursor.execute(s_sql)
        symbolslist = []
        
        while 1:
            row = cursor.fetchone()
            
            if not row:
                break
            symbolslist.append(row[0])
            
        cnxn.close()
        return symbolslist

               
        
    def execute_old(self
                    , symbols
                    , startdate_string='2004-12-31'
                    , period = 'monthly' #or daily
                    , source = 'Yahoo'
                    #, enddate_string='xxx'
                ):
        self.Symbols = symbols
        self.StartDateString = startdate_string
        self.Period = period
        self.Source = source
        
        
        dict_of_dfs = {}
        for symbol in self.Symbols:
            print symbol
            try:
                o = pullreturns.perform(symbol,self.StartDateString,self.Period,self.Source)
                dict_of_dfs[symbol] = o.ReturnsDataframe()
            except:
                print 'skipped', symbol, 'because of error'
                pass
        #print dict_of_dfs
        passed = 0
        for k,v in dict_of_dfs.items():
            if passed == 0:        
                df_align = v[['b_monthend','e_pctchange']]
                df_align = df_align.set_index('b_monthend')
                df_align.columns = [k]
                print df_align
                sLength = len(df_align[k])
                originalid = k
                
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
            print '-----+++++++++'
            #print df_align[k]
            passed = 1

        print '----------------------------------------------------'
        print '                 monthly returns'
        print '----------------------------------------------------'
        df_align = df_align.dropna()
        print df_align

        rows = np.array(list(df_align))[: np.newaxis]

        print '----------------------------------------------------'
        print '                 correlation matrix'
        print '----------------------------------------------------'
        df_align = np.nan_to_num(df_align)
        
        corrmatrix_array = np.corrcoef(df_align.T.values.tolist())
        df_corr = pd.DataFrame(corrmatrix_array, index=rows, columns=list(df_align))
        return df_corr

    def execute(self
                    , symbols
                    , startdate_string='2004-12-31'
                    , period = 'monthly' #or daily
                    , source = 'Yahoo'
                    #, enddate_string='xxx'
                ):
        self.Symbols = symbols
        self.StartDateString = startdate_string
        self.Period = period
        self.Source = source
        
        
        dict_of_dfs = {}
        for symbol in self.Symbols:
            print symbol
            try:
                o = pullreturns.perform(symbol,self.StartDateString,self.Period,self.Source)
                dict_of_dfs[symbol] = o.ReturnsDataframe()
                print 'i = ',len(dict_of_dfs)
            except:
                print 'skipped', symbol, 'because of error'
                pass
        #print dict_of_dfs
        passed = 0
        iterations = 0
        for k,v in dict_of_dfs.items():
            iterations += 1
            print 'iterations',iterations
            if passed == 0:        
                df_align = v[['b_monthend','e_pctchange']]
                df_align = df_align.set_index('b_monthend')
                df_align.columns = [k]
                #print '---------------------------------------------------------------df_align'
                #print df_align
                sLength = len(df_align[k])
                originalid = k
                
            else:
                df_new = v[['b_monthend','e_pctchange']]
                df_new = df_new.set_index('b_monthend')
                df_new.columns = [k]
                df_new.sort_index
                #print df_new
                #df_align[k] = df_new.loc[k].shape[0]
                #print '---------------------------------------------------------------df_new'
                #print df_new
                #df_align[k] = pd.Series(df_new, index=df_align.index)
                #df_align[k] = df_align[originalid].map(lambda x: df_new[k])
                df_align[k] = df_new[k]
            print '-----++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++'
            #print df_align[k]
            passed = 1

        print '----------------------------------------------------'
        print '                 monthly returns'
        print '----------------------------------------------------'
        #df_align = df_align.dropna()
        print df_align
        
        
        rows = np.array(list(df_align))[: np.newaxis]
        
        
        print '----------------------------------------------------'
        print '                 correlation matrix'
        print '----------------------------------------------------'
        df = df_align.astype(float)
        
        #df2 = df.reset_index(drop=True) 
        #df3 = pd.DataFrame(df2.values)
        #print df3
        #print df.corr()

        #corrmatrix_array = np.corrcoef(df_align.T.values.tolist())
        corrmatrix_array = df.corr()
        covmatrix_array = df.cov()
        #corrmatrix_array = df_align.corr()
        #print '====================corrmatrix_array'
        #print corrmatrix_array
        
        df_corr = pd.DataFrame(corrmatrix_array, index=rows, columns=list(df_align))
        df_corr1 = np.round(df_corr, decimals=2)

        

        df_cov = pd.DataFrame(covmatrix_array, index=rows, columns=list(df_align))
        df_cov1 = np.round(df_cov, decimals=6)
        
        self.CorrelationMatrix = df_corr1
        self.CovarianceMatrix = df_cov1
        
        return df_corr1,df_cov
        

if __name__=='__main__':
    print 'running ___name___'

    #from pullsp500weightsassymbols import perform 
    import pullsp500weightsassymbols as pw
    myobject = pw.perform()
    mydict = myobject.DictionaryOfWeights
    symbols = []
    for k,v in mydict.items():
        symbols.append(v['Name'])
    #print symbols
    
    #symbols = ['AAPL','^RUT','^DJI','AAPL','^GSPC','^OEX','^MID']
    symbols = ['AAPL','FB','MSFT','BX','^GSPC']

    print 'len(sys.argv)',len(sys.argv)
    if len(sys.argv) > 1:
        print 'arg1: ', sys.argv[1]
        startdate_string = sys.argv[1]
    else:
        startdate_string = '2014-01-01'
        
    o = perform()
    
    o.execute(symbols,startdate_string,'monthly','Yahoo')
    df_corr = o.CorrelationMatrix
    print df_corr
    print 'df_corr'
    df_cov = o.CovarianceMatrix

    import datetime
    from datetime import timedelta
    filedatetime = datetime.datetime.today()
    filedatetime_string = filedatetime.strftime('%Y%m%d%H%M%S%M')
        
    path_to_csv_corr = config.mycachefolder + '\\correlation_'+filedatetime_string+'.csv'
    df_corr.to_csv(path_to_csv_corr)
    path_to_csv_cov = config.mycachefolder + '\\covariance_'+filedatetime_string+'.csv'
    df_cov.to_csv(path_to_csv_cov)
    print '--- corr ----'
    #print df_corr
    print '--- cov ----'
    #print df_cov
    
    #df = o.ReturnsDataframe()
    #print df
