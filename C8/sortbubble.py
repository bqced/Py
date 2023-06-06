myData = [5, 2, 8, 3, 1, 6, 8]  
# The list of data to be sorted

for i in range(len(myData)):  
# Iterate over the indices of the list
    for j in range(len(myData) - 1):  
# Iterate over the indices from 0 to the second-to-last element
        if myData[j] > myData[j + 1]:  
# Check if the current element is greater than the next element
            myData[j], myData[j + 1] = myData[j + 1], myData[j]  
# Swap the elements if the condition is true

print(myData)  
# Print the sorted list
