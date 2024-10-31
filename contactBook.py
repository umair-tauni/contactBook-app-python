# Contact Book App feature branch - Python

class ContactBook:
    contact_dict = {}
    total_contacts = 0

    @staticmethod
    def welcome():
        print('Welcome to Contact Book')
        print()
    
    # menu display method
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

    # method to view total number of contacts
    def total_number_contacts(self):
        if self.total_contacts == 0:
            print('No contact found')
            print('*******************************')
        else:
            print('Total Contacts:', self.total_contacts)
            print('********************************')

    # method to create new contact
    def creating_contact(self):
        try:
            name = input('Enter Contact Name: ').lower()
            if name in self.contact_dict:
                print(f'Contact with this name {name} already exist')
                print('***********************************************')
            else:
                age = int(input('Enter Age: '))
                email = input('Enter Email: ')
                phone_number = input('Enter Phone Number: ')
                is_fav = input('Is Contact Favorite: (y/n) ').lower()
                favorite = True if is_fav == 'y' else False
                self.contact_dict[name] = {
                    'Age': age,
                    'Email': email,
                    'Phone Number': phone_number,
                    'Favorite': favorite
                }
                print('Contact Saved Successfully!!')
                print('************************************************')
                self.total_contacts+=1
        except Exception as e:
            print(e)

    # method to view contact
    def view_contact(self):
        if self.total_contacts == 0:
            print('No Record Found')
            print('****************************************')
        else:
            for name, info in self.contact_dict.items():
                print(f'{name} - {info}')
            print('*******************************************')
    

# calling static method
ContactBook.welcome()
# create object from class
myContact_book = ContactBook()
# methods run on user choice
result = myContact_book.menu()
if result == 0:
    myContact_book.total_number_contacts()
elif result == 1:
    myContact_book.creating_contact()
elif result == 2:
    myContact_book.view_contact()
