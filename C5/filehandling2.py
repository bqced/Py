# Create a list of names
names = ['Jessa', 'Eric', 'Bob']

# Print a message indicating that names are being saved to a text file
print('Saving names to text file!')

# Open the file 'names.txt' in write mode
# Iterate over the items in the 'names' list and write each name followed by a newline character to the file
# Print 'Done' after writing all the names
with open('names.txt', 'w') as fp:
    for item in names:
        fp.write("%s\n" % item)
    print('Done')

# Create an empty list to store the names
names2 = []
# Print a message indicating that names are being loaded from a text file
print('Loading names from text file!')
# Open the file 'names.txt' in read mode using a context manager
# Iterate over each line in the file
# Remove the newline character from each line and append the modified line to the 'names2' list
with open('names.txt', 'r') as fp:
    for line in fp:
        x = line[:-1]
        names2.append(x)
# Print the contents of the 'names2' list
print(names2)