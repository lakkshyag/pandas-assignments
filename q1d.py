import pandas as pd
import xlrd 

df=pd.read_excel("C:\Lappie\College\FDS\Assignments\Summer-Olympic-medals-1976-to-2008student.xlsx")
df=df.loc[(df['City']=='Sydney')]

print(len(df))