import re
from collections import UserDict

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
        # Перевірка, чи номер містить лише цифри та має довжину 10
        pattern = r"^\d{10}$"
        return re.match(pattern, phone) is not None

class Record:
    def __init__(self, name_value):
        self.name = Name(name_value)
        self.phones = []

    def add_phone(self, phone_value):
        phone = Phone(phone_value)
        self.phones.append(phone)

    def remove_phone(self, phone_index):
        if 0 <= phone_index < len(self.phones):
            del self.phones[phone_index]

    def edit_phone(self, phone_index, new_phone_value):
        if 0 <= phone_index < len(self.phones):
            self.phones[phone_index].value = new_phone_value

    def __str__(self):
        phones_str = ", ".join(str(phone) for phone in self.phones)
        return f"Name: {self.name}\nPhones: {phones_str}"

class AddressBook(UserDict):
    def add_record(self, record):
        self.data[record.name.value] = record

if __name__ == "__main__":
    name = Name('Bill')
    phone = Phone('1234567890')
    rec = Record(name.value)
    rec.add_phone(phone.value)
    ab = AddressBook()
    ab.add_record(rec)
    
    assert isinstance(ab['Bill'], Record)
    assert isinstance(ab['Bill'].name, Name)
    assert isinstance(ab['Bill'].phones, list)
    assert isinstance(ab['Bill'].phones[0], Phone)
    assert ab['Bill'].phones[0].value == '1234567890'
    
    print('All Ok)')
