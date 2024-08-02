#
# TODO Regular expressions
# * also referred to as regex o regexp, is a intelligent form to search
# * for reduce code
# ? ^ matches the beginning of a line
# ? $ matches the end of the line
# ? . matches any character
# ? \s matches whitespaces
# ? \S matches any non-whitespace character
# ? * repeats a character zero or more times
# ? *? repeats a character zero or more times (non-greedy)
# ? + repeats a character one o more times
# ? +? repeats a character one o more times (non-greedy)
# ? [aeiou] matches a single character in the listed set
# ? [^XYZ] matches a single character  not in the listed set
# ? [a-z0-9] the set of characters can include a range
# ? ( indicates where string extraction is to start
# ? ) indicates where string extraction is to end
# * import library import re
# * re.search() returns a true or false depending on whether the string matches the regular expression

import re
hand = open('C:/Users/jumir/Documents/PythonProjects/LearningPython/AccessWebData/mbox-short.txt')

for line in hand:
    line=line.rstrip()
    if re.search('^From:',line):
        print(line)

# ? the dot character matches any character
# ? if yu add the asterisk character, the character is any number of times
for line in hand:
    line=line.rstrip()
    if re.search('^X-.*:',line):
        print(line)

# * another example
for line in hand:
    line=line.rstrip()
    if re.search('^X-\S+:',line): 
        # match start of the line X and - matches any non-whitespace character one or more times and :
        print(line)