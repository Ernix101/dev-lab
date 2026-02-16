import matplotlib.pyplot as plt
import numpy as np

# Pie chart = Circular chart divided into slices to show percentages of the total.
#               Good for visualizing distribution among categories.

# We'll be working on my most recently played games to find out which one I enjoy the most.

games = np.array(["Asphalt 9", "Shadow Fight", "Free Fire", "Blood strike"])
time_spent = np.array([300, 250, 275, 225])

# Set colors for each slice
colors = ["rebeccapurple", "darkblue", "orange", "Red"]

plt.pie(time_spent, labels=games,
        autopct='%1.1f%%',
        colors=colors,
        explode=[0, 0, 0, 0.1],
        shadow=True,
        startangle=90)

plt.title("game hours")


plt.show()