import random

def is_data_valid (min: int, max: int, quantity: int) -> bool:
    return min >= 1 and max <= 1000 and (quantity >= min and quantity <= max)

def get_numbers_ticket(min: int, max: int, quantity: int) -> list:
    list = []

    if is_data_valid(min, max, quantity):
        while len(list) < quantity:
            picked_number = random.randint(min, max)
            if picked_number not in list:
                list.append(picked_number)

    list.sort()    
    return list

print("Ваші лотерейні числа:", get_numbers_ticket(1, 100, 7))
print("Ваші лотерейні числа:", get_numbers_ticket(1, 1001, 7))