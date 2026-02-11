import pandas as pd
import os

# Get the directory where this script lives
script_dir = os.path.dirname(os.path.abspath(__file__))

# Build full path to data.csv in same folder
csv_path = os.path.join(script_dir, "data.csv")


# now read it
df = pd.read_csv(csv_path)

# To be able to print large amounts of data over 50+, we add the to_string function to convert it

# print(df.to_string()) <------



# Let's work with json files as well-------------------------------
import json
json_path = os.path.join(script_dir, "data.json")

# Read the json file as a dictionary first
with open(json_path, 'r') as f:
    data = json.load(f)

# Convert it to a dataframe with a single row
df1 = pd.DataFrame([data])    # Note the [data] wraps in a list



# To read a json file, use the read_json() function

# df1 = pd.read_json(json_path)  (let's leave this for now and just print)

# print(df1) <-------

# OR use pd.Series for a single record (if you only have one object like this)
series = pd.Series(data)

# print(series) <--------