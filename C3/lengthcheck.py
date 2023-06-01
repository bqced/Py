# The code prompts the user to enter words and calculates the length of each word, but only if the word has a length greater than 0.
while True:  
# starts a loop
    word = input('Type a word: ')  
# Prompt the user to enter a word
    if len(word) == 0:  
# Check if the entered word has a length of 0
       break
    else:
        print('Your word is', len(word), 'letters.')  
# Calculate and display the length of the entered word
    print('Thanks for using this program.')  
# Display a thank you messag