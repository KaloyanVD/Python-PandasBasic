import pandas as pd

df = pd.read_csv('pokemon_data.csv')

for index, row in df.iterrows():
    print(index, row['Name'])
