import json

print("Welcome to Your Simple Contact Book!")

contacts = {}

# Load contacts from file
try:
    with open("contacts.txt", "r") as file:
        contacts = json.load(file)
except FileNotFoundError:
    contacts = {}

while True:
    user_input = input("Please choose an option: \n1. Add contact \n2. View all contacts \n3.Exit \n> ")
    if user_input == "1":
        name = input("Enter Contact Name: ")
        number = input("Enter Phone Number: ")
        address = input("Enter Address: ")
        email = input("Enter Email Address: ")
        contacts[name] = {"number": number, "address": address, "email": email}

    elif user_input == "2":
        print("Here are your contacts")
        for name, info in contacts.items():
            print(f"{name} - {info['number']} - {info['address']} - {info['email']}")

    elif user_input == "3":
        # Save contacts to file before exiting
        with open("contacts.txt", "w") as file:
            json.dump(contacts, file)
        print("Goodbye!")
        break

    else:
        print("Invalid option. Please choose a valid option.")