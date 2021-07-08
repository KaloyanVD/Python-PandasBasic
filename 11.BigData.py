import pandas as pd

# shrinking the data size so we can fit big amounts of data
for df in pd.read_csv('pokemon.csv', chunk_size=5):
    print('CHUNK DF')
    print(df)

new_df = pd.DataFrame(columns=df.columns)

new_df = pd.concat([new_df])
