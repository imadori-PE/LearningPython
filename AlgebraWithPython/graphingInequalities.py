import matplotlib.pyplot as plt
import numpy as np

xmin = -10
xmax = 10
ymin = -10
ymax = 10
points = 2*(xmax-xmin)
x = np.linspace(xmin,xmax,points)

fig, ax = plt.subplots()
plt.axis([xmin,xmax,ymin,ymax]) # * window size
plt.plot([xmin,xmax],[0,0],'b') # * blue x axis
plt.plot([0,0],[ymin,ymax], 'b') # * blue y axis

# line 1
y1 = x+6
plt.plot(x, y1,'-') # * - dash lines
plt.fill_between(x, y1, ymax, facecolor='red')

# line 2
y2 = x+3
plt.plot(x, y2,'-')
plt.fill_between(x, y2, y1, facecolor='yellow')

# line 3
y3 = x-1
plt.plot(x, y3)
plt.fill_between(x, y3, y2, facecolor='green')

# line 4
y4 = x-4
plt.plot(x, y4)
plt.fill_between(x, y4, y3, facecolor='blue')

plt.show()

