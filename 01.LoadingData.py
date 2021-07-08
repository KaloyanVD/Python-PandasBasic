import pandas as pd

df = pd.read_csv('pokemon_data.csv')

df_xls = pd.read_excel('pokemon_data.xlsx')

# delimiter is necessary otherwise it will print \ instead of spaces
df_txt = pd.read_csv('pokemon_data.txt', delimiter='\t')

print(df)  # prints all the data

print(df.head(5))  # prints the top 5 rows

print(df.tail(5))  # prints the bottom 5 rows
