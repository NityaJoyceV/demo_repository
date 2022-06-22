s = ["Python",'dsgf',"abcdef,"] # initial string
s=s+1
stringlength = len(s+1)
slicedstring = s[stringlength :: -1]
print (slicedstring)
index = len(s) # calculate length of string and save in index
while index > 0: 
    reversedString += s[ index - 1 ] # save the value of str[index-1] in reverseString
    index = index - 1 # decrement index
print(reversedString) # reversed string
