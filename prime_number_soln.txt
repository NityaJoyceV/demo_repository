# checking whether the number is PRIME OR not
numb = int(input('enter a number '))
print ('the inputted number is ',numb)
for n in range(2,numb):
    quot = numb // n
    remd = numb % n
    #print ('quotient is ',quot,' remainder is ',remd)
    if remd == 0:
        break
if n == numb-1:
    print (numb,' IS PRIME ')
else:
    print (numb,' IS NOT prime ')
print (' ----- Prime Number Program is Over ----------')
