print('Good morning')
age= int(input('Enter your age '))
print('Your age is ', age)
#the age of the user is inputed as an integer, its is later printed in a sentence
numberone = int(input('Enter a number between 1 and 20 '))
numbertwo = int(input('Enter a number between 1 and 20 '))
numberthree = numberone + numbertwo
print(numberthree)
#numberone and numbertwo can be any number from 1 to 20, the input is an integer
#those two variables are added into a new variable called numberthree
numberonefloat = float(input('Enter a number between 1 and 20 '))
numbertwofloat = float(input('Enter a number between 1 and 20 '))
numberthreefloat = numberonefloat + numbertwofloat
print(numberthreefloat)
#numberonefloat and numbertwofloat are variable which store floats as input
#numberthreefloat stores the addition of numberonefloat and numbertwofloat
firstname = str(input('whats your first name '))
lastname = str(input('whats your last name '))
print('your name is ', firstname, lastname)
#the user inputs his first name which is in firstname variable
#the user inputs his last name which is in lastname variable
#The user's full name is printed in sentence
length = int(input('What is the length of the room? '))
width = int(input('What is the width of the room? '))
area = length * width
print('you will need ', area, 'square footage of carpet')
#the length and width of the room is inputted and stored in separate variables
#the area variable store the multiplication of the variables length and width
#the are is printed in a sentence
poundcoin = int(input('How many pound coins? '))
fiftypence = int(input('How many fifty pence pieces? '))
fiftypence = fiftypence * 0.5
twentypence = int(input('How many twenty pence pieces? '))
twentypence = twentypence * 0.2
total = poundcoin + fiftypence + twentypence
print('The total value of change is ', total, 'pounds')
#variable poundcoin stores the amount of £1 coins as input which is an integer
#variable fiftypence stores the amount of £0.50 coins, this amount is multiplied by 0.5
#to calculate the value in pounds; the variable twentypence stores the amount of £0.20 coins
#this amount is multiplied by 0.2, to calculate the value in pounds