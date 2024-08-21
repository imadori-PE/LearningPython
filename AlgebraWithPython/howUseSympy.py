import sympy
from sympy import symbols
from sympy.solvers import solve

x = symbols('x')

# Put the equation here
eq = 2*x**2 - 4

solve(eq,x)

"""Prompt for someone to enter the equation, then solve"""

import sympy
from sympy import symbols
from sympy.solvers import solve

x = symbols('x')
eq = input('Enter equation: 0 = ')

print("x = ", solve(eq,x))

"""Doing more with the solution"""

import sympy
from sympy import symbols
from sympy.solvers import solve

x = symbols('x')

# Put the equation here
eq = 2*x - 4

solution = solve(eq,x)
print("x = ", solution[0])

"""Multiple answers"""

import sympy
from sympy import symbols
from sympy.solvers import solve

x = symbols('x')

eq = input('Enter equation: 0 = ')

solution = solve(eq,x)
for s in solution:
    print("x = ", s)

"""Solving in other ways"""

from sympy import *


var('x y')

# First equation set equal to zero, ready to solve
first = 2*x - y


# Sympy syntax for equation equal to zero, ready to factor
eq1 = Eq(first,0)

# Sympy solve for x
sol = solve(eq1,x)

# Show factored results
print("x = ", sol[0])

"""Factoring"""

import sympy
from sympy import *

var('x y')

# Equation set equal to zero, ready to solve
#eq = x**2-4
eq = x**3 - 2*x**2 - 5*x + 6

sympy.factor(eq)

"""Explaining how each function works"""

# converts string input (including fractions) to float
def string_frac(in_string):
    if "/" in in_string:
        nd = in_string.split("/")
        n = float(nd[0])
        d = float(nd[1])
        ans = n/d
        return ans
    else:
        ans = float(in_string)
        return ans


# Simplest one-step addition
def one_step_add():
    import random
    # Display problem
    a = random.randint(-4,10)
    b = random.randint(2,24)
    print("x + ", a, " = ", b)
    ans = float(input("x = "))
    answer = b-a
    # Test input
    if ans==answer:
        print("Correct! \n")
    else:
        print("Try again")
        print("The correct answer is ", answer, "\n")


# One-step additon with negaive numbers
def one_step_subtract():
    import random
    a = random.randint(-19,-1)
    b = random.randint(2,24)
    print(a, " + x = ", b)
    ans = float(input("x = "))
    # test
    answer = b-a
    if ans==answer:
        print("Correct! \n")
    else:
        print("Try again")
        print("The correct answer is ", answer, "\n")

# One-step multiply
def one_step_mult():
    # Uses string_frac(<input string>)
    import random
    a = random.randint(1,11)
    b = random.randint(2,24)
    print(a, "x = ", b)
    ans_in = (input("x = "))
    answer = b/a
    # test
    if string_frac(ans_in)==answer:
        print("Correct! \n")
    else:
        print("Try again")
        print("The correct answer is ", answer, "\n")

"""Can't do string to fraction"""

print(3/4)

frac = float(input("fraction = "))
print(frac)