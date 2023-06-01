data = [3, 0, 1, 8, 7, 5, 4, 9, 6]
# Initialize a list called 'data' with the given values.
print("Data array is: ")
print(data)
# Print a message indicating that the data array is being displayed.
# Print the contents of the 'data' array.
for x in range(len(data)):
# Start a loop that iterates over the indices of the 'data' array 
    print('Pass: ', x+1)
# Print the current pass number.
    for y in range(0, len(data) - 1):
# Start a nested loop that iterates over the range from 0 to len(data) - 1
        print('Comparing', data[y], 'and', data[y+1])
# Print the elements being compared.
        if data[y] > data[y+1]:
# Check if the element at index 'y' is greater than the element at index 'y+1'.
            print('Swapping', data[y], 'and', data[y+1])
# Print the elements being swapped.
            data[y], data[y+1] = data[y+1], data[y]
# Swap the elements using simultaneous assignment.

print('Sorted array is: ')
print(data)
# Print a message indicating that the sorted array is being displayed.
# Print the contents of the 'data' array after the bubble sort algorithm has been applied.