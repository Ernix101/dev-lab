import pandas as pd

pokemon_file_path = "C:/web projects/test-site/pandas-intro/Pokemon.csv"

df = pd.read_csv(pokemon_file_path, index_col="Name")    # 'index_col="Name" sets the name to act as the index'


# SELECTION BY COLUMN

# print(df["Name"].to_string())
# print(df["Type1"].to_string())
# print(df["HP"].to_string())
# print(df[["Name", "HP", "Attack"]].to_string())       # To show specific columns, we pass in a python list of the column names


# SELECTION BY ROW/S

# print(df.loc["Charizard"])                            # "df.loc[0]" - Is like an index if you haven't set a label for the index
# print(df.loc["Charizard", ["HP", "Attack"]])                      # We can also set a python list of specific columns we wish to select
# print(df.loc["Charizard" : "Blastoise", ["HP", "Attack"]])                        # We can also specify a range we want back
# print(df.iloc[0:11])                                                # We might also prefer integer-based indexing like this
# print(df.iloc[0:11:2])                                          # If we need by interval of every (second) row
# print(df.iloc[0:11:2, 0:3])                                                 # If we need only the first (3) columns, though form is missing😂


# The Exercise ------------
pokemon = input("Enter a pokemon name: ")

try:
    print(df.loc[pokemon])
except KeyError:
    print(f"{pokemon} was not found!")