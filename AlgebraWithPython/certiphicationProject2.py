import numpy as np
import random as rnd
import math
import matplotlib.pyplot as plt
from sympy import *

'''
Build a graphing calculator that performs the functions mentioned in the previous step:

    Graph one or more functions
    Create a table of (x,y) values
    Shade above or below the line
    Solve and graph a system of two equations
    Zoom in or out on a graph
    Solve quadratic equations (given a, b, and c)
'''
def displaying_axis(isTable=False):
  xmin = -20
  xmax = 20
  ymin = -20
  ymax = 20

  fig, ax = plt.subplots()
  ax.grid(True)
  ax.set_xlabel("x")
  ax.set_ylabel("y")
  plt.axis([xmin,xmax,ymin,ymax]) # window size
  if not isTable:
    plt.plot([xmin,xmax],[0,0],'black') # blue x axis
    plt.plot([0,0],[ymin,ymax], 'black') # blue y axis

  points = 10*(xmax-xmin)
  xarr = np.linspace(xmin,xmax,points, endpoint=False)

  return (fig,ax,xarr)

def graph_functions():
    
    print('Enter three functions in terms of x')
    try:
        x = symbols('x')
        firsteq = sympify(input("Enter the first equation: y = "))
        secondeq = sympify(input("Enter the second equation: y = "))
        thirdeq = sympify(input("Enter the third equation: y = "))
        
        # * Create numerical functions from symbolic expressions
        eq1=lambdify(x,firsteq)
        eq2=lambdify(x,secondeq)
        eq3=lambdify(x,thirdeq)
        
        fig,ax,x_vals = displaying_axis()
        y1 = eq1(x_vals)
        y2 = eq2(x_vals)
        y3 = eq3(x_vals)
    
        # * graph equation 1
        plt.plot(x_vals,y1,label=firsteq)
        # * graph equation 2
        plt.plot(x_vals,y2,label=secondeq)
        # * graph equation 2
        plt.plot(x_vals,y3, label=thirdeq)
        plt.legend()
        plt.show()
    except:
        print('Error, try again')

def table_values():
    x = symbols('x')
    print('Enter a function in terms of x') 
    
    try:
        symf = sympify(input('f(x)= '))
        eq1 = lambdify(x,symf)
        fig,ax,x_vals = displaying_axis(True)
     
        #* display table
        ax.set_axis_off()
        title = 'f(x)='+ str(symf)
        cols = ('x', 'y')
        rows = []
    
        for a in range(-10,10):
            rows.append([ a,eq1(a) ]) 
    
        ax.set_title(title)
        ax.table(cellText=rows, colLabels=cols, cellLoc='center', loc='upper left')
        plt.show()
    
    except SympifyError:
        print('Error function')
    except ValueError:
        print('Value Error')
    except:
        print('Error, try again')
        
def shade_above_below():
    x = symbols('x')
    try:
        symf = sympify(input('Enter equation: y = '))
        
         # * Create numerical functions from symbolic expressions
        eq1=lambdify(x,symf)
        fig,ax,x = displaying_axis()
        y = eq1(x)

        option = rnd.randint(1,2) # * 1 above 2 below
         # * graph  2
        plt.plot(x,y)
        if option==1:
            y2=20
            ax.set_title('Shade above the line')
            plt.fill_between(x, y, y2, facecolor='green')
        else:
            y2=-20
            ax.set_title('Shade below the line')
            plt.fill_between(x, y, y2, facecolor='red')
        plt.show()
        
    except:
        print('Error, try again')


def solve_graph_two_equations():
    x,y = symbols('x y')
    
    try:
        print("Solve linear and quadratic equations with x and y as variables, each equation is already set equal to zero")
        firsteq = sympify(input("Enter the first equation: 0 = "))
        secondeq = sympify(input("Enter the second equation: 0 = "))

        solution = nonlinsolve([ firsteq, secondeq], (x, y)) # * substract y for let to the function equal to zero
        xpoints, ypoints = [],[]
        # * solve equations for find intersection point
        for a in range(len(solution.args)):
            print(f'Solution = ( {solution.args[a][0]} , {solution.args[a][1]} )')
            xpoints.append(solution.args[a][0])
            ypoints.append(solution.args[a][1])

        # * Sympy syntax for equation equal to zero, ready to factor
        y_first = Eq(firsteq,0)
        y_second = Eq(secondeq,0)

        # * Sympy solve for y
        sy1 = solve(y_first,y)
        sy2 = solve(y_second,y)
        
        eq1=lambdify(x,sy1)
        eq2=lambdify(x,sy2)
        
        fig,ax,x_vals = displaying_axis()
        
        y1 = eq1(x_vals)
        y2 = eq2(x_vals)

        # * intersection points
        plt.plot(xpoints,ypoints,'ro')
        # * graph equation 1
        plt.plot(x_vals,y1[0])
        # * graph equation 2
        plt.plot(x_vals,y2[0])
        plt.show()
    except:
        print('Error, try again')

def zoom_in_or_out_graph():
    print('Enter function in terms of x')
    try:
        x = symbols('x')
        firsteq = sympify(input("Enter equation: y = "))
        
        # * Create numerical functions from symbolic expressions
        eq1=lambdify(x,firsteq)
        
        fig,ax,x_vals = displaying_axis()
        y1 = eq1(x_vals)
    
        # * graph equation 1
        plt.plot(x_vals,y1,label=firsteq)
        plt.legend()
        plt.show()
    except:
        print('Error, try again')
    
def solve_quadratic_abc():
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
         
while True:
  print('[1] Graph one or more functions')
  print('[2] Create a table of (x,y) values')
  print('[3] Shade above or below the line')
  print('[4] Solve and graph a system of two equations')
  print('[5] Zoom in or out on a graph')
  print('[6] Solve quadratic equations (given a, b, and c)')
  x=int(input('Choose an option [1-6]: '))
  print('------------------------------------------------------------------------')
  if x==1:
    graph_functions()
  elif x==2:
      table_values()
  elif x==3:
      shade_above_below()
  elif x==4:
      solve_graph_two_equations()
  elif x==5:
      zoom_in_or_out_graph()
  elif x==6:
      solve_quadratic_abc()
  else:
      print('No option was selected')
      break