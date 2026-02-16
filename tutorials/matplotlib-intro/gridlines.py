import matplotlib.pyplot as plt

# This is going to be where I create the grid to show the revenue by my coffee shop☕
# Grids make plots easier by adding a reference line

months = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
revenue = [10000, 10500, 11000, 11500, 12000, 12500, 13000, 13500, 14000, 14500, 15000, 15500]


plt.grid(axis="y",
         linewidth=2,
         color="lightgrey",
         linestyle="dashed")

plt.title("Revenue in Ernest's morning diner")
plt.xlabel("Months")
plt.ylabel("revenue")
plt.plot(months, revenue)
plt.xticks(months)
plt.show()




