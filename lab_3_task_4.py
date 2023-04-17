import numpy as np  # импорт модуля numpy для работы с массивами

N = 3
M = 4

# Создаем массив NxM и вычисляем значения элементов
A = np.zeros((N, M))  # создаем массив из нулей размером NxM
for i in range(N):
    for j in range(M):
        A[i, j] = np.sin(N * i + M * j + (1 if A.itemsize == 4 else 0))

# Заменяем отрицательные значения на 0
A[A < 0] = 0

# Выводим массив на экран
print(A)
