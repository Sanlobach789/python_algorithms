# Вводятся три разных числа. Найти, какое из них является средним (больше одного, но меньше другого)

a = int(input("Введите число a: "))
b = int(input("Введите число b: "))
c = int(input("Введите число c: "))

if a > b:
    if a < c:
        print("a - среднее число")
    elif b > c:
        print("b - среднее число")
    elif b < c:
        print("c - среднее число")
else:
    if a > c:
        print("a - среднее число")
    elif b > c:
        print("b - среднее число")
    elif b < c:
        print("c - среднее число")
