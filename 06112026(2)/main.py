import os
import random
from datetime import datetime

from student import Student, ExcellentStudent
from student_manager import StudentManager
from file_manager import save_students, load_students
from student_statistics import show_full_statistics, get_group_statistics


BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_FILE = os.path.join(BASE_DIR, "data", "students.json")


def add_student_menu(manager):
    try:
        student_id = int(input("Введите ID: "))
        name = input("Введите ФИО: ").strip()
        age = int(input("Введите возраст: "))
        group = input("Введите группу: ").strip()
        email = input("Введите email (можно оставить пустым): ").strip()

        excellent = input("Это отличник со стипендией? (да/нет): ").lower()
        if excellent == "да":
            scholarship = float(input("Размер стипендии: "))
            student = ExcellentStudent(student_id, name, age, group, scholarship, email=email)
        else:
            student = Student(student_id, name, age, group, email=email)

        manager.add_student(student)
    except ValueError as error:
        print("Ошибка ввода:", error)


def add_grade_menu(manager):
    try:
        student_id = int(input("Введите ID студента: "))
        student = manager.find_student(student_id)
        if student is None:
            print("Студент не найден.")
            return
        grade = int(input("Введите оценку от 2 до 5: "))
        student.add_grade(grade)
        print("Оценка добавлена.")
    except ValueError as error:
        print("Ошибка:", error)


def show_student_by_id(manager):
    try:
        student_id = int(input("Введите ID: "))
        student = manager.find_student(student_id)
        if student:
            student.show_info()
        else:
            print("Студент не найден.")
    except ValueError:
        print("ID должен быть числом.")


def show_student_by_name(manager):
    name = input("Введите имя или часть ФИО: ").strip()
    result = manager.find_by_name(name)
    if not result:
        print("Студенты не найдены.")
    for student in result:
        student.show_info()


def show_group(manager):
    group = input("Введите название группы: ").strip()
    students = manager.find_by_group(group)
    if not students:
        print("В этой группе студентов нет.")
        return
    for student in students:
        student.show_info()

    stats = get_group_statistics(manager.students, group)
    print("Количество:", stats["count"])
    print("Средний балл:", round(stats["average"], 2))
    print("Отличников:", stats["excellent"])
    print("Неуспевающих:", stats["not_successful"])


def main():
    manager = StudentManager()
    manager.students = load_students(DATA_FILE)

    while True:
        print("""
        СИСТЕМА УПРАВЛЕНИЯ СТУДЕНТАМИ
        1. Добавить студента
        2. Показать всех студентов
        3. Найти студента по ID
        4. Найти студента по имени
        5. Удалить студента
        6. Изменить данные студента
        7. Добавить оценку
        8. Показать статистику
        9. Показать студентов по группе
        10. Случайный студент
        11. Сохранить данные
        12. Загрузить данные
        13. Выход
        0. Выход""")
        choice = input("Введите номер действия: ").strip()

        if choice == "1":
            add_student_menu(manager)

        elif choice == "2":
            manager.show_students()

        elif choice == "3":
            show_student_by_id(manager)

        elif choice == "4":
            show_student_by_name(manager)

        elif choice == "5":
            try:
                student_id = int(input("Введите ID для удаления: "))
                manager.delete_student(student_id)
            except ValueError:
                print("ID должен быть числом.")

        elif choice == "6":
            try:
                student_id = int(input("Введите ID студента: "))
                manager.update_student(student_id)
            except ValueError:
                print("ID должен быть числом.")

        elif choice == "7":
            add_grade_menu(manager)

        elif choice == "8":
            show_full_statistics(manager.students)

        elif choice == "9":
            show_group(manager)

        elif choice == "10":
            if manager.students:
                student = random.choice(manager.students)
                print("Сегодня отвечает:")
                student.show_info()
            else:
                print("Список студентов пуст.")

        elif choice == "11":
            save_students(manager.students, DATA_FILE)
            print("Последнее изменение:", datetime.now().strftime("%d.%m.%Y %H:%M:%S"))

        elif choice == "12":
            manager.students = load_students(DATA_FILE)

        elif choice == "13" or choice == "0":
            save_students(manager.students, DATA_FILE)
            print("Программа завершена.")
            break

        else:
            print("Такого пункта меню нет. Попробуйте еще раз.")


if __name__ == "__main__":
    main()
