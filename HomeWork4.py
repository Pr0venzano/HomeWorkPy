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


# 2. Представлен список чисел. Необходимо вывести элементы исходного списка,
# значения которых больше предыдущего элемента.
# Подсказка: элементы, удовлетворяющие условию, оформить в виде списка. Для формирования списка использовать генератор.

numbers = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]  # Пример исходного списка
print(list(numbers[el] for el in range(1, len(numbers)) if numbers[el] > numbers[el-1]))  # [12, 44, 4, 10, 78, 123]


# 3. Для чисел в пределах от 20 до 240 найти числа, кратные 20 или 21. Необходимо решить задание в одну строку.
# Подсказка: использовать функцию range() и генератор.

print(list(number for number in range(20, 240) if number % 20 == 0 or number % 21 == 0))  # 240 не включительно


# 4. Представлен список чисел. Определить элементы списка, не имеющие повторений.
# Сформировать итоговый массив чисел, соответствующих требованию.
# Элементы вывести в порядке их следования в исходном списке.
# Для выполнения задания обязательно использовать генератор.

numbers_2 = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]  # Пример исходного списка
print(list(number for number in numbers_2 if numbers_2.count(number) == 1))  # [23, 1, 3, 10, 4, 11]
