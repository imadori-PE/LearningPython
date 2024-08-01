#
# ! A list is a kind of collection

pokemons = ['pikachu','lucario','dragonite','gengar','greninja']

# ? range function returns a list
zzz=range(5)
print(zzz)

for pkm in pokemons:
    print(pkm)
    
# ? list are mutable we can change a element of a list using the index operator
pokemons[0]='raichu'
print(pokemons)

# ? how long is a list
x = [1,2,'eevee',99.0]
print(len(x)) 

# ? list()
numlist = list()
while True:
    inp=input('Enter a number: ')
    if inp=='done': break
    value=float(inp)
    numlist.append(value)
    
average=sum(numlist)/len(numlist)
print('Average', average)

# ? split
line = 'A lot'
etc=line.split()
print(etc)

line='first;second;third'
thing=line.split()
print(thing)
thing=line.split(';')
print(thing)
print(type(thing), dir(thing))

# ? sorted
numbers = [6,8,1,3,4,7,4,0,9,3,2]
numbers = sorted(numbers)
print(numbers)
numbers = [6,8,1,3,4,7,4,0,9,3,2]
numbers.sort()
print(numbers)

# ? exercise
a = [1, 2, 3, 4, 7]
b = [4, 5, 6]
c = a + b
print(len(c))

fruit = 'Banana'
fruit[0] = 'b' #'str' object does not support item assignment
print(fruit)

'''
Open the file romeo.txt and read it line by line. For each line, split the line
into a list of words using the split() method. The program should build a list of words. 
For each word on each line check to see if the word is already in the list and if not 
append it to the list. When the program completes, sort and print the resulting words 
in python sort() order as shown in the desired output.
'''

fname = input("Enter file name: ")
fh = open(fname)
lst = list()
for line in fh:
    line=line.rstrip()
    lstLine=line.split()
    for word in lstLine:
        if word not in lst:
            lst.append(word)

lst.sort()          
print(lst)

'''
Open the file mbox-short.txt and read it line by line. When you find a line that starts with 
'From ' like the following line:
From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008
You will parse the From line using split() and print out the second word in the line (i.e.
the entire address of the person who sent the message). Then print out a count at the end.
Hint: make sure not to include the lines that start with 'From:'. Also look at the last line 
of the sample output to see how to print the count.
'''

fname = input("Enter file name: ")
if len(fname) < 1:
    fname = "mbox-short.txt"

fh = open(fname)
count = 0
for line in fh:
    line=line.strip()
    if line.startswith('From '):
        words=line.split()
        print(words[1])
        count=count+1
    
print("There were", count, "lines in the file with From as the first word")