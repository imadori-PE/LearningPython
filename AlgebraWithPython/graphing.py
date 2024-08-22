#
# ? pip install matplotlib
import matplotlib.pyplot as plt
import numpy as np

def graphWithFunctionLoop(xmin:float,xmax:float,ymin:float,ymax:float):
    fig, ax = plt.subplots()
    '''
    matplotlib.pyplot.subplots() is one of the most versatile and used functions of the Matplotlib library in Python. 
    Used to create a figure and a grid of subplots (subgraphs) in that figure. 
    It is useful when you want to create multiple charts in a single window or when you need to 
    have more granular control over the layout of the charts.
    
    matplotlib.pyplot.subplots(nrows=1, ncols=1, sharex=False, sharey=False, squeeze=True, subplot_kw=None, gridspec_kw=None, **fig_kw)
    Main parameters:
        nrows: Number of rows of subplots (graphs) you want in the grid.
        ncols: Number of subplot columns in the grid.
        sharex: If True, all subplots will share the same x-axis.
        sharey: If True, all subplots will share the same y-axis.
        squeeze: If True, the resulting axis will be reduced to the minimum possible dimension. 
                 If there is a single subplot, it returns a single Axes object, rather than a list of them.
        subplot_kw: A dictionary with additional keywords passed to each subplot.
        gridspec_kw: A dictionary with additional keywords to specify the subplot layout.
        fig_kw: Additional keywords passed to figure creation.
        
    Return:
        subplots() returns two objects:
            fig: An object of type Figure that represents the figure on which the subplots will be drawn.
            ax: An object of type Axes or an array of Axes objects (depending on the values ​​of nrows and ncols) 
                that represents each of the subplots within the figure.
    
    '''
     
    plt.axis([xmin,xmax,ymin,ymax]) # * window size
    plt.plot([xmin,xmax],[0,0],'b') # * blue x axis
    '''
    The matplotlib.pyplot.plot() function is one of the most fundamental functions in Matplotlib. 
    It is used to create line charts, which are useful for visualizing the relationship between two sets of data, 
    such as the x-axis and y-axis.
    matplotlib.pyplot.plot(*args, **kwargs)
    Main parameters:
        *args: You can receive several types of input:
        plot(y): Takes a single argument, interpreted as the values ​​on the y-axis. 
                The x-axis values ​​will be automatically generated as a numerical sequence [0, 1, 2, ..., n-1].
        plot(x, y): Takes two arguments, where x and y are the values ​​on the x and y axes, respectively.
        plot(x, y, format): In addition to the x and y values, a format string can be specified to define the
                            line style and markers.
        **kwargs: Named arguments that allow you to customize the chart, such as color, linestyle, linewidth, marker, label, etc.
    '''
    
    plt.plot([0,0],[ymin,ymax], 'b') # * blue y axis

    for x in range(10):
        y = 0.5*x + 1
        plt.plot([x],[y], 'ro')
    plt.show()
 
def graphArrayAsInput(xmin:float,xmax:float,ymin:float,ymax:float):   
    points = 2*(xmax-xmin)
    x = np.linspace(xmin, xmax, points, endpoint=False)
    '''
    numpy.linspace is a function in Python's NumPy library that is used to generate a sequence of numbers 
    evenly distributed over a specified range. It is especially useful when you need a set of values ​​between 
    two boundaries with a specific number of points.
    '''
    
    fig, ax = plt.subplots()
    ax.set_title('Graph NDarray input')
    plt.axis([xmin,xmax,ymin,ymax]) # * window size
    plt.plot([xmin,xmax],[0,0],'r') # * red x axis
    plt.plot([0,0],[ymin,ymax], 'r') # *red y axis
    
    y = 2*x +1
    print(x)
    print(y)
    plt.plot(x,y, 'navy',label='y = 2*x +1')
    plt.legend() # ? to add a legend explaining each line.

    plt.show()
    
def customizeAGraph(xmin:float,xmax:float,ymin:float,ymax:float):
    points = 2*(xmax-xmin)
    x = np.linspace(xmin, xmax, points)

    fig, ax = plt.subplots()
    plt.axis([xmin,xmax,ymin,ymax]) # window size
    plt.plot([xmin,xmax],[0,0],'b') # blue x axis
    plt.plot([0,0],[ymin,ymax], 'b') # blue y axis

    ax.set_xlabel("x values")
    ax.set_ylabel("y values")
    ax.set_title("Customize a Graph")
    ax.grid(True)

    ax.set_xticks(np.arange(xmin, xmax, 1))
    ax.set_yticks(np.arange(ymin, ymax, 1))
    '''
    np.arange is a function of NumPy, a popular Python library for numerical computing. 
    The np.arange function is used to create arrays of numbers with a given range. It is similar to Python's 
    range built-in function, but returns a NumPy array.

    Syntax: np.arange([start, ]stop, [step, ], dtype=None, *, like=None)
    
    Parameters:
    start (optional): The initial value of the range. The default value is 0.
    stop (required): The end value of the range. The range includes start but does not include stop.
    step (optional): The difference between consecutive values ​​in the array. The default value is 1.
    dtype (optional): The data type of the resulting array. If not specified, NumPy tries to infer the data type automatically.
    '''
    y = 2*x +1
    plt.plot(x,y, label='y=2x+1')
    plt.plot([4],[6], 'ro', label='point')
    plt.plot(x,3*x, label='y=3*x')
    plt.legend()
    plt.show()
#graphWithFunctionLoop(-10,10,-10,10)
#graphArrayAsInput(-10,10,-10,10)
customizeAGraph(-10,10,-10,10)
