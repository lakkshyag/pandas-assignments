import pandas as pd
dict={
        'English':[85,73,98], 
        'Math':[60,80,58], 
        'Science':[90,60,74], 
        'French': [95,87,92] 
     }

df=pd.DataFrame(dict, index=[2018, 2019, 2020])                                   # making a dataframe df from the given question values, using the listed dictionary dict
print(df)
print('\n')

print('Modifying a single value:')
df.loc[2020, 'French']=29                                                           # changing the value of 2020 index French column to 29 using loc
print(df)   
