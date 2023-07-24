from datetime import datetime, timedelta

def get_birthdays_per_week(users):
    # Отримуємо поточну дату та час
    current_date = datetime.now()
    
    # Рахуємо дату наступного понеділка
    next_monday = current_date + timedelta(days=(7 - current_date.weekday()))
    
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

    # Цикл для обробки кожного користувача
    for user in users:
        name = user.get('name')
        birthday = user.get('birthday')
        
        if name and birthday:
            # Перевіряємо, чи день народження є на наступному тижні
            next_birthday = birthday.replace(year=current_date.year)
            if next_birthday < current_date:
                next_birthday = next_birthday.replace(year=current_date.year + 1)
            
            # Визначаємо день тижня для дня народження
            birthday_weekday = next_birthday.weekday()
            day_of_week = days_of_week.get(birthday_weekday)

            # Якщо день народження був на вихідних, виводимо у понеділок
            if birthday_weekday >= 5:  # 5 - Saturday, 6 - Sunday
                day_of_week = 'Monday'

            # Додаємо користувача в словник під відповідним днем тижня
            birthdays_per_week[day_of_week].append(name)

    # Виводимо результат
    for day, users in birthdays_per_week.items():
        if users:
            print(f"{day}: {', '.join(users)}")


# Тестовий список users
users = [
    {"name": "Bill", "birthday": datetime(2023, 5, 17)},
    {"name": "Jill", "birthday": datetime(2023, 5, 17)},
    {"name": "Kim", "birthday": datetime(2023, 5, 20)},
    {"name": "Jan", "birthday": datetime(2023, 5, 21)},
]

# Викликаємо функцію з тестовим списком
get_birthdays_per_week(users)
