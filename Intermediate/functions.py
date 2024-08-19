
def adition(*numbers):
    total = 0
    for i in numbers:
        total = total + i
    return total

def operations2(**kwargs):
    # * sum
    sumTotal = 0
    for llave, valor in kwargs.items():
        print(f'{llave} {valor}')

def operations(*arg):
    if len(arg)==2:
        return arg[0]*arg[1]    
    elif len(arg)==3:
        return sum(arg)/len(arg)
    else:
        return 'Error send args'
   
dic_data = {'g1': 9.812, 'euler':2.719, 'pi':3.14159} 
print(operations())
print(operations(12,4))
print(operations(12,4,2))
print(operations2(p1= 12, p2=17, p3=3))
print(operations2(**dic_data))
print(adition(1,2,3,4,5,6,7,8,9,10))

quit()


# TODO implements the calculation of the electric force between two point charges q1 and q2 separated by a distance d meters. using Coulomb's law
# ? function with default parameter value
def couloumb(q1,q2,d,K = 9*10**9):
    return K*q1*q2/d**2

F1 = couloumb(5.6*10**(-12), 3.9*10**(-11),2.8*10**(-2))
# * modifying the value of K
F2 = couloumb(5.6*10**(-12), 3.9*10**(-11),2.8*10**(-2) , 9.81*10**9)
# * We use arguments by name
F3 = couloumb(d= 2.8*10**(-2), q2 = 5.6*10**(-12), q1 =3.9*10**(-11))
print(F1,F2, F3)


# TODO EXERCISES
# ? Which is obtained from the following execution:
upper = lambda string: string.upper()
print(upper("Python Intermedio"))

# ? How many elements does list x have?
cad1 = "Python Intermedio"
x = [c for c in cad1 if c.isdigit()]
print(x, len(x))

# ? How many times does the integer 2 appear in the following list of lists:
 # ? [[j * 2 for j in range (1,555)] for i in range (1,666)] => 665

# ? How many keys does the dictionary have?
x = [x**(3.141589) for x in range(1,2024)]
y = {i: i * i for i in x}
print(len(y))

