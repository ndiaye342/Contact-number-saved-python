save_contact = input("Enter contact name to save: ")
phone_number = input("Enter phone number: ")

file = open("contacts.txt", "w")
file.write(f"{save_contact}: {phone_number}\n")
file.close()

addanother = input("Add another contact? (y/n): ")
if addanother.lower() == "y":
    save_contact = input("Enter contact name to save: ")
    phone_number = input("Enter phone number: ")

    file = open("contacts.txt", "a")
    file.write(f"{save_contact}: {phone_number}\n")
    file.close()

read = input("Read all contacts from file? (y/n): ")
if read.lower() == "y":
    file = open("contacts.txt", "r")
    content = file.read()
    print("\nContacts List:")
    print(content)
    file.close()
else:
    print("Goodbye!")

