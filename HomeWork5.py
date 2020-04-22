#  1 Создать программно файл в текстовом формате, записать в него построчно данные, вводимые пользователем.
#  Об окончании ввода данных свидетельствует пустая строка.

with open("new_file.txt", "w") as new_f:  # открыть файл на запись, если файла нет - создать новый
    print('Введите строки для зхаписи в файл')
    print('Для выхода введите q')
    while True:
        text = input()
        if text == 'q':
            break
        new_f.write(f'{text}\n')  # запись одной строки в файл


# 2 Создать текстовый файл (не программно), сохранить в нем несколько строк,
# выполнить подсчет количества строк, количества слов в каждой строке.

with open('for_HomeWork5_task_2.txt', encoding='utf-8') as f_2:  # открыть уже существующий файл для чтения
    content = f_2.read().split('\n')
    if len(content) == 1:
        print(f'Файл {f_2.name} пустой')
    else:
        print(f'Количество строк в файле {f_2.name} = {len(content)}')
        for i in range(len(content)):
            print(f'Количество слов в {i+1}-й строке = {len(content[i].split(" "))}')


# 3 Создать текстовый файл (не программно), построчно записать фамилии сотрудников и величину их окладов.
# Определить, кто из сотрудников имеет оклад менее 20 тыс., вывести фамилии этих сотрудников.
# Выполнить подсчет средней величины дохода сотрудников.

with open('text_3.txt', encoding='utf-8') as t_2:
    while True:
        content = t_2.read()
        if not content:
            break
        print(f'Список всех сотрудников и их зарплата:\n{content}\n')
        content_list = content.split('\n')
        print("Список сотрудников с зарплатой < 20'000: ")
        result = 0
        count = 0
        for i in content_list:
            el = (i.split(' '))
            if float(el[1]) < 20000:
                print(el[0])
            result += float(el[1])
            count += 1
        print(f'\nСредний доход сотрудников = {result/count}')


# 4 Создать (не программно) текстовый файл со следующим содержимым:
# One — 1
# Two — 2
# Three — 3
# Four — 4
# Необходимо написать программу, открывающую файл на чтение и считывающую построчно
# данные. При этом английские числительные должны заменяться на русские. Новый блок строк
# должен записываться в новый текстовый файл.

from googletrans import Translator  # модуль гугл переводчика

with open("text_4.txt", encoding='utf-8') as t_4:  # открыть существующий файл на чтение
    content = t_4.readlines()  # прочитать содержимое файла
    translator = Translator()  # создать переменную типа translator
    for i in content:
        result = translator.translate(i, src='en', dest='ru')  # перевод текста с eng на rus
        with open("text_4ru.txt", "a", encoding='utf-8') as t_4ru:  # открыть (или создать) файл на дозапись
            print(f'{result.text}\n', file=t_4ru)  # печать в файл 2 перевод текста файла 1

# Альтернативное решение
from googletrans import Translator  # модуль гугл переводчика

with open("text_4ru.txt", "w", encoding='utf-8') as t_4ru:
    with open("text_4.txt", encoding='utf-8') as t_4:
        text = t_4.read()
    t_4ru .write(Translator().translate(text, dest='ru'))


# 5 Создать (программно) текстовый файл, записать в него программно набор чисел, разделенных пробелами.
# Программа должна подсчитывать сумму чисел в файле и выводить ее на экран.

from random import randint  # набор чисел будет создан через генератор случайных чисел

result = 0
with open("text_5.txt", 'w') as t_5:  # Открыть (создать) файл на запись
    for i in list(randint(0, 10) for number in range(5)):  # каждый элемент из генерации чисел
        t_5.write(f'{i} ')  # записать через пробел в файл
        result += i  # сразу счиатать сумму записываемых чисел
        print(result)  # результат суммирования выводить печать


# 6 Необходимо создать (не программно) текстовый файл, где каждая строка описывает учебный
# предмет и наличие лекционных, практических и лабораторных занятий по этому предмету и их
# количество. Важно, чтобы для каждого предмета не обязательно были все типы занятий.
# Сформировать словарь, содержащий название предмета и общее количество занятий по нему. Вывести словарь на экран.
# Примеры строк файла:
# Информатика: 100(л) 50(пр) 20(лаб).
# Физика: 30(л) — 10(лаб)
# Физкультура: — 30(пр) —
# Пример словаря: {“Информатика”: 170, “Физика”: 40, “Физкультура”: 30}

with open('text_6.txt', encoding='utf-8') as t_6:
    content = t_6.read().split('\n')
    result = {}
    for i in content:
        key, value = (i.split(':')[0]), (i.split(':')[1])  # выделение ключа и значения
        digits_only = ''.join((dig if dig in '1234567890' else ' ') for dig in value)  # str, замена не цифр на пробел
        numbers_value = [int(i) for i in digits_only.split()]  # генерация списка чисел из сроки, разделитель - пробел
        result.update({key: sum(numbers_value)})
    print(result)


# 7 Создать вручную и заполнить несколькими строками текстовый файл, в котором каждая
# строка должна содержать данные о фирме: название, форма собственности, выручка, издержки.
# Пример строки файла: firm_1 ООО 10000 5000.
# Необходимо построчно прочитать файл, вычислить прибыль каждой компании, а также среднюю прибыль.
# Если фирма получила убытки, в расчет средней прибыли ее не включать. Далее реализовать список.
# Он должен содержать словарь с фирмами и их прибылями, а также словарь со средней прибылью.
# Если фирма получила убытки, также добавить ее в словарь (со значением убытков).
# Пример списка: [{“firm_1”: 5000, “firm_2”: 3000, “firm_3”: 1000}, {“average_profit”: 2000}].
# Итоговый список сохранить в виде json-объекта в соответствующий файл.
# Пример json-объекта: [{ "firm_1" : 5000 , "firm_2" : 3000 , "firm_3" : 1000 }, { "average_profit" : 2000 }]
# Подсказка: использовать менеджер контекста.

import json

with open('text_7.txt', encoding='utf-8') as t_7:
    while True:
        content = t_7.read()  # построчное чтение файла через while
        count = 0
        result = {}
        profit_sum = 0
        average_profit = 0
        if not content:
            break
        for i in content.split('\n'):
            key = f'{i.split(" ")[0]} {i.split(" ")[1]}'
            profit = int(i.split(" ")[2]) - int(i.split(" ")[3])  # выручка - издержки
            result.update({key: profit})
            if profit > 0:
                count += 1
                profit_sum += profit
                average_profit = profit_sum/count
            result_list = [result, {'average_profit': average_profit}]
            with open("text_7.json", 'w', encoding="utf-8") as t_7j:
                json.dump(result_list, t_7j, ensure_ascii=False, indent=4)
        print(result_list)  # вывод результата программы на печать
