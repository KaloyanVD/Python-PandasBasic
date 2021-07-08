import pandas as pd

df = pd.read_csv('pokemon_data.csv')

# reading headers
print(df.columns)

# reading each column
# we must use double [] if we are printing several columns names
print(df[['Name', 'Type 1', 'HP']][0:5])

# print(df.Name) this doesn't work if the column name is 2 seperate words

# read each row
print(df.iloc[1:4])


# read a specific location
print(df.iloc[2, 1])
