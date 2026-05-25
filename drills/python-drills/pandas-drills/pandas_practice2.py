import pandas as pd 
import numpy as np 


coffee_sales = {
    "Item": ["Latte","Espresso", "Mocha", "Latte", "Tea", "Espresso", "Mocha", "Tea", "Latte", "Espresso"],
    "Date": ["2026-03-01", "2026-03-01", "2026-03-01", "2026-03-02", "2026-03-02", "2026-03-02", "2026-03-03", "2026-03-03", "2026-03-03", "2026-03-03"],
    "Size": ["M", "S", "L", "S", "M", "S", "M", "L", "L", "S"],
    "Price": [3.50, 2.50, 4.25, 3.00, 2.75, 2.50, 3.75, 3.25, 4.00, 2.50],
    "Quantity": [2, 1, 1, 1, 3, 2, 2, 1, 1, 1],
    "Payment": ["card", "cash", "card", "cash", "card", "card", "card", "cash", "card", "card"]
}

# Q1: Load the data into a DataFrame and show the first 5 rows.
# Q2: Select only the columns: item, size, price, qty.
# Q3: Filter rows where payment is "card".
# Q4: Filter rows where item is "Latte" and size is "L".
# Q5: Create a new column called total = price * qty.
# Q6: Find the total revenue (sum of total).
# Q7: Group by item and get total revenue per item.
# Q8: Group by date and get total qty sold per date.
# Q9: Which item has the highest total revenue?
# Q10: Sort the DataFrame by total revenue descending.

df = pd.DataFrame(coffee_sales)
first_five = df.loc[0:5]

# print(first_five)
# print(df[["Item", "Size", "Price","Quantity"]])
# print(df[df["Payment"] == "card"])
# print(df[(df["Item"] == "Latte") & (df["Size"] == "L")])
total_col = df["Price"] * df["Quantity"]
df["Total"] = pd.DataFrame(total_col)

total_revenue = df["Total"].sum()
# print(total_revenue)

# print(df.groupby("Item").sum())
# print(df.groupby("Date").sum())
revenue_by_item = pd.Series(df.groupby("Item")["Total"].sum())
# print(revenue_by_item)

sorted_items_by_price = revenue_by_item.sort_values(ascending=False)
# print(sorted_items_by_price)

# print(df)
quantity_by_date = pd.Series(df.groupby("Date")["Quantity"].sum())
print(quantity_by_date)

highest_item = revenue_by_item.idxmax()
# print(highest_item)


print(f"Item with highest revenue = {highest_item}")