# format a column into categorical values for consistency

def format_time(x):
    if ':' in str(x):
        if int(x.split(':')[0]) >= 12 and int(x.split(':')[0]) <= 18:
            x = 'Afternoon'
        elif int(x.split(':')[0]) < 12:
            x = 'Morning'
        elif int(x.split(':')[0]) > 18:
            x = 'Night'
    elif 'evening' in str(x).lower():
        x = 'Evening'
    elif 'early morning' in str(x).lower() or 'late morning' in str(x).lower():
        x = 'Morning'
    elif 'overnight' in str(x).lower():
        x = 'Night'
    else:
        x = 'Not Known'
    return x


import pandas as pd

df = pd.read_csv('./Data/landslides.csv')

# print(df.info())
# print(df['time'].value_counts())


df['time'] = df['time'].apply(format_time)
print(df['time'].value_counts())
