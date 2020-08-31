import random
import sys


def deep_getsizeof(obj):
    sum_size = 0
    array = []
    try:
        iterator = iter(obj)
    except TypeError:
        sum_size += sys.getsizeof(obj)
    else:
        for i in obj:
            sum_size += sys.getsizeof(i)
    return sum_size



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
    return locals()


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

    return locals()


# вариант 3_______________________________________________________________________
def var_3(size):
    min_item = 0
    max_item = 100
    array = [random.randint(min_item, max_item) for _ in range(size)]

    min_1 = min(array)
    array.remove(min_1)
    min_2 = min(array)

    return locals()


sum_mem = 0


print(deep_getsizeof(var_1(100)))

print(deep_getsizeof(var_2(100)))

print(deep_getsizeof(var_3(100)))


