# Пользователь вводит данные о количестве предприятий, их наименования и прибыль за 4 квартал (т.е. 4 числа)
# для каждого предприятия. Программа должна определить среднюю прибыль (за год для всех предприятий) и
# отдельно вывести наименования предприятий, чья прибыль выше среднего и ниже среднего.
from collections import namedtuple

ent_count = int(input('Введите кол-во: прдеприятий: '))
QUART = 4
Enterprise = namedtuple('Enterprise', 'name, quarters, profit')
result_info = set()
total_profit = 0

for ent in range(1, ent_count+1):
    quarters = []
    name = input('Введите название предприятия: ')
    for i in range(1, QUART+1):
        quarters.append(int(input(f'Введите прибыль за {i} квартал: ')))
    profit = sum(i for i in quarters)
    ent_info = Enterprise(name=name, quarters=tuple(quarters), profit=profit)
    result_info.add(ent_info)
    print(f'Компания "{name}" суммарно заработала {profit} руб за отчетный период \n')
    total_profit += profit

ave_profit = total_profit/ent_count
print(f'Средняя прибыль составила {ave_profit}')

for j in result_info:
    if j.profit > ave_profit:
        print(f'Предприятие {j.name} получило прибыль выше среднего: {j.profit} ')
    elif j.profit < ave_profit:
        print(f'Предприятие {j.name} получило прибыль ниже среднего: {j.profit} ')