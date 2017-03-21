# -*- coding: utf-8 -*-
"""
Created on Wed Jul 29 17:31:47 2015

@author: justin.malinchak
"""

# -*- coding: utf-8 -*-
"""
Created on Wed Jul 29 17:18:11 2015

@author: justin.malinchak
"""

class output:

    def set_PermutationsDataframe(self,PermutationsDataframe):
        self._PermutationsDataframe = PermutationsDataframe
    def get_PermutationsDataframe(self):
        return self._PermutationsDataframe
    PermutationsDataframe = property(get_PermutationsDataframe, set_PermutationsDataframe)

    def set_EfficientFrontierObject(self,EfficientFrontierObject):
        self._EfficientFrontierObject = EfficientFrontierObject
    def get_EfficientFrontierObject(self):
        return self._EfficientFrontierObject
    EfficientFrontierObject = property(get_EfficientFrontierObject, set_EfficientFrontierObject)

    def myfunc(self,x, pos=0): 
        return '%1.1f%%'%(100*x)
  
    
    def __init__(self,
                     list_of_symbols 
                     ,  startdate_string = '2005-01-01'
                     ,  bottomconstraint = 0
                     ,  topconstraint = 100
                     #,  iterations = 10
                     ):
                         
        self._setup(list_of_symbols 
                     ,  startdate_string
                     ,  bottomconstraint 
                     ,  topconstraint 
                     #,  iterations
                     )

    def _setup(self,list_of_symbols 
                     ,  startdate_string
                     ,  bottomconstraint 
                     ,  topconstraint 
                     ):
        
        import efficientfrontier as ef   
        
        o = ef.perform(list_of_symbols,startdate_string,bottomconstraint,topconstraint) # '^GSPC','^OEX','^MID','^RUT','^DJI'
        
        self.EfficientFrontierObject = o
        
    def permutationstodataframe(self,iterations):
        import pandas as pd
        df_permutations = self.EfficientFrontierObject.permutationstodataframe(iterations)
        mydf = pd.DataFrame(columns=('portfolioreturn', 'portfoliostandarddeviation','weightstring'))
        
        #Do map here to make quicker
        for index, row in df_permutations.iterrows():
            randomweightseries = row['value']['randomweightseries']
            weightstring = ''
            for idx in randomweightseries.iteritems():
                weightstring = weightstring + str(idx[0])+'='+ str(idx[1]*100)+'% '
            weightstring = weightstring[:-1]
            portfolioreturn = row['value']['portfolioreturn']
            portfoliostandarddeviation = row['value']['portfoliostandarddeviation'] 
            mydf.loc[index] = [portfolioreturn,portfoliostandarddeviation,weightstring]
        return mydf

    def drawsail(self,numberofpermutations,optimalpctasdecimal = 0.90):
        df = o.permutationstodataframe(numberofpermutations)
        df['returnoverrisk'] = df.portfolioreturn / df.portfoliostandarddeviation
        maxreturnoverriskseries = df.ix[df['returnoverrisk'].idxmax()]
        df['maxreturnoverrisk'] = maxreturnoverriskseries['returnoverrisk']
        print 'the max returnoverrisk is:',maxreturnoverriskseries['returnoverrisk']
        #df.apply(lambda row: min([row['A'], row['B']])-row['C'], axis=1)
        #df.plot(title='Title Here')
        import matplotlib.pylab as plt
        #import numpy as np
        #import pandas as pd
        #import numpy as np
        #df = pd.DataFrame(np.random.randn(10,2), columns=['col1','col2'])
        #df['col3'] = np.arange(len(df))**2 * 100 + 100
        #print df
        #plt.scatter(df.col1, df.col2, s=df.col3)
        #colors = np.where(df.col3 > 300, 'r', 'k')

        #fig = plt.figure()
        fig = plt.figure(figsize=(12.0, 9.0)) # in inches!
        
        cond = df.returnoverrisk > df.maxreturnoverrisk * optimalpctasdecimal
        subset_a = df[cond].dropna()
        subset_b = df[~cond].dropna()
        plt.scatter(subset_a.portfoliostandarddeviation, subset_a.portfolioreturn, s=7, c='red', label='frontier >' + str(int(optimalpctasdecimal*100))+'%',marker='s', edgecolors='none')
        plt.scatter(subset_b.portfoliostandarddeviation, subset_b.portfolioreturn, s=7, c='dodgerblue', label='suboptimal',marker='s', edgecolors='none') 
        
        from matplotlib.ticker import FuncFormatter 
        ax = plt.subplot(111)
        ax.xaxis.set_major_formatter(FuncFormatter(self.myfunc)) 
        ax.yaxis.set_major_formatter(FuncFormatter(self.myfunc)) 
        
        plt.legend(fontsize=12)    
        fig.suptitle('Optimal Weights  (Inception ' + self.EfficientFrontierObject.StartDateString +')' +
            chr(10) + 
            maxreturnoverriskseries['weightstring'] + 
            chr(10) +
            'N=' + str(numberofpermutations) + '   '
            'Annualized Return=' + str(round(maxreturnoverriskseries['portfolioreturn']*100,2)) + '%   ' +
            'StDev=' + str(round(maxreturnoverriskseries['portfoliostandarddeviation']*100,2)) + '%', fontsize=12)
        plt.xlabel('Risk (StDev)', fontsize=12)
        plt.ylabel('Return (%)', fontsize=12)
        fig.savefig('date16.jpg')

        # To get a list of colors        
#        import matplotlib        
#        for name, hex in matplotlib.colors.cnames.iteritems():
#            print(name, hex)

        

if __name__=='__main__':
    o = output(['MCD','AAPL'],'2005-12-31') 
    # 'WMT','NKE','T','MCD','JPM','^RUT','XOM','MSFT','YHOO','QQQ','HD','GS','BAC','LEO'
    # '^GSPC','^OEX','^MID','^RUT','^DJI','^IXIC','^GSPC','^DJI','^OEX','^RUT'
    #'WMT','NKE','T','MCD','JPM','^RUT'
    #'^GSPC','^OEX','^MID','^RUT','^DJI'
    print o.EfficientFrontierObject.CorrelationMatrix
    print o.EfficientFrontierObject.MonthlyReturnsDataframe
    print o.EfficientFrontierObject.portfolioriskreturnrandomweight
    o.drawsail(2000,0.90)
