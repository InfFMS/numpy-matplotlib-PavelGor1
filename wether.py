# Задача:
# Создайте массив из 365 случайных чисел, представляющих дневную температуру (например, от −10 до 35).
# Найдите:
# Среднюю температуру за год.
# Количество дней с температурой выше 25.
# Самую длинную последовательность дней, когда температура была ниже 0.
# Визуализируйте:
# Линейный график температуры по дням.
# Гистограмму распределения температуры.
# Подсветку "холодных" и "жарких" дней на линейном графике.
import matplotlib.pyplot as plt
import numpy as np
s = 365
random_array = np.random.randint(-10, 35, s)
sr=0
k=0
for i in random_array:
    sr +=i
    if i > 25:
        k+=1
sr = sr/365
print(random_array)
s = 0
counter_days = np.zeros(5)
for j in random_array:
    if j >= -10 and j <=-2:
        counter_days[0]+=1
    if j >-2 and j <= 7:
        counter_days[1] +=1
    if j>7 and j<=16:
        counter_days[2]+=1
    if j>16 and j<=25:
        counter_days[3]+=1
    if j>26 and j<=35:
        counter_days[4]+=1
categories = ["-10 до -2", "-1 до 7", "8 до 16", "17 до 25", "26 до 35"]
fig, axs = plt.subplots(1, 2, figsize=(10, 4))

axs[0].bar(categories, counter_days, color='purple')

axs[1].plot(list(range(365)), random_array, color="red")
plt.show()