# The code prompts the user to enter a number between 1 and 10 and ensures valid input.
answered = False  

while answered == False:  
# Enter the loop until valid input is received
    num = int(input('Enter a number between 1 and 10 or 20 and 30: '))  
# Prompt the user to enter a number

    if (num >= 1 and num <= 10) or (num >= 20 and num <= 30):
# Check if the entered number is outside the valid range
        print('Please enter valid data!')  
# Display an error message if the input is invalid
    else:
        answered = True  
# Set the flag to True if valid input is received
        print('Thanks for entering valid data!')  
# Display a success message
