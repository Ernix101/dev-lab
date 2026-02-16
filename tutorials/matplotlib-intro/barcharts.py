import matplotlib.pyplot as plt
import numpy as np

# This is going to be a chart showing how different items are sold in my restaurant🍗
# Bar charts compare categories of data by representing each category with a bar

Foods = np.array(["Burgers","beef","pizza","Fish","salads","Chicken","Pilau","chips"])
sales = np.array([30000, 40000, 35000, 50000, 35000, 52000, 39000, 40000])

plt.bar(Foods, sales, color="brown")        # Brown bars
# plt.barh(Foods, sales, color="brown")        # For a horizontal bar chart use barh

plt.title("Restaurant Sales")
plt.xlabel("Foods", fontsize=11,
           color="brown")
plt.ylabel("Sales", fontsize=11,
           color="green")


plt.show()


