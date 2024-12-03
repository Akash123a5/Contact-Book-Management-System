import os

FILE_NAME = "contacts.txt"

def load_contacts():
    contacts = {}
    if os.path.exists(FILE_NAME):
        with open(FILE_NAME, 'r') as file:
            for line in file:
                phone, name, email, address = line.strip().split('|')
                contacts[phone] = {"name": name, "email": email, "address": address}
    return contacts

def save_contacts(contacts):
    with open(FILE_NAME, 'w') as file:
        for phone, details in contacts.items():
            file.write(f"{phone}|{details['name']}|{details['email']}|{details['address']}\n")
