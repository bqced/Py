class Node:
    def __init__(self, dataval=None):  
# Define a Node class with method that initializes dataval and nextval attributes
        self.dataval = dataval
        self.nextval = None

class SLinkedList:
    def __init__(self):  
# Define a singly linked list class with  method that initializes the headval attribute
        self.headval = None

    def listprint(self):  
# Define a method to print the values of the linked list
        printval = self.headval
        while printval is not None:  
# Iterate through the linked list until the end is reached
            print(printval.dataval)  
# Print the value of the current node
            printval = printval.nextval  
# Move to the next node

mylist = SLinkedList()  
# Create an instance of the SLinkedList class called 'mylist'
mylist.headval = Node(input("Enter data for node 1: "))  
# Create a new node and assign its value based on user input
e2 = Node(input("Enter data for node 2: "))  
# Create a new node and assign its value based on user input
e3 = Node(input("Enter data for node 3: "))  
# Create a new node and assign its value based on user input
e4 = Node(input("Enter data for node 4: "))  
# Create a new node and assign its value based on user input
e5 = Node(input("Enter data for node 5: "))  
# Create a new node and assign its value based on user input

mylist.headval.nextval = e2  
# Link the first node to the second node
e2.nextval = e3  
# Link the second node to the third node
e3.nextval = e4  
# Link the third node to the fourth node
e4.nextval = e5  
# Link the fourth node to the fifth node

mylist.listprint()  
# Print the values of the linked list