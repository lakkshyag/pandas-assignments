import pandas as pd
import xlrd 

df=pd.read_excel("C:\Lappie\College\FDS\Assignments\Summer-Olympic-medals-1976-to-2008student.xlsx")
df=df.loc[(df['City']=='Sydney') & (df['Medal']=='Gold')]                                              # filtering for rows which have city as sydney and medal as gold

print(len(df))                                                                                         # finding no. of rows in this dataframe to find number of golds
