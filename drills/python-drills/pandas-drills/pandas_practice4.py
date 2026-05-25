import csv
import pandas as pd
import numpy as np

# Data loading test


favorite_foods = {
    "protein": ['beef', 'fish', 'potato'],
    "carbs": ['cereal', 'pancakes', 'rice'],
    "veggies": ['lettuce', '', 'tomatoes'],
    "fruits": ['apple', 'orange', 'banana'],
    "calories": [1000, 2000, 2500]
}

foods_df = pd.DataFrame(favorite_foods)

# print(foods_df['protein'].dtype)
# print(foods_df['calories'].dtype)
# print(foods_df.describe())



ufo_path = r"C:\Users\ERNEST\Downloads\archive\scrubbed.csv"

df = pd.read_csv(ufo_path)


# Selection and filtering!

df['duration(seconds)'] = pd.to_numeric(df['duration(seconds)'], errors='coerce')

# first_secs = df['duration(seconds)'].head(5)
# their_mean = first_secs.mean()
# print(float(their_mean))

mean_secs = df['duration(seconds)'].mean()
above_mean = df[df['duration(seconds)'] > mean_secs]

# print(f"Mean: {mean_secs:.2f}")
# print(above_mean[['city', 'state', 'shape', 'duration(seconds)']])

# print(df.loc[10:25, ['city', 'shape']])
# print(df.iloc[-5:, :3])        # last 5 rows and first 3 columns

median_time_secs = df['duration(seconds)'].median(numeric_only=True)
df.fillna({'duration(seconds)': f'{median_time_secs}'})

# print(df[['datetime', 'city', 'duration(seconds)']])

df = df.rename(columns={
    'duration(seconds)': 'seconds',
})

# print(df['seconds'])
df['seconds'] = df['seconds'].astype(float)
# print(df['seconds'].dtypes)

df = df.drop_duplicates()
df = df.fillna({'seconds': 'None'})
# print(df['seconds'])

df['latitude'] = pd.to_numeric(df['latitude'], errors='coerce')
df['multiplied_location'] = df['latitude'] * df['longitude']
# print(df['multiplied_location'])

# print(f"{df['longitude'].dtype} is for longitude and {df['latitude'].dtype} is for latitude")

df['seconds'] = pd.to_numeric(df['seconds'], errors='coerce')
# print(df['seconds'].dtype)
def time_seen(time):
    if time >= 4000:
        return "Very Long"
    elif time <= 4000 >= 2000:
        return "Long"
    else:
        return "Short time"
    
df['How_long'] = df['seconds'].apply(time_seen)
# print(df['How_long'])

max_of_seconds = df.groupby('shape')['seconds'].max()
count_of_seconds = df.groupby('shape')['seconds'].count()
# print(mean_of_seconds.sort_values(ascending=False))
# print()
# print(max_of_seconds)
# print()
# print(count_of_seconds)
df1 = pd.DataFrame({
    'city': ['Nairobi', 'Mombasa', 'Kisumu'],
    'cases':[200, 150, 80]
})

df2 = pd.DataFrame({
    'city': ['Nairobi', 'Mombasa', 'Eldoret'],
    'population': [4000000, 1200000, 500000]
})

inner = pd.merge(df1, df2, on='city')     # Only matching cities
left = pd.merge(df1, df2, on='city', how='left')   # All of df1, match where possible

df['date posted'] = pd.to_datetime(df['date posted'])
df = df.set_index('date posted')

monthly = df['seconds'].resample('ME').sum()
print(monthly)
