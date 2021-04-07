# 2. Создайте собственный класс-исключение, обрабатывающий ситуацию деления на нуль.
# Проверьте его работу на данных, вводимых пользователем. При вводе пользователем нуля в качестве
# делителя программа должна корректно обработать эту ситуацию и не завершиться с ошибкой.

class OwnZeroError(ZeroDivisionError):
    pass


a = int(input("Enter number a:"))
b = int(input("Enter number b:"))

try:
    res = a / b
    if a == 0 or b == 0:
        raise OwnZeroError

except OwnZeroError:
    print("Zero not allowed")

else:
    print(res)
