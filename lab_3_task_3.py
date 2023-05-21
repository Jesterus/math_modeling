import numpy as np
from lab_3_task_1.py import g

V = 5
x0 = 1
y0 = 1

for t in range (0, 6, 1):
    x = x0 + V*t
    y = y0 + V*t - g*t**2/2
    a = []
    a.append(t)
    a.append(y)
    a.append(x)
    print(a)