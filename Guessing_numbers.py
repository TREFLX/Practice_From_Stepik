import math
import random


print('Введите правую границу(маскимальное число)')
maxx =int(input())

hidden_number = random.randint(1,maxx+1)

number_ttempts = 0
print("Добро пожаловать в числовую угадайку")
def is_valid(a):
    if 1 < a < maxx:
        return True
    else:
        return False

while True:
    a = int(input())
    if is_valid(a) == False:
        print(f"А может быть все-таки введем целое число от 1 до {maxx}?")
        number_ttempts += 1
    else:
        if a < hidden_number:
            print("Ваше число меньше загаданного, попробуйте еще разок")
            number_ttempts+=1
        elif a > hidden_number:
            print('Ваше число больше загаданного, попробуйте еще разок')
            number_ttempts+=1
        elif a == hidden_number:
            print('Вы угадали, поздравляем!')
            print(f'Вы использовали {number_ttempts} попыток')
print('Спасибо, что играли в числовую угадайку. Еще увидимся...')
