import pullreturns
import config
import mytools
import os
import pandas as pd
import shutil

class perform:
    def set_Symbol(self,Symbol):
        self._Symbol = Symbol
    def get_Symbol(self):
        return self._Symbol
    Symbol = property(get_Symbol, set_Symbol)

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
    
    def __init__(self
                    , symbol
                    , startdate_string='2004-12-31'
                    , period = 'monthly' #or daily
                    , source = 'Yahoo'
                    #, enddate_string='xxx'
                ):
                self.Symbol = symbol
                self.StartDateString = startdate_string
                self.Period = period
                self.Source = source
                o = pullreturns.perform(symbol,startdate_string,period,source)
                self.ReturnsDataframe = o.ReturnsDataframe
                df = o.ReturnsDataframe()
                print 'Length of returns dataframe', len(df)
                enddate = df.tail(1)['b_monthend'].values[0]
                print 'enddate', enddate
                mycachefolder = config.mycachefolder
                
                mytools.general().make_sure_path_exists(mycachefolder)

                cachedfilepathname = mycachefolder + '\\procoutput returnsyahoo '+ symbol + ' ' + startdate_string + ' ' + enddate + '.csv'
                watchfolderpathname = config.mywatcherfolder + '\\procoutput returnsyahoo '+ symbol + ' ' + startdate_string + ' ' + enddate + '.csv'
                df.to_csv(cachedfilepathname,columns=('a_symbol',   'b_monthend',    'd_end', 'e_pctchange'))

                if os.path.isfile(cachedfilepathname):
                    print('   Found cached file:  '+cachedfilepathname)
                    df_hist = pd.read_csv(cachedfilepathname,index_col=0)
                else:
                    print('   Getting new file:'+cachedfilepathname)
                    #df_hist = DataReader(symbol,  "yahoo", fromdate,todate)
                    
                print '------ copying file to watchfolder ------'
                #E:\DATA\Batches\prod\WatchFolder\incoming
                print config.mywatcherfolder
                shutil.copy(cachedfilepathname, config.mywatcherfolder)
                if os.path.isfile(watchfolderpathname):
                    
                    print('   Found watch file:  '+watchfolderpathname)
                    #df_hist = pd.read_csv(watchfolderpathname,index_col=0)
                else:
                    print('   Did not find watch file:  '+watchfolderpathname)


                #os.system("C:/Batches/AutomationProjects/Watcher/code/bat/$execute-run-sql-script.bat     ")
                os.system(config.mywatchbatchfolder + '\\$execute-run-sql-script.bat     ')
                #C:\Batches\AutomationProjects\Watcher\code\bat\$execute-run-sql-script.bat    
                #from subprocess import Popen
                #p = Popen("$execute-run-sql-script.bat", cwd=r"C:\Batches\AutomationProjects\Watcher\code\bat")
                #stdout, stderr = p.communicate()

                

if __name__=='__main__':
    print 'running ___name___'
    symbol = 'BX' #,^RUT,'^DJI','AAPL','^GSPC','^OEX','^MID'
    startdate_string = '2008-12-31'
    
    o = perform(symbol,startdate_string,'daily','Yahoo')
    
    df = o.ReturnsDataframe()
