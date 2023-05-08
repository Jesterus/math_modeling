import numpy as np

N = 3
M = 4

A = np.zeros((N, M))
for i in range(N):
    for j in range(M):
        A[i, j] = np.sin(N * i + M * j)

print("Исходный массив:")
print(A)

A[:, [0, 2]] = A[:, [2, 0]]

print("Измененный массив:")
print(A)
