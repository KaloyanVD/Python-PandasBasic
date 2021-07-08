import pandas as pd

df = pd.read_csv('pokemon_data.csv')

# adding a new column first way
df['Total'] = df['HP'] + df['Attack'] + df['Defense'] + \
    df['Sp. Atk'] + df['Sp. Def'] + df['Speed']  #

print(df.head(5))

# adding a new column second way
# df['Total'] = df.iloc[:, 4:10].sum(axis=1)

# delete column
df = df.drop(columns=['Total'])

# rearranging columns
cols = list(df.columns.values)

df = df[cols[0:4] + [cols[-1]] + cols[4:12]]
