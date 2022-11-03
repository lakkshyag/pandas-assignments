import pandas as pd

dict1={
       'mark1':[10, 40, 15, 40],
       'mark2':[15, 45, 30, 70],
      }

df1=pd.DataFrame(dict1, index=['zero', 'one', 'two', 'three'])
print(df1)