# 2. Пользователь вводит время в секундах. Переведите время в часы, минуты и
# секунды и выведите в формате чч:мм:сс. Используйте форматирование строк.


s = int(input("Введите время в секундах:"))
hours = s // 3600
minutes = (s - 3600 * hours) // 60
seconds = (s - 3600 * hours) % 60
h = str("{:02}".format(hours))
m = str("{:02}".format(minutes))
s = str("{:02}".format(seconds))
print(h, m, s, sep=':')
print(f'{hours:02}:{minutes:02}:{seconds:02}')

s = int(input("Введите время в секундах:"))
hours = s // 3600
minutes = (s//60) - (hours*60)
seconds = s % 60
print(f'{hours:02}:{minutes:02}:{seconds:02}')
