# use labels to extract or subset data
# set index as a column from file
# extract records from certain location from the file and select columns with "mnt" name

import pandas as pd

df = pd.read_csv('./Data/marketing_campaign.csv')
print(df.head(10))
df_new = df.set_index('ID')
print(df_new.loc[7446:2114,'MntWines':'MntGoldProds'])
#print(df.info())