# 3. Реализовать функцию my_func(), которая принимает три позиционных аргумента,
# и возвращает сумму наибольших двух аргументов.


def my_func(my_var1, my_var2, my_var3):
    my_list = [my_var1, my_var2, my_var3]
    try:
        my_list.remove(min(my_list))
        print(sum(my_list))
    except TypeError:
        return "Enter number"


my_func(5, 4, 10)
