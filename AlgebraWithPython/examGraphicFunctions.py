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
    print("Solve linear and quadratic equations with x and y as variables, each equation is already set equal to zero")
    firsteq = input("Enter the first equation: 0 = ")
    secondeq = input("Enter the second equation: 0 = ")
    try:
        eq1=eval(firsteq)
        eq2=eval(secondeq)
    except  Exception:
        print(f"Error evaluating any equation")
        return
    
    solution = nonlinsolve([eq1, eq2], (x, y))
    for a in range(len(solution.args)):
        print(f'Solution = ( {solution.args[a][0]} , {solution.args[a][1]} )')
    

def graph_two_equations():
    x,y = symbols('x y')
    firsteq = input("Enter the first equation: y = ")
    secondeq = input("Enter the second equation: y = ")
    try:
        eq1=eval(firsteq)
        eq2=eval(secondeq)
    except  Exception:
        print(f"Error evaluating any equation")
        return
    
    solution = nonlinsolve([ eq1-y, eq2-y], (x, y)) # * substract y for let to the function equal to zero
    xpoints, ypoints = [],[]
    # * solve equations for find intersection point
    for a in range(len(solution.args)):
        print(f'Point of intersection = ( {solution.args[a][0]} , {solution.args[a][1]} )')
        xpoints.append(solution.args[a][0])
        ypoints.append(solution.args[a][1])
        
    fig,ax,x = displaying_axis()
    
    eq1=eval(firsteq)
    eq2=eval(secondeq)
        
    # * intersection points
    plt.plot(xpoints,ypoints,'ro')
    # * graph equation 1
    plt.plot(x,eq1)
    # * graph equation 2
    plt.plot(x,eq2)
    plt.show()

def plot_roots_quadraticf():
    print("0 = ax\u00b2 + bx + c")
    a = float(input("a = "))
    b = float(input("b = "))
    c = float(input("c = "))
    
    # * Check for non-real answers:
    if b**2-4*a*c < 0:
        print('No real roots')
    else:
        fig,ax,x = displaying_axis()
        y = a *x**2 + b*x + c
        # * vertex
        vx = - b /(2*a)
        vy = a * vx ** 2 + b * vx + c
        print(f'Vertex = ( {vx} , {vy})')
        plt.plot(vx,vy,'ro')
        # * Write your code here, changing x1 and x2
        x1 = (-b + math.sqrt(b**2 - 4*a*c))/(2*a)
        x2 = (-b - math.sqrt(b**2 - 4*a*c))/(2*a)
        print('The roots are ', x1, ' and ', x2)
        plt.plot(x1,0,'ro')
        plt.plot(x2,0,'ro')
        plt.plot(x,y)
        
        plt.show()

print('[1] Display the graph and a table of values for any "y=" equation input')
print('[2] Solve a system of two equations without graphing')
print('[3] Graph two equations and plot the point of intersection')
print('[4] Given a, b and c in a quadratic equation, plot the roots and vertex')

x=int(input('Choose an option [1-4]: '))
print('------------------------------------------------------------------------')
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
