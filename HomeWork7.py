# 1. Реализовать класс Matrix (матрица). Обеспечить перегрузку конструктора класса (метод __init__()),
# который должен принимать данные (список списков) для формирования матрицы.
# Подсказка: матрица — система некоторых математических величин, расположенных в виде прямоугольной схемы.
# Примеры матриц вы найдете в методичке.
# Следующий шаг — реализовать перегрузку метода __str__() для вывода матрицы в привычном виде.
# Далее реализовать перегрузку метода __add__() для реализации операции сложения двух объектов
# класса Matrix (двух матриц). Результатом сложения должна быть новая матрица. Подсказка: сложение элементов матриц
# выполнять поэлементно — первый элемент первой строки первой матрицы складываем с первым элементом первой строки
# второй матрицы и т.д.


class Matrix:
    def __init__(self, matrix):
        self.matrix = matrix

    def __add__(self, other):
        """Складывает 2 мартицы одинаковой размености"""
        result = []
        for i in range(len(self.matrix)):
            sum = []
            for j in range(len(self.matrix[i])):
                sum.append(self.matrix[i][j] + other.matrix[i][j])
            result.append(sum)
        return Matrix(result)

    def __str__(self):  # вывод в привычном в математике виде
        return '\n'.join([' '.join([str(i) for i in row]) for row in self.matrix])


matrix_1 = Matrix([[1, 2], [3, 4], [5, 6]])
matrix_2 = Matrix([[7, 8], [9, 10], [11, 12]])
print(f'Матрица1:\n{matrix_1}\n')
print(f'Матрица2:\n{matrix_2}\n')
print(f'Сумма матриц:\n{matrix_1 + matrix_2}\n')


# 2 Реализовать проект расчета суммарного расхода ткани на производство одежды.
# Основная сущность (класс) этого проекта — одежда, которая может иметь определенное название.
# К типам одежды в этом проекте относятся пальто и костюм. У этих типов одежды существуют параметры:
# размер (для пальто) и рост (для костюма). Это могут быть обычные числа: V и H, соответственно.
# # Для определения расхода ткани по каждому типу одежды использовать формулы: для пальто (V/6.5 + 0.5),
# для костюма (2 * H + 0.3). Проверить работу этих методов на реальных данных.
# # Реализовать общий подсчет расхода ткани. Проверить на практике полученные на этом уроке знания:
# реализовать абстрактные классы для основных классов проекта, проверить на практике работу декоратора @property.

from abc import ABC, abstractmethod


class Wear (ABC):
    def __init__(self, length):
        self.length = length

    @abstractmethod
    def fabric(self):
        pass

    def __add__(self, other):
        return f'Всего требуется {round(self.length / 6.5 + 0.5) + round(2 * other.length + 0.3)}м ткани'


class Coat(Wear):
    @property
    def fabric(self):
        return f'Для пошива пальто требуется {round(self.length / 6.5 + 0.5)}м ткани'


class Costume(Wear):
    @property
    def fabric(self):
        return f'Для пошива костюма требуется {round(2 * self.length + 0.3)}м ткани'


coat = Coat(10)
costume = Costume(2)
print(coat.fabric)
print(costume.fabric)
print(coat + costume)


# 3 Реализовать программу работы с органическими клетками, состоящими из ячеек. Необходимо создать класс Клетка.
# В его конструкторе инициализировать параметр, соответствующий количеству ячеек клетки (целое число).
# В классе должны быть реализованы методы перегрузки арифметических операторов: сложение (__add__()),
# вычитание (__sub__()), умножение (__mul__()), деление (__truediv__()) . Данные методы должны применяться только к
# клеткам и выполнять увеличение, уменьшение, умножение и целочисленное (с округлением до целого) деление клеток,
# соответственно.
# Сложение. Объединение двух клеток. При этом число ячеек общей клетки должно равняться
# сумме ячеек исходных двух клеток.
# Вычитание. Участвуют две клетки. Операцию необходимо выполнять только если разность
# количества ячеек двух клеток больше нуля, иначе выводить соответствующее сообщение.
# Умножение. Создается общая клетка из двух. Число ячеек общей клетки определяется как
# произведение количества ячеек этих двух клеток.
# Деление. Создается общая клетка из двух. Число ячеек общей клетки определяется как
# целочисленное деление количества ячеек этих двух клеток.
# В классе необходимо реализовать метод make_order(), принимающий экземпляр класса и
# количество ячеек в ряду. Данный метод позволяет организовать ячейки по рядам.
# Метод должен возвращать строку вида * ****\n*****\n*****..., где количество ячеек между \n
# равно переданному аргументу. Если ячеек на формирование ряда не хватает, то в последний
# ряд записываются все оставшиеся.
# Например, количество ячеек клетки равняется 12, количество ячеек в ряду — 5. Тогда метод
# make_order() вернет строку: *****\n*****\n** .
# Или, количество ячеек клетки равняется 15, количество ячеек в ряду — 5. Тогда метод
# make_order() вернет строку: *****\n*****\n***** .

class Cell:
    def __init__(self, cells_num):
        self.cells_num = cells_num

    def make_order(self, cells_row):
        return '\n'.join(['*' * cells_row for i in range(self.cells_num // cells_row)]) + '\n' + '*' * (self.cells_num % cells_row)

    def __add__(self, other):
        return f'Сумма клеток = {self.cells_num + other.cells_num}'

    def __sub__(self, other):
        return f'Разность клеток = {self.cells_num - other.cells_num}' if self.cells_num - other.cells_num > 0 else \
            f'Операция невозможа! Во второй ячейке клеток {other.cells_num} больше, чем в первой {self.cells_num}.'

    def __mul__(self, other):
        return f'Произведение клеток = {self.cells_num * other.cells_num}'

    def __truediv__(self, other):
        return f'Частное клеток = {round(self.cells_num / other.cells_num)}'


cell_1 = Cell(2)
cell_2 = Cell(5)
print(cell_1 + cell_2)
print(cell_1 - cell_2)
print(cell_2 - cell_1)
print(cell_1 * cell_2)
print(cell_2 / cell_1)
print(cell_2.make_order(2))
print(cell_2.make_order(3))