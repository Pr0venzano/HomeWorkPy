# 1. Реализовать функцию, принимающую два числа (позиционные аргументы) и выполняющую их деление.
# Числа запрашивать у пользователя, предусмотреть обработку ситуации деления на ноль.


def division(a, b):
    """ Функция принимает 2 числа и возвращает результат их деления.
        При делении на 0 выводит соответствующее сообщение.
    """
    try:
        print(f'Результат деления: {a / b}')
    except ZeroDivisionError:
        print("На ноль делить нельзя!")


division(float(input("Введите делимое: ")), float(input("Введите делитель: ")))


# 2. Реализовать функцию, принимающую несколько параметров, описывающих данные пользователя:
# имя, фамилия, год рождения, город проживания, email, телефон.
# Функция должна принимать параметры как именованные аргументы.
# Реализовать вывод данных о пользователе одной строкой.


def user_info(**kwargs):
    """ Принимает любое количество именованных параметров (информация о пользователе: имя, фамилия,
        год рождения, город проживания, email, телефон) и выводит их на печать в хдвух вариантах:
        1 - в виде словаря ключ-значение
        2 - в виде строки значений
    """
    print(kwargs)  # через словарь

    result = ""  # через строку
    for key in kwargs:
        result += f'{kwargs.get(key)} '  # значение по каждому ключу преобразовать в строку и добавить в результат
    print(result)


user_info(first_name='Ivan', second_name='Petrov', year=1970, city='USSR', email='i_petrov@mail.ru', phone_number=123)


# # 3. Реализовать функцию my_func(), которая принимает три позиционных аргумента
# и возвращает сумму наибольших двух аргументов.

my_func = lambda a, b, c: a + b + c - min(a, b, c)  # через lambda-функцию, как доп требование к задаче
""" Сумирует два наимбольших числа из трёх, путём вычитания наименьшего числа из общей суммы """
print(my_func(30, 10, 20))


# 4. Программа принимает действительное положительное число x и целое отрицательное число y.
# Необходимо выполнить возведение числа x в степень y. Задание необходимо реализовать в виде функции
# my_func(x, y). При решении задания необходимо обойтись без встроенной функции возведения числа в степень.
# Подсказка: попробуйте решить задачу двумя способами:
# Первый — возведение в степень с помощью оператора **.
# Второй — более сложная реализация без оператора **, предусматривающая использование цикла.


def exponentiation(x, y, n):
    """ Принимает действительное положительное число X, целое отрицательное число Y
        и число N - как вариант вычисления. Возводит X в степень Y.
        Варианты вычислений:
        1 - при помощи оператора **
        2 - альтернативны способ при помощи оператора **
        3 - через цикл
    """
    if n == 1:
        return x ** y  # через **
    elif n == 2:
        return 1 / (x ** abs(y))  # альтернативный вариант через **
    elif n == 3:
        result = 1  # через цикл
        for i in range(abs(y)):
            result = result * x
        return 1 / result
    # elif n == 4:
    #     return x.pow(y)  # через pow(), если бы X был целым числом


# без проверок вводимых данных
a_float = float(input('Введите действительное положительное число: '))
b_int = int(input('Введите целое отрецательное число: '))

variant = ''
while variant != 'q':
    variant = (input('\nВведите вариант вычисления:\n'
                     '1 - при помощи оператора **\n'
                     '2 - альтернативны способ при помощи оператора **\n'
                     '3 - через цикл\n'
                     'для выхода выведите q: '))
    if variant == 'q':
        break
    elif 1 <= int(variant) <= 3:
        print(f'\n{a_float} в степени {b_int} = {exponentiation(a_float, b_int, int(variant))}')
    else:
        print('Введено некорректное значение')
