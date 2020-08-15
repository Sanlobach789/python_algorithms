def func(x):
    if x // 10 == 0:
        return f'{x}'
    numb = x % 10
    return f'{numb}{func(x // 10)}'


y = int(input('Введите натуральное число: '))
print(func(y))
