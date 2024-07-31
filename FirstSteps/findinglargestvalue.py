def findLargest(numbers):
    largest_so_far=-1
    for i in numbers:
        if i>largest_so_far:
            largest_so_far=i
    return largest_so_far

sn = input('Array Length= ')
try:
    size=int(sn)
except:
    size=0  
    print('error read number')

if size !=0:
    # * creat list with size 
    numbers = [0] * size
    while size >0:
        temp= input('Number: ')
        try:
            numbers[size-1]=float(temp)
        except:
            #error reading number
            continue
        size-=1
    
    print('Array[]', numbers)
    print('the largest value is ', findLargest(numbers))
    