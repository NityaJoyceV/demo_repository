# input 10 nos find sum of those numbers which are in range (200 and 300) and display the highest input

high = 0
sum=0
for i in range(0,10):
    number = int(input("enter the 10 numbers:"))
    if number >= 200 and number<=300:
        sum=sum+number

    if number > high:
        high = number
        print('highest', high)
        print("sum of numbers between 200 and 300 is    ", sum)
