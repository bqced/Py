failcount = 0  
# Counter to keep track of the number of failed checks
userin = input('Please enter 5 characters: ')
if len(userin) != 5:  
# Check if the input has exactly 5 characters
    print('Invalid input. Please enter exactly 5 characters.')
else:
    if userin[0].isdigit():  
# Check if the first character is a digit
        print('Check 1 passed')
    else:
        print('Check 1 failed')
        failcount += 1
    if userin[1].isalpha():  
# Check if the second character is a letter
        print('Check 2 passed')
    else:
        print('Check 2 failed')
        failcount += 1
    if userin[2].isalnum():  
# Check if the third character is alphanumeric
        print('Check 3 failed')
        failcount += 1
    else:
        print('Check 3 passed')
    if userin[3:].isalpha(): 
 # Check if the fourth and fifth character is a letter
        print('Check 4 passed')
    else:
        print('Check 4 failed')
        failcount += 1
# Calculate the percentage of characters entered correctly
percentage = ((5 - failcount) / 5) * 100
print('Percentage of characters entered correctly: ', percentage, 'percent')
