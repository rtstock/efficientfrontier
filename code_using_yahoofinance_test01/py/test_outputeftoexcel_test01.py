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
              , startdatestring = '2012-12-31'
              , enddate_string = '2013-12-31'
              , returnsmonthlyordaily = 'monthly'
              , pctchangeorlogreturn = 'pctchange'
              , numberofpermutations = 1000, optimalpctasdecimal = 0.90
            ):
                
        self.tryit(list_of_symbols
            , startdatestring
            , enddate_string 
            , returnsmonthlyordaily
            , pctchangeorlogreturn
            , numberofpermutations , optimalpctasdecimal )


 
    #----------------------------------------------------------------------
    def createworkbook(self,filepath = 'demo.xlsx') :
        import xlsxwriter
        # Create an new Excel file and add a worksheet.
        workbook = xlsxwriter.Workbook('demo.xlsx')
        worksheet = workbook.add_worksheet()
        print worksheet.name
 
    #----------------------------------------------------------------------
    def createworkbook_old(self,filepath = 'test.xls'):
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
              , enddate_string 
              , returnsmonthlyordaily
              , pctchangeorlogreturn
              , numberofpermutations , optimalpctasdecimal 
              ):
        import xlsxwriter
        # ##########
        # Date setup
        import datetime
        today_datetime = datetime.datetime.today()
        #today_date = datetime.date.today()
        #print today_date
        today_datetime_string_forfilename = today_datetime.strftime('%Y%m%d%H%M%S')
        print today_datetime_string_forfilename
        finalfilename =  today_datetime_string_forfilename+'.xlsx'
        inputfilename = today_datetime_string_forfilename+'-temp.xlsx'
        #self.createworkbook(config.myoutputpath+'\\'+inputfilename)
                # Create an new Excel file and add a worksheet.
        

        #if os.path.isfile(config.myoutputpath+'\\'+inputfilename):
        # ------------------------------------
        # Get the data first
        import outputefficientfrontier as oef
        o = oef.output( list_of_symbols
                        ,  startdatestring
                        ,  enddate_string
                        ,  returnsmonthlyordaily
                        ,  pctchangeorlogreturn
                    ) 
#            for index, row in df.iterrows():
#                try:
#                    fartomidpricechangedelta = (row['priceDaysBackMid'] - row['priceDaysBackFar']) / row['priceDaysBackFar']

        # --------------------------------
        # Then open the workbook here
        #from win32com.client import Dispatch
        #xlApp = Dispatch("Excel.Application")
        #xlApp.Visible = 1
        #workbook = xlApp.Workbooks.Open(config.myoutputpath+'\\'+inputfilename)
        workbook = xlsxwriter.Workbook(config.myoutputpath+'\\'+inputfilename)
        formatdate = workbook.add_format()
        formatcolumnheader = workbook.add_format()
        
        formatdate.set_num_format('yyyy-mm-dd')  # Format string.
        formatcolumnheader.set_num_format(0x0F)          # Format index.
      
        # --------------------------------
        # Then populate the worksheet here - returns
        worksheet = workbook.add_worksheet()
        worksheet.name = 'pricehistory'
        df = o.EfficientFrontierObject.PriceHistoryDataframe
        #print df
        titlesrow = 3
        titlescolumn = 3
        rowid = 0
        colid = 0
        for cname in df.columns:
            #print 'column',cname
            colid = colid + 1
            worksheet.write(titlesrow,titlescolumn+colid,cname)
            #worksheet.Cells(titlesrow,titlescolumn+colid).Value = cname
            
        for index, row in df.iterrows():
            rowid = rowid + 1
            worksheet.write(titlesrow + rowid,titlescolumn,index,formatdate)
            
            #worksheet.Cells(titlesrow + rowid,titlescolumn).Value = index
            #print 'x'
            colid = 0
            #for cl in row:
            for cname in df.columns:
                colid = colid + 1
                #print rowid,colid,cl
                #print str(df.loc[index][cname]) == str('nan')
                if not str(df.loc[index][cname]) == str('nan'):
                    worksheet.write(titlesrow+rowid,titlescolumn+colid,df.loc[index][cname])
                    #worksheet.Cells(titlesrow+rowid,titlescolumn+colid).Value = df.loc[index][cname]

        # --------------------------------
        # Then populate the worksheet here - returns
        worksheet = workbook.add_worksheet()
        worksheet.name = 'returns'
        df = o.EfficientFrontierObject.ReturnsDataframe
        #print df
        titlesrow = 3
        titlescolumn = 3
        rowid = 0
        colid = 0
        for cname in df.columns:
            #print 'column',cname
            colid = colid + 1
            worksheet.write(titlesrow,titlescolumn+colid,cname)
            #worksheet.Cells(titlesrow,titlescolumn+colid).Value = cname
            
        for index, row in df.iterrows():
            rowid = rowid + 1
            worksheet.write(titlesrow + rowid,titlescolumn,index,formatdate)
            
            #worksheet.Cells(titlesrow + rowid,titlescolumn).Value = index
            #print 'x'
            colid = 0
            #for cl in row:
            for cname in df.columns:
                colid = colid + 1
                #print rowid,colid,cl
                #print str(df.loc[index][cname]) == str('nan')
                if not str(df.loc[index][cname]) == str('nan'):
                    worksheet.write(titlesrow+rowid,titlescolumn+colid,df.loc[index][cname])
                    #worksheet.Cells(titlesrow+rowid,titlescolumn+colid).Value = df.loc[index][cname]

        # --------------------------------
        # Then populate the worksheet here - annualizedreturnseries
        worksheet = workbook.add_worksheet()
        worksheet.name = 'annualizedreturns'
        #print df
        titlesrow = 3
        titlescolumn = 3
        rowid = 0
        colid = 0
        worksheet.write(titlesrow+1,titlescolumn,'annualizedreturns')
        for cname in o.EfficientFrontierObject.ReturnsDataframe:
            #print 'column',cname
            colid = colid + 1
            worksheet.write(titlesrow,titlescolumn+colid,cname)
            annualizedreturnvalue = o.EfficientFrontierObject.AnnualizedReturnsSeries[cname]
            worksheet.write(titlesrow+1,titlescolumn+colid,annualizedreturnvalue)
            #worksheet.Cells(titlesrow,titlescolumn+colid).Value = cname
            
        
        # ---------------------------------------------------
        # Then populate the worksheet here - covariancematrix
        worksheet = workbook.add_worksheet()
        worksheet.name = 'covariancematrix'
        df = o.EfficientFrontierObject.covariancematrix()                    
        
        titlesrow = 3
        titlescolumn = 3
        rowid = 0
        colid = 0
        for cname in df.columns:
            #print 'column',cname
            colid = colid + 1
            worksheet.write(titlesrow,titlescolumn+colid, cname)
            #worksheet.Cells(titlesrow,titlescolumn+colid).Value = cname
            
        for index, row in df.iterrows():
            rowid = rowid + 1
            worksheet.write(titlesrow + rowid,titlescolumn,index)
            #worksheet.Cells(titlesrow + rowid,titlescolumn).Value = index
            #print 'x'
            colid = 0
            for cl in row:
                colid = colid + 1
                #print rowid,colid,cl
                worksheet.write(titlesrow+rowid,titlescolumn+colid,cl)
                #worksheet.Cells(titlesrow+rowid,titlescolumn+colid).Value = cl

        # ----------------------------------------------------
        # Then populate the worksheet here - correlationmatrix
        worksheet = workbook.add_worksheet()
        worksheet.name = 'correlationmatrix'
        df = o.EfficientFrontierObject.correlationmatrix()                    
        
        titlesrow = 3
        titlescolumn = 3
        rowid = 0
        colid = 0
        for cname in df.columns:
            #print 'column',cname
            colid = colid + 1
            worksheet.write(titlesrow,titlescolumn+colid, cname)
            #worksheet.Cells(titlesrow,titlescolumn+colid).Value = cname
            
        for index, row in df.iterrows():
            rowid = rowid + 1
            worksheet.write(titlesrow + rowid,titlescolumn,index)
            #worksheet.Cells(titlesrow + rowid,titlescolumn).Value = index
            #print 'x'
            colid = 0
            for cl in row:
                colid = colid + 1
                #print rowid,colid,cl
                worksheet.write(titlesrow+rowid,titlescolumn+colid,cl)
                #worksheet.Cells(titlesrow+rowid,titlescolumn+colid).Value = cl



        # ----------------------------------------------------
        # Build the drawsail object
        drawsailfilepath = o.drawsail(numberofpermutations , optimalpctasdecimal )

        # ----------------------------------------------------
        # Then populate the worksheet here - PermutationsDataframe
        worksheet = workbook.add_worksheet()
        worksheet.name = 'permutations'
        df = o.PermutationsDataframe                    
        #print df
        
        titlesrow = 3
        titlescolumn = 3
        rowid = 0
        colid = 0
        for cname in df.columns:
            #print 'column',cname
            colid = colid + 1
            worksheet.write(titlesrow,titlescolumn+colid, cname)
            #worksheet.Cells(titlesrow,titlescolumn+colid).Value = cname
            
        for index, row in df.iterrows():
            rowid = rowid + 1
            worksheet.write(titlesrow + rowid,titlescolumn,index)
            #worksheet.Cells(titlesrow + rowid,titlescolumn).Value = index
            #print 'x'
            colid = 0
            for cl in row:
                colid = colid + 1
                #print rowid,colid,cl
                worksheet.write(titlesrow+rowid,titlescolumn+colid,cl)
                #worksheet.Cells(titlesrow+rowid,titlescolumn+colid).Value = cl

        # ----------------------------------------------------
        # Then populate the worksheet here - drawsail
        worksheet = workbook.add_worksheet()
        worksheet.name = 'drawsail'        
        #print '---- drawsail filepath -----'
        #print drawsailfilepath        
        # To set column width
        #worksheet.set_column('B:B', 30)        
        # Insert an image.
        worksheet.insert_image('D4', drawsailfilepath)


        # ----------------------------------------------------
        # Close the workbook and rename it properly
        workbook.close() # see note 1
        #xlApp.Quit()
        #xlApp.Visible = 0 # see note 2
        #del xlApp
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
    #'^RUT','NKE','T','GOOG','WMT','LEO','VTR','FB','BX','DDD','MSFT','IWM','EWZ']
    #'^GSPC','^IWM'   '^OEX','^MID','^RUT','^DJI','^IXIC
    #'FB','AAPL','NFLX','M'
    o = output(list_of_symbols = ['HPQ','MSFT','MU','CSCO']
              , startdatestring = '2012-12-31'
              , enddate_string = '2015-09-30'
              , returnsmonthlyordaily ='daily'
              , pctchangeorlogreturn = 'pctchange'
              , numberofpermutations = 1000
              , optimalpctasdecimal = 0.80
              ) 