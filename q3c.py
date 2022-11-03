import pandas as pd

dict1={
       'mark1':[10, 40, 15, 40],
       'mark2':[15, 45, 30, 70],
      }

dict2={
       'mark1':[30, 20, 20, 50],
       'mark2':[20, 25, 30, 30]
      }

df1=pd.DataFrame(dict1)
df2=pd.DataFrame(dict2)

print(df1.subtract(df2))