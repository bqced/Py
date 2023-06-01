import random
word = "Superbowlpowerchamp"
print(word, "is", len(word), "characters long")
#string is stored in word variable
#string is printed to say how many characters long it is

word1 = "football"
print(word1, "is", len(word1), "characters long")
#string is stored in word variable
#string is printed to say how many characters long it is
whichletter = random.randint(0, (len(word1)))
chosenletter = word1[whichletter]
#variable whichletter stores a random integer from 0 to the last index of the string word1
print("Character", whichletter, "of", word1, "is", chosenletter)
#prints the random character of the string word1 and its index

# Extracting a substring from word3
word3 = "elegant"
word4 = word3[1:4]
print("Extracted string is", word4)

# Concatenating two strings
part1 = "i am a footballer "
part2 = "in the premier league"
sentence = part1 + part2
print("Concatenated string is:", sentence)

# Adding two numbers of different data types
num1 = 150
num2 = 1.50
num_new = num1 + num2
print("datatype of num1:", type(num1))
print("datatype of num2:", type(num2))

print("Value of num_new:", num_new)
print("datatype of num_new:", type(num_new))

# Converting data types and performing addition
numint = 123
numstr = "978"
print("Data type of numint is", type(numint))
print("Data type of numstr is", type(numstr))
print(numint + int(numstr))