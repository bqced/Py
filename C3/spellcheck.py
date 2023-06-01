dictionary = ['these', 'are', 'common', 'words']  
# Initialize a list of words
print('Current dictionary is:', dictionary)  
# Print the current dictionary
while True:  
# Start a loop
    sentence = input('Enter a sentence: ')  
# Prompt the user to enter a sentence
    if sentence == ' ':  
# Check if the entered sentence is empty
        print('bye!!')  
# Print exit message
        break  
# Exit the loop if the sentence is empty
    myList = sentence.split()  
# Split the sentence into a list of words 
    for word in myList:  
# Iterate over each word in the list
        if word not in dictionary:  
# Check if the word is not in the dictionary
            print('Word', word, '- not in dictionary')  
# Print a message for words not in the dictionary
            answer = False  
# Initialize a flag for user input
            while answer == False:  
# Start a loop for user input
                addMe = input('Would you like to add the word to the dictionary? (Y/N): ')  
# Prompt the user to add the word             
                if addMe.lower() == "y":  
# Check if the user chooses to add the word
                    dictionary.append(word)  
# Add the word to the dictionary
                    print('Appended word', word, 'to the dictionary')  
# Print a confirmation message
                    answer = True  
# exits the loop
                elif addMe.lower() == "n":  
# Check if the user chooses not to add the word
                    print('Not appended word', word, 'to the dictionary')  
# Print a message for not adding the word
                    answer = True  
# exits the loop
                else:  
# If the user enters an invalid choice
                    print('Invalid choice - try again (Y/N)')  
# Print an error message for invalid input
print('Final dictionary is:', dictionary)  
# Print the final dictionary