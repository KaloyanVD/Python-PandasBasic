import pandas as pd
import re
# https: // youtu.be/vmEHCJofslg?t = 2529

df = pd.read_csv('pokomen_data.csv')

# filter based on multiple conditions
new_df = df.loc[(df['Type 1'] == 'Grass') & (
    df['Type 2'] == 'Poison') & (df['HP'] > 15)]


# if we don't do it the indexes remain the same as they were before the conditions
new_df = new_df.reset_index(drop=True, inplace=True)


# removes all names that contains 'Mega'
df.loc[~df['Name'].str.contains('Mega')]

# filter based on regex (grass=re.I) ignores if the words are capital or not
df.loc[df['Type 1'].str.contains('fire|grass', grass=re.I, regex=True)]
