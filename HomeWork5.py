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

