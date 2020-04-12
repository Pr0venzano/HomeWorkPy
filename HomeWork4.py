# 1. Реализовать скрипт, в котором должна быть предусмотрена функция расчета заработной платы сотрудника.
# В расчете необходимо использовать формулу: (выработка в часах * ставка в час) + премия.
# Для выполнения расчета для конкретных значений необходимо запускать скрипт с параметрами.
from sys import argv

salary = lambda p, r, b: int(p) * int(r) + int(b)
""" расчитывает заработную плату: (выроботка * ставку + премия) и выводит результат на печать """

script_name, production, rate, bonus = argv
print('Имя скрипта: ', script_name)
print('Выроботка в часах: ', production)
print('Ставка в час: ', rate)
print('Премия: ', bonus)
print(f'Зарплата = {salary(int(production), int(rate), int(bonus))}')
