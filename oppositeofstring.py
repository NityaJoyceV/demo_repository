# take inputs
string = 'Know Program'

# splitting the string into list of words
words = string.split(' ')
# reversing each word and creating a new list of words
reverseWords = [word[::-1] for word in words]
# joining the new list of words to for a new string
reverseString = " ".join(reverseWords)
