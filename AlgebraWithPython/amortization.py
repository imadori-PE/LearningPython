p = float(input('Input principle: '))
r = float(input('Input rate: '))
t = float(input('input years - 18 months equals 1.5 year: '))


# * Break down that formula into parts
numerator = (r/12)*(1+(r/12))**(12*t)
denominator = (1+(r/12))**(12*t) - 1
payment = round(p* numerator/denominator, 2)

print("payment = ", payment)

# * loop to show interest amounts
balance = round(p,2)
print("month \t balance \t mensuality \t interest \t amortization")
for a in range(int(12*t)):
    interest = round(balance*r/12, 2)
    #if a%24==0 or a==359:
    print(a, "\t", balance, "\t", payment, "\t", interest, "\t", round(payment - interest,2))
    balance = round(balance+interest-payment,2)
