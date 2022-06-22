sentence = input("Enter sentence : ")
print(sentence)
count=0
#checks for each character in the string
for i in sentence:
    if i == '.' or i== ',' or i == ';' or i == '!' or i == ':':
        count=count+1
print(count)
   
