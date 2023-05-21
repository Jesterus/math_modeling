import math

def area(shape):
    if shape == "круг":
        radius = float(input("Введите радиус круга: "))
        area = math.pi * radius**2
    elif shape == "прямоугольник":
        length = float(input("Введите длину прямоугольника: "))
        width = float(input("Введите ширину прямоугольника: "))
        area = length * width
    elif shape == "треугольник":
        length = float(input("Введите длину стороны треугольника: "))
        height = float(input("Введите длину высоты, которая опирается на эту сторону: "))
        area = 0.5 * length * height
    else:
        return "Нужно выбрать ту, что имеется в списке =)"

    return area

selected_shape = input("Чтобы найти площадь, выбери фигуру из списка: круг, прямоугольник, треугольник: ")
result = area(selected_shape)
if result is None:
    print("Что-то не так =/")
else:
    print(result)