str = input('Enter a word')
# Check if the length of the string is less than 2
if len(str) < 2:
    # Print a space if the condition is true
    print(" ")
else:
    # Extract the first two characters and the last two characters of the string
    str1 = str[:2] + str[-2:]
    # Print the extracted substring
    print(str1)

# Define list1
list1 = [2, 56, 78, 6]

# Calculate the sum of the elements in the list
print(sum(list1))

list1 = []  
# Initialize an empty list to store the numbers
while True:
    num = int(input("Enter a number: "))
    if num == 0:
        break  
# Exit the loop if the user enters 0
    list1.append(num)  
# Add the number to the list

print("List of numbers:", list1)
print("Sum of numbers:", sum(list1))
