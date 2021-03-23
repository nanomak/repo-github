# 6. Необходимо создать (не программно) текстовый файл, где каждая строка описывает учебный
# предмет и наличие лекционных, практических и лабораторных занятий по этому предмету и их
# количество. Важно, чтобы для каждого предмета не обязательно были все типы занятий.
# Сформировать словарь, содержащий название предмета и общее количество занятий по нему.
# Вывести словарь на экран.
# Примеры строк файла:
#
# Информатика: 100(л) 50(пр) 20(лаб).
# Физика: 30(л) — 10(лаб)
# Физкультура: — 30(пр) —
# Пример словаря:
#
# {“Информатика”: 170, “Физика”: 40, “Физкультура”: 30}

my_dict = {}
with open('subject', 'r', encoding='utf-8') as f:
    for line in f:
        subj, num_subj = line.split(':')
        my_dict[subj] = sum(map(int, ''.join(i for i in num_subj if i in "1234567890 ").split()))
    print(my_dict)

my_dict_2 = {}
with open('subject', 'r', encoding='utf-8') as f_1:
    for line in f_1:
        line = line.replace(':', '').replace('(л)', '').replace('(пр)', '').replace('(лаб)', '')
        my_dict_2[line.split()[0]] = sum(map(int, line.split()[1:]))
    print(my_dict_2)

result = {}
with open('subject', 'r', encoding='utf-8') as f_3:
    for line in f_3:
        lesson_time = []
        lesson = ([el for el in line.split()])
        for el in lesson:
            lesson_time.append(''.join(i for i in list(el) if i.isdigit()))
        result[line.split(':')[0]] = sum([int(i) for i in lesson_time if i.isdigit()])
print(result)