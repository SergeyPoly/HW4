from datetime import datetime, timedelta

def get_upcoming_birthdays (users: list) -> list:
    upcoming_birthdays = []
    current_date = datetime.today().date()
    current_year = datetime.now().year
    target_date = current_date + timedelta(days=7)

    for user in users:
        birth_date = datetime.strptime(user["birthday"], "%Y.%m.%d").date()
        birthday_this_year = birth_date.replace(year=current_year)
        
        if current_date <= birthday_this_year <= target_date:
            congratulation_info = {
                "name": user["name"], 
            }
            weekday = birthday_this_year.weekday()

            if weekday < 5:
                congratulation_info["congratulation_date"] = birthday_this_year.strftime("%Y.%m.%d")
            else:
                congratulation_info["congratulation_date"] = (birthday_this_year + timedelta(days=(7-weekday))).strftime("%Y.%m.%d")

            upcoming_birthdays.append(congratulation_info)
   
    return upcoming_birthdays

users = [
    {"name": "John Doe", "birthday": "1985.10.04"},
    {"name": "Jane Smith", "birthday": "1990.01.27"},
    {"name": "Max Brown", "birthday": "1995.10.03"},
    {"name": "Alex Drake", "birthday": "1998.09.29"}
]

upcoming_birthdays = get_upcoming_birthdays(users)
print("Список привітань на цьому тижні:", upcoming_birthdays)