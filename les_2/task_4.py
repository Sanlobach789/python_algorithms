# 6. В программе генерируется случайное целое число от 0 до 100.
# Пользователь должен его отгадать не более чем за 10 попыток.
# После каждой неудачной попытки должно сообщаться, больше или меньше введенное
# пользователем число, чем то, что загадано.
# Если за 10 попыток число не отгадано, вывести правильный ответ.
import random

right_answer = int(random.random() * 100)
user_answer = ''
max_attempts = 11
attempts = 1
while attempts < max_attempts and user_answer != right_answer:
    user_answer = int(input('Введите загаданное число (попыток осталось - ' + str(max_attempts - attempts) + '): '))
    if user_answer > right_answer:
        print('Ваше число больше загаданного')
    elif user_answer < right_answer:
        print('Ваше число меньше загаданного')

    attempts += 1

if user_answer == right_answer:
    print('Вы угадали!!!')
else:
    print('Вы не угадали... правильный ответ - ' + str(right_answer))
