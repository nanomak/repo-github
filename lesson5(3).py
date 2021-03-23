# 3. Создать текстовый файл (не программно), построчно записать фамилии сотрудников
# и величину их окладов. Определить, кто из сотрудников имеет оклад менее 20 тыс.,
# вывести фамилии этих сотрудников.
# Выполнить подсчет средней величины дохода сотрудников

with open('text.txt', 'r', encoding='utf-8') as f:
    salary_dict = {line.split()[0]: float(line.split()[1]) for line in f}
    print(salary_dict)
    print(f'Средняя зарплата = {round(sum(salary_dict.values()) / len(salary_dict), 2)}\n'
    f'Сотрудники с зарплатой меньше 20т{[i[0] for i in salary_dict.items() if i[1] < 20000]}')



