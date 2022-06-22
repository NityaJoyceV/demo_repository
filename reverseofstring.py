# Python program to reverse each word in a string

def reverseWords(s):  #user-defined function
    return " ".join(word[::-1] for word in s.split(" "))

# take inputs
string = input('Enter the string: ')

# calling function and display result
print('The reverse is', reverseWords(string))
