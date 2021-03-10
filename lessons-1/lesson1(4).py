# 4. Пользователь вводит целое положительное число. Найдите самую большую цифру в числе.
# Для решения используйте цикл while и арифметические операции.

number = int(input("Введите целое положительное число:"))
max_number = number % 10
num = number // 10
while num > 0:
    if num % 10 > max_number:
        max_number = num % 10
    num = num // 10
print(f'{max_number} самая большая цифра в числе {number}')

