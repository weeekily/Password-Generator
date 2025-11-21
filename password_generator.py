import string
import random

letters = list(string.ascii_letters)  # a-z + A-Z
numbers = list(string.digits)  # 0-9
symbols = list(string.punctuation)  # svi

print("Welcome to Password Generator!")
n_letters = int(input("How many letters would your like in your password?\n"))
n_symbols = int(input("How many symbols would you like?\n"))
n_numbers = int(input("How many numbers would you like?\n"))

password_list = []

for char in range(1, n_letters + 1):
    password_list.append(random.choice(letters))

for num in range(1, n_numbers + 1):
    password_list.append(random.choice(numbers))

for sym in range(1, n_symbols + 1):
    password_list.append(random.choice(symbols))

random.shuffle(password_list)

password = ""
for char in password_list:
    password += char

print(f"You new password is: {password}")












