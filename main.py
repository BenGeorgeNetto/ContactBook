from pprint import pprint


class ContactBook:

    def __init__(self):
        self.tempLi = []
        self.phoneBook = []
        self.state = 0

    def add(self):
        self.tempLi = []
        name: str = str(input('Name: '))
        phone: int = int(input('Phone: '))
        email: str = str(input('Email ID: '))
        self.tempLi = [name, phone, email]
        self.phoneBook.append(self.tempLi)

    def delete(self):
        name = str(input('Name to remove: '))
        for i in range(len(self.phoneBook)):
            if name == self.phoneBook[i][0]:
                self.phoneBook.pop(i)
                print('Contact removed')
                break

    def display_all(self):
        if not self.phoneBook:
            print("List is empty: []")
        else:
            for i in range(len(self.phoneBook)):
                print(self.phoneBook[i])

    def search(self):
        choice = int(input('Enter search criteria\n\n1. Name\n2. Number\n3. Email ID \n\nPlease enter: '))
        temp = []

        if choice == 1:
            query = input("Please enter the name of the contact you wish to search: ")
            for i in range(len(self.phoneBook)):
                if query == self.phoneBook[i][0]:
                    temp.append(self.phoneBook[i])

        elif choice == 2:
            query = int(
                input("Please enter the number of the contact you wish to search: "))
            for i in range(len(self.phoneBook)):
                if query == self.phoneBook[i][1]:
                    temp.append(self.phoneBook[i])

        elif choice == 3:
            query = str(input("Please enter the e-mail ID of the contact you wish to search: "))
            for i in range(len(self.phoneBook)):
                if query == self.phoneBook[i][2]:
                    temp.append(self.phoneBook[i])

        else:
            print("Invalid search criteria")
            return -1

        print(temp)

    def delete_all(self):
        self.phoneBook = []

    def show_all(self):
        pprint(self.phoneBook)
        # for i in self.phoneBook:
        #     for n, p, e in self.phoneBook[i]:
        #         print(f"\n\nName: {n} \nPhone: {p} \nEmail ID: {e}")

    def menu(self):
        print('Contact Book\n\n')
        print('\nSelect an option\n')
        print('1. Add a contact')
        print('2. Delete a contact')
        print('3. Search for contact')
        print('4. Display all contacts')
        print('5. Delete all contacts')
        print('6. Exit')

        while 1:
            self.state = int(input('\n\nEnter choice: '))
            if self.state == 1:
                self.add()

            if self.state == 2:
                self.delete()

            if self.state == 3:
                self.search()

            if self.state == 4:
                self.show_all()

            if self.state == 5:
                self.delete_all()

            if self.state == 6:
                break


c = ContactBook()

c.menu()
