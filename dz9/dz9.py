# Декоратор для обробки помилок введення користувача
def input_error(func):
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except KeyError as e:
            return f"Error: Contact '{e.args[0]}' not found. Please check the name and try again."
        except ValueError as e:
            return "Error: Invalid input format. Please provide both name and phone number separated by a space."
        except IndexError:
            return "Error: Please provide both name and phone number separated by a space."
    return wrapper

# Функція для додавання контакту
@input_error
def add_contact(data):
    name, phone = data.split(' ')
    contacts[name] = phone
    return f"Contact '{name}' with phone '{phone}' has been added."

# Функція для зміни номера телефону існуючого контакту
@input_error
def change_phone(data):
    name, phone = data.split(' ')
    if name not in contacts:
        raise KeyError(name)
    contacts[name] = phone
    return f"Phone number for '{name}' has been changed to '{phone}'."

# Функція для виведення номера телефону контакту
@input_error
def show_phone(data):
    name = data
    if name not in contacts:
        raise KeyError(name)
    return f"Phone number for '{name}' is '{contacts[name]}'."

# Функція для виведення всіх контактів
def show_all():
    if not contacts:
        return "The contact list is empty."
    result = "\n".join(f"{name}: {phone}" for name, phone in contacts.items())
    return result

# Основна функція для взаємодії з користувачем
def main():
    print("How can I help you?")
    while True:
        command = input().lower()
        if command in {"good bye", "close", "exit"}:
            print("Good bye!")
            break
        elif command == "hello":
            print("How can I help you?")
        elif command.startswith("add"):
            print(add_contact(command[4:]))
        elif command.startswith("change"):
            print(change_phone(command[7:]))
        elif command.startswith("phone"):
            print(show_phone(command[6:]))
        elif command == "show all":
            print(show_all())
        else:
            print("Invalid command. Please try again.")

# Зберігаємо контакти в словнику
contacts = {}

# Запускаємо бота
if __name__ == "__main__":
    main()
