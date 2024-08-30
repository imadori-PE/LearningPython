import matplotlib.pyplot as plt
import numpy as np


xmin = -10
xmax = 10
ymin = - 10
ymax = 10
points = 4*(xmax-xmin)
x = np.linspace(xmin,xmax,points) #

fig, ax = plt.subplots()
plt.axis([xmin,xmax,ymin,ymax]) # window size
plt.plot([xmin,xmax],[0,0],'b') # blue x axis
plt.plot([0,0],[ymin,ymax], 'b') # blue y axis

plt.plot(x, np.cbrt(x))


plt.show()