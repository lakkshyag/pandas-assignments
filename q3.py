import pandas as pd
import numpy as np
NaN=np.nan

dict={
      'Name':['Amitabh', 'Rekha', 'Shahrukh', 'Salman', 'Priyanka', 'Hema'],
      'Movies':[500, 470, 450, 467, NaN, 340],
      'Serial':[45, 3, NaN, 2, 1, 1],
      'Ads':[13, 10, 15, NaN, NaN, 13]
     }

df=pd.DataFrame(dict)
df=df.loc[df['Movies']>460]
print(len(df))