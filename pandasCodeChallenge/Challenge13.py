#extract customers who buy online
# extract customer who have more than 5 web purchases

import pandas as pd

df = pd.read_csv('./Data/marketing_campaign.csv')

print(df.info())
print(df.head(5))

print(df['NumWebPurchases'].value_counts())
print(df['NumDealsPurchases'].value_counts())

df_filter_data = df.loc[(df['NumWebPurchases'] > 5) | (df['NumDealsPurchases'] > 5) ]


print(df_filter_data)
