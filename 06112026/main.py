from MathLibrary import (
    rectangle_area,
    rectangle_perimeter,
    square_area,
    square_perimeter,
    circle_area,
    circle_circumference,
    triangle_area,
    triangle_perimeter,
    trapezoid_area,
    trapezoid_perimeter
)

def get_number(message):
    while True:
        try:
            number = float(input(message))

            if number <= 0:
                print("Число должно быть больше нуля. Попробуйте ещё раз.")
            else:
                return number

        except ValueError:
            print("Нужно ввести число. Попробуйте ещё раз.")

while True:
    print("\n МАТЕМАТИЧЕСКИЙ КАЛЬКУЛЯТОР ")
    print("Выберите фигуру:")
    print("1. Прямоугольник")
    print("2. Квадрат")
    print("3. Круг")
    print("4. Треугольник")
    print("5. Трапеция")
    print("0. Выход")

    choice = input("Ваш выбор: ")

    try:
        if choice == "1":
            print("\nПрямоугольник")
            length = get_number("Введите длину: ")
            width = get_number("Введите ширину: ")

            print("Площадь:", rectangle_area(length, width))
            print("Периметр:", rectangle_perimeter(length, width))

        elif choice == "2":
            print("\nКвадрат")
            side = get_number("Введите сторону: ")

            print("Площадь:", square_area(side))
            print("Периметр:", square_perimeter(side))

        elif choice == "3":
            print("\nКруг")
            radius = get_number("Введите радиус: ")

            print("Площадь:", round(circle_area(radius), 2))
            print("Длина окружности:", round(circle_circumference(radius), 2))

        elif choice == "4":
            print("\nТреугольник")
            a = get_number("Введите первую сторону: ")
            b = get_number("Введите вторую сторону: ")
            c = get_number("Введите третью сторону: ")

            print("Площадь:", round(triangle_area(a, b, c), 2))
            print("Периметр:", triangle_perimeter(a, b, c))

        elif choice == "5":
            print("\nТрапеция")
            a = get_number("Введите первое основание: ")
            b = get_number("Введите второе основание: ")
            height = get_number("Введите высоту: ")
            c = get_number("Введите третью сторону: ")
            d = get_number("Введите четвёртую сторону: ")

            print("Площадь:", trapezoid_area(a, b, height))
            print("Периметр:", trapezoid_perimeter(a, b, c, d))

        elif choice == "0":
            print("Программа завершена.")
            break

        else:
            print("Такого пункта нет. Выберите число от 0 до 5.")

    except ValueError as error:
        print("Ошибка:", error)

    input("\nНажмите Enter, чтобы вернуться в меню...")
