# 1. Реализовать функцию, принимающую два числа (позиционные аргументы) и
# выполняющую их деление. Числа запрашивать у пользователя,
# предусмотреть обработку ситуации деления на ноль.

def div_fun(var_1, var_2):
    if var_1 != 0 and var_2 != 0:
        return round((var_1 / var_2), 2)
    else:
        return "Zero not allowed"


print(div_fun(float(input('enter first number:')), float(input('enter second number:'))))


def div_fun(var_1, var_2):
    try:
        var_1, var_2 = float(var_1), float(var_2)
        return round((var_1 / var_2), 2)
    except ZeroDivisionError:
        return "Zero not allowed"


print(div_fun(input('enter first number:'), input('enter second number:')))
