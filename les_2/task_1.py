# 2. Посчитать четные и нечетные цифры введенного натурального числа. Например, если
# введено число 34560, в нем 3 четные цифры (4, 6 и 0) и 2 нечетные (3 и 5).
#
x = int(input("Введите натуральное число: "))
evnumb_count = 0  # четные
oddnumb_count = 0  # нечетные

while x != 0:
    if (x % 10) % 2 == 0:
        evnumb_count += 1
    else:
        oddnumb_count += 1
    x //= 10

print(f'{evnumb_count=}, {oddnumb_count=}')
