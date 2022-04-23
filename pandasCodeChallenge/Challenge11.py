# extract customers who are married

import pandas as pd

df = pd.read_csv('./Data/marketing_campaign.csv')

print(df.info())

print(df['Marital_Status'].value_counts())

df_filter = df.loc[(df['Marital_Status']) == 'Married']
print(df_filter)

