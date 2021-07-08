import pandas as pd

df = pd.read_csv('pokemon_data.csv')

# prints the median of the columns of all type 1 pokemons and sort them by defense descending
print(df.groupby('Type 1').mean().sort_values('Defense', ascending=False))


# sums the values of type 1 pokemons
df.groupby('Type 1').sum()

# counts the different type of pokemons type 1
df.groupby('Type 1').count()


# count several different types of pokemons
df.groupby(['Type 1', 'Type 2']).count()['count']
