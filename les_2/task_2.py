# 3. Сформировать из введенного числа обратное по порядку входящих в него цифр и
# вывести на экран. Например, если введено число 3486, надо вывести 6843.


def func(x):
    if x // 10 == 0:
        return f'{x}'
    numb = x % 10
    return f'{numb}{func(x // 10)}'


y = int(input('Введите натуральное число: '))
print(func(y))
