# find avg amount of products purchased by each martial status group
# study group of customers based on purchase

import pandas as pd

df = pd.read_csv('./Data/marketing_campaign.csv')

print(df.describe())

print(df['Marital_Status'].value_counts())

amt_brought = [
    'MntWines',
    'MntFruits',
    'MntMeatProducts',
    'MntFishProducts',
    'MntSweetProducts',
    'MntGoldProds'
]

print(df.groupby(['Marital_Status']).mean()[amt_brought])