import numpy as np
import math
import matplotlib.pyplot as plt
from sympy import *

'''
Building on what you have already done, create a menu with the following options:

Display the graph and a table of values for any "y=" equation input
Solve a system of two equations without graphing
Graph two equations and plot the point of intersection
Given a, b and c in a quadratic equation, plot the roots and vertex
Then think about how you will define a function for each item.

'''
def displaying_axis():
  xmin = -20
  xmax = 20
  ymin = -20
  ymax = 20

  fig, ax = plt.subplots()
  ax.grid(True)
  plt.axis([xmin,xmax,ymin,ymax]) # window size
  plt.plot([xmin,xmax],[0,0],'black') # blue x axis
  plt.plot([0,0],[ymin,ymax], 'black') # blue y axis

  points = 10*(xmax-xmin)
  xarr = np.linspace(xmin,xmax,points, endpoint=False)

  return (fig,ax,xarr)

def graph_table_equation():
  strf = input('Enter equation "y=" ')
  fig,ax,x = displaying_axis()
  try: 
    y = eval(strf)
    # * Use eval to convert the string equation into a function.
  except  Exception:
    print(f"Error evaluating the equation: {strf}")
    return
  
  plt.plot(x,y)
  plt.show()

  #* display table
  ax2 = plt.subplot()
  ax2.set_axis_off()
  title = strf 
  cols = ('x', 'y')
  rows = []
  for a,b in list(zip(x,y)):
      rows.append([a,round(b,4)])

  ax2.set_title(title)
  ax2.table(cellText=rows[:20], colLabels=cols, cellLoc='center', loc='upper left')
  plt.show()

def solve_two_equations():
    x,y = symbols('x y')
    print("Remember to use Python syntax with x and y as variables, each equation is already set equal to zero")
    firsteq = input("Enter the first equation: 0 = ")
    secondeq = input("Enter the second equation: 0 = ")
    solution = linsolve([firsteq, secondeq], (x, y))
    x_solution = solution.args[0][0]
    y_solution = solution.args[0][1]
    
    print("x = ", x_solution)
    print("y = ", y_solution)

def graph_two_equations():
    x,y = symbols('x y')
    firsteq = input("Enter the first equation: y = ")
    secondeq = input("Enter the second equation: y = ")
    solution = linsolve([firsteq -y, secondeq-y], (x, y))
    xpoints, ypoints = [],[]
    # * solve equations for find intersection point
    print()
    for a in range(len(solution.args)):
        xpoints.append(solution.args[a][0])
        ypoints.append(solution.args[a][1])
        
    fig,ax,x = displaying_axis()
    try:
        y1=eval(firsteq)
        y2=eval(secondeq)
    except  Exception:
        print(f"Error evaluating any equation")
        return
    
    print(xpoints,ypoints)
    plt.plot(xpoints,ypoints,'ro')
    plt.plot(x,y1)
    plt.plot(x,y2)
    plt.show()

def plot_roots_quadraticf():
  pass

print('[1] Display the graph and a table of values for any "y=" equation input')
print('[2] Solve a system of two equations without graphing')
print('[3] Graph two equations and plot the point of intersection')
print('[4] Given a, b and c in a quadratic equation, plot the roots and vertex')

x=int(input('Choose an option [1-4]: '))
if x==1:
  graph_table_equation()
elif x==2:
    solve_two_equations()
elif x==3:
    graph_two_equations()
elif x==4:
    plot_roots_quadraticf()
else:
    print('No option was selected')
