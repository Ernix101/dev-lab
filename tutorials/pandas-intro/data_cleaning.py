import pandas as pd

pokemon_file_path = "C:/dev-lab/tutorials/pandas-intro/pokemon-2.csv"

# Data Cleaning = The process of fixing/removing:
#                   incomplete, incorrect, or irrelevant data.
#                   75% of work done with Pandas is data cleaning.

df = pd.read_csv(pokemon_file_path)

# 1.    Drop irrelevant columns
# df = df.drop(columns=["Legendary"])         # Removes the Legendary column entirely
# df = df.drop(columns=["Legendary", "#"])             # What if we wanted to drop the #/Number column together with legendary

# 2.    Handle Missing data
# df = df.dropna(subset=["Type 2"])              # Drops any rows with no value ie: NaN
# df = df.fillna({"Type 2": "None"})                  # Fills any NaN rows with None

# 3.   Fix inconsistent values
# df["Type 1"] = df["Type 1"].replace({"Grass": "GRASS"})   # Replaces instance of Grass with GRASS for Type 1 pokemon
# df["Type 1"] = df["Type 1"].replace({"Grass": "GRASS",
#                                      "Fire": "FIRE",
#                                      "Water": "WATER"})     # Replaces multiple Instances

# 4.   Standardize Text
# df["Name"] = df["Name"].str.lower()                     # Makes all names lowercase. You can also make it .title() for any health data in future

# 5.    Fix data types
# df["Legendary"] = df["Legendary"].astype(bool)          # Makes the column with 1 or 0 to a boolean of True or False

# 6.    Remove Duplicates
# df = df.drop_duplicates()



print(df.to_string())