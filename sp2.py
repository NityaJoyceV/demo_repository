special=0
str=input("enter the string")
for i in str:
    if(i=='.') or (i==',') or (i=='#') or (i=='!') or (i=='#') or (i==':') or (i==':'):
        special+=1
print("special",special)
