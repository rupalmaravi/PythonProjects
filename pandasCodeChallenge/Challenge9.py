# extract data and show distribution

import pandas as pd
import matplotlib as mpl

df = pd.read_csv('./Data/landslides.csv')
print(df.info())
print(df['date'])

df['parsed_date'] = pd.to_datetime(df['date'], format='%m/%d/%y') # convert date into datetime format
df['month_of_landslide'] = df['parsed_date'].dt.month # extract month from date time field
#print(df.isna().sum())

df = df[~df['date'].isnull()]
print(df)
