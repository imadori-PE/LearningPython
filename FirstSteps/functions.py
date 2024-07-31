def thing():
    print('numbers')
    print('functions')
# * reusable piece of code "functions"

def greet(lang):
    if lang=='es':
        return 'hola'
    elif lang=='fr':
        return 'Bonjour'
    else:
        return 'Hello'
   #function with parameter
   
def greet2():
    return 'Hello'

def addTwo(a,b):
    added = a + b
    return added


thing()
print(greet('en'),'imadori')
print(greet('es'),'junior')
print(greet('fr'),'miguel')
print(addTwo(1234,57))