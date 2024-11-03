
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
    
    # method to update contact
    def update_contact(self):
        try:
            name = input('Enter Contact Name: ').lower()
            if name not in self.contact_dict:
                print(f'Contact with this name {name} not exist')
                print('*******************************************')
            else:
                age = int(input('Enter Age: '))
                email = input('Enter Email: ')
                phone_number = input('Enter Phone Number: ')
                is_fav = input('Is Contact Favorite (y/n): ').lower()
                favorite = True if is_fav is 'y' else False
                self.contact_dict[name] = {
                    'Age': age,
                    'Email': email,
                    'Phone Number': phone_number,
                    'Favorite': favorite
                }
                print('Contact Updated Successfully')
                print('*******************************************')
        except Exception as e:
            print(e)

    # method to search contact
    def search_contact(self):
        name = input('Enter name to search: ').lower()
        if name not in self.contact_dict:
            print('No Record Found')
            print('*******************************************')
        else:
            s_contact = self.contact_dict[name]
            print(f'Contact Found - {name}')
            for attribute, value in s_contact.items():
                print(f'{attribute} - {value}')
            print('******************************************')

    # method to delete contact
    def delete_contact(self):
        try:
            name = input('Enter Contact Name: ')
            if name not in self.contact_dict:
                print(f'No contact found with this {name} name')
                print('***************************************')
            else:
                del self.contact_dict[name]
                self.total_contacts-=1
                print(f'{name} Conatact deleted successfully')
                print('***************************************')
        except Exception as e:
            print(e)

# calling static method
ContactBook.welcome()
# create object from class
myContact_book = ContactBook()

# while loop to run program continuously
while True:
    try:
        # conditions to run methods on user choice
        result = myContact_book.menu()
        if result == 0:
            myContact_book.total_number_contacts()
        elif result == 1:
            myContact_book.creating_contact()
        elif result == 2:
            myContact_book.view_contact()
        elif result == 3:
            myContact_book.update_contact()
        elif result == 4:
            myContact_book.search_contact()
        elif result == 5:
            myContact_book.delete_contact()
        elif result == 6:
            break
        else:
            print('Please choose valid number..')
    except Exception as e:
        print(e)

