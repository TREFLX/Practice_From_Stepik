import random

DIGITS = '0123456789'
LOWERCASE_LATTERS = 'abcdefghijklmnopqrstuvwxyz'
UPPERCASE_LATTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
PUNCTUATION = '!#$%&*+-=?@^_'
chars = ''

number_of_passwords_to_generate = int(input('Количество паролей:'))
password_length = int(input("Длина одного пароля:"))
numbers_act = input('Включать ли цифры 0123456789? (y/n)')
ABC_act = input('Включать ли прописные буквы ABCDEFGHIJKLMNOPQRSTUVWXYZ? (y/n)')
abc_act = input('Включать ли строчные буквы abcdefghijklmnopqrstuvwxyz? (y/n)')
ch_act = input('Включать ли символы !#$%&*+-=?@^_? (y/n)')
exc_act = input('Исключать ли неоднозначные символы il1Lo0O? (y/n)')


if numbers_act == 'y':
    chars += DIGITS
if ABC_act == 'y':
    chars += LOWERCASE_LATTERS
if abc_act == 'y':
    chars += UPPERCASE_LATTERS
if ch_act == 'y':
    chars += PUNCTUATION
if exc_act == 'y':
    for c in 'il1Lo0O':
        chars.replace(c,'')

def generate_password(password_length, chars):
    password = ''
    for j in range(password_length):
        password += random.choice(chars)
    print(password)

for g in range(number_of_passwords_to_generate):
    generate_password(password_length, chars)