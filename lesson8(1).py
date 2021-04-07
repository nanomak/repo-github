# 1. Реализовать класс «Дата», функция-конструктор которого должна принимать дату в виде строки
# формата «день-месяц-год». В рамках класса реализовать два метода. Первый, с декоратором
# @classmethod, должен извлекать число, месяц, год и преобразовывать их тип к типу «Число».
# Второй, с декоратором @staticmethod, должен проводить валидацию числа, месяца и года
# (например, месяц — от 1 до 12). Проверить работу полученной структуры на реальных данных.

class Data:
    def __init__(self, data_str):
        self.data_str = data_str

    @classmethod
    def number(cls, data_str):
        return tuple(map(int, data_str.split('-')))

    @staticmethod
    def validator(data):
        if int(data[0]) > 31 or int(data[1]) > 12 or len(str(data[2])) != 4:
            print('Data  is not valid')
        else:
            print ('data is valid')



data = Data('30-10-2021')
print(Data.number(data.data_str))
Data.validator(Data.number(data.data_str))
