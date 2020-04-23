# 1.Создать класс TrafficLight (светофор) и определить у него один атрибут color ( цвет) и метод
# running (запуск). Атрибут реализовать как приватный. В рамках метода реализовать
# переключение светофора в режимы: красный, желтый, зеленый. Продолжительность первого
# состояния (красный) составляет 7 секунд, второго (желтый) — 2 секунды, третьего (зеленый)
# — на ваше усмотрение. Переключение между режимами должно осуществляться только в
# указанном порядке (красный, желтый, зеленый). Проверить работу примера, создав экземпляр
# и вызвав описанный метод.
# Задачу можно усложнить, реализовав проверку порядка режимов, и при его нарушении
# выводить соответствующее сообщение и завершать скрипт.

import time  # для осуществения временной задержки
import itertools as it


class TrafficLight:
    def __init__(self):
        # Фиксированный атрибут - словарь {Цвет: [задержка в сек., код цвета]}
        self.__color = {'Red': [7, '[31m'], 'Yellow': [2, '[33m'], 'Green': [5, '[32m']}

    def running(self):
        n = 1  # счетчик для остановки бесконечного цикла
        for i in it.cycle(self.__color):
            if n > 5:
                print('Night! TrafficLighter is off.')
                break
            # \033 - команда, управляющая цветом
            print(f'Color is \033{self.__color.get(i)[1]}{i}\033[0m (for {self.__color.get(i)[0]} sec)')
            time.sleep(self.__color.get(i)[0])
            n += 1


a = TrafficLight()  # экземпляр
a.running()  # вызов метода


# 2 Реализовать класс Road (дорога), в котором определить атрибуты: length (длина), width (ширина).
# Значения данных атрибутов должны передаваться при создании экземпляра класса.
# Атрибуты сделать защищенными. Определить метод расчета массы асфальта, необходимого
# для покрытия всего дорожного полотна. Использовать формулу: длина*ширина*масса
# асфальта для покрытия одного кв метра дороги асфальтом, толщиной в 1 см*число см
# толщины полотна. Проверить работу метода.
# Например: 20м*5000м*25кг*5см = 12500 т

class Road:
    def __init__(self, lenth, width):
        self._length = lenth
        self._width = width

    def mass_calculation(self):
        mass = int(input('Уточните массу асфальта (кг): '))
        thick = int(input('Уточните толщину полотна (см): '))
        print(f'{self._length}м*{self._width}м*{mass}кг*{thick}см = {int(self._length*self._width*mass*thick/1000)}т')


b = Road(20, 5000)
b.mass_calculation()


# 3 Реализовать базовый класс Worker (работник), в котором определить атрибуты: name,
# surname, position (должность), income (доход). Последний атрибут должен быть
# защищенным и ссылаться на словарь, содержащий элементы: оклад и премия, например,
# {"wage": wage, "bonus": bonus}. Создать класс Position (должность) на базе класса Worker.
# В классе Position реализовать методы получения полного имени сотрудника (get_full_name) и
# дохода с учетом премии (get_total_income) . Проверить работу примера на реальных данных
# (создать экземпляры класса Position , передать данные, проверить значения атрибутов,
# вызвать методы экземпляров).

class Worker:
    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {"wage": wage, "bonus": bonus}


class Position(Worker):
    def get_full_name(self):
        print(f'Сотрудник {self.name} {self.surname}')

    def get_total_income(self):
        print(f'Доход {int(self._income["wage"]) + int(self._income["bonus"])}')


c = Position("Кирилл", "Зю", "Врач", "30000", "80000")
c.get_full_name()
c.get_total_income()
print(c.position)

d = Position("Василий", "Дэ", "Уборщик", "15000", "3000")
d.get_full_name()
d.get_total_income()

# print(d.income)  # ошибка
print(d._income)  # доступ к защищённой переменной
