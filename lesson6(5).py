# 5. Реализовать класс Stationery (канцелярская принадлежность). Определить в нем атрибут title
# (название) и метод draw (отрисовка). Метод выводит сообщение “Запуск отрисовки.” Создать три дочерних
# класса Pen (ручка), Pencil (карандаш), Handle (маркер). В каждом из классов реализовать переопределение
# метода draw. Для каждого из классов методы должен выводить уникальное сообщение. Создать экземпляры классов
# и проверить, что выведет описанный метод для каждого экземпляра.


class Stationery:
    stationery_title = 'title'

    def draw(self):
        print('Запуск отрисовки')


class Pen(Stationery):
    def draw(self):
        print('Отрисовка карандашом')


class Pencil(Stationery):
    def draw(self):
        print('Отрисовка ручкой')


class Handle(Stationery):
    def draw(self):
        print('Отрисовка маркером')


pen_1 = Stationery()
pen_1.draw()

pen_2 = Pen()
pen_2.draw()

pen_3 = Pencil()
pen_3.draw()

pen_4 = Handle()
pen_4.draw()


class Stationery:
    def __init__(self, title):
        self.title = title

    def draw(self):
        print('Запуск отрисовки')


class Pen(Stationery):
    def draw(self):
        print(f'Отрисовка карандашом {self.title}')


class Pencil(Stationery):
    def draw(self):
        print(f'Отрисовка ручкой {self.title}')


class Handle(Stationery):
    def draw(self):
        print(f'Отрисовка маркером {self.title}')


pen_1 = Stationery('Parker')
pen_1.draw()

pen_2 = Pen('Parker')
pen_2.draw()

pen_3 = Pencil('Parker')
pen_3.draw()

pen_4 = Handle('Parker')
pen_4.draw()
