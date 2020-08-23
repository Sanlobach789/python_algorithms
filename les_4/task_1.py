# В одномерном массиве целых чисел определить два наименьших элемента.
# Они могут быть как равны между собой (оба являться минимальными), так и различаться.
import random
import timeit


# вариант 1___________________________________________________________________
def var_1(size):
    min_item = 0
    max_item = 100
    array = [random.randint(min_item, max_item) for _ in range(size)]

    min_elem_1 = array[0]
    min_elem_2 = array[0]

    for i in array:
        if i <= min_elem_1:
            min_elem_1 = i

    array.pop(array.index(min_elem_1))

    for i in array:
        if i <= min_elem_2:
            min_elem_2 = i
    return print(f'{min_elem_1=} \n{min_elem_2=}')


# вариант 2_________________________________________________________________
def var_2(size):
    min_item = 0
    max_item = 100
    array = [random.randint(min_item, max_item) for _ in range(size)]

    min_first, min_second = (0, 1) if array[0] < array[1] else (1, 0)

    for i in range(2, len(array)):
        if array[i] < array[min_first]:
            spam = min_first
            min_first = i
            if array[spam] < array[min_second]:
                min_second = spam
            elif array[i] < array[min_second]:
                min_second = i

    return print(f'Число {array[min_first]} в ячейке {min_first} \n Число {array[min_second]} в ячейке {min_second}')


# вариант 3_______________________________________________________________________
def var_3(size):
    min_item = 0
    max_item = 100
    array = [random.randint(min_item, max_item) for _ in range(size)]

    min_1 = min(array)
    array.remove(min_1)
    min_2 = min(array)
    print(min_1, min_2)


# print(timeit.timeit('var_1(1000)', number=1000, globals=globals())) # 0.6325255 (1000 элементов массива)
# print(timeit.timeit('var_1(2000)', number=1000, globals=globals())) # 1.2709323 (2000 элементов массива)
# print(timeit.timeit('var_1(4000)', number=1000, globals=globals())) # 2.4411326 (4000 элементов массива)

# print(timeit.timeit('var_2(1000)', number=1000, globals=globals()))   # 0.6516306000000001 (1000 элементов массива)
# print(timeit.timeit('var_2(2000)', number=1000, globals=globals()))   # 1.2838705 (2000 элементов массива)
# print(timeit.timeit('var_2(4000)', number=1000, globals=globals()))   # 2.5094061 (4000 элементов массива)


# print(timeit.timeit('var_3(1000)', number=1000, globals=globals()))   # 0.6217686 (1000 элементов массива)
# print(timeit.timeit('var_3(2000)', number=1000, globals=globals()))   # 1.2398569 (2000 элементов массива)
# print(timeit.timeit('var_3(4000)', number=1000, globals=globals()))     # 2.4339030000000004 (4000 элементов массива)


# ВЫВОД. Наиболее оптимальный вариант кода - var_3 (с использованием встроенной функции).
# Преимущества: наиболее быстрое время выполнения, наиболее простой/читабельный код.