# extract customers not married , not together and oborn after 1990 ; Chained condition

import  pandas as pd

df = pd.read_csv('./Data/marketing_campaign.csv')

print(df.info())
print(df['Marital_Status'].value_counts())
print(df['Year_Birth'].value_counts())

df_filter_data = df.loc[(~df['Marital_Status'].isin(['Married','Together'])) & (df['Year_Birth'] > 1990) ]

print(df_filter_data)