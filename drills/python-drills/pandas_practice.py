import pandas as pd
import numpy as np

df = pd.read_csv('C:/dev-lab/drills/python-drills/titanic.csv')

# print(df.head(8))
# print(df.tail(8))
# print(df.info())
# print(df.shape)
# print(df.columns)

new_df = df[["Name", "Sex", "Age", "Survived"]]             # Selected columns of these characteristics

# print(new_df)

# print(df.loc[4])                # passenger 5, Henry did not survive😟

# print(df.iloc[10:16, 2:6])


# print(df[df["Survived"] == 1].shape[0])         # How many survived add shape[0]     343
# print(df[(df["Survived"] == 1) & (df["Sex"] == "female")].shape[0])         # How many females survived add shape[0]  233 survived



# print(df[(df["Pclass"] == 1) & (df["Fare"] > 100)])         # Nothing like high class🍷

# print(df[(df["Age"] < 18) | (df["Age"] > 60)])              # The vulnerable type ages

# print(df.groupby('Sex')['Age'].mean())                          # Group by both age and sex and find average M=30.7, F=27.9

# print(df.groupby('Pclass')['Survived'].mean())                  # Average of survivors in classes; 1= 0.62, 2= 0.47, 3=0.24


# print(df.groupby('Embarked')['Fare'].mean())                    # Average fare paid per class

# print(df.groupby('Sex')['Survived'].value_counts())                 # Value counts for each of non-survived or survived per male and female


# Add a new column of familysize that adds on the existing columns
df["FamilySize"] = df['SibSp'] + df['Parch'] + 1

 


# print(df[['SibSp', 'Parch', 'FamilySize']].head(10))
# print(df['FamilySize'].value_counts().sort_index())

# Let's see whether it's a child-------

# df['IsChild'] = df['Age'] < 18

# Or np where
df['IsChild'] = np.where(df['Age'] < 18, True, False)

# print(df[['Name', 'IsChild']].head(15))

# How many children
print("Number of children:", df['IsChild'].sum())           #133

# Survival rate of children vs others           # Basically mean of survived / all & mean of non-survived / all

print(df.groupby('IsChild')['Survived'].mean().round(3))




#  How to create categories for your values in ranges

bins = []
# FaresCategory 
# df['FaresCategory'] = 


