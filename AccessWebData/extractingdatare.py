import re
# ? if we actually want the matching strings to be extracted, we use re.findall()
x = 'My 2 favorite numbers are 69 and 24'
y= re.findall('[0-9]+',x)
print(y)
y=re.findall('[AEIOU]+',x)
print(y)

# ? greedy matching