#  2. Для списка реализовать обмен значений соседних элементов, т.е.
#  Значениями обмениваются элементы с индексами 0 и 1, 2 и 3 и т.д.
#  При нечетном количестве элементов последний сохранить на своем месте.
#  Для заполнения списка элементов необходимо использовать функцию input().

list_user = list(input('Введите список элементов:'))
j = 0
for i in range(int(len(list_user) / 2)):
    list_user[j], list_user[j + 1] = list_user[j + 1], list_user[j]
    j += 2
print(list_user)

list_user = list(input('Введите список элементов:'))
for i in range(1, len(list_user), 2):
    list_user[i - 1], list_user[i] = list_user[i], list_user[i - 1]
print(list_user)
