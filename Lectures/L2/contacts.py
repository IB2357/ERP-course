def view(contacts):
    print("Contacts:")
    for name, number in contacts.items():
        print(f"{name}: {number}")

def add(contacts, name, number):
    contacts[name] = number
    print(f"Contact {name} added successfully!")

def update(contacts, name, new_number):
    if name in contacts:
        contacts[name] = new_number
        print(f"Contact {name} updated successfully!")
    else:
        print(f"Contact {name} not found!")

def delete(contacts, name):
    if name in contacts:
        del contacts[name]
        print(f"Contact {name} deleted successfully!")
    else:
        print(f"Contact {name} not found!")


contacts = {}

while True:
    print("\nMenu:")
    print("1. View Contacts")
    print("2. Add Contact")
    print("3. Update Contact")
    print("4. Delete Contact")
    print("5. Exit")
    
    choice = input("Enter your choice: ")
    
    if choice == '1':
        view(contacts)
    elif choice == '2':
        name = input("Enter name: ")
        number = input("Enter number: ")
        add(contacts, name, number)
    elif choice == '3':
        name = input("Enter name: ")
        new_number = input("Enter new number: ")
        update(contacts, name, new_number)
    elif choice == '4':
        name = input("Enter name: ")
        delete(contacts, name)
    elif choice == '5':
        print("Exiting...")
        break
    else:
        print("Invalid choice, please try again.")
print(contacts)