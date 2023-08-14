import re
from collections import UserDict

# Базовий клас для полів
class Field:
    def __init__(self, value=None):
        self.value = value

    def __str__(self):
        return str(self.value)

# Клас для імені з валідацією
class Name(Field):
    def __init__(self, value):
        super().__init__(value)
        if not self.validate_name(value):
            raise ValueError("Invalid name format")

    @staticmethod
    def validate_name(name):
        pattern = r"^[a-zA-Z']{2,}$"
        return re.match(pattern, name) is not None

# Клас для телефону з валідацією
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

# Клас для запису
class Record:
    def __init__(self, name, phone):
        self.name = name
        self.phones = [phone]

    def add_phone(self, phone_value):
        # Створюємо об'єкт телефону і передаємо значення в конструктор
        phone = Phone(phone_value)
        self.phones.append(phone)

    def remove_phone(self, phone_index):
        if 0 <= phone_index < len(self.phones):
            del self.phones[phone_index]

    def edit_phone(self, phone_index, new_phone_value):
        if 0 <= phone_index < len(self.phones):
            # Змінюємо значення телефону через об'єкт телефону
            self.phones[phone_index].value = new_phone_value

    def __str__(self):
        phones_str = ", ".join(str(phone) for phone in self.phones)
        return f"Name: {self.name}\nPhones: {phones_str}"

# Клас для адресної книги
class AddressBook(UserDict):
    def add_record(self, record):
        # Додаємо запис до словника, де ключ - це ім'я з об'єкта запису
        self.data[record.name.value] = record

if __name__ == "__main__":
    name = Name('Bill')
    phone = Phone('1234567890')
    rec = Record(name, phone)  # Передаємо об'єкти Name та Phone
    ab = AddressBook()
    ab.add_record(rec)
    
    assert isinstance(ab['Bill'], Record)
    assert isinstance(ab['Bill'].name, Name)
    assert isinstance(ab['Bill'].phones, list)
    assert isinstance(ab['Bill'].phones[0], Phone)
    assert ab['Bill'].phones[0].value == '1234567890'
    
    print('All Ok)')
