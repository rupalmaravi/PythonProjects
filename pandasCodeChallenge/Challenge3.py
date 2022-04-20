# Display quantitative summary stats for all numerical and categorical columns
# Display and Visualize the data distribution of different classes of the categorical values

import pandas as pd

df = pd.read_csv('./Data/auto_mpg.csv', header=0,
                 names=['MPG', 'Cylinders', 'Displacement', 'Horsepower', 'Weight', 'Acceleration', 'Model_Year',
                        'Origin'])

print(df.describe())

print(df.describe(include="object"))

print(df["Origin"].value_counts().plot(kind="bar"))
