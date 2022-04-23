# find top purchaser among customer group
# display top five online purchaser from each group based on their education level

import pandas as pd
df = pd.read_csv('./Data/marketing_campaign.csv')

def top(df, n=5, column='NumWebPurchases'):
    return df.sort_values(by=column)[-n:]
purchases =[
    'NumDealsPurchases',
    'NumWebPurchases',
    'NumCatalogPurchases',
    'NumStorePurchases'
]

df_req_vlaue = df.groupby(['Education']).apply(top)[purchases]
print(df_req_vlaue)

