# * repeated steps

#* finish iteration with continue
while True:
    line = input('> ')
    if line == '#':
        continue
    if line == 'done':
        break
    print(line)
print('Done!') 
###########################################
n=5
while n>0:
    print(n)
    n=n-1 
print('finish while')
print(n)

# * the break statement ends the current loop and jumps to the stament inmediately

while True:
    line = input('> ')
    if line == 'done':
        break
    print(line)
print('Done!') 

# * a simple definite loop
for i in [5,4,3,2,1]:
    print(i)
print('Finish')

#########################

pokemons = ['pikachu', 'gengar' , 'dragonite','lucario', 'flygon']

for pkm in pokemons:
    print('Pokemon: ',pkm)
