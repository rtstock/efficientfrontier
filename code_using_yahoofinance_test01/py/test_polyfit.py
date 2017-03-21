import matplotlib
matplotlib.use("Agg")

import numpy as np
import pylab as pl

A1=np.loadtxt('/tmp/A1.txt',delimiter=',')
A1_extrema = [min(A1),max(A1)]
A2=np.loadtxt('/tmp/A2.txt',delimiter=',')

pl.close()
ab = np.polyfit(A1,A2,1)
print ab
fit = np.poly1d(ab)
print fit
r2 = np.corrcoef(A1,A2)[0,1]
print r2
pl.plot(A1,A2,'r.', label='TMP36 vs. DS18B20', alpha=0.7)
pl.plot(A1_extrema,fit(A1_extrema),'c-')
pl.annotate('{0}'.format(r2) , xy=(min(A1)+0.5,fit(min(A1))), size=6, color='r' )

pl.title('Sensor correlations')
pl.xlabel("T(x) [degC]")
pl.ylabel("T(y) [degC]")
pl.grid(True)
pl.legend(loc='upper left', prop={'size':8})
import config

pl.savefig(config.mycachefolder + '//C123.png')
