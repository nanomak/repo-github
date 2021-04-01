# 1. Реализовать класс Matrix (матрица). Обеспечить перегрузку конструктора класса (метод __init__()),
# который должен принимать данные (список списков) для формирования матрицы.
# Подсказка: матрица — система некоторых математических величин, расположенных в виде прямоугольной схемы.
# Примеры матриц вы найдете в методичке.
# Следующий шаг — реализовать перегрузку метода __str__() для вывода матрицы в привычном виде.
# Далее реализовать перегрузку метода __add__() для реализации операции сложения двух объектов
# класса Matrix (двух матриц). Результатом сложения должна быть новая матрица.
# Подсказка: сложение элементов матриц выполнять поэлементно — первый элемент первой строки первой матрицы с
# кладываем с первым элементом первой строки второй матрицы и т.д.
import random


def arrays():
    return [[random.randint(0, 20) for i in range(2)] for j in range(3)]


class Matrix:
    def __init__(self, array):
        self.array = array
        print(self.array)

    def __str__(self):
        return '\n'.join(map(str, self.array))

    def __add__(self, other):
        sum_matrix = []
        for i in range(len(self.array)):
            sum_matrix.append([])
            for j in range(len(self.array[0])):
                sum_matrix[i].append(self.array[i][j] + other.array[i][j])
        return '\n'.join(map(str, sum_matrix))


matrix_1 = Matrix(arrays())
matrix_2 = Matrix(arrays())
sum_matr = matrix_1 + matrix_2
print(sum_matr)
