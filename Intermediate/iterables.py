import math as m
from functools import reduce  # * for use reduce

# TODO --------- 1 -------------
# ? get the square of a list of elements

def square(num):
    return num*num
# * list
lst = [12,3,45,22,56,18]

result = map(square,lst)
print(list(result))

# TODO --------- 2 -------------
# ? lambda functions

lst = [12,3,45,22,56,18]

result2 = map(lambda x:x*x,lst)
print(list(result2))

# TODO --------- 3 -------------
#? Each element must be raised to its corresponding element in the other list
baseList= [12,6,8,13,45.67]
baseExponent =[ 3,-2 , 0.8, 5]
result3 = list (map( m.pow, baseList, baseExponent))
print(result3)

# TODO --------- 4 -------------
# ? using filter
def greater_than_five(num):
    return num>5

# * tuple
t1 = (12,3,5,7,-4,0.002)
result4 = tuple(filter(greater_than_five, t1))
print(result4)
print(list(result4))

# TODO --------- 5 -------------
# ? using filter with lambda function
# * tuple
t1 = (12,3,5,7,-4,0.002)
result5 = tuple(filter(lambda x:x>5, t1))
print(result5)
print(list(result5))

# TODO --------- 6  -------------
# ? using filter for even numbers with lambda function
l1 = [12 , 34, 345, 124, 56, 67, 8888, -235]
result6 = list(filter(lambda x: x % 2 == 0, l1))
print(result6)

# TODO --------- 7 -------------
# ? function reduce (apply function, iterable object, default value)

# * whithout reduce
listNumbers= [ -45, 12 , 45, 67, 23, 67, 89, 121, 345]
total = 0
for element in listNumbers:
    total = total + element
print(total)

# * using reduce
def func_sum(total = 0 , element = 0):
    return total + element
    
result7 = reduce (func_sum ,listNumbers) 
print(result7)

# TODO --------- 8 -------------
# ? function reduce (apply function, iterable object) and anonimous function  (lambda)
# * reduce a list of items to a single value

# * whithout reduce
listNumbers= [ -45, 12 , 45, 67, 23, 67, 89, 121, 345]
result8 = reduce (lambda total =0 , acumulator =0 : total + acumulator ,listNumbers) 
print(result8)

