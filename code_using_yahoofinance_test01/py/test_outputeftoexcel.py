# -*- coding: utf-8 -*-
"""
Created on Wed Aug 12 15:17:22 2015

@author: justin.malinchak
"""

import shutil
 
def copyFile(src, dest):
    try:
        shutil.copy(src, dest)
    # eg. src and dest are the same file
    except shutil.Error as e:
        print('Error: %s' % e)
    # eg. source or destination doesn't exist
    except IOError as e:
        print('Error: %s' % e.strerror)

def get_sheet_by_name(book, name):
    """Get a sheet by name from xlwt.Workbook, a strangely missing method.
    Returns None if no sheet with the given name is present.
    """
    # Note, we have to use exceptions for flow control because the
    # xlwt API is broken and gives us no other choice.
    import itertools
    try:
        for idx in itertools.count():
            sheet = book.get_sheet(idx)
            if sheet.name == name:
                return sheet
    except IndexError:
        return None
        
import datetime
def last_day_of_month(date):
    if date.month == 12:
        return date.replace(day=31)
    return date.replace(month=date.month+1, day=1) - datetime.timedelta(days=1)

import ntpath  
def path_leaf(path):
    head, tail = ntpath.split(path)
    return tail or ntpath.basename(head)

def assure_path_exists(path):
    import os
    dir = os.path.dirname(path)
    if not os.path.exists(dir):
            os.makedirs(dir)
            
import os
import xlwt
import config

class output:
    def __init__(self
              , list_of_symbols = ['NKE','T']
              , startdatestring = '2005-12-31'
              , returnsmonthlyordaily = 'monthly'
            ):
        self.tryit(list_of_symbols
            ,startdatestring
            ,returnsmonthlyordaily)


 
    #----------------------------------------------------------------------
    def createworkbook(self,filepath = 'test.xls'):
        """"""
        book = xlwt.Workbook()
        sheet1 = book.add_sheet("returns")
        sheet1 = book.add_sheet("covariancematrix")
        sheet1 = book.add_sheet("correlationmatrix")
        print sheet1.name
#        cols = ["A", "B", "C", "D", "E"]
#        txt = "Row %s, Col %s"
#     
#        for num in range(5):
#            row = sheet1.row(num)
#            for index, col in enumerate(cols):
#                value = txt % (num+1, col)
#                row.write(index, value)
     
        book.save(filepath)
 
#----------------------------------------------------------------------

    def tryit(self
              , list_of_symbols 
              , startdatestring 
              , returnsmonthlyordaily
              ):
        # ##########
        # Date setup
        import datetime
        today_datetime = datetime.datetime.today()
        #today_date = datetime.date.today()
        #print today_date
        today_datetime_string = today_datetime.strftime('%Y%m%d%H%M%S')
        print today_datetime_string
        finalfilename =  today_datetime_string+'.xls'
        inputfilename = today_datetime_string+'-temp.xls'
        self.createworkbook(config.myoutputpath+'\\'+inputfilename)
        if os.path.isfile(config.myoutputpath+'\\'+inputfilename):
            # ------------------------------------
            # Get the data first
            import outputefficientfrontier as oef
            o = oef.output(list_of_symbols,startdatestring,returnsmonthlyordaily) 
            


#            for index, row in df.iterrows():
#                try:
#                    fartomidpricechangedelta = (row['priceDaysBackMid'] - row['priceDaysBackFar']) / row['priceDaysBackFar']

            # --------------------------------
            # Then open the workbook here
            from win32com.client import Dispatch
            xlApp = Dispatch("Excel.Application")
            xlApp.Visible = 1
            wb = xlApp.Workbooks.Open(config.myoutputpath+'\\'+inputfilename)
            
            # --------------------------------
            # Then populate the worksheet here
            df = o.EfficientFrontierObject.ReturnsDataframe
            #print df
            titlesrow = 3
            titlescolumn = 3
            rowid = 0
            colid = 0
            for cname in df.columns:
                #print 'column',cname
                colid = colid + 1
                wb.Sheets('returns').Cells(titlesrow,titlescolumn+colid).Value = cname
                
            for index, row in df.iterrows():
                rowid = rowid + 1
                wb.Sheets('returns').Cells(titlesrow + rowid,titlescolumn).Value = index
                #print 'x'
                colid = 0
                #for cl in row:
                for cname in df.columns:
                    colid = colid + 1
                    #print rowid,colid,cl
                    #print str(df.loc[index][cname]) == str('nan')
                    if not str(df.loc[index][cname]) == str('nan'):
                        
                        wb.Sheets('returns').Cells(titlesrow+rowid,titlescolumn+colid).Value = df.loc[index][cname]

            # --------------------------------
            # Then populate the worksheet here - covariancematrix
            df = o.EfficientFrontierObject.covariancematrix()                    
            
            titlesrow = 3
            titlescolumn = 3
            rowid = 0
            colid = 0
            for cname in df.columns:
                #print 'column',cname
                colid = colid + 1
                wb.Sheets('covariancematrix').Cells(titlesrow,titlescolumn+colid).Value = cname
                
            for index, row in df.iterrows():
                rowid = rowid + 1
                wb.Sheets('covariancematrix').Cells(titlesrow + rowid,titlescolumn).Value = index
                #print 'x'
                colid = 0
                for cl in row:
                    colid = colid + 1
                    #print rowid,colid,cl
                    wb.Sheets('covariancematrix').Cells(titlesrow+rowid,titlescolumn+colid).Value = cl
            wb.Close(SaveChanges=1) # see note 1
            xlApp.Quit()
            xlApp.Visible = 0 # see note 2
            del xlApp
            os.rename(config.myoutputpath+'\\'+inputfilename,config.myoutputpath+'\\'+finalfilename)



#    
#    #    
#    #    # ------------------------------------------------
#    #    # Create the Excel file from template if necessary
#    #    if len(maxperiod) > 0:
#    #        print 'maxperiod:',maxperiod
#    #        
#    #        inputfilename = template_inputfilename.replace('YYYY-MM',maxperiod).replace('%','')
#    #        
#    #        month_asminimalcharacters = str(int(lastdayofmaxperiod.strftime("%m")))
#    #        year_as2character = (lastdayofmaxperiod.strftime("%Y"))[-2:]
#    #        resolved_destination_pathfile = resolved_destination_path + '\\' + path_leaf(template_inputfilename).replace('YYYY-MM',month_asminimalcharacters+'-'+year_as2character).replace('%','').replace('inputs','inputs (automated)')
#    #    
#    #        
#    #        if not os.path.isfile(inputfilename):
#    #            print 'file',inputfilename, 'does not exist'
#    #            copyFile(template_inputfilename,inputfilename)
#    #            if not os.path.isfile(inputfilename):
#    #                print 'tried to copy',template_inputfilename,'to make the file, but process failed.'
#    #            else:
#    #                print 'ok ok, your file now exists.'
#    #                
#            # ---------------------------------------
#            # Now open the excel file and populate it
#                
#            # ------------------------------------------------------------------------------------
#            # Couldn't find much from pandas on how to do it, you may want to look into this later 
#            #    import pandas as pd
#            #    xl = pd.ExcelFile(inputfilename)
#            #    
#            #    for sn in xl.sheet_names:
#            #        print sn
#            #        print sn.cells(1,18)
#            #    xl.close        
#                    
#            # -----------------------
#            # This seems to work fine
#            if os.path.isfile(inputfilename):
#                # ------------------------------------
#                # Get the data into a dictionary first
#                dict_ref = {}
#                from xlrd import open_workbook
#                book = open_workbook(inputfilename,on_demand=True)        
#        
#                sheet = book.sheet_by_name('Sheet1')
#                        
#                for k,v in dict_returns.items():
#                    # Attempt to find a matching row (search the first column for 'john')
#                    rowIndex = -1
#                    for cell in sheet.col(1): # 
#                        rowIndex = rowIndex + 1
#                        if k == cell.value:
#                            print 'found it:',k,v,sheet.cell(rowIndex,3).value,rowIndex+1
#                            dict_ref[k] = [rowIndex+1,v]
#        
#                # --------------------------------
#                # Then populate the worksheet here
#                from win32com.client import Dispatch
#                xlApp = Dispatch("Excel.Application")
#                xlApp.Visible = 1
#                xlApp.Workbooks.Open(inputfilename)
#                
#                for k,v in dict_ref.items():
#                    print k,v
#                    xlApp.ActiveWorkbook.ActiveSheet.Cells(v[0],4).Value = v[1]
#                    xlApp.ActiveWorkbook.ActiveSheet.cells(v[0],3).Value = lastdayofmaxperiod_formatted
#                xlApp.ActiveWorkbook.Close(SaveChanges=1) # see note 1
#                xlApp.Quit()
#                xlApp.Visible = 0 # see note 2
#                del xlApp
#                
#                assure_path_exists(resolved_destination_pathfile)
#                copyFile(inputfilename,resolved_destination_pathfile)
#                print 'You can find your final file here:',resolved_destination_pathfile
#    ## =====================================
#    #print 'my test here'
#    #print '----------'
#    #query = "Select * from ProductValues where SourceName = 'MSCI' and ProductName like '%USA%' and Period = '2015-05';"
#    #df = psql.read_sql(query, conn)
#    #print df
#    ## =====================================
#    import outputefficientfrontier as oef
#    o = oef.output(['WMT','NKE','T','JPM','^RUT'],'2005-12-31','monthly') 
#    df = o.EfficientFrontierObject.covariancematrix()

if __name__=='__main__':
    #o = output(list_of_symbols = ['^RUT','NKE','T','GOOG','WMT','LEO','VTR','FB','BX','DDD','MSFT','IWM','EWZ']
    o = output(list_of_symbols = ['GOOG','FB']
              , startdatestring = '2009-12-31'
              , returnsmonthlyordaily ='daily'
              ) 