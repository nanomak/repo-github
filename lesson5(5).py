# 5. Создать (программно) текстовый файл, записать в него программно набор чисел,
# разделенных пробелами.  Программа должна подсчитывать сумму чисел в файле и выводить ее на экран.

from random import randint

with open('text_number.txt', 'w', encoding='utf-8') as my_file:
    my_list =[randint(1, 10) for i in range(10)]
    print(my_list)
    my_file.write(' '.join(map(str,my_list)))
print(f'Sum of elements- {sum(my_list)}')