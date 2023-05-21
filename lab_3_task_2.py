# Задание 1
import numpy as np
from numpy import tan 
from numpy import pi
from lab_3_task_1.py import g

h = 100
α = np.pi / 3
β = 30

v = np.sqrt((g * h * np.tan(β)**2) / (2 * np.cos(α)**2 * (1-np.tan(β)*np.tan(α))))

print(v)

# Задание 2
from lab_3_task_1.py import ħ
from lab_3_task_1.py import k
from lab_3_task_1.py import e 

T = 200
ε = 300

N = (2 / np.sqrt(np.pi)) * (ħ / (k*T**(3/2))) * e**(-ε/k*T) * ε**(T/2)
print(N)