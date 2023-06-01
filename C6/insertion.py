5data = []
n = int(input("Enter the number of elements: "))
# Prompt the user to enter the number of elements they want to sort.
for i in range(n):
    num = int(input("Enter a number: "))
    data.append(num)
# Prompt the user to enter each number, and append them to the 'data' list.
# Initialize a list called 'data' with the given values.
print('Data array is: ', data)
# Print the contents of the 'data' array.
for i in range(1, len(data)):
# Start a loop that iterates from index 1 to the length of the 'data' array 
    key = data[i]
# Store the value at index 'i' in the variable 'key'.
    print('Number to place: ', key)
    y = i-1
    # Initialize a variable 'y' to the previous index of 'i'.
    while y >= 0 and key < data[y]:
        # Start a loop that continues as long as 'y' is greater than or equal to 0
        # and the value at index 'y' is greater than the 'key' value.
        print(key, 'less than', data[y])
        # Print the comparison between the 'key' value and the value at index 'y'.
        data[y+1] = data[y]
        # Shift the value at index 'y' one position to the right.
        y -= 1
        # Decrement the 'y' variable.
        data[y+1] = key
        # Place the 'key' value in the correct position.
        print('Inserting', key)
        print(data)
print('Sorted array is: ', data)
# Print the contents of the 'data' array after the insertion sort algorithm has been applied.