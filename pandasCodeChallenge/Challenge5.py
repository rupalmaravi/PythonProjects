# select specific columns from file 

import pandas as pd

df = pd.read_csv('./Data/marketing_campaign.csv')
df_selected_cols = df[['MntWines','MntFruits','MntMeatProducts','MntFishProducts','MntSweetProducts','MntGoldProds']]
print(df.head(10))
print(df.columns)
print(df_selected_cols)