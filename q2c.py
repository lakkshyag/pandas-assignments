import pandas as pd
dict={
        'English':[85,73,98], 
        'Math':[60,80,58], 
        'Science':[90,60,74], 
        'French': [95,87,92] 
     }

df=pd.DataFrame(dict, index=[2018, 2019, 2020])

df.loc[2022, :] = [89,21,87,59]                                         #added the row containing marks for 2022

print(df)