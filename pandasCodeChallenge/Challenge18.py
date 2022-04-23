# Calculate yearly stock return of four organization
# read stock file
# from the time series data calculate daily return followed by yearly return after extracting year from data

import pandas as pd

df = pd.read_csv('./Data/stock_data.csv', index_col='Unnamed: 0',parse_dates=True)
print(df.head(5))
print(df.columns)

daily_returns = df.pct_change().dropna()
print(daily_returns)

get_year = lambda x: x.year

by_year_stock = daily_returns.groupby(get_year).sum()*100
print(by_year_stock)