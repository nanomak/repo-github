# 5. Запросите у пользователя значения выручки и издержек фирмы. Определите,
# с каким финансовым результатом работает фирма (прибыль — выручка больше издержек,
# или убыток — издержки больше выручки). Выведите соответствующее сообщение.
# Если фирма отработала с прибылью, вычислите рентабельность выручки (соотношение прибыли к выручке).
# Далее запросите численность сотрудников фирмы
# и определите прибыль фирмы в расчете на одного сотрудника.
#
profit = int(input("Введите значение выручки:"))
lost = int(input("Введите значение издержек:"))
if profit > lost:
    print("Фирма в прибыли")
    b = (profit - lost) / lost * 100
    print("Рентабильность фирмы", str(b),"%")
    workers = int(input("Введите количество сотрудников:"))
    v = int((profit - lost) / workers)
    print("Прибыль на сотрудника", str(v))

else:
    print("Фирма в убытках")
