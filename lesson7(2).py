# 2. Реализовать проект расчета суммарного расхода ткани на производство одежды. Основная сущность
# (класс) этого проекта — одежда, которая может иметь определенное название. К типам одежды в этом проекте
# относятся пальто и костюм. У этих типов одежды существуют параметры: размер (для пальто) и рост (для костюма)
# . Это могут быть обычные числа: V и H, соответственно.
# Для определения расхода ткани по каждому типу одежды использовать формулы: для пальто (V/6.5 + 0.5),
# для костюма (2 * H + 0.3). Проверить работу этих методов на реальных данных.
# Реализовать общий подсчет расхода ткани. Проверить на практике полученные на этом уроке знания: реализовать
# абстрактные классы для основных классов проекта, проверить на практике работу декоратора @property.

from abc import ABC, abstractmethod


class Clothes(ABC):

    def __init__(self, param):
        self.param = param

    @property
    @abstractmethod
    def result(self):
        pass

    def __add__(self, other):
        return round(self.result + other.result)


class Coat(Clothes):

    @property
    def result(self):
        return self.param / 6.5 + 0.5


class Suite(Clothes):

    @property
    def result(self):
        return (self.param * 2 + 0.3)/100


coat = Coat(50)
suite = Suite(170)
print(coat + suite)
