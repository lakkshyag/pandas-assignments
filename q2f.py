import pandas as pd

dict={
      'Radius(cm)':[1.0, 1.5, 2.5, 4.0, 6.0],                                                    
      'Color':['Red', 'Blue', 'Orange', 'Green', 'Red'],
      'Area(cmsq)':[3.140, 7.065, 19.625, 50.240, 113.040],
     }

df=pd.DataFrame(dict, index=['Circle 1', 'Circle 2', 'Circle 3', 'Circle 4', 'Circle 5'])

areaMax=df['Area(cmsq)'].max()
df=df.drop(df[df['Area(cmsq)']==areaMax].index)                                                                 # removing the row which fulfills the condition of area being the maximum
print(df)
