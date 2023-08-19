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
    def __init__(self, chunk_size=10):
        super().__init__()
        self.chunk_size = chunk_size

    def add_record(self, record):
        self.data[record.name.value] = record

    def __iter__(self):
        self._iter_index = 0
        self._keys_chunked = list(self.data.keys())
        return self

    def __next__(self):
        if self._iter_index < len(self._keys_chunked):
            chunk = self._keys_chunked[self._iter_index : self._iter_index + self.chunk_size]
            records = [self.data[key] for key in chunk]
            self._iter_index += self.chunk_size
            return records
        else:
            raise StopIteration

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
