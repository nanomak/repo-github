# 1. Поработайте с переменными, создайте несколько, выведите на экран, запросите у пользователя
# несколько чисел и строк и сохраните в переменные, выведите на экран.

a = 1
print(a, type(a))
b = "Max"
print(b, type(b))
c = 1.5
print(c, type(c))
d = False
print(d, type(d))
some_list = [1, 2, a, b, c]
print(some_list, type(some_list))
some_tuple = (1, 2, some_list)
print(some_tuple, type(some_tuple))
some_dict = {'one': 1, 'two': 2}
print(some_dict, type(some_dict))
name = input('Введите имя пользователя:')
print(name, type(name))
numbers = input('Input some numbers:')
print(numbers, type(numbers))
string = input('Input some strings: ')
print(string, type(string))
