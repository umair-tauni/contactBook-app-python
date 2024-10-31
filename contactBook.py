# Contact Book App feature branch - Python

class ContactBook:
    contact_dict = {}
    total_contacts = 0

    @staticmethod
    def welcome():
        print('Welcome to Contact Book')
        print()
    
    def menu(self):
        print('0. Total Number Contacts')
        print('1. Create Contact')
        print('2. View Contact')
        print('3. Update Contact')
        print('4. Search Contact')
        print('5. Delete Contact')
        print('6. Exit')
        choice = int(input('Choose: '))
        return choice

# calling static method
ContactBook.welcome()
# create object from class
myContact_book = ContactBook()