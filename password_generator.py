import random
import string

def password_generator(lenght=20, numbers=True, symbols=True):
    if numbers:
        slova = string.ascii_letters + string.digits
    else:
        slova = string.ascii_letters
    if numbers:
        slova = string.ascii_letters + string.punctuation
    else:
        slova = string.ascii_letters
    return ''.join(random.choices(slova, k=lenght))

if __name__ == '__main__':
    print(password_generator(30, True, True))