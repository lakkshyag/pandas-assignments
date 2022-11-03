import pandas as pd
import xlrd

df=pd.read_excel("C:\Lappie\College\FDS\Assignments\Height-and-Weight.xlsx")

dfW=df.loc[(df['Gender']=='W') & (df['Country/Team']=='Algeria')]
print(dfW)
print(dfW['Height(cm)'].mean())