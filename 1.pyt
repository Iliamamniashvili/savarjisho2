from datetime import datetime

def days_from_birthday(birthdate):
    birthdate_obj = datetime.strptime(birthdate, "%Y-%m-%d")
    today = datetime.now()
    days_difference = (today - birthdate_obj).days
    return days_difference

//მაგალითი
my_birthday = "2000-12-20"
days_since_birthday = days_from_birthday(my_birthday)
print(f"Days since your birthday: {days_since_birthday}")
