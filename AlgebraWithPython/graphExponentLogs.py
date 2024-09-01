import matplotlib.pyplot as plt
import numpy as np
import math

xmin = -10
xmax = 10
ymin = -10
ymax = 10
plt.axis([xmin,xmax,ymin,ymax]) # window size
plt.plot([xmin,xmax],[0,0],'k') # x axis
plt.plot([0,0],[ymin,ymax], 'k') # y axis

# Same x values for two lines
x1 = np.linspace(xmin, xmax, 1000)

# Blue line for y = 2^x
plt.plot(x1,2**x1, 'b',label ='y = 2^x')  # Change this line

# Red line for y = x
plt.plot(x1, x1, 'r', label ='y = x')

# Different x values for y = log(x) because x > 0
x2 = np.linspace(.001, xmax, 500)

# Green line for y = log2(x)
plt.plot(x2, np.log2(x2), 'g',label ='y = log2(x)')  # Change this line
plt.legend()
plt.show()
