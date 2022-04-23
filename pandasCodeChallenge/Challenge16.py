# extract income of customer group
# find median income of customer by education and martial status

import pandas as pd

df = pd.read_csv('./Data/marketing_campaign.csv')

print(df.columns)

median_income = df.groupby(['Education', 'Marital_Status'])['Income'].agg(['median', 'mean'])
print(median_income)
