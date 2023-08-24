import re
import json
from collections import UserDict
from datetime import datetime, date

class Field:
    def __init__(self, value=None):
        self.value = value

    def __str__(self):
        return str(self.value)

class Name(Field):
    def __init__(self, value):
        super().__init__(value)
        if not self.validate_name(value):
            raise ValueError("Invalid name format")

    @staticmethod
    def validate_name(name):
        pattern = r"^[a-zA-Z']{2,}$"
        return re.match(pattern, name) is not None

class Phone(Field):
    def __init__(self, value):
        super().__init__(value)
        if not self.validate_phone(value):
            raise ValueError("Invalid phone number format")

    @staticmethod
    def validate_phone(phone):
        pattern = r"^\d{10}$"
        return re.match(pattern, phone) is not None

class Birthday(Field):
    def __init__(self, value):
        super().__init__(value)
        if not self.validate_date(value):
            raise ValueError("Invalid date format")

    @staticmethod
    def validate_date(date_str):
        try:
            datetime.strptime(date_str, "%Y-%m-%d")
            return True
        except ValueError:
            return False

class Record:
    def __init__(self, name, phone, birthday=None):
        self.name = name
        self.phones = [phone]
        self.birthday = Birthday(birthday.value) if birthday is not None else None

    def days_to_birthday(self):
        if self.birthday:
            today = date.today()
            next_birthday = date(today.year, self.birthday.value.month, self.birthday.value.day)

            if next_birthday < today:
                next_birthday = date(today.year + 1, self.birthday.value.month, self.birthday.value.day)

            days_left = (next_birthday - today).days
            return days_left

    def add_phone(self, phone_value):
        phone = Phone(phone_value)
        self.phones.append(phone)

class AddressBook(UserDict):
    def __init__(self, chunk_size=10):
        super().__init__()
        self.chunk_size = chunk_size

    def add_record(self, record):
        self.data[record.name.value] = record

    def save_to_file(self, filename):
        data = {
            "records": {
                name: {
                    "name": record.name.value,
                    "phones": [phone.value for phone in record.phones],
                    "birthday": record.birthday.value if record.birthday else None
                }
                for name, record in self.data.items()
            }
        }
        with open(filename, "w") as f:
            json.dump(data, f, indent=4)

    def load_from_file(self, filename):
        try:
            with open(filename, "r") as f:
                data = json.load(f)
                for name, record_data in data.get("records", {}).items():
                    name_field = Name(record_data["name"])
                    phones = [Phone(phone) for phone in record_data["phones"]]
                    birthday = Birthday(record_data["birthday"]) if record_data["birthday"] else None
                    rec = Record(name_field, phones[0], birthday)
                    for phone in phones[1:]:
                        rec.add_phone(phone.value)
                    self.add_record(rec)
        except FileNotFoundError:
            pass

    def search(self, search_term):
        results = []
        for name, record in self.data.items():
            if search_term in name or any(search_term in phone.value for phone in record.phones):
                results.append(record)
        return results

if __name__ == "__main__":
    ab = AddressBook()
    ab.load_from_file("address_book.json")

    while True:
        print("1. Add Record")
        print("2. Search")
        print("3. Save")
        print("4. Save and Exit")

        choice = input("Enter your choice: ")
        if choice == "1":
            name = input("Enter name: ")
            phone = input("Enter phone number: ")
            while not Phone.validate_phone(phone):
                print("Invalid phone number format. Please enter 10 digits.")
                phone = input("Enter phone number: ")
            birthday = input("Enter birthday (YYYY-MM-DD, optional): ")
            while birthday and not Birthday.validate_date(birthday):
                print("Invalid date format. Please use YYYY-MM-DD format or leave empty.")
                birthday = input("Enter birthday (YYYY-MM-DD, optional): ")
            rec = Record(Name(name), Phone(phone), Birthday(birthday) if birthday else None)
            ab.add_record(rec)
        elif choice == "2":
            search_term = input("Enter search term: ")
            results = ab.search(search_term)
            if results:
                for result in results:
                    print("Name:", result.name.value)
                    print("Phone:", ", ".join(phone.value for phone in result.phones))
                    if result.birthday:
                        print("Birthday:", result.birthday.value)
                    print("-" * 20)
            else:
                print("No results found.")
        elif choice == "3":
            ab.save_to_file("address_book.json")
            print("Data saved.")
        elif choice == "4":
            ab.save_to_file("address_book.json")
            print("Data saved. Exiting...")
            break
