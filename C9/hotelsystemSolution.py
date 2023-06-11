import os  # Import the os module for operating system-related functionalities
import random  # Import the random module for generating random numbers

# Specify the file directory and path to the data file
file_directory = "path/to/your/directory"
data_file = r"C:\Users\cedri\Downloads\data1.txt"

# Open the data file in append mode and close it to create the file if it doesn't exist
with open(data_file, "a") as file:
    pass

# Function to add a new member to the record
def add_member():
    surname = input("Enter surname: ")
    year_joined = input("Enter year joined: ")
    nights_booked = input("Enter nights booked: ")

    member_id = generate_member_id(surname, year_joined)
    membership_status = "Silver"
    points_balance = 0

    member_record = [member_id, surname, year_joined, membership_status, nights_booked, str(points_balance)]
    append_member_record(member_record)

    print("Member added successfully")

# Function to generate a unique member ID based on surname and year joined
def generate_member_id(surname, year_joined):
    surname_abbreviation = surname[:3].title()
    year_abbreviation = year_joined[-2:]
    random_digits = str(random.randint(100, 999))
    return surname_abbreviation + random_digits + year_abbreviation

# Function to append a member's record to the data file
def append_member_record(member_record):
    with open(data_file, "a") as file:
        file.write(",".join(member_record) + "\n")

# Function to update a member's record in the data file
def update_member_record(member_records):
    with open(data_file, "w") as file:
        for member in member_records:
            file.write(",".join(member) + "\n")

# Function to record the number of nights booked for a member
def record_nights_booked():
    member_id = input("Enter Member ID: ")
    nights_booked = int(input("Enter nights booked: "))

    member_records = get_all_member_records()

    for member_record in member_records:
        if member_record[0] == member_id:
            member_record[4] = str(int(member_record[4]) + nights_booked)
            update_points_balance(member_record)
            update_member_record(member_records)
            print("Nights booked added.")
            return

    print("Member not found.")

# Function to record the number of loyalty points redeemed by a member
def record_points_redeemed():
    member_id = input("Enter Member ID: ")
    redeemed_points = int(input("Enter redeemed points: "))

    member_records = get_all_member_records()

    for member_record in member_records:
        if member_record[0] == member_id:
            points_balance = int(member_record[5])
            if redeemed_points > points_balance:
                print("Insufficient loyalty points.")
            else:
                member_record[5] = str(points_balance - redeemed_points)
                update_member_record(member_records)
                print("Points redeemed successfully.")
            return

    print("Member not found.")

# Function to update the loyalty points balance for a member
def update_points_balance(member_record):
    membership_status = member_record[3]
    nights_booked = int(member_record[4])

    points_multiplier = {"Silver": 2500, "Gold": 3000, "Platinum": 4000}
    member_record[5] = str(nights_booked * points_multiplier.get(membership_status, 0))

# Function to upgrade the membership status of members based on nights booked
def upgrade_membership_status():
    member_records = get_all_member_records()

    for member_record in member_records:
        nights_booked = int(member_record[4])
        membership_status = member_record[3]
        if nights_booked >= 30 and membership_status == "Silver":
            member_record[3] = "Gold"
        elif nights_booked >= 100 and membership_status == "Gold":
            member_record[3] = "Platinum"

    update_member_record(member_records)

# Function to retrieve all member records from the data file
def get_all_member_records():
    member_records = []
    with open(data_file, "r") as file:
        for line in file:
            member_records.append(line.strip().split(","))
    return member_records

# Function to display information for all members
def display_member_information():
    member_records = get_all_member_records()

    if not member_records:
        print("No member records found.")
        return

    for member_record in member_records:
        print("Member ID:", member_record[0])
        print("Surname:", member_record[1])
        print("Year Joined:", member_record[2])
        print("Membership Status:", member_record[3])
        print("Nights Booked:", member_record[4])
        print("Points Balance:", member_record[5])

# Test the code
display_member_information()
add_member()
record_nights_booked()
record_points_redeemed()
upgrade_membership_status()
display_member_information()