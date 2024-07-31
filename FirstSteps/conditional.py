#Conditional Steps

#Comparison Operators
# < less than
# <= less than or equal to
# == equal to
# >= greater than or equal to
# > greater than
# != not equal

x = 5
if x == 5 :
    print('Equals to 5')
if x > 4:
    print('Greater than 4')
if x >=5:
    print('Greater than or equals 5')
if x < 6:
    print('Less than 6')
if x != 6:
    print ('not equal 6')
    
#in python indentation is very important because it is used to define the structure and flow of the code
print ('Before 5')
if x==5:
    print('Is 5')
    print('Is still 5')
    print('Third 5')
print ('afterward 5')
print ('Before 6')
if x==6:
    print('Is 6')
    print('Is still 6')
    print('Third 6')
print ('afterward 6')

# * nested decitions
x=42
if x>1:
    print('More than one')
    if x<100:
        print('Less than 100')
print('All done')

# * Two way decistion
x=5
if x < 10:
    print('smaller')
else:
    print('Bigger')

print('finish')

# * Multiway conditions
x = 5
if x < 2:
    print('small')
elif x<10:  
    print('medium')
elif x<20:
    print('big')
elif x<40:
    print('large')
else:
    print('huge')