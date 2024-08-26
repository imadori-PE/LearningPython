from sympy import *
from sympy.plotting import plot
from sympy import sqrt

x,y = symbols('x y')

# * First equation set equal to zero, ready to solve
first = -x**2 - y + 10
#first = sqrt(x) - y

# * Second equation set equal to zero, ready to solve
second = 2*x**2 - 2*y - 4
#second = -x + 5 - y

# * Solve - can be linear or nonlinear equations
solution = nonlinsolve([first, second], (x, y))
for a in range(len(solution.args)):
    x_solution = solution.args[a][0]
    y_solution = solution.args[a][1]
    print("Solution = (", x_solution, ",", y_solution, ")")

# * Sympy syntax for equation equal to zero, ready to factor
y_first = Eq(first,0)

# * Sympy solve for y
y1 = solve(y_first,y)

# * Same two steps for second equation
y_second = Eq(second,0)
y2 = solve(y_second,y)

# * Show factored results
print("y = ", y1[0])
print("y = ", y2[0])

# * Plot solution
x = symbols('x')
xmin = -10
xmax = 10
plot(y1[0], y2[0], (x,xmin,xmax))
