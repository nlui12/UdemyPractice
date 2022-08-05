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

evenNums = list(range(0,11,2))
print (evenNums)

###########################################################################################################################

#Use a List Comprehension to create a list of all numbers between 1 and 50 that are divisible by 3.

#for loop and range(50) initialization, also empty list to hold divisible by 3
#divisible by 3 means num % 3 == 0

divide3 = [_x for _x in range(1,51) if _x % 3 == 0]
print(divide3)

###########################################################################################################################

#To start use split() on the string to separate the words in a list
#Once we have words in a list we can 

st2 = 'Print every word in this sentence that has an even number of letters'

#len gives back the length of a 
for word in st2.split():
    if len(word) % 2 == 0:
        print(word+ " <- is even in length")

#########################################################################################################################

#Write a program that prints the integers from 1 to 100. But for multiples of three print "Fizz" instead of the number, and for the multiples of five print "Buzz". For numbers which are multiples of both three and five print "FizzBuzz".

for x in range(1, 100):
    if (x % 5 == 0) & (x % 3 == 0):
        print('fizzbuzz')
    elif (x % 5 == 0):
        print('buzz')
    elif (x % 3 == 0):
        print('fizz')
    else:
        print(x)

########################################################################################################################

#Use a List Comprehension to create a list of the first letters of every word in the string below:

st3 = 'Create a list of the first letters of every word in this string'


firstletterList = [x[0] for x in st3.split(" ")]
print(firstletterList)



