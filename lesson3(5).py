# 5. Программа запрашивает у пользователя строку чисел, разделенных пробелом.
# При нажатии Enter должна выводиться сумма чисел. Пользователь может продолжить
# ввод чисел, разделенных пробелом и снова нажать Enter. Сумма вновь введенных чисел
# будет добавляться к уже подсчитанной сумме. Но если вместо числа вводится специальный
# символ, выполнение программы завершается. Если специальный символ введен после нескольких
# чисел, то вначале нужно добавить сумму этих чисел к полученной
# ранее сумме и после этого завершить программу.


sum_number = 0
is_exit = False
while True:
    number = input("Введите последовательность целых чисел через пробел, для выхода q:").split()
    for item in number:
        if item == "q":
            is_exit = True
            break
        try:
            item = int(item)
        except ValueError:
            pass
        sum_number += item
    print("сумма:", sum_number)
    if is_exit:
        break


def sum_number():
    s = 0
    while True:
        number = input("Введите последовательность целых чисел через пробел, для выхода q:").split()
        for item in number:
            if item == 'q':
                return s
            else:
                try:
                    s += int(item)
                except ValueError:
                    pass
        print("Сумма чисел=", s)


print(sum_number())
