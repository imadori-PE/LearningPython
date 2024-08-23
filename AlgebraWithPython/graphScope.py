import matplotlib.pyplot as plt
import numpy as np
import re

def coordinate(txt):
    
    coord = input(txt).replace(' ','')
    xy = coord.split(',')
       
    if len(xy) !=2  or not re.search('^\(-?[0-9]+,-?[0-9]+\)$',coord):
        print('Wrong coordinate')   
        coordinate(txt)
    else:
        try:
            return ( int(str(xy[0])[1:]), int( str(xy[1])[:len(str(xy[1]))-1] ) )
        except:
            print('Wrong coordinate. Format is (int, int) ')
            coordinate(txt)

print('Input coordinates Example: (x1,y1)')
x1,y1 = coordinate(' (x1,y1) = ')
x2,y2 = coordinate(' (x2,y2) = ')
print(f'Calculate scope : ({x1},{y1}) and ({x2},{y2})' )

# Develop the equation y = mx + b
m = (y2 - y1) / (x2 - x1)
b = y1 - m*x1
print("y = ", m, "x + ", b)

# For the graph
xmin = min(x1,x2)-20
xmax = max(x1,x2)+20
ymin = min(y1,y2)-20
ymax = max(y1,y2)+20

# For the line on the graph
y3 = m*xmin + b 
y4 = m*xmax + b 

# Basic setup for the graph
fig, ax = plt.subplots()
plt.axis([xmin,xmax,ymin,ymax]) # window size
plt.plot([xmin,xmax],[0,0],'b') # blue x axis
plt.plot([0,0],[ymin,ymax], 'b') # blue y axis

# Add details to the graph
ax.set_xlabel("x")
ax.set_ylabel("y")
ax.grid(True)


# Plot the linear function as a red line
plt.plot([xmin,xmax],[y3,y4],'r',label=f'y={m}x+{b}')
plt.legend()
plt.show()
