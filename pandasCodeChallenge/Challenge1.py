# Use the pandas read_csv() to read the file
# Provide the correct file path to the function
# Column names - MPG, Cylinders, Displacement , Horsepower , Weight , Acceleration , ModelYear, Origin
# Display top 10 rows

import pandas as pd

df = pd.read_csv('./Data/auto_mpg.csv', header=0, names =['MPG', 'Cylinders', 'Displacement' , 'Horsepower' , 'Weight' , 'Acceleration' , 'Model_Year', 'Origin'])
print(df.head(10))
print(df.tail(10))