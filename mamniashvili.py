# 1)

from datetime import datetime

def days_from_birthday(birthdate):
    birthdate_obj = datetime.strptime(birthdate, "%Y-%m-%d")
    today = datetime.now()
    days_difference = (today - birthdate_obj).days
    return days_difference

#მაგალითი
my_birthday = "2000-12-20"
days_since_birthday = days_from_birthday(my_birthday)
print(f"Days since your birthday: {days_since_birthday}")

# 2)

def double_result(func):
    def wrapper(*args):
        result = func(*args)
        return result * 2
    return wrapper

@double_result
def add_numbers(a, b):
    return a + b

@double_result
def multiply_numbers(a, b):
    return a * b

#მაგალითი
print(add_numbers(3, 4))  # Output: 14
print(multiply_numbers(3, 4))  # Output: 24  
