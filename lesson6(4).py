# 4. Реализуйте базовый класс Car. У данного класса должны быть следующие
# атрибуты: speed, color, name, is_police (булево). А также методы: go, stop, turn(direction),
# которые должны сообщать, что машина поехала, остановилась, повернула (куда). Опишите несколько дочерних классов:
# TownCar, SportCar, WorkCar, PoliceCar. Добавьте в базовый класс метод show_speed, который должен показывать
# текущую скорость автомобиля. Для классов TownCar и WorkCar переопределите метод show_speed.
# При значении скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение о превышении скорости.
# Создайте экземпляры классов, передайте значения атрибутов. Выполните доступ к атрибутам, выведите результат.
# Выполните вызов методов и также покажите результат.

class Car:
    def __init__(self, name, color, speed, is_police=False):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police
        print(f'{self.name} {self.color} {self.speed}')

    def go(self):
        print(f'{self.name} go')

    def stop(self):
        print(f'{self.name}  stop')

    def turn(self, direction):
        print(f'{self.name} turn {"left" if direction == "left" else "right"}')

    def show_speed(self):
        print(f'The {self.name}  is moved at a speed {self.speed}')


class Towncar(Car):

    def show_speed(self):
        print(f'The {self.name} exeeds speed ' if self.speed > 60 else \
                  f'The {self.name} has speed {self.speed}')


class WorkCar(Car):

    def show_speed(self):
        print(f'The {self.name} exeeds speed if self.speed > 40 else'
              f'The {self.name} has speed {self.speed}')


class PoliceCar(Car):

    def __init__(self, name, color, speed, is_police=True):
        super().__init__(name, color, speed, is_police)


class SportCar(Car):
    pass




auto_1 = Towncar('Towncar', 'white', 70)
auto_1.show_speed()
auto_1.go()
auto_1.stop()
auto_1.turn('left')

auto_2 = SportCar('Sportcar', 'red', 120)
auto_2.go()
auto_2.show_speed()
auto_2.stop()
auto_2.turn('strait')

auto_4 = PoliceCar('Policecar', 'white', 90, True)
auto_4.go()
auto_4.show_speed()
auto_4.turn('right')
auto_4.stop()

auto_3 = WorkCar('Workcar', 'blue', 30)
auto_3.go()
auto_3.show_speed()
auto_3.stop()
auto_3.turn('left')
