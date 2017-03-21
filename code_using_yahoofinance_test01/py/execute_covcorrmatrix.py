# -*- coding: utf-8 -*-
"""
Created on Tue Jul 28 16:16:39 2015

@author: justin.malinchak
"""
#import numpy as np
#x = np.array([[5, 300, 0],
#       [3, 0, 5],
#       [5, 500, 0],
#       [1, 100, 7]])
#
#print np.cov(x)


#import pandas as pd
#import numpy as np
#x = np.array([[0, 2], [1, 1], [2, 0]]).T
#print np.cov(x)

#import pandas as pd

#'^GSmr   ^OEX    ^VIX    ^OEX    ^MID   ^RUT   ^DJI

import numpy as np
import pandas as pd
import pullreturns as pr
dict_of_dfs = {}

mysymbolslist = ['^GSPC','^DJI','^MID','^OEX','AAPL','LEO']

for symbol in mysymbolslist:
    df = pr.monthlyreturnsusingyahoosymbol(symbol,'2005-01-01')
    dict_of_dfs[symbol] = df

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


passed = 0
for k,v in dict_of_dfs.items():
    if passed == 0:        
        df_align = v[['b_monthend','e_pctchange']]
        df_align = df_align.set_index('b_monthend')
        df_align.columns = [k]
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
    passed = 1
print '----------------------------------------------------'
print '                 monthly returns'
print '----------------------------------------------------'

df_align = df_align.dropna()
print df_align

covmatrix_array = np.cov(df_align,None,0)
#good np.savetxt("cov.csv", covmatrix_array, delimiter=",", fmt='%s')

rows = np.array(list(df_align))[: np.newaxis]
str_data = np.char.mod("%10.6f", df_align)

#print str_data
#print rows
#print list(df_align)


df_cov = pd.DataFrame(covmatrix_array, index=rows, columns=list(df_align))
print '----------------------------------------------------'
print '                 covariance matrix'
print '----------------------------------------------------'
print df_cov
df_cov.to_csv('cov1.csv',columns=(list(df_align)))

#print df_align
#print np.hsplit(df_align, 4)[3]
#x1 = np.hsplit(df_align, 4)
#df_align_values = df_align.values.view()
#records_align = df_align.to_records()[2][1]#.view([('^GSPC', '<f8')])

#ls = df_align['^GSPC'].tolist(),df_align['^VIX'].tolist()
#ls = [list(x) for x in df_align.T.itertuples()]
#print ls
#print df_align['^GSPC'].tolist()

corrmatrix_array = np.corrcoef(df_align.T.values.tolist())
#print corrmatrix_array

df_corr = pd.DataFrame(corrmatrix_array, index=rows, columns=list(df_align))
print '----------------------------------------------------'
print '                 correlation matrix'
print '----------------------------------------------------'

print df_corr
df_corr.to_csv('corr1.csv',columns=(list(df_align)))
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
