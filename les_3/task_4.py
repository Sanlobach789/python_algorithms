#Определить, какое число в массиве встречается чаще всего.
import random

#SIZE = 10
#MIN_ITEM = 0
#MAX_ITEM = 100
#array = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]

array = [1, 2, 3, 4, 5, 1, 1, 3, 3, 5, 3, 3, 3, 8, 9, 9]

print(array)

count = 0
pos = 0

for i in array:
    if array.count(i) > count:
        count = array.count(i)
        pos = i

print(f'число с индексом {array.index(pos)} встречается {count} раз')

