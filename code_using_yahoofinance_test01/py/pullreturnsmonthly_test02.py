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

#    def set_Period(self,Period):
#        self._Period = Period
#    def get_Period(self):
#        return self._Period
#    Period = property(get_Period, set_Period)

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
                    #, period = 'monthly' #or daily
                    , source = 'Yahoo'
                    #, enddate_string='xxx'
                ):
        print('Initialized class pullreturns.perform')
        
        self.Symbol = symbol
        self.StartDateString = startdate_string
        #self.Period = period
        
        import datetime
        #today_datetime = datetime.datetime.today()
        #today_date = datetime.date.today()
        yesterday_date = datetime.date.fromordinal(datetime.date.today().toordinal()-1)
        
        import pullprices as pp
        self.StockHistoryDataframe = pp.stockhistorybackfilledtodatframeofstockhistoryinstancesusingcache(symbol,startdate_string,str(yesterday_date)) #,str(today_date))
        self.ReturnsDataframe = self.monthlyreturns

    def monthlyreturns(self,):
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
        #print list(df_00)#['Close','Adj Close']
        #print df_00[['Close','Adj Close']]
        
        import pandas as pd
        dates1 = pd.date_range('1910-01', str(today_date)[:7], freq='M')
        
        dummy_date = datetime.datetime.strptime("1801-01-01", "%Y-%m-%d")
        prev_date = dummy_date
        prev_value = float('Nan')
        
        rows_monthlyreturns = []        
        #rows_optionpricescurrent.append(['optionsymbol','stockprice','strike','pdeltapct_to_sell_price','cumprob_to_sell_price','bid','ask','last'])
        #rows_monthlyreturns.append(['a_symbol','b_periodend','e_pctchange','d_end'])
        rows_monthlyreturns.append(['a_symbol','b_periodend','e_pctchange','f_logreturn','d_end'])

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
                    rows_monthlyreturns.append([symbol,curr_date,change_pct,logreturn_pct,curr_value])
                    #'{percent:.2%}'.format(percent=pdeltapct_to_sell_price)
                    #print symbol,curr_date,change_pct
                    
                prev_date = dt.date()
                prev_value = myobj['Adj Close']
        
        
        headers = rows_monthlyreturns.pop(0)
        df_monthlyreturns = pd.DataFrame(rows_monthlyreturns,columns=headers)
        import numpy as np
        df_monthlyreturnsfinite = df_monthlyreturns[np.isfinite(df_monthlyreturns['e_pctchange'])]
        #print df_monthlyreturnsfinite
        #print df_00
        import pullprices as pp
        stock_dataframe = pp.stock_dataframe(symbol)
        myobj = df_00.loc[str(prev_date)]
        prev_ending = myobj['Adj Close']
        curr_price = stock_dataframe['last'][0]
        if is_number(curr_price) and is_number(prev_ending):
            curr_logreturn = math.log(float(curr_price) / float(prev_ending)) 
            curr_pctchange = (float(curr_price) - float(prev_ending)) / float(prev_ending)
        else:
            curr_pctchange = float('NaN')
        
        #df_curr = pd.DataFrame([symbol,today_date,curr_pctchange], columns=['a_symbol','b_periodend','e_pctchange'])
        #newrow = np.array([symbol,today_date,curr_pctchange])
        #columns=['a_symbol','b_periodend','e_pctchange','d_end']
        
        #import numpy as np
        
        mydict = {}
        mydict[0] = {'a_symbol':symbol,'b_periodend':str(today_date),'e_pctchange':curr_pctchange,'f_logreturn':curr_logreturn,'d_end':curr_price}
        df_curr = pd.DataFrame(mydict).T
        #print df_curr.T
        
        
        df_monthlyreturnstotoday = df_monthlyreturnsfinite.append(df_curr, ignore_index=True)
        #print df_monthlyreturns
        #print str(today_date)[:7]
        return df_monthlyreturnstotoday
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
        
        #df_monthlyreturnsfinite.append(s)
        #print df_monthlyreturnsfinite
        
        #print ls_00
        
        
        #import datetime
        #
        #start = datetime.datetime.strptime("2014-01-01", "%Y-%m-%d")
        #end = datetime.datetime.strptime("2015-07-31", "%Y-%m-%d")
        #date_generated = [start + datetime.timedelta(days=x) for x in range(0, (end-start).days)]
        #
        #for date in date_generated:
        #    print date.strftime("%d-%m-%Y")

    def annualizedreturn(self,uselogreturns=False):
        if uselogreturns == False:
            ar = self._annualizedmonthlyreturn()            
        else:
            ar = self._annualizedmonthlyreturnusinglogreturns()

        return ar
        
#    def annualizedreturn(self,):
#        
#        ar = self._annualizedmonthlyreturn()
#        return ar
        
    def _annualizedmonthlyreturn(self,):
        #=PRODUCT(F85:F155)^(1/($B85/12))-1
        df_monthlyreturnsusingyahoosymbol = self.monthlyreturns()
        df_monthlyreturnsusingyahoosymbol = df_monthlyreturnsusingyahoosymbol.dropna()
        df_monthlyreturnsusingyahoosymbol.sort_index(inplace = True)                
        df_monthlyreturnsusingyahoosymbol.loc[df_monthlyreturnsusingyahoosymbol.index,'e_pctchangeunitized']= df_monthlyreturnsusingyahoosymbol.loc[df_monthlyreturnsusingyahoosymbol.index, 'e_pctchange'] + float(1.0)
        ls_monthlyreturnsusingyahoosymbol = df_monthlyreturnsusingyahoosymbol['e_pctchangeunitized'].values.tolist()
        listmultiplied = reduce(lambda x, y: x*y, ls_monthlyreturnsusingyahoosymbol)
        annualizedreturn = listmultiplied ** (float(1)/(float(len(ls_monthlyreturnsusingyahoosymbol)/float(12)))) - 1.0
        return annualizedreturn


    def _annualizedmonthlyreturnusinglogreturns(self,):
        # =PRODUCT(F85:F155)^(1/($B85/12))-1
        # [(1.13)*(0.98)*(1.15)*(1.08)]^(12/42)-1
        df_monthlyreturns = self.monthlyreturns()
        df_monthlyreturns = df_monthlyreturns.dropna()
        
        df_monthlyreturns.sort_index(inplace = True)
        #ttttt
        #firstdate = df_monthlyreturns.loc[0]['b_periodend']
        firstdate = self.StartDateString
        #print firstdate
        lastdate = df_monthlyreturns.loc[len(df_monthlyreturns)-1]['b_periodend']
        #print lastdate
        #print df_monthlyreturns
        df_monthlyreturns.loc[df_monthlyreturns.index,'f_logreturnunitized']= df_monthlyreturns.loc[df_monthlyreturns.index, 'f_logreturn'] + float(1.0)
        ls_monthlyreturns = df_monthlyreturns['f_logreturnunitized'].values.tolist()
        listmultiplied = reduce(lambda x, y: x*y, ls_monthlyreturns)
        #print listmultiplied

        #years between
        import datetime
        time1 = datetime.datetime.strptime(str(firstdate) + ' 16:00', "%Y-%m-%d %H:%M")
        time2 = datetime.datetime.strptime(str(lastdate) + ' 16:00', "%Y-%m-%d %H:%M") #datetime.datetime.now() 
        elapsedTime = time2 - time1
        yrs = float(divmod(elapsedTime.total_seconds(), 60.0)[0]/60.0/24.0/365.0)
        #print 'yrs',yrs

        adr = listmultiplied ** (float(1)/(yrs)) - 1.0
        return adr


    def standarddeviationofmonthlyreturns(self,):
        df_monthlyreturnsusingyahoosymbol = df_monthlyreturnsusingyahoosymbol = self.MonthlyReturnsDataframe
        std_float = float(df_monthlyreturnsusingyahoosymbol['e_pctchange'].std())
        return std_float
    
if __name__=='__main__':
    symbol = '^GSPC' # ,'^RUT','^DJI','AAPL','^GSPC','^OEX','^MID'
    startdate = '2012-12-31'
    o = perform(symbol,startdate)
    print '------ MonthlyReturnsDataframe ------'
    print o.monthlyreturns()
    print 'annualizedreturn', o.annualizedreturn(True)
