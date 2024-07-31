import random

def setValuesInArray(numbers):
    i=0
    for n in numbers:
        numbers[i]=int(random.random()*100+1)
        i=i+1

quantity = random.randint(8,50)
numbers = [0] * quantity
setValuesInArray(numbers)
print('Array', numbers)

count = 0
sum=0
smallest=None

for thing in numbers:
    if smallest is None:
        smallest=thing
    elif thing < smallest:
        smallest=thing
        
    count = count +1 
    sum = sum + thing
    
print('smallest ',smallest)
print('Size ',count)
print('Sum', sum)
print('average', sum/count)
