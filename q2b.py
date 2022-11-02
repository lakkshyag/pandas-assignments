import pandas as pd
dict={
        'English':[85,73,98], 
        'Math':[60,80,58], 
        'Science':[90,60,74], 
        'French': [95,87,92] 
     }

df=pd.DataFrame(dict, index=[2018, 2019, 2020])
df['Economics']=[99, 99, 99]

df.loc[2019, 'Economics']=54                                                               # modifying marks in the econoics column for indices 2019 and 2020
df.loc[2020, 'Economics']=45

print(df)