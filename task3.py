import re

def add_prefix (phone_number: str, country_code: str = "38") -> str:
    pattern = rf"^{re.escape(country_code)}"

    if re.match(r"^\+", phone_number):
        return phone_number

    if re.match(pattern, phone_number):
        return "+" + phone_number
    
    return "+" + country_code + phone_number

def normalize_phone (phone_number: str) -> str:
    cleaned_phone = re.sub(r"[^+\d]", "", phone_number)
    phone_with_prefix = add_prefix(cleaned_phone)

    return phone_with_prefix

raw_numbers = [
    "067\\t123 4567",
    "(095) 234-5678\\n",
    "+380 44 123 4567",
    "380501234567",
    "    +38(050)123-32-34",
    "     0503451234",
    "(050)8889900",
    "38050-111-22-22",
    "38050 111 22 11   ",
]

sanitized_numbers = [normalize_phone(num) for num in raw_numbers]
print("Нормалізовані номери телефонів для SMS-розсилки:", sanitized_numbers)
