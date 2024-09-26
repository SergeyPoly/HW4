from datetime import datetime
import re

date_pattern = r"^\d{4}-(0[1-9]|1[0-2])-(0[1-9]|[12]\d|3[01])$"

def is_date_valid (date: str) -> bool:
    return re.match(date_pattern, date)


def get_days_from_today(date: str) -> int:
    if is_date_valid(date):
        datetime_object = datetime.strptime(date, "%Y-%m-%d")
        current_datetime = datetime.today()
        difference = current_datetime - datetime_object

        return difference.days
    else:
       print("warning! this app supports YYYY-MM-DD format of date only")
       return 0

print(get_days_from_today('2023-11-20'))
print(get_days_from_today('2026-05-13'))
print(get_days_from_today('23-05-2019'))
