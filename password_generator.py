import random
import string

def generate_password(n_letters, n_symbols, n_numbers):
    letters = list(string.ascii_letters)   # a-z + A-Z
    numbers = list(string.digits)          # 0-9
    symbols = list(string.punctuation)     # !@#$%^&*...

    password_list = []
    for _ in range(n_letters):
        password_list.append(random.choice(letters))

    for _ in range(n_numbers):
        password_list.append(random.choice(numbers))

    for _ in range(n_symbols):
        password_list.append(random.choice(symbols))

    random.shuffle(password_list)

    password = ''.join(password_list)
    return password
