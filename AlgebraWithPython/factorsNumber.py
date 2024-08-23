number = int(input('Input number '))
# Find all factors
print('Factors :')
for test_factor in range(1,number+1):
    if number%test_factor==0:
        print(test_factor)