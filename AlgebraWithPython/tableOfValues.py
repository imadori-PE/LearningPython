import numpy as np
import matplotlib.pyplot as plt

ax = plt.subplot()
ax.set_axis_off()
title = "y = 3x + 2" # Change this title
cols = ('x', 'y')
rows = [[0,0]]
for a in range(1,10):
    rows.append([a, 3*a + 2]) # Change only the function in this line

ax.set_title(title)
plt.table(cellText=rows, colLabels=cols, cellLoc='center', loc='upper left')
plt.show()