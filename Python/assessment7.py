# Python Udemy Assesment for 07-statements

#Question 1: Use for, .split(), and if to create a Statement that will print out words that start with 's'
st = 'Print only the words that start with s in this sentence'
onlyS = []

#used st.split() to split up the strings using the whitespaces as delimiters
separatedWord = st.split(' ')

#start of the for loop that iterates through separateWord and sees if it starts with 's'
for words in separatedWord:
    if (words[0] == 's'):
        onlyS.append(words)

#the split() method takes a string and depending on the delimiter splits the words into elements of a list
print (onlyS)

###########################################################################################################################

#Question 2: Use range() to print all the even numbers from 0 to 10.

for even in range(10):
    if ((even % 2) == 0):
        print( even, end = " ")
print('\n')

###########################################################################################################################

#Use a List Comprehension to create a list of all numbers between 1 and 50 that are divisible by 3.

#for loop and range(50) initialization, also empty list to hold divisible by 3
#divisible by 3 means num % 3 == 0

threeRange = []
for counter in range(50):
    if counter % 3 == 0:
        threeRange.append(counter)

print(threeRange)

###########################################################################################################################

#To start use split() on the string to separate the words in a list
#Once we have words in a list we can 