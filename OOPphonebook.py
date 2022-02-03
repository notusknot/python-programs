class Phonebook:
    def __init__(self):
        self.contacts = {}
        
    def addContact(self, name, number):
        if name not in self.contacts:
            self.contacts[name]=number
        else:
            print('\nContact already here\n')
            
    def removeContact(self, name):
        ans = input('\nAre you sure you want to delete this? \n')
        if ans == 'y' or ans == 'yes':
            del self.contacts[name]

    def searchContact(self,name):
        if name in self.contacts:
            print(self.contacts[name])
        else:
            print('\nThis name is not registered\n')

    def listContacts(self):
        for loop in self.contacts:
            print(loop, self.contacts[loop])
        
book1=Phonebook()
while True:
    choice = int(input('Option 1: add contact \nOption 2: remove contact \nOption 3: search for contact \nOption 4: list all contacts \nOption 5: quit \n'))
    if choice == 1:
        name = input('Enter name: ')
        number = input('Enter number: ')
        book1.addContact(name,number)
    elif choice == 2:
        name = input('Enter name: ')
        book1.removeContact(name)
    elif choice == 3:
        name = input('Enter name: ')
        book1.searchContact(name)
    elif choice == 4:
        book1.listContacts()
    elif choice == 5:
        print('\nThank you\n')
        break
    
    
