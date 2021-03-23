# 2. Создать текстовый файл (не программно), сохранить в нем несколько строк,
# выполнить подсчет количества строк, количества слов в каждой строке.

with open('text.txt', encoding='utf-8') as f:
    my_file = f.readlines()
    for ind, value in enumerate(my_file, 1):
        number_words = len(value.split())
        print(f'Строка {ind} содержит {number_words} слова')


