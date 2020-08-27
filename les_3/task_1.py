# В диапазоне натуральных чисел от 2 до 99 определить,
# сколько из них кратны каждому из чисел в диапазоне от 2 до 9.

MIN_ITEM = 2
MAX_ITEM = 99
array = [i for i in range(MIN_ITEM, MAX_ITEM+1)]
print(array)
x = 2
y = 9

for i in range(x, y):
    count = 0
    for j in array:
        if j % i == 0:
            count += 1
    print(f'кратных {i}: {count}')
