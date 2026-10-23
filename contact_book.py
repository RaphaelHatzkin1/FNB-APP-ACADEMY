# contact_book.py

contacts = []


def add_contact():
    name = input("Enter name: ")
    phone = input("Enter phone number: ")
    email = input("Enter email: ")

    contact = {
        "name": name,
        "phone": phone,
        "email": email
    }

    contacts.append(contact)
    print("Contact added successfully!")


def search_contact(name):
    for contact in contacts:
        if contact["name"].lower() == name.lower():
            return contact

    return None


def delete_contact(name):
    for contact in contacts:
        if contact["name"].lower() == name.lower():
            contacts.remove(contact)
            print("Contact deleted successfully!")
            return

    print("Contact not found.")


def view_all():
    if not contacts:
        print("No contacts available.")
        return

    print("\n--- All Contacts ---")

    for contact in contacts:
        print(f"Name:  {contact['name']}")
        print(f"Phone: {contact['phone']}")
        print(f"Email: {contact['email']}")
        print("--------------------")


while True:
    print("\n=== Contact Book ===")
    print("1. Add Contact")
    print("2. Search Contact")
    print("3. Delete Contact")
    print("4. View All Contacts")
    print("5. Exit")

    choice = input("Choose an option: ")

    if choice == "1":
        add_contact()

    elif choice == "2":
        name = input("Enter name to search: ")
        contact = search_contact(name)

        if contact:
            print("\nContact found:")
            print(f"Name:  {contact['name']}")
            print(f"Phone: {contact['phone']}")
            print(f"Email: {contact['email']}")
        else:
            print("Contact not found.")

    elif choice == "3":
        name = input("Enter name to delete: ")
        delete_contact(name)

    elif choice == "4":
        view_all()

    elif choice == "5":
        print("Goodbye!")
        break

    else:
        print("Invalid choice. Please select 1-5.")