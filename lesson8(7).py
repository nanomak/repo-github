# 7. Реализовать проект «Операции с комплексными числами». Создайте класс «Комплексное число»,
# реализуйте перегрузку методов сложения и умножения комплексных чисел. Проверьте работу проекта,
# создав экземпляры класса (комплексные числа) и выполнив сложение и умножение созданных экземпляров.
# Проверьте корректность полученного результата.


class Complex_number:
    def __init__(self, a, b):
        self.a = a
        self.b = b
        print(f'{self.a}+ {self.b}i')

    def __add__(self, other):
        print(f'num_1 + num_2 = ')
        return f'{self.a + other.a} + {self.b + other.b}i'


    def __mul__(self, other):
        print(f'num_1 * num_2 =')
        return f'{self.a * other.a - (self.b * other.b)} + {self.a * other.b + (other.a * self.b)}i'


num_1 = Complex_number(1, 6)
num_2 = Complex_number(3, 4)
print(num_1 + num_2)
print(num_1 * num_2)
