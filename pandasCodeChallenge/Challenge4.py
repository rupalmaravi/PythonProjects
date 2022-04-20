# create new variable using existing variable
# displacement per unit power (displacement/horsepower)
# Weight per cylinder (weight/cylinder)
# acceleration per unit power (acceleration/horse power)

import pandas as pd

df = pd.read_csv('./Data/auto_mpg.csv', header=0,
                 names=['MPG', 'Cylinders', 'Displacement', 'Horsepower', 'Weight', 'Acceleration', 'Model_Year',
                        'Origin'])
df['dis_per_unit'] = df['Displacement'] / df['Horsepower']
df['weight_per_cylinder'] = df['Weight'] / df['Cylinders']
df['acc_per_unit'] = df['Acceleration'] / df['Horsepower']
print(df.head(10))
print(df.columns)
