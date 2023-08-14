import re
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
    def add_record(self, record):
        self.data[record.name.value] = record

if __name__ == "__main__":
    name = Name('Bill')
    phone = Phone('1234567890')
    birthday = Birthday('2000-05-20')
    rec = Record(name, phone, birthday)
    ab = AddressBook()
    ab.add_record(rec)

    assert isinstance(ab['Bill'], Record)
    assert isinstance(ab['Bill'].name, Name)
    assert isinstance(ab['Bill'].phones, list)
    assert isinstance(ab['Bill'].phones[0], Phone)
    assert isinstance(ab['Bill'].birthday, Birthday)

    print('All Ok)')
