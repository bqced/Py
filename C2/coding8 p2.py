# Initialize the variable to keep track of the number of guesses
guesses = 1

# Ask the user to guess a name and convert it to title case
myName = input('Guess my name? ').title()

# Keep looping until the guessed name is 'Cedric'
while myName != 'Cedric':
    # Print a message indicating that the guessed name is incorrect
    print('My name is not', myName, 'try again!')

    # Ask the user to guess the name again and convert it to title case
    myName = input('What is my name?').title()

    # Check if the guessed name is 'Joshua' or 'Sara'
    if myName == 'Joshua':
        print('My name is not Joshua')
    elif myName == 'Sara':
        print('Shut up')

    # Increment the number of guesses
    guesses += 1

# Print a message indicating that the correct name has been guessed and the number of guesses made
print('Correct, you guessed in', guesses)


