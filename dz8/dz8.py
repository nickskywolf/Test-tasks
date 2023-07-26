from datetime import datetime, timedelta

def get_birthdays_per_week(users):
    current_date = datetime.now()
    
    next_monday = current_date + timedelta(days=(7 - current_date.weekday()))
    
    last_monday = current_date - timedelta(days=current_date.weekday())

    # Створюємо словник з днями тижня
    days_of_week = {
        0: 'Monday',
        1: 'Tuesday',
        2: 'Wednesday',
        3: 'Thursday',
        4: 'Friday',
        5: 'Saturday',
        6: 'Sunday'
    }

    # Створюємо порожні словники для кожного дня тижня
    birthdays_per_week = {day: [] for day in days_of_week.values()}
    current_week_birthdays = []
    next_week_birthdays = []
    last_week_birthdays = []

    # Цикл для обробки кожного користувача
    for user in users:
        name = user.get('name')
        birthday = user.get('birthday')
        
        if name and birthday:
            # Визначаємо день тижня для дня народження
            birthday_weekday = birthday.weekday()
            day_of_week = days_of_week.get(birthday_weekday)

            # Якщо день народження був на вихідних, переносимо в понеділок
            if birthday_weekday >= 5:  # 5 - Saturday, 6 - Sunday
                day_of_week = 'Monday'
            
            # Перевіряємо, чи день народження вже минув у поточному році
            next_birthday = birthday.replace(year=current_date.year)
            if next_birthday < current_date:
                if next_birthday >= last_monday and next_birthday < next_monday:
                    last_week_birthdays.append(f"{day_of_week}: {name}")
            elif next_birthday >= next_monday:
                next_week_birthdays.append(f"{day_of_week}: {name}")
            else:
                current_week_birthdays.append(f"{day_of_week}: {name}")
            
            # Додаємо користувача в словник під відповідним днем тижня
            birthdays_per_week[day_of_week].append(name)

    # Виводимо результат
    if last_week_birthdays:
        print("Пройшли")
        for birthday in last_week_birthdays:
            print(birthday)
        print()

    if current_week_birthdays:
        print("Поточний тиждень:")
        for birthday in current_week_birthdays:
            print(birthday)
        print()

    if next_week_birthdays:
        print("Наступний тиждень:")
        for birthday in next_week_birthdays:
            print(birthday)
        print()


# Оновлений тестовий список users
users = [
    {"name": "Last_0", "birthday": datetime(2023, 6, 19)},
    {"name": "Last_1", "birthday": datetime(2023, 6, 24)},
    {"name": "Last_week_0", "birthday": datetime(2023, 7, 18)},
    {"name": "Last_week_1", "birthday": datetime(2023, 7, 21)},
    {"name": "Bill_1", "birthday": datetime(2023, 7, 24)},
    {"name": "Jill_2", "birthday": datetime(2023, 7, 25)},
    {"name": "Kim_3", "birthday": datetime(2023, 7, 27)},
    {"name": "Ja_4", "birthday": datetime(2023, 7, 28)},
    {"name": "Jarvan_4", "birthday": datetime(2023, 7, 29)},
    {"name": "Orn_5", "birthday": datetime(2023, 8, 3)},
]

# Викликаємо функцію з оновленим тестовим списком
get_birthdays_per_week(users)
