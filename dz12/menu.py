from address_book import AddressBook, address_book_main, Record, Name, Phone, Birthday


def main_menu():
    ab = AddressBook()

    while True:
        print("Main Menu:")
        print("1. Address Book")
        print("2. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            address_book_main(ab)
        elif choice == "2":
            print("Exiting Main Menu...")
            break
        else:
            print("Invalid choice. Please select a valid option.")

if __name__ == "__main__":
    main_menu()
