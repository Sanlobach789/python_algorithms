from collections import deque

BASE = 16

HEX_NUMBERS = ('0', '1', '2', '3', '4', '5', '6', '7', '8', '9',
               'A', 'B', 'C', 'D', 'E', 'F')

DEC_NUMBERS = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5,
               '6': 6, '7': 7, '8': 8, '9': 9, 'A': 10, 'B': 11,
               'C': 12, 'D': 13, 'E': 14, 'F': 15}


def hex_to_dec(numb):
    x = 1
    result = []
    for i in numb:
        number = DEC_NUMBERS.get(i)
        degree = int(numb.__len__())
        result.append(number * BASE ** (degree - x))
        x += 1
    return sum(result)


def dec_to_hex(dec_numb):
    first_result = deque()
    result = []
    while dec_numb // BASE != 0:
        remainder = dec_numb % BASE
        first_result.appendleft(remainder)
        dec_numb = dec_numb // BASE
        if dec_numb // BASE == 0:
            first_result.appendleft(dec_numb)
    for i in first_result:
        result.append(HEX_NUMBERS.__getitem__(i))

    return result


a = deque(input('Введите первое число в hex формате (только цифры от 0 до f): ').upper())
b = deque(input('Введите первое число в hex формате (только цифры от 0 до f): ').upper())

a_dec = hex_to_dec(a)
b_dec = hex_to_dec(b)

summation = a_dec + b_dec
multiply = a_dec * b_dec

print(dec_to_hex(summation))
print(dec_to_hex(multiply))
