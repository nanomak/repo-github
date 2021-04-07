# 4. Начните работу над проектом «Склад оргтехники». Создайте класс, описывающий склад.
# А также класс «Оргтехника», который будет базовым для классов-наследников. Эти классы —
# конкретные типы оргтехники (принтер, сканер, ксерокс). В базовом классе определить параметры,
# общие для приведенных типов. В классах-наследниках реализовать параметры, уникальные для каждого
# типа оргтехники.
# 5. Продолжить работу над первым заданием. Разработать методы, отвечающие за приём оргтехники на
# склад и передачу в определенное подразделение компании. Для хранения данных о наименовании и
# количестве единиц оргтехники, а также других данных, можно использовать любую подходящую структуру,
# например словарь.
# 6. Продолжить работу над вторым заданием. Реализуйте механизм валидации вводимых пользователем
# данных. Например, для указания количества принтеров, отправленных на склад, нельзя использовать
# строковый тип данных.
# Подсказка: постарайтесь по возможности реализовать в проекте «Склад оргтехники» максимум возможностей,
# изученных на уроках по ООП.

class Store:
    def __init__(self):
        self._dict = {}

    def add_to_store(self, orgtechnika):
        self._dict.setdefault(orgtechnika.group_name(), []).append(orgtechnika)

    def take_out_store(self, name, n):
        if self._dict[name]:
            self._dict.setdefault(name).pop(n)


class Orgtechnika:
    def __init__(self, name, price):
        self.name = name
        self.price = price
        self.group = self.__class__.__name__

    def group_name(self):
        return f'{self.group}'

    def __repr__(self):
        return f'{self.name} {self.price}'


class Printer(Orgtechnika):
    def __init__(self, name, price, color):
        super().__init__(name, price)
        self.color = color

    def __repr__(self):
        return f'{self.name} {self.price} {self.color}'

    def action(self):
        return 'Print'


class Scaner(Orgtechnika):
    def __init__(self, name, price, size):
        super().__init__(name, price)
        self.size = size

    def __repr__(self):
        return f'{self.name} {self.price} {self.size}'

    def action(self):
        return 'Scan'


class Xerox(Orgtechnika):
    def __init__(self, name, price, type):
        super().__init__(name, price)
        self.type = type

    def __repr__(self):
        return f'{self.name} {self.price} {self.type}'

    def action(self):
        return 'Copy'


store = Store()
scaner_1 = Scaner('hp', '2000', 'formatA4')
store.add_to_store(scaner_1)
scaner_2 = Scaner('hp', '3000', 'formatA4')
store.add_to_store(scaner_2)
xerox = Xerox('hp', '2000', 'color')
store.add_to_store(xerox)
printer = Printer('sony', '5000', 'color')
store.add_to_store(printer)
print(store._dict)
store.take_out_store('Scaner', 1)
print()
print(store._dict)

