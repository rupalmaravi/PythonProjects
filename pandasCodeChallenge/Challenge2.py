# Number of records and columns
# Name of the columns
# Index Columns
# Data Type of Each column

import pandas as pd

df = pd.read_csv('./Data/auto_mpg.csv', header=0,
                 names=['MPG', 'Cylinders', 'Displacement', 'Horsepower', 'Weight', 'Acceleration', 'Model_Year',
                       'Origin'])

print(df.shape)
print(df.columns)
print(df.index)
print(df.info())
