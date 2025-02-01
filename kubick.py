# Задача:
# Смоделируйте 1000 бросков игрального кубика.
# Найдите:
# Сколько раз выпадало каждое значение (от 1 до 6).
# Вероятность выпадения каждого значения.
# Максимальное количество подряд выпавших одинаковых значений.
# Визуализируйте результаты в виде гистограммы.
import matplotlib.pyplot as plt
import numpy as np
def max_i(maxi):
    s = 1
    max_1 = 1
    for i in range(1, len(maxi)):
        if maxi[i] == maxi[i - 1]:
            s += 1
        else:
            max_1 = max(max_1, s)
            s = 1
    max_1 = max(max_1, s)
    return max_1
s = 1000
random_array = np.random.randint(1, 7, s)
array = random_array[::]
result = max_i(array)
print("Максимальное количество подряд идущих значений кубика:", result)
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
plt.subplots_adjust(bottom=0.1)
plt.title("Столбчатая диаграмма вероятности выпадения числа от 1 до 6")
plt.show()

