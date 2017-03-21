# -*- coding: utf-8 -*-
"""
Created on Tue Jul 21 14:40:39 2015

@author: justin.malinchak
"""
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

    def set_MonthlyReturnsDataframe(self,MonthlyReturnsDataframe):
        self._MonthlyReturnsDataframe = MonthlyReturnsDataframe
    def get_MonthlyReturnsDataframe(self):
        return self._MonthlyReturnsDataframe
    MonthlyReturnsDataframe = property(get_MonthlyReturnsDataframe, set_MonthlyReturnsDataframe)
    
    def __init__(self,
                     symbol,startdate_string='2004-12-31'):
        print('Initialized class pullreturns.perform')
        self.Symbol = symbol
        self.StartDateString = startdate_string
        self.MonthlyReturnsDataframe = self._monthlyreturnsusingyahoosymbol()
        
    def _monthlyreturnsusingyahoosymbol(self,):
        # Parameters
        #startdate_string = '2004-12-31'
        #symbol = '^GSPC   ^OEX    ^VIX    ^OEX    ^MID   ^RUT
        symbol = self.Symbol 
        startdate_string = self.StartDateString
        # ##########
        # Date setup
        import datetime
        #today_datetime = datetime.datetime.today()
        today_date = datetime.date.today()
        yesterday_date = datetime.date.fromordinal(datetime.date.today().toordinal()-1)
        #print str(today_date)
        
        import pullprices as pp
        df_00 = pp.stockhistorybackfilledtodatframeofstockhistoryinstancesusingcache(symbol,startdate_string,str(yesterday_date)) #,str(today_date))
        #print list(df_00)#['Close','Adj Close']
        #print df_00[['Close','Adj Close']]
        
        import pandas as pd
        dates1 = pd.date_range('1910-01', str(today_date)[:7], freq='M')
        
        dummy_date = datetime.datetime.strptime("1801-01-01", "%Y-%m-%d")
        prev_date = dummy_date
        prev_value = float('Nan')
        
        rows_monthlyreturns = []        
        #rows_optionpricescurrent.append(['optionsymbol','stockprice','strike','pdeltapct_to_sell_price','cumprob_to_sell_price','bid','ask','last'])
        rows_monthlyreturns.append(['a_symbol','b_monthend','e_pctchange','d_end'])
        
        
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
                        change_pct = (float(curr_value) - float(prev_value))/float(prev_value)
                    else:
                        change_pct =  float('NaN')
                    
                    #print symbol,prev_date,prev_value,curr_date,curr_value,change_pct
                    rows_monthlyreturns.append([symbol,curr_date,change_pct,curr_value])
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
        
        stock_dataframe = pp.stock_dataframe(symbol)
        myobj = df_00.loc[str(prev_date)]
        prev_ending = myobj['Adj Close']
        curr_price = stock_dataframe['last'][0]
        if is_number(curr_price) and is_number(prev_ending):
            curr_pctchange = (float(curr_price) - float(prev_ending)) / float(prev_ending)
        else:
            curr_pctchange = float('NaN')
        
        #df_curr = pd.DataFrame([symbol,today_date,curr_pctchange], columns=['a_symbol','b_monthend','e_pctchange'])
        #newrow = np.array([symbol,today_date,curr_pctchange])
        #columns=['a_symbol','b_monthend','e_pctchange','d_end']
        
        #import numpy as np
        
        mydict = {}
        mydict[0] = {'a_symbol':symbol,'b_monthend':str(today_date),'e_pctchange':curr_pctchange,'d_end':curr_price}
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
    
    def annualizedreturns(self,):
        #=PRODUCT(F85:F155)^(1/($B85/12))-1
        df_monthlyreturnsusingyahoosymbol = self.MonthlyReturnsDataframe
        df_monthlyreturnsusingyahoosymbol = df_monthlyreturnsusingyahoosymbol.dropna()

        #print '----- e_pctchange 2 ------'
        #print df_monthlyreturnsusingyahoosymbol.loc['e_pctchange']
        #df_monthlyreturnsusingyahoosymbol.set_index(['b_monthend'], inplace=True)
        df_monthlyreturnsusingyahoosymbol.sort_index(inplace = True)
        
        
        #df_monthlyreturnsusingyahoosymbol['e_pctchangeunitized'] = df_monthlyreturnsusingyahoosymbol.loc[df_monthlyreturnsusingyahoosymbol.index, 'e_pctchange'] + float(1.0)
        df_monthlyreturnsusingyahoosymbol.loc[df_monthlyreturnsusingyahoosymbol.index,'e_pctchangeunitized']= df_monthlyreturnsusingyahoosymbol.loc[df_monthlyreturnsusingyahoosymbol.index, 'e_pctchange'] + float(1.0)
        #df_monthlyreturnsusingyahoosymbol['e_pctchangeunitized'] = df_monthlyreturnsusingyahoosymbol['e_pctchange'] + float(1.0)
        #print '----- df_monthlyreturnsusingyahoosymbol ------'
        #print df_monthlyreturnsusingyahoosymbol
        #print df_monthlyreturnsusingyahoosymbol
        #print df_monthlyreturnsusingyahoosymbol #
        ls_monthlyreturnsusingyahoosymbol = df_monthlyreturnsusingyahoosymbol['e_pctchangeunitized'].values.tolist()
        #print ls_monthlyreturnsusingyahoosymbol
        #df_monthlyreturnsusingyahoosymbol
        listmultiplied = reduce(lambda x, y: x*y, ls_monthlyreturnsusingyahoosymbol)
        annualizedreturn = listmultiplied ** (float(1)/(float(len(ls_monthlyreturnsusingyahoosymbol)/float(12)))) - 1.0
        return annualizedreturn
        #print listmultiplied,len(ls_monthlyreturnsusingyahoosymbol)
        #print reduce(lambda x, y: x*y, [1,2,3,4,5,6])
    #    
    #    import operator
    #    import functools
    #    print functools.reduce(operator.mul, ls_monthlyreturnsusingyahoosymbol, 1)
        
    
        #return df_monthlyreturnsusingyahoosymbol
    def standarddeviationofmonthlyreturns(self,):
        df_monthlyreturnsusingyahoosymbol = df_monthlyreturnsusingyahoosymbol = self.MonthlyReturnsDataframe
        std_float = float(df_monthlyreturnsusingyahoosymbol['e_pctchange'].std())
        return std_float
    
if __name__=='__main__':
    symbol = 'MCD' # ,'^RUT','^DJI','AAPL','^GSPC','^OEX','^MID'
    startdate = '2005-12-31'
    o = perform(symbol,startdate)
    print '------ MonthlyReturnsDataframe ------'
    print o.MonthlyReturnsDataframe
    print '------ standarddeviationofmonthlyreturns() ------'
    print o.standarddeviationofmonthlyreturns()
    print '------ annualizedreturns() ------'
    print o.annualizedreturns()

    print 'there was no method from chosen library pullreturns **************************************** '