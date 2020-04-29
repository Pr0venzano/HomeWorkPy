# 1. Реализовать класс «Дата», функция-конструктор которого должна принимать дату в виде
# строки формата «день-месяц-год». В рамках класса реализовать два метода. Первый, с
# декоратором @classmethod, должен извлекать число, месяц, год и преобразовывать их тип к
# типу «Число». Второй, с декоратором @staticmethod, должен проводить валидацию числа,
# месяца и года (например, месяц — от 1 до 12). Проверить работу полученной структуры на
# реальных данных.


class Date:
    """Переводит дату в формате 'дд-мм-гггг' в число"""

    def __init__(self, day=0, month=0, year=0):
        self.day = day
        self.month = month
        self.year = year

    @staticmethod
    def check_date(date):
        """Валидация (проверка) корректности даты"""
        day, month, year = map(int, date.split('-'))
        if (month in {1, 3, 5, 7, 8, 10, 12} and day > 31 or  # 31 в месяце
            month in {4, 6, 9, 11} and day > 30 or  # 30 дней в месяце
            day > 28 and month == 2 and year % 4 == 0) or day > 29 and month == 2 and year % 4 != 0:
            print("Ошибка! Введена некорректная дата (число)")
        if month > 12:
            print("Ошибка! Введена некорректная дата (месяц)")

    @classmethod
    def str_to_int(cls, date):  # альтернативный способ обращения к переменной из конструктора не нашёл :(
        """Преобразование строковой записи к числовой"""
        day, month, year = map(int, (date.split('-')))
        print(f'Дата - {day}, месяц - {month}, год - {year}')


date_1 = Date.str_to_int('28-04-2020')
date_2 = Date.check_date('32-04-2020')
data_3 = Date.check_date('15-13-2020')


# 2 Создайте собственный класс-исключение, обрабатывающий ситуацию деления на нуль.
# Проверьте его работу на данных, вводимых пользователем. При вводе пользователем нуля в
# качестве делителя программа должна корректно обработать эту ситуацию и не завершиться с ошибкой.

class OwnError(Exception):  # собственный класс исключения, дожен быть обязательно потомком класса всех ошибок
    def __init__(self, txt):
        self.txt = txt


n = 100
while True:
    try:
        inp_data = int(input(f"Делимое {n}. Введите делитель: "))
        if inp_data == 0:
            raise OwnError("Ошибка: деление на ноль!")
        else:
            print(f'{n} / {inp_data} = {round(n / inp_data, 2)}')
        break
    except ValueError:  # Ошибка значения
        print("Ошибка: введено некорректное значение!")
    except OwnError as err:  # Наш собственный класс ошибки
        print(err)


# 3 Создайте собственный класс-исключение, который должен проверять содержимое списка на
# наличие только чисел. Проверить работу исключения на реальном примере. Необходимо
# запрашивать у пользователя данные и заполнять список только числами. Класс-исключение
# должен контролировать типы данных элементов списка.
# Примечание: длина списка не фиксирована. Элементы запрашиваются бесконечно, пока
# пользователь сам не остановит работу скрипта, введя, например, команду “stop”. При этом
# скрипт завершается, сформированный список с числами выводится на экран.
# Подсказка: для данного задания примем, что пользователь может вводить только числа и
# строки. При вводе пользователем очередного элемента необходимо реализовать проверку
# типа элемента и вносить его в список, только если введено число. Класс-исключение должен
# не позволить пользователю ввести текст (не число) и отобразить соответствующее
# сообщение. При этом работа скрипта не должна завершаться.


class OwnError(Exception):  # собственный класс исключения, дожен быть обязательно потомком класса всех ошибок
    def __init__(self, txt):
        self.txt = txt


print('Для выхода введите stop')
result = []
while True:
    try:
        inp_data = input("Введите значение:")
        if inp_data.lower() == 'stop':
            print(f"Итоговый список: {result}")
            break
        elif not inp_data.isdigit():  # по условию задачи есть только числа и только текст (текст с цифрами = текст)
            raise OwnError("Ошибка: введено не числовое значение, данные не будут добавлены в результат.")
        else:
            result.append(int(inp_data))
    except OwnError as err:  # Наш собственный класс ошибки
        print(err)


# 7 Реализовать проект «Операции с комплексными числами». Создайте класс «Комплексное число»,
# реализуйте перегрузку методов сложения и умножения комплексных чисел. Проверьте работу проекта,
# создав экземпляры класса (комплексные числа) и выполнив сложение и умножение созданных экземпляров.
# Проверьте корректность полученного результата.

def test():
    """ Тест - проверка корректности работы методов класса Complex"""
    print("#Test1 - ok" if str(dig_1 + dig_2) == str(complex(2, 5) + complex(5, -7)) else "#Test1 - fail")
    print("#Test2 - ok" if str(dig_1 * dig_2) == str(complex(2, 5) * complex(5, -7)) else "#Test2 - fail")


class Complex:
    def __init__(self, digit_1=0, digit_2=0):
        self.digit_1 = digit_1
        self.digit_2 = digit_2
        self.comp = complex(digit_1, digit_2)

    def __repr__(self):
        return f'{self.comp}'

    def __add__(self, other):
        return Complex(self.digit_1 + other.digit_1, self.digit_2 + other.digit_2)

    def __mul__(self, other):
        return Complex((self.digit_1 * other.digit_1) - (self.digit_2 * other.digit_2),
                       (self.digit_1 * other.digit_2) + (self.digit_2 * other.digit_1))


dig_1 = Complex(2, 5)
dig_2 = Complex(5, -7)
print(dig_1 + dig_2)
print(dig_1 * dig_2)
test()

# 4 Начните работу над проектом «Склад оргтехники». Создайте класс, описывающий склад. А
# также класс «Оргтехника», который будет базовым для классов-наследников. Эти классы —
# конкретные типы оргтехники (принтер, сканер, ксерокс). В базовом классе определить
# параметры, общие для приведенных типов. В классах-наследниках реализовать параметры,
# уникальные для каждого типа оргтехники.


class Warehouse:
    pass


class OfficeEquipment:
    def __init__(self, name, model):
        self.name = name
        self.model = model


class Printer(OfficeEquipment):
    def __init__(self, name, model, print_speed):
        super().__init__(name, model)  # вариант с урока
        # super(Printer, self).__init__(name, model)  # вариант, который предлагает PyCharm
        self.print_speed = print_speed


class Scaner(OfficeEquipment):
    def __init__(self, name, model, scan_speed):
        super().__init__(name, model)  # вариант с урока
        self.scan_speed = scan_speed


class Copier(OfficeEquipment):
    def __init__(self, name, model, copy_speed):
        super().__init__(name, model)  # вариант с урока
        self.copy_speed = copy_speed
