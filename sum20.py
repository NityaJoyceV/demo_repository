high = 0
sum=0
for i in range(0,20):
    number = int(input("enter the 20 numbers:"))
    if number >= 160 and number<=225:
        sum=sum+number

    if number > high:
        high = number
        print('highest', high)
        print("sum of numbers between 160 and 225 is    ", sum)


 
 
