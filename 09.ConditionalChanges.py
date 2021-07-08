import pandas as pd


df = pd.read_csv('pokemon_data.csv')

# changes all type 1 fire to Flamer
df.loc[df['Type 1'] == 'Fire', 'Type 1'] = 'Flamer'

# if it's true it will set the generation and legendary column to test value
df.loc[df['Total'] > 500, ['Generation', 'Legendary']] = 'TEST VALUE'
