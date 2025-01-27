# Задача:
# Смоделируйте 1000 бросков игрального кубика.
# Найдите:
# Сколько раз выпадало каждое значение (от 1 до 6).
# Вероятность выпадения каждого значения.
# Максимальное количество подряд выпавших одинаковых значений.
# Визуализируйте результаты в виде гистограммы.
import matplotlib.pyplot as plt
import numpy as np
s = 1000
random_array = np.random.randint(1, 7, s)
a=0
b=0
c=0
d=0
e=0
f=0
for i in random_array:
    if i == 1:
        a +=1
    if i == 2:
        b +=1
    if i == 3:
        c +=1
    if i == 4:
        d +=1
    if i == 5:
        e +=1
    if i == 6:
        f +=1
ver_a = a/s
ver_b = b/s
ver_c = c/s
ver_d = d/s
ver_e = e/s
ver_f = f/s
categories = ["1", "2", "3", "4", "5", "6",]
values = [ver_a, ver_b, ver_c, ver_d, ver_e, ver_f]
plt.xlabel("Значения кубика")
plt.ylabel("Вероятность выпадения")
plt.bar(categories, values, color='purple')
plt.subplots_adjust(bottom=0.35)
plt.title("Столбчатая диаграмма вероятности выпадения числа от 1 до 6")
plt.show()

