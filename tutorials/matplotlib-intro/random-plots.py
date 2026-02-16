import matplotlib.pyplot as plt
import numpy as np

# This is going to be the number of gbs I use per year on internet😂
x = np.array([ 2020, 2021, 2022, 2023, 2024, 2025 ])
y1 = np.array([ 10000, 11000, 11500, 10500, 12000, 12500 ])
y2 = np.array([ 10200, 10500, 11000, 12000, 11900, 11500 ])
y3 = np.array([ 10100, 11500, 11300, 12500, 12900, 10500 ])

line_style = dict( marker=".",
               markersize=20,
               markerfacecolor="red",
               markeredgecolor="blue",
               linestyle="dashdot",
               linewidth=3.5,
               color="blue")
line_style2 = dict( marker=".",
               markersize=20,
               markerfacecolor="cyan",
               markeredgecolor="black",
               linestyle="dashed",
               linewidth=3.5,
               color="green")
line_style3 = dict( marker=".",
               markersize=20,
               markerfacecolor="blue",
               markeredgecolor="black",
               linestyle="dotted",
               linewidth=3.5,
               color="green")

plt.title("Amount of Data Spent in the years", fontsize=15,
                                                family="arial",
                                                fontweight="bold",
                                                color="darkblue")

plt.xlabel("Year", fontsize=15,
                    family="arial",
                    fontweight="bold",
                    color="darkblue")
plt.ylabel("GBs", fontsize=15,
                    family="arial",
                    fontweight="bold",
                    color="darkred")

plt.tick_params(axis="both",
                color="blue")

plt.plot(x, y1, **line_style)
plt.plot(x, y2, **line_style2)
plt.plot(x, y3, **line_style3)

plt.xticks(x)

plt.show()


