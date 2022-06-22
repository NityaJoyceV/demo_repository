c= 0
for i in range(150, 310):
    print(i)
    if (i%7==0) and (i%5==0):
        print (i)
        c=c+1
print('count', c)
