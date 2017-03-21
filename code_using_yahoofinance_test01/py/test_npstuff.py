import pandas as pd
import numpy as np

np.random.seed(0)
df = pd.DataFrame(np.random.randn(100,5), columns=list('ABCDE'))
df[df < 0] = np.nan
print df
print df.corr()
