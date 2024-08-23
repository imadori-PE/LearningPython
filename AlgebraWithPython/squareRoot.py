import math
import sympy
from sympy import symbols

n = int(input('Input number '))
print('n',n)
# Use these variables
upper_limit = math.floor(math.sqrt(n)) + 1
print('\nupper_limit :', upper_limit)
max_factor = 1
other_factor = 1
square_root = 1

# Slightly different variable strategy
for maybe_factor in range(1, upper_limit):
    if n % (maybe_factor**2) == 0:
        max_factor = maybe_factor**2

# Divide out the greatest square factor
print('max_factor', max_factor)
other_factor = n/max_factor
print('other_factor = n/max_factor = ', other_factor)

# Output variables
square_root = int(math.sqrt(max_factor))
print('Square root ',square_root, 'sqrt(',other_factor ,')')
other_factor = int(other_factor)
output = square_root*sympy.sqrt(other_factor)

# Sympy output without print statement - must be last line
print('Square root n with sympy libray',output)