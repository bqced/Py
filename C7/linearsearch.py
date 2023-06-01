def linearSearch(alist, item):
    # Initialize pos and found variables
    pos = 0
    found = False
    # Perform linear search while position is within the list and found is false
    while pos < len(alist) and found == False:
        if alist[pos] == item:
            found = True
        else:
            pos += 1
    # Return whether the item is found or not
    return found

# Define a list 'alist'
alist = [1, 2, 32, 8, 17, 42, 13, 0]

# Call the linearSearch function to search for the item 3 in the list
print(linearSearch(alist, 3))
# Call the linearSearch function to search for the item 13 in the list
print(linearSearch(alist, 13))
