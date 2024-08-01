# 
# ! collections List and Dictionary (key-value pair)
# * a dictionary permit random access to the data 

cabinet= dict()
cabinet['summer']=12
cabinet['fall']=3
cabinet['spring']=75
print(cabinet)

# ? dictionary tracebacks 
ccc=dict()
# ! Exception has occurred: KeyError print(ccc['csev'])
print('csev' in ccc)
ccc['csev']='thing'
print('csev' in ccc)

# ? when we see a new name
counts = dict()
typePokemons=['grass','bug','rock','ghost','grass','bug']
for tpk in typePokemons:
    if tpk not in counts:
        counts[tpk]=1
    else:
        counts[tpk]=counts[tpk] + 1
print(counts)

# ?  count with get()
counts = dict()
typePokemons=['grass','bug','rock','ghost','grass','bug']
for tpk in typePokemons:
    counts[tpk]= counts.get(tpk,0)+1
print(counts)

# ? counting pattern
counts=dict()
sfile=input('Enter file path: ')
fhandler=open(sfile)
for line in fhandler:
    line=line.strip()
    words=line.split()
    for word in words:
        counts[word]=counts.get(word,0) + 1
                   
print("Counts",counts)

# ? definite loops and dictionaries
counts = {'junior': 3, 'miguel':2, 'jesus':5}
# * It loops through the keys in the dictionary
for keys in counts:
    print(keys, counts[keys])

# ? retrieving list of Keys and Values
print(list(counts.keys())) # get a list of keys
print(list(counts.values())) #get a list of values
print(list(counts.items())) #both

#? two iteratiosn variables
for key, value in counts.items():
    print(key, value)
    
# ? exercises
stuff = dict()
print(stuff.get('candy',-1))

'''
Write a program to read through the mbox-short.txt and figure out who has sent the greatest 
number of mail messages. The program looks for 'From ' lines and takes the second word of 
those lines as the person who sent the mail. The program creates a Python dictionary that 
maps the sender's mail address to a count of the number of times they appear in the file. 
After the dictionary is produced, the program reads through the dictionary using a maximum 
loop to find the most prolific committer.
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
print(senders)
# * reads through the dictionary
prolificCommiter=None
count=None
for key,value in senders.items():
    if count is None or count<value:
        count=value
        prolificCommiter=key
print(prolificCommiter,count)