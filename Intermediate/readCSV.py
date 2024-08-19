import os   
import csv
import string
# ? return list folder and files => os.listdir()
listNames = []
with open('babyNamesUSYOB-mostpopular.csv','r') as file: 
    lectureCSV = csv.reader(file)
    for line in lectureCSV:
        listNames.append(line[1])
        
# ? first 10 names
print(listNames[:10])

# ? implement a function where the first argument is a list of names and the second argument is a letter character. 
# ? The function will return the number of names that start with that letter

def count_names( lt, letter):
    return len(list(filter(lambda x: str(x).startswith(letter) , lt)))

print(count_names(listNames,'A'))

# ? calculate how many names exist with each letter of the alphabet
dataAlphabet = {}.fromkeys(string.ascii_uppercase)
dataAlphabet = dict(list(map( lambda x: ( x[0] , count_names(listNames,x[0]) ),dataAlphabet)))
print(dataAlphabet)

# ? Call a function using arguments by names
print(count_names(letter = 'Z' , lt = listNames))