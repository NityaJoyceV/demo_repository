while True:
    try:
        income = int(input("Please enter your taxable income in india: "))
    except ValueError:
        print("Sorry, We didn't understand that please enter taxable income as a number")
        continue
    else:
        break

if income <= 50000:
    tax = 0
elif income <= 100000:
    tax = (income - 50000) * 0.05
elif income <= 200000:
    tax = (income - 100000) * 0.10
else
    tax = (income - 150000) * 0.15
print('tax')




while True:
    try:
        income = int(input("Please enter your income in india: "))
    except ValueError:
        print(" please enter  income as a number")
        continue
    else:
        break
if income <= 50000:
    print('tax = 0')
elif income <= 100000:
    tax = (income - 50000) * 0.05
    print( ' tax is :', tax)
elif income <= 200000:
    tax1 = (income - 100000) * 0.10
    print(' tax is :', tax1)
else:
    tax2 = (income - 200000) * 0.15
    print('tax is :', tax2)