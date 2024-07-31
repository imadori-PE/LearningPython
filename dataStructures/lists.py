#
# ! A list is a kind of collection

pokemons = ['pikachu','lucario','dragonite','gengar','greninja']

# * range function returns a list
zzz=range(5)
print(zzz)

for pkm in pokemons:
    print(pkm)
    
# * list are mutable we can change a element of a list using the index operator
pokemons[0]='raichu'
print(pokemons)

# * how long is a list
x = [1,2,'eevee',99.0]
print(len(x)) 

