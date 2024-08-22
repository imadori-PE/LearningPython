import matplotlib.pyplot as plt
import numpy as np

def coordinate(txt):
    coord = input(txt)
    xy = coord.split(',')
    if len(xy) !=2 and not coord.startswith('(') and not coord.endswith(')'):
        print('Wrong coordinate')
        coordinate(txt)
    else:
        try:
            print(str(xy[0])[1:])
            print(str(xy[1])[:len(str(xy[1]))])
            return ( int(str(xy[0])[1:]), int( str(xy[1])[:len(str(xy[1]))-1] ) )
        except:
            print('Wrong coordinate. Format is (int, int) ')
            coordinate(txt)

print('Input coordinates Example: (12,3)')
coordinate(' (x1,y1) = ')
coordinate(' (x2,y2) = ')
#print(f'Calculate scope : ({x1},{y1}) and ({x2},{y2})' )
quit()
# Develop the equation y = mx + b
m = (y2 - y1) / (x2 - x1)
b = y1 - m*x1
print("y = ", m, "x + ", b)

# For the graph
xmin = 0
xmax = 100
ymin = 0
ymax = 50

# For the line on the graph
y3 = m*xmin + b 
y4 = m*xmax + b 

# Basic setup for the graph
fig, ax = plt.subplots()
plt.axis([xmin,xmax,ymin,ymax]) # window size
plt.plot([xmin,xmax],[0,0],'b') # blue x axis

plt.plot([0,0],[ymin,ymax], 'b') # blue y axis

# Add details to the graph
ax.set_xlabel("thousands")
ax.set_ylabel("tons")
ax.grid(True)
#ax.set_xticks(np.arange(xmin, xmax, 2))
#ax.set_yticks(np.arange(ymin, ymax, 1))


# Plot the linear function as a red line
plt.plot([xmin,xmax],[y3,y4],'r')

plt.show()
