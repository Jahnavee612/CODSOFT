contact = {}


def display_contact():
    print("Name\t\tContact Number")
    for key in contact:
        print("{}\t\t{}" .format(key,contact.get(key)))


while True:
    choice = int(input("1.Add contact \n2.View contact list \n3.Search Contact \n4.Update Contact \n5.Delete Contact \nEnter your choice: "))
    if choice == 1:
        name = input("Enter the contact name ")
        phone = input("Enter the mobile number")
        contact[name] = phone
    elif choice == 2:
        if not contact: 
            print("Empty contact book")
        else:
            display_contact()
    elif choice == 3:
        search_name = input("Enter the contacts name")
        if search_name in contact:
            print(search_name,"'s contact number is",contact[search_name])
        else:
            print("Name is not found in contact book")

    elif choice == 4:
        edit_contact = input("Enter the contact to be edited")
        if edit_contact in  contact:
            phone = input("Enter mobile number")
            contact[edit_contact]=phone
            print("Contact Updated")
            display_contact()
        else:
            print("Name is not found in contact book")
    elif choice == 5:
        del_contact = input("Enter the contac to be deleted")
        if del_contact in contact:
            confirm = input("Do you want to delete this contact y/n?")
            if confirm == 'y' or confirm == 'Y':
                contact.pop(del_contact)
            display_contact()
        else:
            print("Name is not found inn contact book")
    else:
        break