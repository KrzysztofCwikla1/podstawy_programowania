
from contact import Contact
from contact_list import ContactList

def main():
    contact_list = ContactList()

    contacts = [
        Contact("John Brown", "brown@onet.pl", "555234000"),
        Contact("Anna May", "am@o2.pl", "232000199"),
        Contact("George Small", "smallg@google.pl", "222999100"),
        Contact("Paola Big", "bigpaola@poczta.pl", "100200300"),
    ]

    for c in contacts:
        contact_list.add_contact(c)

    contact_list.display_contacts()

if __name__ == "__main__":
    main()
