#
# ! tuples
# * are like lists another kind of sequence
# * tuples are inmutable
# * tuples are more efficient, so in our program when we are making
# * temporary variables we prefer tuples over lists


'''
Write a program to read through the mbox-short.txt and figure out the distribution by hour 
of the day for each of the messages. You can pull the hour out from the 'From ' line by 
finding the time and then splitting the string a second time using a colon.
From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008
Once you have accumulated the counts for each hour, print out the counts, sorted by hour as shown below.
'''

name = input("Enter file:")
if len(name) < 1:
    name = "mbox-short.txt"
handle = open(name)
senders=dict()
for line in handle:
    line=line.strip()
    if line.startswith('From '):
        words=line.split()
        blockHour=words[5].split(':')
        hour=blockHour[0]
        senders[hour]=senders.get(hour,0)+1
lst=list()
lst=sorted([(k,v) for k,v in senders.items()])
for k,v in lst:
    print(k,v)
quit()

x = ('eevee','vaporeon','flaeron','jolteon')
lst = ['eevee','vaporeon','flaeron','jolteon']
#print(dir(x))
print(x.index('vaporeon'), lst.index('vaporeon'))
# * index work both in Python lists and Python tuples
print(x[2])
quit()

for iter in x:
    print(iter)
    
# ! x[0]='glaceon'  'tuple' object does not support item assignment
# ! print(x)

# ? tuples and assignment
(x,y)=(4,'fred')
print(y)

# ? tuples are comparable
# * if the first item is equal, python goes on the next element
print((0,1,2)<(5,1,2))
print((0,1,2000000)<(0,3,4))

# ? sorting list of tuples
d = {'a':10 , 'c':22, 'b' :1}
t=sorted(d.items()) 
# * A list of tuples
print(t)
for k,v in t:
    print(k,v)
    
# ? sort by values insted of key
c = {'a':10 , 'b':1, 'c' :22}
tmp = list()
for k,v in c.items():
    tmp.append((v,k))
tmp= sorted(tmp, reverse=True)
print(tmp, tmp[0])

# ? exercises
x,y=3,4
print(y)

'''
Write a program to read through the mbox-short.txt and figure out who has sent the greatest 
number of mail messages. The program looks for 'From ' lines and takes the second word of 
those lines as the person who sent the mail. The program creates a Python dictionary that 
maps the sender's mail address to a count of the number of times they appear in the file. 
After the dictionary is produced, the program reads through the dictionary using a maximum 
loop to find the most prolific committer.
USING TUPLES
'''

name = input("Enter file: ")
if len(name) < 1:
    name = "mbox-short.txt"
handle = open(name)
senders=dict()
for line in handle:
    line=line.strip()
    if line.startswith('From '):
        words=line.split()
        whoSentEmail=words[1]
        senders[whoSentEmail]=senders.get(whoSentEmail,0)+1

lst=list()
# * reads through the dictionary
# TODO shorter version, list comprehension creates a dynamic list
lst=sorted([(k,v) for k,v in senders.items()],reverse=True)
print(lst[0])