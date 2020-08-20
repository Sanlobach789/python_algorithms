# В массиве случайных целых чисел поменять местами минимальный и максимальный элементы.
import random

SIZE = 10
MIN_ITEM = 0
MAX_ITEM = 100
array = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]
print(array)

max_elem = array[0]
max_pos = 0
min_elem = array[0]
min_pos = 0
i = 0

while i < len(array):
    if array[i] > max_elem:
        max_elem = array[i]
        max_pos = i
    if array[i] < min_elem:
        min_elem = array[i]
        min_pos = i
    i += 1
array[max_pos], array[min_pos] = array[min_pos], array[max_pos]
print(str(max_elem) + '\n' + str(min_elem))
print(array)

#Знаю, что решение явно не оптимальное, скорее всего на уроке следующем будет разбор,
# и я запомню, как лучше)