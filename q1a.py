import pandas as pd
import xlrd                              # maybe not necessary ?

df=pd.read_excel("C:\Lappie\College\FDS\Assignments\Summer-Olympic-medals-1976-to-2008student.xlsx")           # reading .xlsx file

df=df.loc[df['City']=='Sydney']                                                                                # filtering data to only show rows where city==sydney
print(df['Medal'].mode())                                                                                      # printing the mode of medal column (medal won the most amount of times)

