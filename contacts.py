contacts = {
    "John": "0821112222",
    "Mary": "0813334444",
    "David": "0855556666"
}

name = input("Enter the name of the friend you want to look up: ")

if name in contacts:
    print(f"Found! {name}'s number is {contacts[name]}")
else:
    print("Contact not found.")