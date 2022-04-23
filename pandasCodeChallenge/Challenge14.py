# extract customers with advanced degree
# income is greater than 65,000
# no children living at home

import pandas as pd

df = pd.read_csv('./Data/marketing_campaign.csv')

print(df.head(5))
print(df.columns)
print(df['Kidhome'].value_counts())

df_filter_data = df.loc[(df['Education'].isin(['Graduation','PhD','Master'])) & (df['Income'] > 65000) & (df['Kidhome'] ==0)]
print(df_filter_data)