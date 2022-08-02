# Python Udemy Assesment for 07-statements

#Question 1: Use for, .split(), and if to create a Statement that will print out words that start with 's'
st = 'Print only the words that start with s in this sentence'
onlyS = []


separatedWord = st.split(' ')

#start of the for loop that iterates through separateWord and sees if it starts with 's'
for words in separatedWord:
    if (words[0] == 's'):
        onlyS.append(words)

#the split() method takes a string and depending on the delimiter splits the words into elements of a list
print (onlyS)

###########################################################################################################################

