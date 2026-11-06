def calculate_group_average(students):
    if not students:
        return 0
    total = 0
    for student in students:
        total += student.get_average_grade()
    return total / len(students)


def count_excellent_students(students):
    count = 0
    for student in students:
        if student.get_average_grade() >= 4.5:
            count += 1
    return count


def find_best_student(students):
    if not students:
        return None
    return max(students, key=lambda student: student.get_average_grade())


def get_group_statistics(students, group):
    group_students = [s for s in students if s.group.lower() == group.lower()]
    not_successful = 0
    for student in group_students:
        if student.get_average_grade() < 3:
            not_successful += 1

    return {
        "count": len(group_students),
        "average": calculate_group_average(group_students),
        "excellent": count_excellent_students(group_students),
        "not_successful": not_successful
    }


def sort_students_by_average(students):
    return sorted(students, key=lambda student: student.get_average_grade(), reverse=True)


def show_full_statistics(students):
    if not students:
        print("Нет данных для статистики.")
        return

    print("Количество студентов:", len(students))
    print("Средний балл:", round(calculate_group_average(students), 2))
    print("Количество отличников:", count_excellent_students(students))

    best = find_best_student(students)
    print("Лучший студент:", best.name, "-", round(best.get_average_grade(), 2))

    worst = min(students, key=lambda s: s.get_average_grade())
    print("Минимальный средний балл:", worst.name, "-", round(worst.get_average_grade(), 2))

    print("\nСтуденты со средним баллом выше 4:")
    for student in students:
        if student.get_average_grade() > 4:
            print(student.name)

    print("\nСтуденты старше 18 лет:")
    for student in students:
        if student.age > 18:
            print(student.name)

    print("\nСортировка по среднему баллу:")
    for student in sort_students_by_average(students):
        print(student.name, "-", round(student.get_average_grade(), 2))
