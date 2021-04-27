import random
import string

def password_generator(numbers, symbols, lenght):
    if numbers:
        slova = string.ascii_letters + string.digits
    else:
        slova = string.ascii_letters
    if symbols:
        slova = string.ascii_letters + string.punctuation
    else:
        slova = string.ascii_letters
    return ''.join(random.choices(slova, k=lenght))

if __name__ == '__main__':
    print(password_generator(True, True, 20))