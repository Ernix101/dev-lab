import matplotlib.pyplot as plt
import numpy as np

x = np.array([2023, 2024, 2025, 2026])
y1 = np.array([15, 25, 30, 20])
y2 = np.array([17, 23, 38, 5])

line_style = dict(marker=".",
                  markersize=30,
                  markerfacecolor="#1cd3fc",
                  markeredgecolor="#1cd3fc",
                  linestyle="solid",
                  linewidth=4,
                  color="#1c5bfc")


plt.plot(x, y1, **line_style)

plt.plot(x, y2, **line_style)

plt.show()