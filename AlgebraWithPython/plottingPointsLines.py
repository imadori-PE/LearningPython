import matplotlib.pyplot as plt

# TODO Plotting Points and Lines
'''
Notice the subtle difference between plotting points and lines. Each plot() statement takes an array of x values, an array of y values, 
and a third argument to tell what you are plotting. The default plot is a line. The letters 'r' and 'b' (and 'g' and a few others) 
indicate common colors. The "o" in 'ro' indicates a dot, where 'rs' would indicate a red square and 'r^' would indicate a red triangle. 
Plot a red line and two green squares.
'''
# * Use these numbers:
linex = [2,4]
liney = [1,5]
pointx = [1,6]
pointy = [6,3]

# * Keep these lines:
xmin = -10
xmax = 10
ymin = -10
ymax = 10

fig, ax = plt.subplots()
plt.axis([xmin,xmax,ymin,ymax]) # window size
plt.plot([xmin,xmax],[0,0],'b') # blue x axis
plt.plot([0,0],[ymin,ymax], 'b') # blue y axis

# *  red line
plt.plot(linex,liney,'r')
# * green square 
plt.plot(pointx,pointy,'gs')
# * dot
plt.plot([7.5],[7.5],'bo')

plt.show()
