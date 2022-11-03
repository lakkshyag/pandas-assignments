import pandas as pd
import xlrd

df=pd.read_excel("C:\Lappie\College\FDS\Assignments\Height-and-Weight.xlsx")

dfW=df.loc[df['Gender']=='W']                                                                       # creating another dataframe dfW which only has the rows from df with value of gender as 'W'

print(dfW['Height(cm)'].mean())                                                                     # printing means of the Weight and Height columns
print(dfW['Weight(kg)'].mean())