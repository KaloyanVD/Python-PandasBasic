import pandas as pd

df = pd.read_csv('pokemon_data.csv')

df['Total'] = df['HP'] + df['Attack'] + df['Defense'] + \
    df['Sp. Atk'] + df['Sp. Def'] + df['Speed']

# it saves the modified file as csv / index=False won't save the index numbers in the file
df.to_csv('modified.csv', index=False)


df.to_excel('modified.xlsx')  # saving to excel

df.to_csv('modified.txt', index=False, sep='\t')
