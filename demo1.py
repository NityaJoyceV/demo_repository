print ('This program gives solution to generate Fibonacci terms')   
nterms = int(input("How many terms? "))
n1, n2 = 0, 1
count = 0
if nterms <= 0:
    print("Please enter a positive integer")
elif nterms == 1:
    print("Fibonacci sequence upto",nterms,":")
    print(n1)
else:
    print("Fibonacci sequence:")  
    for i in range(0,nterms):
        print(n1,end=" ")
        nth = n1 + n2
        n1 = n2
        n2 = nth    
print('\nProgram Completed.......')
