import sympy
from sympy import  Eq, symbols
from sympy.solvers import solve

def solveForX1():
    x = symbols('x')
    # Put the equation here
    eq = 2*x**2 - 4
    result = solve(eq,x)
    print(f'{eq} = 0 \nResult : {result}')
    

# ? Doing more with the solution

def solveForX2():
    x = symbols('x')
    # Put the equation here
    eq = 2*x - 4
    solution = solve(eq,x)
    print(f'\n{eq} = 0 \nResult[0] : {solution[0]}')
    
# ? Solving in other ways

def solvingOtherWays():
    x,y = symbols('x y')
    # First equation set equal to zero, ready to solve
    first = 2*x - y
    # Sympy syntax for equation equal to zero, ready to factor
    eq1 = Eq(first,0)
    # Sympy solve for x
    sol = solve(eq1,x)
    # Show factored results
    # print("x = ", sol[0])
    print(f'\n{eq1} \nResult : {sol[0]}')

# ? Factoring

def factoring():
    x,y = symbols('x y')
    # Equation set equal to zero, ready to solve
    # #eq = x**2-4
    eq = x**3 - 2*x**2 - 5*x + 6
    result=sympy.factor(eq)
    print(f'\nFactoring {eq} \nResult : {result} ')
    
# ? Solve for a variable

def solveForAVariable():
    # Identify all variables
    a,b,c,x = symbols('a b c x')

    # Left and right sides of the equal sign
    left = 0
    right = a*x**2 + b*x + c

    # Variable to solve for
    variable = x

    # Sympy equation left = right
    eq1 = Eq(left,right)

    # Sympy solve for that variable
    sol = solve(eq1,variable)
    print(f'\n{eq1}')
    # Show factored results
    for s in sol:
        print(variable, " = ", s)

# TODO ------------------------------------------------------------------------------------------------------

# ? Prompt for someone to enter the equation, then solve

def solveInputEquation():
    try:
        x = symbols('x')
        eq = input('\nEnter equation: 0 = ')
        print(sympy.factor(eq))
        print("x = ", solve(eq,x))
    except:
        print('Formula Syntax Error, try again')
        solveInputEquation()


# ? Multiple answers

def solveMultipleAnswers():
    x = symbols('x')
    eq = input('\nEnter equation with multiple answers: 0 = ')
    solution = solve(eq,x)
    for s in solution:
        print("x = ", s)
    print(sympy.factor(eq))

# ? test
solveForX1()
solveForX2()
solvingOtherWays()
factoring()
solveForAVariable()
print('')
for i  in range(1,3):
    solveInputEquation()
    solveMultipleAnswers()
    