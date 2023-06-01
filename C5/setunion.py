maths = set(["Leon", "John", "James", "Prince", "Sharon"])  
# Create a set of people in the math group
computing = set(["Leon", "Kim", "Sharon", "Cedric"])  
# Create a set of people in the computing group
art = set(["Cedric", "Basquiat", "Prince", "Amanda"])  
# Create a set of people in the art group

print("Math people are", maths)  
# Print the people in the math group
print("Computer people are", computing)  
# Print the people in the computing group
print("Arts people are", art)  
# Print the people in the art group

allGroups = maths.union(computing, art)  
# Find the union of all three sets
print("All people are", allGroups)  
#Print all the people in the combined sets

intersectGroups = maths.intersection(computing)  
# Find the intersection between math and computing sets
print("People in both math and computing are", intersectGroups)  
# Print the common people in math and computing sets
intersectGroups1 = maths.intersection(art)  
# Find the intersection between math and art sets
print("People in math and art", intersectGroups1)  
# Print the common people in math and art sets
intersectGroups2 = computing.intersection(art)  
# Find the intersection between art and computing sets
print("People in both art and computing", intersectGroups2) 

compdif = computing.difference(maths, art)  
# Find the difference between computing and math/art sets
mathsdif = maths.difference(computing, art)  
# Find the difference between math and computing/art sets
artdif = art.difference(maths, computing)  
# Find the difference between art and math/computing sets

print("People in computing but not in maths or art are", compdif)  
# Print people in computing but not in math or art
print("People in maths but not in computing or arts are", mathsdif)  
# Print people in math but not in computing or art
print("People in art but not in maths or computing are", artdif)  
# Print people in art but not in math or computing

people1sets = set()
people1sets.update(maths.intersection(computing))  
# Find people present in both math and computing
people1sets.update(maths.intersection(art))  
# Find people present in both math and art
people1sets.update(computing.intersection(art))  
# Find people present in both computing and art

print("People in more than one set are", people1sets)  
# Print people present in more than one set