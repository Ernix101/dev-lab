import pandas as pd

# print(pd.__version__)

# Series = A series is a one-dimensional labeled array capable of holding any data type
#          Think of it as a column in a spreadsheet or a SQL table(1-dimensional array)

data = [100, 102, 104, 200, 202]

# series = pd.Series(data, index=["a", "b", "c", "d", "e"])

# series.loc["c"] = 200  --for changing one of the values of the array

# print(series.iloc[2]) -- for accessing a value by integer position
# print(series[series < 200])

calories = {"Day 1": 1750, "Day 2": 2100, "Day 3": 1700}

series = pd.Series(calories)

# series.loc["Day 3"] += 500  addition of values to one of the days
print(series[series < 2000])