print("-----------Contact Book----------")

class Book:
    def __init__(self):
        self.contact = {}

    def Add_Contact(self, name, number):
        self.contact[name] = number

    def Display_Contacts(self):
        if len(self.contact) == 0:
            print("No contacts available.")
        else:
            for name, number in self.contact.items():
                print(f"Name : {name} | Number : {number}")

    def Search_Contact(self, name):
        if name in self.contact:
            print(f"{name} number is {self.contact[name]}")
        else:
            print("This contact does not exist.")

book = Book()
while True:
    print("1. Add Contact")
    print("2. Display All Contacts")
    print("3. Search Contact")
    print("4. Delete Contact")
    print("5. Exit")
    try:
        n = int(input("Enter The Option : "))
    except ValueError:
        print("Enter a valid number.")
        continue
    if n == 1:
        name = input("Enter the name : ")
        number = input("Enter the number : ")
        if number.isdigit():
            book.Add_Contact(name, number)
            print("Contact added successfully.")
        else:
            print("Enter a valid phone number.")
    elif n == 2:
        book.Display_Contacts()
    elif n == 3:
        name = input("Enter the name : ")
        book.Search_Contact(name)
    elif n == 4:
        name = input("Enter the contact you want to delete : ")
        if name in book.contact:
            book.contact.pop(name)
            print("Contact deleted successfully.")
        else:
            print("This contact does not exist.")
    elif n == 5:
        print("Thank you for using Contact Book.")
        break
    else:
        print("Invalid Option.")