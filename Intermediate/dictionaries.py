import random as rnd
from functools import reduce

# TODO --------- 1 -------------
# ? condition on the values
data1 = {'A':34,  'B':15 , 'C': 11 , 'D': 69}
# ? .items() get a list of tuples
result1= dict(filter(lambda x: x[1]>20, data1.items()))
print(result1)

# TODO --------- 2 -------------
# ? condition on the keys
result2= dict(filter(lambda x: x[0]== 'B', data1.items()))
print(result2)

# TODO --------- 3 -------------
# ? function map on dictionaries
# * generate a dictionary from another
result3 = dict(map(lambda x:(x[0] + str(rnd.randint(1,2)), x[1]*rnd.randint(0,5)), data1.items()))
print(result3)

# TODO --------- 4 -------------
# ? reduce dictionaries
# * generate a dictionary from another
result4 = reduce(lambda x,y: x + y[1], data1.items(), 0)
print(result4)

# TODO --------- 5 -------------
# ? function zip: It is used to group elements of multiple iterables (such as lists or tuples) into tuples of corresponding elements.
name = ['junior','miguel', 'victoria','jesus','william','nn']
surNames = ['romero','maza','silva','ibañez','patiño']
result5 = list(zip(name,surNames))
print(result5)
print(dict(result5))