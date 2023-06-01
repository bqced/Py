import random  
# Import the random module for generating random values
def showinventory(inv, bell):  
# Define a function to display inventory and bells
    print("\nYour current inventory is:")  
# Print a message for inventory
    for item in inv:  
# Iterate over each item in the inventory
        print(item)  
# Print the item
    print("\nYour current bells are:", bell)  # Print the current bell value

inventory = []  
# Initialize an empty list for inventory
# Define a 2D list of items and their values
masterlist = [["Softwood", 60], ["Clay", 100],  
              ["Clump of Weeds", 10],
              ["Hardwood", 60],
              ["Iron Nugget", 375],
              ["Stone", 75],
              ["Tree Branch", 5],
              ["Wood", 75],
              ["Gold Nugget", 1000]]

print("Generating random inventory and bells for you!")  
# Print a message
for i in range(0, 10):  
# Iterate 10 times
    num = random.randint(0, len(masterlist) - 1)  
# Generate a random index within the range
    inventory.append(masterlist[num][0])  
# Add a random item to the inventory
bells = random.randint(1000, 5000)  
# Generate a random bells value
showinventory(inventory, bells)  
# Call the showinventory function to display inventory and bells

print("Welcome to Nook's Cranny...")  
# Print a welcome message
input("There are some nice items, what can i offer you:")  
# Prompt for user input

total = 0  
# Initialize a variable to keep track of the total value
for item in inventory:  
# Iterate over each item in the inventory
    for master in masterlist:  
# Iterate over each item in the masterlist
        if item == master[0]:  
# Check if the item matches the masterlist item
            print("Match", item, "value =", master[1])  
# Print a match message with item and value
            total += master[1]  
# Add the value to the total

print(total, "bells")  
# Print the total value
sell = input("Do you accept? (Y/N): ")  
# Prompt for user input
if sell.lower() == "y" or sell.lower() == "yes":  
# Check if the user accepts the offer
    bells += total  
# Add the total value to the bells
    inventory.clear()  
# Clear the inventory list
    print("\nThanks for doing business with us today, come again!")  
# Print thank you message
else:
    print("\nThat's a shame, never mind, there's always next time!")  
# Print a message if the offer is not accepted

showinventory(inventory, bells)  
# Call the showinventory function to display updated inventory and bells