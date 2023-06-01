BABY = 1
CHILD = 12
TEEN = 13
# these variable contain numbers which will be subtracted
#by the age we input to calculate how many years ago we were
#a baby, child or teen
name = input('What is your name? ')
age = int(input('How old are you? '))
#variable name asks the user to enter their name as input
#variable age ask the user to enter their age as input, the input type is an integer
print('You were a baby', age-BABY, 'years ago')
print('You were a child', age-CHILD, 'years ago')
#the number we inputted in the age variable is substracted
#to work out how many years ago the user was a baby or child
if age > TEEN:
    print('You became a teen', age-TEEN, 'years ago')
#if the number we inputed in age variable is bigger the 13
#the age is substracted by 13 to work out how many years ago the user was a teen

salesAmount = float(input('Enter the amount of money in £'))
#amount of money is input as a float type
if salesAmount > 20:
 print('You qualify for a £3 voucher')
 #if the user spend more than £20 they qualify for £3 voucher
elif salesAmount > 10:
   print('You qualify for a £1 voucher')
   #if the user spend more than £10 they qualify for a £1 voucher
else:
   print("I'm afraid you didn't spend enough money to get a voucher")
   #if they didnt spend at least more than £10 then they dont qualify for a voucher
