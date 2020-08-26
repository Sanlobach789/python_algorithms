# В одномерном массиве целых чисел определить два наименьших элемента.
# Они могут быть как равны между собой (оба являться минимальными), так и различаться.
import random

SIZE = 10
MIN_ITEM = 0
MAX_ITEM = 100
array = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]
print(array)
min_elem_1 = array[0]
min_elem_2 = array[0]

for i in array:
    if i <= min_elem_1:
        min_elem_1 = i

array.pop(array.index(min_elem_1))

for i in array:
    if i <= min_elem_2:
        min_elem_2 = i

print(f'{min_elem_1=} \n{min_elem_2=}')


#________________________________________________________________________________________________


