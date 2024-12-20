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

#3

def CallDate():
    def wrapper(*args):
        call_time = datetime.now()
        result = func(*args)
        print(f"Function '{func.__name__}' was called at {call_time}")
        print(f"Result: {result}")
        return {"name": func.__name__, "time": call_time, "result": result}
    return wrapper

@CallDate
def add_numbers(a, b):
    return a + b
    
#მაგალითი    
add_result = add_numbers(3, 4)
print(add_result)    

#4

import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLineEdit, QPushButton, QVBoxLayout

app = QApplication(sys.argv)

window = QWidget()
window.setWindowTitle("Simplified Example")
window.resize(500, 250)

text_input = QLineEdit()
text_input.setPlaceholderText("Type your name here...")

button = QPushButton("Submit")

layout = QVBoxLayout()
layout.addWidget(text_input)
layout.addWidget(button)

window.setLayout(layout)

window.show()

sys.exit(app.exec_())

