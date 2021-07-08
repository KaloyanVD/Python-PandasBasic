import pandas as pd

df = pd.read_csv('pokemon_data.csv')

print(df.describe())  # gives statistics about the data

df.sort_values('Name', ascending=False)

# df.sort_values(['Type 1', 'HP'], ascending=[1, 0]) sorts first column by ascending and the second descending
