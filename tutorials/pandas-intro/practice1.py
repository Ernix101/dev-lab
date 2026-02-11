import pandas as pd
import janitor            # <---we don't need this yet

patients = {
    "patient_id": ["P01", "P02", "P03", "P04", "P05", "P06", "P07", "P01", "P09", "P10", "P11", "P12"],
    "age": [12, 4, 30, 20, 67, 28, 50, 40, 44, 37, 70, 10],
    "gender": ["M", "F", "F", "M", "F", "M", "F", "M", "F", "M", "M", "F"],
    "facility": ["FAC02", "FacC03", "FAC08", "FAc05", "FAC02", "FaC05", "FAC03", "fac08", "FAC02", "FAC05", "FAC03", "FAC08"],
    "visit_type": ["Inpatient", "Outpatient", "Observation", "Outpatient", "Inpatient", "Observation", "Outpatient", "Observation", "Inpatient", "Outpatient", "Inpatient", "Observation"],
    "bill amount": [2500, 3200, 5000, 4000, 2500, 3500, 4500, 3000, 2200, 3500, 1500, 2500],
    "has insurance": [True, True, False, True, False, True, False, False, True, False, True, False],
}

df = pd.DataFrame(patients)

# print(df.iloc[0:5])               # ✅ First 5 rows
# last_rows = df.iloc[-3]
# print(df.iloc[-3:])                  # ✅ last 3 rows
df_shape = df.shape

# print(f"Dataframe shape:  {df_shape}")      # ✅ data frame's shape
# print(df.dtypes)                                   # ✅ column and rows data type
# print(df.age.dtypes)                              # ✅ column data type      (for age in this case)

# numeric_stats = df.describe()
# print(numeric_stats)                       # Summary statistics for numeric columns


# df = df.clean_names()                       # Standardized to snake_case  (using pyjanitor)
# df_head = df.head()                          # Shows first 6 rows
# df_tail = df.tail()                           # Shows last 6 rows
# df_col = df.columns                           # Gives you a python list of column names
# df_info = df.info()                           # Gives a description of your dataframe


# df.rename(columns={
#     "facility": "FAC",
#     "visit_type": "Type_Of_Visit"                 # Renaming columns
# }, inplace=True)


df = df[['patient_id', 'age', 'gender', 'facility', 'visit_type', 'has insurance' ,'bill amount']]   # Re-ordering columns

# print(df[["age", "facility", "bill amount"]].to_string)
# print(df["age"].to_string)
# print(df["facility"].to_string)
# print(df["bill amount"].to_string)


# # older_than_40 = df['age'] > 40
# older_and_insurance = df[(df[['age'] > 40]) & 
#                         (df['has insurance'] == True)]
older_and_insurance_and_billAboveAverage = df[
                                            (df['age'] > 30) &
                                            (df['has insurance'] == True) &
                                            (df['bill amount'] > 3000)
]

print(older_and_insurance_and_billAboveAverage)
