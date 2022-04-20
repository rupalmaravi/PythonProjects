# filter the data to get affected rows
# show alternate records from index 50 to 300
# show above data only for last 9 columns

import pandas as pd

df = pd.read_csv('./Data/marketing_campaign.csv')

print(df.head(5))

print(df.iloc[50:300:2, -9:])
