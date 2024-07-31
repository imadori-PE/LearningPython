pokemon = 'dragonite'
letter= pokemon[3]

x=6
letter2= pokemon[x-1]
print(letter, letter2)
# ! you will get  a python error if you attempt to index beyond the end of a string

print(len(pokemon)) # *number of characters in the word

# ? loop and counting 

word = 'banana'
count = 0
for letter in word:
    if letter == 'a':
        count = count + 1
print('number of letter a in the word ', count)

# ? slicing strings

phrase = 'Expected expression'
print (phrase[3:7]) # * second number is one beyond the end of the slice "up to but not including"
print (phrase[0:1]) 
print (phrase[:6]) 
print (phrase[6:]) 

# ? string concatenation
a = 'hello'
b = a + ' ' +'there'
print(b)

# ? using in as a logical operator
if 'a' in 'logical':
    print('Found it')
print('a' in 'fruit')

# ? string comparison
word = input('type a pokemon: ')
if word == 'GENGAR':
    print('all right GENGAR')
elif word < 'GENGAR':
    print('Your pokemon: '+ word + ', comes before GENGAR')
elif word > 'GENGAR':
    print('Your pokemon: '+ word + ', comes after GENGAR')
    
#? string library
greet = 'Hello bob'
zap = greet.lower()
print(zap,greet.upper())

# ? methods in class string
stuff ='hello world'
print(type(stuff))
print(dir)

# ? searching a string
fruit = 'banana'
pos = fruit.find('na')
print(pos)
pos = fruit.find('z')
print(pos)

# ? search and replace
greet= 'Hello Bob'
nstr= greet.replace('Bob','Jane')
print(greet,nstr)

# ? stripping whitespace
greet= '    Hello bob   '
print(greet)
print(greet.lstrip().rstrip())

# ? prefixes
line = 'Please have a nice day'
print(line.startswith('Please'))
print(line.startswith('p'))

# ? parsing and extracting
data = 'From imadorisempai@gmail.com Wed 31 15:10 2024'
atpos = data.find('@')
sppos=data.find(' ', atpos)
host = data[atpos+1:sppos]
print(host)

# ? exercises
x = 'From marquard@uct.ac.za'
print(x[8])
print(x[14:17])
print(len('banana')*7)

data = 'From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008'
pos = data.find('.')
print(data[pos:pos+3])

thing= '     imadori          '
print(thing.strip()+'|')

'''
Write code using find() and string slicing  to extract the number
at the end of the line below. Convert the extracted value to a floating point number 
and print it out.
'''

text = "X-DSPAM-Confidence:    0.8475"
pos=text.find('0')
strn=text[pos:]
number=float(strn)
print(number)