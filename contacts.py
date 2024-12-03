from utils import validate_string, validate_phone_number


def add_contact(contacts):
    while True:
        try:
            name = input("Enter Name: ")
            if not all(x.isalpha() or x.isspace() for x in name):
                raise ValueError("Name must letters and ")
            
            
            break
        except ValueError as e:
            print(f"Error: {e}")
            print("Please try again.")

    while True:
        try:
            phone = input("Enter Phone Number: ")
            if not phone.isdigit():
                raise ValueError("Phone number must only digits.")
            if len(phone) != 11:
                raise ValueError("Phone number must be 11 digits long.")
            if phone in contacts:
                raise ValueError("This number already exists.")

            break
        except ValueError as e:
            print(f"Error: {e}")
            print("Please try again.")

    email = input("Enter Email: ")
    address = input("Enter Address: ")
    
    contacts[phone] = {"name": name, "email": email, "address": address}
    print("Contact added successfully!")








def view_contacts(contacts):
    if not contacts:
        print("No contacts available.")
        return
    print("\nContacts:")
    for phone, details in contacts.items():
        print(f"Name: {details['name']}, Phone: {phone}, Email: {details['email']}, Address: {details['address']}")

def search_contact(contacts):
    search_term = input("Enter name, phone, or email to search: ").lower()
    found = False
    for phone, details in contacts.items():
        if (search_term in details['name'].lower() or 
            search_term in phone or 
            search_term in details['email'].lower()):
            print(f"Found: Name: {details['name']}, Phone: {phone}, Email: {details['email']}, Address: {details['address']}")
            found = True
    if not found:
        print("No contact found.")

def remove_contact(contacts):
    phone = input("Enter the phone number of the contact to remove: ")
    if phone in contacts:
        del contacts[phone]
        print("Contact removed successfully!")
    else:
        print("Contact not found.")
