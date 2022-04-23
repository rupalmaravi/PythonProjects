# check the data and handle missing values
# identify columns with missing values
# determine total number of missing values
# treat missing values (Drop rows , fill with a value)

import pandas as pd

df = pd.read_csv('./Data/landslides.csv')
print(df.columns)

# filter
print(df.isna().sum())

df = df[~df['date'].isnull()]
print(df)
print(df.isna().sum())

# fill with value

print(df['time'].isna().sum())

df['time'] = df['time'].fillna("Not known")

print(df['time'].isna().sum())

# replace value
mean = df['fatalities'].mean()

print(mean)

df['fatalities'] = df['fatalities'].fillna(mean)

print(df['fatalities'].isna().sum())

print(df)

#group by counts

print(df['time'].value_counts())