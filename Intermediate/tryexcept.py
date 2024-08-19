import sys
# 
# ? I recommend practicing on Google Colab

# TODO -------- 01 --------
# * calculate the reciprocal of the elements of a list
data2= [0.5,0.58,'13',1.25,0,3.45]

for element in data2:
    try:
        print('Input : ',element)
        print('Ouput : ',1/element)
    except:
        print('Ouput : Error')
        # * get the error
        print('Exception : ' , sys.exc_info()[1])
    finally: 
        print('-----------------------')

# TODO -------- 02 --------
# * Customizing exceptions
data2= [0.5,0.58,'13',1.25,0,3.45]

for element in data2:
    try:
        print('Input : ',element)
        print('Ouput : ',1/element)
    except TypeError:
        print('Ouput : This operation is illegal')
    except ZeroDivisionError:    
        print('Ouput : you can\'t divide by zero')
    except: 
        print('Ouput : Error')
        # * get the error
        print('Exception : ' , sys.exc_info()[1])
    print('-----------------------')
    
# TODO -------- 03 --------
# * add only 5 integers to a list
list = []
num = 0
while num<5:
    try:
        tmp = int(input('Input number '))
        list.append(tmp)
        num  = num + 1
    except ValueError:
        print('input isn\'t a integer')

print(list)