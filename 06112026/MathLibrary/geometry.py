import math


# Площадь прямоугольника
def rectangle_area(length, width):
    if length <= 0 or width <= 0:
        raise ValueError("Стороны должны быть больше нуля")
    return length * width


# Периметр прямоугольника
def rectangle_perimeter(length, width):
    if length <= 0 or width <= 0:
        raise ValueError("Стороны должны быть больше нуля")
    return 2 * (length + width)


# Площадь квадрата
def square_area(side):
    if side <= 0:
        raise ValueError("Сторона должна быть больше нуля")
    return side * side


# Периметр квадрата
def square_perimeter(side):
    if side <= 0:
        raise ValueError("Сторона должна быть больше нуля")
    return 4 * side


# Площадь круга
def circle_area(radius):
    if radius <= 0:
        raise ValueError("Радиус должен быть больше нуля")
    return math.pi * radius * radius


# Длина окружности
def circle_circumference(radius):
    if radius <= 0:
        raise ValueError("Радиус должен быть больше нуля")
    return 2 * math.pi * radius


# Периметр треугольника
def triangle_perimeter(a, b, c):
    if a <= 0 or b <= 0 or c <= 0:
        raise ValueError("Стороны должны быть больше нуля")
    if a + b <= c or a + c <= b or b + c <= a:
        raise ValueError("Треугольник с такими сторонами не существует")
    return a + b + c


# Площадь треугольника по формуле Герона
def triangle_area(a, b, c):
    perimeter = triangle_perimeter(a, b, c)
    half_perimeter = perimeter / 2
    return math.sqrt(
        half_perimeter
        * (half_perimeter - a)
        * (half_perimeter - b)
        * (half_perimeter - c)
    )


# Площадь трапеции
def trapezoid_area(a, b, height):
    if a <= 0 or b <= 0 or height <= 0:
        raise ValueError("Основания и высота должны быть больше нуля")
    return (a + b) * height / 2


# Периметр трапеции
def trapezoid_perimeter(a, b, c, d):
    if a <= 0 or b <= 0 or c <= 0 or d <= 0:
        raise ValueError("Все стороны должны быть больше нуля")
    return a + b + c + d
