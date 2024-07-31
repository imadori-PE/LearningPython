# Numeric Expressions
xx=2
xx=xx+2
print('Sum: ',xx)

xx = 440
yy=xx* 4535
print('multiplication', yy)

jj=23
zz = jj / 5
print('division', zz)

kk=jj % 5
print('remainder', kk)

pp = kk ** 3
print('power', pp)

##order evaluations
##when we string operators together python must know which one to do first
##this is called "operators precedence" 
##Order: parenthesys, power, multiplication, addition, left to right

x = 1 + 2 * 3 - 8 / 2 ** 3
print ('1 + 2 * 3 - 8 / 2 ** 3 = ', x)

x = 1 + 2 ** 3 / 4 * 5
print ('1 + 2 ** 3 / 4 * 5=', x)

##type matters
#python knows whta type everything is 
#cannot add 1 to string

eee = 'hello' + 'there'
#eee = eee + 1 #error here beacuse can't convert int to str implicity
print(type(eee), type(1), eee)

##serveral type of numbers
##integers, floating point numbers

xx=1
temp=98.5
print(type(xx), type(temp), type(1), type(1.0))

#type conversions
#integer divisions produce  a floating poin result
#with int() and float() convert string in number
x = float(99)+100
print(x, type(x))
s = '123'
print(s, type(s))
s= int(s)+77
print(s, type(s))
x= int(98.6)
print('round x or not?', x)

#user input
nam = input ('what is your favorite pokemon?')
print ('ohhh is ',nam )

