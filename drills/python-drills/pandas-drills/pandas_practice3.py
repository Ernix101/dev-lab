import pandas as pd

# Pandas Drill 3: Orders + Customers
# Goal: practice filtering, grouping, merging, and reshaping.

orders = {
    "order_id": [101, 102, 103, 104, 105, 106, 107, 108, 109, 110],
    "customer_id": [1, 2, 1, 3, 2, 4, 1, 3, 4, 2],
    "date": ["2026-03-01", "2026-03-01", "2026-03-02", "2026-03-02", "2026-03-03", "2026-03-03", "2026-03-04", "2026-03-04", "2026-03-05", "2026-03-05"],
    "product": ["Notebook", "Pen", "Backpack", "Pen", "Notebook", "Water Bottle", "Pen", "Notebook", "Backpack", "Pen"],
    "price": [4.50, 1.20, 24.00, 1.20, 4.50, 9.50, 1.20, 4.50, 24.00, 1.20],
    "qty": [3, 10, 1, 5, 2, 1, 12, 4, 1, 7],
    "payment": ["card", "cash", "card", "cash", "card", "card", "cash", "card", "card", "cash"],
}

customers = {
    "customer_id": [1, 2, 3, 4],
    "name": ["Amina", "Brian", "Chao", "Dina"],
    "segment": ["student", "pro", "student", "pro"],
    "city": ["Nairobi", "Kisumu", "Nairobi", "Mombasa"],
}

# Q1: Load orders into a DataFrame called df_orders.
# Q2: Add a column total = price * qty.
# Q3: Filter orders where payment is "card" AND total >= 10.
# Q4: Find total revenue by product (sum of total), sorted high to low.
# Q5: Find total qty sold by date.
# Q6: Find the single order with the highest total.
# Q7: Merge orders with customers to include customer name and segment.
# Q8: After merging, find total revenue by segment.
# Q9: Create a pivot table: rows = city, columns = product, values = total (sum).
# Q10: Bonus: Find the top 2 customers by total revenue.


df_orders = pd.DataFrame(orders)

total = df_orders["price"] * df_orders["qty"]
df_orders["total"] = total

# Filter for card orders above >= 10
f_orders = df_orders[(df_orders['payment'] == "card" ) & (df_orders['total'] >= 10)]
# print(f_orders)

# Total revenue by product
revenue_by_product = df_orders.groupby("product")["total"].sum()
# print(revenue_by_product.sort_values(ascending=False))

# Total qty by date
# print(df_orders.groupby('date')['qty'].sum())

# The order with the highest total
highest_order = df_orders.groupby('product')['total'].sum()
# print(highest_order.idxmax())

df_customers = pd.DataFrame(customers)

df_merged = df_orders.merge(df_customers, on="customer_id")

# print(df_merged.groupby('segment')['total'].sum())

pivot_table = pd.pivot_table(df_merged, columns='product' , values=['total'], index='city', aggfunc='sum', fill_value=0)
# print(pivot_table)

print(df_merged.groupby('name')['total'].sum().sort_values(ascending=False).head(2))