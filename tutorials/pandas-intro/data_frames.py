import pandas as pd

data = {
        "Name": ["Spongebob", "Patrick", "Squidward"],
        "Age": [30, 35, 50]
}

df = pd.DataFrame(data, index=["Employee 1", "Employee 2", "Employee 3"])


# Add a new column
df["Job"] = ["Cook", "N/A", "Cashier"]

# Add new row(s)
new_rows = pd.DataFrame([{"Name": "Sandy", "Age": 28, "Job": "Engineer"}, 
                        {"Name": "Eugene", "Age": 60, "Job": "Manager"}],
                       index=["Employee 4", "Employee 5"])

# TO ADD A NEW ROW TO THE EXISTING DF, USE CONCAT() FUNCTION
df = pd.concat([df, new_rows])



print(df)
