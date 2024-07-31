astr= 'Hello bob'
# *  when the first conversion fails - it just drop into the except: clause and the program continues
try:
    istr = int(astr)
    print('this line not print')
except:
    istr=-1
print('First', istr)

astr='123'
try:
    istr = int(astr)
except:
    istr=-1
print('Second', istr)