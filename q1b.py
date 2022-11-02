import pandas as pd
dict={
        'English':[85,73,98], 
        'Math':[60,80,58], 
        'Science':[90,60,74], 
        'French': [95,87,92] 
     }

df=pd.DataFrame(dict, index=[2018, 2019, 2020])
df.loc[2020, 'French']=29

meanEnglish=df['English'].mean()                                                            # using .mean() to find the means of the values in mentioned columns
meanScience=df['Science'].mean()

print(f"Mean of English marks: {meanEnglish}")
print(f"Mean of Science marks: {meanScience}")