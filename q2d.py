import pandas as pd                                                                              # adding a column for perimeter

dict={
      'Radius(cm)':[1.0, 1.5, 2.5, 4.0, 6.0],                                                    # created a listed dictionary with valeus from the question
      'Color':['Red', 'Blue', 'Orange', 'Green', 'Red'],
      'Area(cmsq)':[3.140, 7.065, 19.625, 50.240, 113.040],
     }

df=pd.DataFrame(dict, index=['Circle 1', 'Circle 2', 'Circle 3', 'Circle 4', 'Circle 5'])
df['Perimeter(cm)']=[6, 8, 12 , 15, 20]                                                          # added a column Perimeter(cm) with some bogus values
print(df)