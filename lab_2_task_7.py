print("Введите коэффициенты a, b и c для уравнения ax^2 + bx + c = 0:")
a = float(input("a = "))
b = float(input("b = "))
c = float(input("c = "))

D = b**2 - 4*a*c  # Вычисляем дискриминант

if D < 0:
    print("Корней нет")
elif D == 0:
    x = -b / (2*a)
    print("Один корень: x =", x)
else:
    x1 = (-b + D**(1/2)) / (2*a)
    x2 = (-b - D**(1/2)) / (2*a)
    print("Два корня: x1 =", x1, ", x2 =", x2)
