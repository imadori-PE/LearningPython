import re

# ? if we actually want the matching strings to be extracted, we use re.findall()
# * return A list of strings
x = 'My 2 favorite numbers are 69 and 24'
y= re.findall('[0-9]+',x)
print(y)
y=re.findall('[AEIOU]+',x)
print(y)

x = 'From: Using the : character'
y = re.findall('^F.+:', x)
print(y)

# ? greedy matching to match the largest possible string
x = 'From: using the : character'
y = re.findall('^F.+:',x) #greedly outward in both directions
print(y)
y = re.findall('^F.+?:',x) # non greedly
print(y)

# ? fine tuning string stractio, You can refine the match for re.findall()
x = 'From stephen.marquard@uct.ac.za Sat Jan 5 09:14:16 2008'
y = re.findall('\\S+@\\S+',x) 
# * \S at least one non-white space character
print(y)
# * parentheses are not part of the match - but they tell where to start and stop what string to extract
y= re.findall('From (\\S+@\\S+)',x)
print(y)

# ? the double split pattern
# * sometimes we split a line one way, and then grab one of the pieces of the line and split
x = 'From stephen.marquard@uct.ac.za Sat Jan 5 09:14:16 2008'
y = re.findall('@([^ ]*)',x) 
# * [^ ] means everything but non-blank characters
print(y)

# ? even cooler regex version
x = 'From stephen.marquard@uct.ac.za Sat Jan 5 09:14:16 2008'
y = re.findall('^From .*@([^ ]*)',x) 
# * split @([^ ]*) with starts with From
print(y)

# ? exercise: spam confidence
sfile=input('Enter path file: ')
hand = open(sfile)
numlist=list()
for line in hand:
    line = line.rstrip()
    stuff = re.findall('^X-DSPAM-Confidence: ([0-9.]+)',line)
    if len(stuff) != 1 :continue
    print(stuff)
    num = float(stuff[0])
    numlist.append(num)
print('Maximun:', max(numlist))