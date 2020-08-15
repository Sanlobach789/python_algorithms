#Найти сумму и произведение цифр трехзначного числа, которое вводит пользователь.
# https://drive.google.com/file/d/1juf_LBYRMuwNtwc7idRXalmPOXkdDQs6/view?usp=sharing

x = int(input("Введите трехзначное число х: "))
a = x // 100
b = x % 100 // 10
c = x % 10

print(f'{a=}, {b=}, {c=}')
sum = a + b + c
mult = a * b * c
print(f'Сумма={sum}')
print(f'Произведение={mult}')
