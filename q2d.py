import pandas as pd
dict={
        'English':[85,73,98], 
        'Math':[60,80,58], 
        'Science':[90,60,74], 
        'French': [95,87,92] 
     }

df=pd.DataFrame(dict, index=[2018, 2019, 2020])

df.loc[2022, :] = [89,21,87,59]
df.drop(index=2018, inplace=True)                                                       #removed the 2018 row
print(df)