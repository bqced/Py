#Open a file named "newdata.txt" in write mode
myfile = open("newdata.txt", "w")
#Write the string "This is test data" to the file
myfile.write("This is test data")
#Close the file
myfile.close()

#Open a file named "data.txt" in read mode
myfile = open("data.txt", "r")
# Read the contents of the file and store it in the variable filedata
filedata = myfile.read()
#Print the message "data in file is: "
print("data in file is: ")
#Print the contents of the file
print(filedata)
#Close the file
myfile.close()