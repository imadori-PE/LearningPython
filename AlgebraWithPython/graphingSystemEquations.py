import matplotlib.pyplot as plt
import numpy as np

xmin = -10
xmax = 10
ymin = -10
ymax = 10

# ? Define how many points to plot
points = 10*(xmax-xmin)

# ? Define the array of x values once
x = np.linspace(xmin,xmax,points)

fig, ax = plt.subplots()
plt.axis([xmin,xmax,ymin,ymax]) # window size
plt.plot([xmin,xmax],[0,0],'b') # blue x axis
plt.plot([0,0],[ymin,ymax], 'b') # blue y axis

# ? line 1
y1 = 3*x
plt.plot(x, y1,label= 'y=3*x')

# ? line 2
y2 = x**3
plt.plot(x, y2,label= 'y=x**3')
plt.legend()
ax.grid(True)
plt.show()