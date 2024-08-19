#
# ? open file from my computer
fname = 'wordss.txt'
try:
    with open('wordss.txt') as file:
        data = file.read()
except FileNotFoundError:
    print('Exception, file can\'t open')
else:
    print('Exception has not ocurred')
    
quit()

# ? raise NameError('You don\'t read documentation')
# ? raise ZeroDivisionError ('i want to instantiate a ZeroDivisionError')

try:
    x = 3.141519 / 0
except:
    print('Incorrect operation')
    x = float(input('Input numerator '))
    y = float (input('Input denominator '))
else:
    print('No error has occurred')
