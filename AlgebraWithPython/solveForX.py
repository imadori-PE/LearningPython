
# TODO import sympy could not be resolved
# ? info https://www.sympy.org/es/   
# ? more info https://docs.sympy.org/latest/tutorials/intro-tutorial/index.html
'''
    Symbolic computation deals with the computation of mathematical objects symbolically. 
    This means that the mathematical objects are represented exactly, not approximately, 
    and mathematical expressions with unevaluated variables are left in symbolic form.
'''
# * pip install -U sympy
import sympy 
from sympy import symbols 
from sympy.solvers import solve 

x = symbols('x') 

# Put the equation here
eq = 2*x ** 2 - 16

print("x = ", solve(eq,x))