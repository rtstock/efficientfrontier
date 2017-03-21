# -*- coding: utf-8 -*-
"""
Created on Tue Jul 21 14:40:39 2015

@author: justin.malinchak
"""

def geometric_mean(nums):
    ''' 
        Return the geometric average of nums
        @param    list    nums    List of nums to avg
        @return   float   Geometric avg of nums 
    '''
    return (reduce(lambda x, y: x*y, nums))**(1.0/len(nums))

import datetime
def validate_date(date_text):
    try:
        datetime.datetime.strptime(date_text, '%Y-%m-%d')
        return True
    except ValueError:
        #raise ValueError("Incorrect data format, should be YYYY-MM-DD")
        return False
        
 
def is_number(s):
    try:
        float(s)
        return True
    except ValueError:
        return False
        
def test_builddataframe():
    import pandas as pd
    import numpy as np
    
    df = pd.DataFrame({'a':np.random.randn(5),
                        'b':np.random.randn(5),
                        'c':np.random.randn(5),
                        'd':np.random.randn(5)})
    cols_to_keep = ['a', 'c', 'd']
    dummies = ['d']
    not_dummies = [x for x in cols_to_keep if x not in dummies]
    data = df[not_dummies]
    print(data)

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

    def set_EndDateString(self,EndDateString):
        self._EndDateString = EndDateString
    def get_EndDateString(self):
        return self._EndDateString
    EndDateString = property(get_EndDateString, set_EndDateString)

    def set_Period(self,Period):
        self._Period = Period
    def get_Period(self):
        return self._Period
    Period = property(get_Period, set_Period)

    def set_StockHistoryDataframe(self,StockHistoryDataframe):
        self.StockHistoryDataframe = StockHistoryDataframe
    def get_StockHistoryDataframe(self):
        return self._StockHistoryDataframe
    StockHistoryDataframe = property(get_StockHistoryDataframe, set_StockHistoryDataframe)

    def set_ReturnsDataframe(self,ReturnsDataframe):
        self._ReturnsDataframe = ReturnsDataframe
    def get_ReturnsDataframe(self):
        return self._ReturnsDataframe
    ReturnsDataframe = property(get_ReturnsDataframe, set_ReturnsDataframe)

    def set_PriceHistoryDataframe(self,PriceHistoryDataframe):
        self._PriceHistoryDataframe = PriceHistoryDataframe
    def get_PriceHistoryDataframe(self):
        return self._PriceHistoryDataframe
    PriceHistoryDataframe = property(get_PriceHistoryDataframe, set_PriceHistoryDataframe)

    #FirstDateOfPriceHistory
    def set_FirstDateOfPriceHistory(self,FirstDateOfPriceHistory):
        self._FirstDateOfPriceHistory = FirstDateOfPriceHistory
    def get_FirstDateOfPriceHistory(self):
        return self._FirstDateOfPriceHistory
    FirstDateOfPriceHistory = property(get_FirstDateOfPriceHistory, set_FirstDateOfPriceHistory)

#    def set_MonthDayCharacter(self,MonthDayCharacter):
#        self._MonthDayCharacter = MonthDayCharacter
#    def get_MonthDayCharacter(self):
#        return self._MonthDayCharacter
#    MonthDayCharacter = property(get_MonthDayCharacter, set_MonthDayCharacter)



#    def set_MonthlyReturnsDataframe(self,MonthlyReturnsDataframe):
#        self._MonthlyReturnsDataframe = MonthlyReturnsDataframe
#    def get_MonthlyReturnsDataframe(self):
#        return self._MonthlyReturnsDataframe
#    MonthlyReturnsDataframe = property(get_MonthlyReturnsDataframe, set_MonthlyReturnsDataframe)
#
#    def set_DailyReturnsDataframe(self,DailyReturnsDataframe):
#        self._DailyReturnsDataframe = DailyReturnsDataframe
#    def get_DailyReturnsDataframe(self):
#        return self._DailyReturnsDataframe
#    DailyReturnsDataframe = property(get_DailyReturnsDataframe, set_DailyReturnsDataframe)
    
    def __init__(self
                    , symbol
                    , startdate_string='2004-12-31'
                    , enddate_string=''
                    , period = 'monthly' #or daily
                    , source = 'Yahoo'
                    #, enddate_string='xxx'
                ):
        print('Initialized class pullreturns.perform')

        #today_date = datetime.date.today()
        
        self.Symbol = symbol
        self.StartDateString = startdate_string
        self.EndDateString = enddate_string
        self.Period = period
        
        import datetime
        #today_datetime = datetime.datetime.today()
        
        
        startdate_date = datetime.datetime.strptime(startdate_string, "%Y-%m-%d")
        my_enddate_string = enddate_string
        yesterday_date = datetime.date.fromordinal(datetime.date.today().toordinal()-1)
        if len(my_enddate_string) == 0:
            my_enddate_string = str(yesterday_date)

        enddate_date = datetime.datetime.strptime(my_enddate_string, "%Y-%m-%d")
        
        if enddate_date <= startdate_date:
            my_enddate_string = str(yesterday_date)
            
        
        import pullprices as pp
        if period == 'monthly':
            self._StockHistoryDataframe = pp.stockhistorybackfilledtodatframeofstockhistoryinstancesusingcache(symbol,startdate_string,my_enddate_string) #,str(today_date))
            #self.MonthDayCharacter = 'M'
        else:
            self._StockHistoryDataframe = pp.stockhistorynobackfilltodataframeusingcache(symbol,startdate_string,my_enddate_string) #,str(today_date))
            #self.MonthDayCharacter = 'D'

        #Append todays price if no end date specified
        appendtodaysprice = False
        if enddate_string == '':
            appendtodaysprice = True
            
        self.ReturnsDataframe = self.calculatereturns(period=period,appendtodaysprice=appendtodaysprice)
        
        self.PriceHistoryDataframe = self.getpricehistory(period=period,appendtodaysprice=appendtodaysprice)
        self.FirstDateOfPriceHistory = self.PriceHistoryDataframe.index.tolist()[0]

    def getpricehistory(self,period='',appendtodaysprice=True):
        # Parameters
        #startdate_string = '2004-12-31'
        #symbol = '^GSPC   ^OEX    ^VIX    ^OEX    ^MID   ^RUT
        symbol = self.Symbol 
#        startdate_string = self.StartDateString
        # ##########
        # Date setup
        import datetime
        #today_datetime = datetime.datetime.today()
        today_date = datetime.date.today()
        df_00 = self.StockHistoryDataframe
        df_00.sort_index(inplace = True) 
        
        ##################
        #print df_00
        #print 'firstdate',df_00.index.tolist()[0]
        #wwwww
        

        import pandas as pd
        if period == '':
            period = self.Period
            
        if period == 'monthly':
            dates1 = pd.date_range('1910-01', str(today_date)[:7], freq='M')
        else:
            dates1 = pd.date_range('1910-01-01', str(today_date), freq='D')

        rows_stockhistory = []        
        rows_stockhistory.append(['a_symbol','b_periodend','e_adjclose'])

        for dt in dates1:
            if str(dt.date()) in df_00.index:
                #print str(dt.date()),'ok'
                myobj = df_00.loc[str(dt.date())]
                #print myobj
                curr_date = dt.date()
                curr_value = myobj['Adj Close']
                #if prev_date != dummy_date:
                rows_stockhistory.append([symbol,curr_date,curr_value])
        #print df_00.index       
        headers = rows_stockhistory.pop(0)
        df_monthlyprices = pd.DataFrame(rows_stockhistory,columns=headers)

        import numpy as np
        df_pricehistorytotodayfinite = df_monthlyprices[np.isfinite(df_monthlyprices['e_adjclose'])]
        if appendtodaysprice == True:
            import pullprices as pp
            stock_dataframe = pp.stock_dataframe(symbol)
            curr_price = stock_dataframe['last'][0]
    
            mydict = {}
            mydict[0] = {'a_symbol':symbol,'b_periodend':today_date,'e_adjclose':curr_price}
            df_curr = pd.DataFrame(mydict).T
            
            df_pricehistorytotoday = df_pricehistorytotodayfinite.append(df_curr, ignore_index=True)
        else:
            df_pricehistorytotoday = df_pricehistorytotodayfinite
            
        df_pricehistorytotoday.set_index(['b_periodend'], inplace=True)
        #print df_pricehistorytotoday
        return df_pricehistorytotoday

        
    def calculatereturns(self,period='',appendtodaysprice=True):
        # Parameters
        #startdate_string = '2004-12-31'
        #symbol = '^GSPC   ^OEX    ^VIX    ^OEX    ^MID   ^RUT
        symbol = self.Symbol 
#        startdate_string = self.StartDateString
        # ##########
        # Date setup
        import datetime
        #today_datetime = datetime.datetime.today()
        today_date = datetime.date.today()
#        yesterday_date = datetime.date.fromordinal(datetime.date.today().toordinal()-1)
        #print str(today_date)
        
#        import pullprices as pp
#        df_00 = pp.stockhistorybackfilledtodatframeofstockhistoryinstancesusingcache(symbol,startdate_string,str(yesterday_date)) #,str(today_date))
        df_00 = self.StockHistoryDataframe


        import pandas as pd
        #dates1 = pd.date_range('1910-01', str(today_date)[:7], freq=self.MonthDayCharacter)
        if period == '':
            period = self.Period
        if period == 'monthly':
            dates1 = pd.date_range('1910-01', str(today_date)[:7], freq='M')
        else:
            dates1 = pd.date_range('1910-01-01', str(today_date), freq='D')
            
        dummy_date = datetime.datetime.strptime("1801-01-01", "%Y-%m-%d")
        prev_date = dummy_date
        prev_value = float('Nan')
        
        rows_calculatereturns = []        
        #rows_optionpricescurrent.append(['optionsymbol','stockprice','strike','pdeltapct_to_sell_price','cumprob_to_sell_price','bid','ask','last'])
        #rows_calculatereturns.append(['a_symbol','b_periodend','e_pctchange','d_end'])
        rows_calculatereturns.append(['a_symbol','b_periodend','e_pctchange','e_logreturn','d_end'])

        import math
        for dt in dates1:
            if str(dt.date()) in df_00.index:
                #print dt.date()
                myobj = df_00.loc[str(dt.date())]
                #print myobj
                curr_date = dt.date()
                curr_value = myobj['Adj Close']
                if prev_date != dummy_date:
                    #print 'pullreturns curr_value,prev_value',curr_value,prev_value
                    if is_number(curr_value) and is_number(prev_value):
                        logreturn_pct = math.log(float(curr_value) / float(prev_value)) 
                        change_pct = (float(curr_value) - float(prev_value))/float(prev_value)
                    else:
                        change_pct =  float('NaN')
                    
                    #print symbol,prev_date,prev_value,curr_date,curr_value,change_pct
                    rows_calculatereturns.append([symbol,curr_date,change_pct,logreturn_pct,curr_value])
                    #'{percent:.2%}'.format(percent=pdeltapct_to_sell_price)
                    #print symbol,curr_date,change_pct
                    
                prev_date = dt.date()
                prev_value = myobj['Adj Close']
        
        
        headers = rows_calculatereturns.pop(0)
        df_calculatereturns = pd.DataFrame(rows_calculatereturns,columns=headers)
        import numpy as np
        df_calculatereturnsfinite = df_calculatereturns[np.isfinite(df_calculatereturns['e_pctchange'])]
        #print df_calculatereturnsfinite
        #print df_00
        #yyyyyy
        if appendtodaysprice == True:
            import pullprices as pp
            stock_dataframe = pp.stock_dataframe(symbol)
            myobj = df_00.loc[str(prev_date)]
            prev_ending = myobj['Adj Close']
            curr_price = stock_dataframe['last'][0]
            if is_number(curr_price) and is_number(prev_ending):
                curr_logreturn = math.log(float(curr_price) / float(prev_ending)) 
                curr_pctchange = (float(curr_price) - float(prev_ending)) / float(prev_ending)
            else:
                curr_logreturn = float('NaN')
                curr_pctchange = float('NaN')
            
            #df_curr = pd.DataFrame([symbol,today_date,curr_pctchange], columns=['a_symbol','b_periodend','e_pctchange'])
            #newrow = np.array([symbol,today_date,curr_pctchange])
            #columns=['a_symbol','b_periodend','e_pctchange','d_end']
            
            #import numpy as np
            
            mydict = {}
            mydict[0] = {'a_symbol':symbol,'b_periodend':today_date,'e_pctchange':curr_pctchange,'e_logreturn':curr_logreturn,'d_end':curr_price}
            df_curr = pd.DataFrame(mydict).T
            #print df_curr.T
            
            
            df_calculatereturnstotoday = df_calculatereturnsfinite.append(df_curr, ignore_index=True)
        else:
            df_calculatereturnstotoday = df_calculatereturnsfinite
            
        df_calculatereturnstotoday.set_index(['b_periodend'], inplace=True)
        #print df_calculatereturns
        #print str(today_date)[:7]
        return df_calculatereturnstotoday
        #index = np.arange(1) # array of numbers for the number of samples
        #df_curr = pd.DataFrame(columns=columns, index = index)
        #df.ix[0] = item
        #df_curr = pd.DataFrame(columns=columns)
        #df_curr.add(newrow,axis=columns)
        #print df_curr
        #data=newrow, index=[str(today_date)], 
        #DataFrame.add(other, axis='columns', level=None, fill_value=None)¶
        #s = df_curr.xs(0)
        #s.name = str(today_date)
        #print s
        
        #df_calculatereturnsfinite.append(s)
        #print df_calculatereturnsfinite
        
        #print ls_00
        
        
        #import datetime
        #
        #start = datetime.datetime.strptime("2014-01-01", "%Y-%m-%d")
        #end = datetime.datetime.strptime("2015-07-31", "%Y-%m-%d")
        #date_generated = [start + datetime.timedelta(days=x) for x in range(0, (end-start).days)]
        #
        #for date in date_generated:
        #    print date.strftime("%d-%m-%Y")
           
        

#    def annualizedreturn(self,uselogreturns=False):
#        if uselogreturns == False:
#            ar = self._annualizedmonthlyreturn()            
#        else:
#            ar = self._annualizedlogreturns()
#
#        return ar
        
#    def annualizedreturn(self,):
#        
#        ar = self._annualizedmonthlyreturn()
#        return ar
        
#    def _annualizedmonthlyreturn(self,):
#        #=PRODUCT(F85:F155)^(1/($B85/12))-1
#        df_calculatereturnsusingyahoosymbol = self.calculatereturns()
#        df_calculatereturnsusingyahoosymbol = df_calculatereturnsusingyahoosymbol.dropna()
#        df_calculatereturnsusingyahoosymbol.sort_index(inplace = True)                
#        df_calculatereturnsusingyahoosymbol.loc[df_calculatereturnsusingyahoosymbol.index,'e_pctchangeunitized']= df_calculatereturnsusingyahoosymbol.loc[df_calculatereturnsusingyahoosymbol.index, 'e_pctchange'] + float(1.0)
#        ls_calculatereturnsusingyahoosymbol = df_calculatereturnsusingyahoosymbol['e_pctchangeunitized'].values.tolist()
#        listmultiplied = reduce(lambda x, y: x*y, ls_calculatereturnsusingyahoosymbol)
#        annualizedreturn = listmultiplied ** (float(1)/(float(len(ls_calculatereturnsusingyahoosymbol)/float(12)))) - 1.0
#        return annualizedreturn


#    def _annualizedlogreturns(self,):
#        # =PRODUCT(F85:F155)^(1/($B85/12))-1
#        # [(1.13)*(0.98)*(1.15)*(1.08)]^(12/42)-1
#        df_calculatereturns = self.calculatereturns()
#        df_calculatereturns = df_calculatereturns.dropna()
#        
#        df_calculatereturns.sort_index(inplace = True)
#        #ttttt
#        #firstdate = df_calculatereturns.loc[0]['b_periodend']
#        firstdate = self.StartDateString
#        #print firstdate
#        lastdate = df_calculatereturns.loc[len(df_calculatereturns)-1]['b_periodend']
#        #print lastdate
#        #print df_calculatereturns
#        df_calculatereturns.loc[df_calculatereturns.index,'e_logreturnunitized']= df_calculatereturns.loc[df_calculatereturns.index, 'e_logreturn'] + float(1.0)
#        ls_calculatereturns = df_calculatereturns['e_logreturnunitized'].values.tolist()
#        listmultiplied = reduce(lambda x, y: x*y, ls_calculatereturns)
#        #print listmultiplied
#
#        #years between
#        import datetime
#        time1 = datetime.datetime.strptime(str(firstdate) + ' 16:00', "%Y-%m-%d %H:%M")
#        time2 = datetime.datetime.strptime(str(lastdate) + ' 16:00', "%Y-%m-%d %H:%M") #datetime.datetime.now() 
#        elapsedTime = time2 - time1
#        yrs = float(divmod(elapsedTime.total_seconds(), 60.0)[0]/60.0/24.0/365.0)
#        #print 'yrs',yrs
#
#        adr = listmultiplied ** (float(1)/(yrs)) - 1.0
#        return adr

    #ttttttt
    def annualizedreturn(self,logreturnorpctchange):
        # =PRODUCT(F85:F155)^(1/($B85/12))-1
        # [(1.13)*(0.98)*(1.15)*(1.08)]^(12/42)-1
        
        #df_calculatereturns = self.calculatereturns()
        #df_calculatereturns = df_calculatereturns.dropna()
        
        df_returns = self.ReturnsDataframe
        df_returns.sort_index(inplace = True)
        
        #print '-------- df_returns--------'
        #print df_returns
        
        #ttttt
        #firstdate = df_returns.loc[0]['b_periodend']
        ls_indexes = df_returns.index.get_values()
        
        #print 'first index=',ls_indexes[0]
        #print 'last index=',ls_indexes[len(ls_indexes)-1]
        firstdate = self.StartDateString # ls_indexes[0]
        #print 'firstdate',firstdate
        lastdate = ls_indexes[len(ls_indexes)-1] #df_returns.loc[len(df_returns)-1]['b_periodend']
        #print 'lastdate',lastdate
        #print df_returns
        df_returns['e_returnunitized'] = df_returns['e_'+logreturnorpctchange] + float(1.0)

        #print ' --------------------- df_returns-----------------'
        #print 'first date changed to:',str(df_returns.index.tolist()[0])
        #firstdate = str(df_returns.index.tolist()[0])
        firstdate = str(self.FirstDateOfPriceHistory)
        print 'self.FirstDateOfPriceHistory',str(self.FirstDateOfPriceHistory)
        
        ls_calculatereturns = df_returns['e_returnunitized'].values.tolist()
        listmultiplied = reduce(lambda x, y: x*y, ls_calculatereturns)
        #print listmultiplied

        #years between
        import datetime
        time1 = datetime.datetime.strptime(str(firstdate) + ' 09:30', "%Y-%m-%d %H:%M")
        #print time1
        time2 = datetime.datetime.strptime(str(lastdate) + ' 16:00', "%Y-%m-%d %H:%M") #datetime.datetime.now() 
        elapsedTime = time2 - time1
        yrs = float(divmod(elapsedTime.total_seconds(), 60.0)[0]/60.0/24.0/365.0)
        print 'time1',time1
        print 'time2',time2
        print 'yrs',yrs
        
        annualizedreturn = listmultiplied ** (float(1)/(yrs)) - 1.0
#        annualizedreturn = listmultiplied ** (float(1)/(float(len(ls_calculatereturnsusingyahoosymbol)/float(12)))) - 1.0
        return annualizedreturn



#    def standarddeviationofcalculatereturns(self,):
#        df_returnsusingyahoosymbol = df_returnsusingyahoosymbol = self.MonthlyReturnsDataframe
#        std_float = float(df_calculatereturnsusingyahoosymbol['e_pctchange'].std())
#        return std_float
    
if __name__=='__main__':
    #symbol = '^DJI' # ,'^RUT','^DJI','AAPL','^GSPC','^OEX','^MID'

    #import datetime
    today_datetime = datetime.datetime.today()
    today_datetime_string_forfilename = today_datetime.strftime('%Y%m%d%H%M%S')

    o = perform( symbol='^GSPC' # ,'^RUT','^DJI','AAPL','^GSPC','^OEX','^MID'
                ,startdate_string='2009-01-01'
                ,enddate_string='2015-08-07'
                ,period='daily')
    
    #df = o.PriceHistoryDataframe
    #print '------ ReturnsDataframe ------'
    #print o.ReturnsDataframe
    #import config
    #o.ReturnsDataframe.to_csv(config.myoutputpath + '/pullreturnsbyperiod ' + today_datetime_string_forfilename + '.csv',columns=('a_symbol','e_pctchange','e_logreturn','d_end'))
    
    logreturn = o.annualizedreturn('logreturn')
    print 'annualizedreturn log', logreturn
    pctchange = o.annualizedreturn('pctchange')
    print 'annualizedreturn pctchange', pctchange
    #print o.PriceHistoryDataframe