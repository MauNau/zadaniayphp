import json
import os
from student import Student, ExcellentStudent


def save_students(students, filename="data/students.json"):
    folder = os.path.dirname(filename)
    if folder:
        os.makedirs(folder, exist_ok=True)

    data = []
    for student in students:
        data.append(student.to_dict())

    with open(filename, "w", encoding="utf-8") as file:
        json.dump(data, file, ensure_ascii=False, indent=4)

    print("Данные сохранены.")


def load_students(filename="data/students.json"):
    if not os.path.exists(filename):
        print("Файл пока не существует. Будет создан пустой список.")
        return []

    try:
        with open(filename, "r", encoding="utf-8") as file:
            data = json.load(file)

        students = []
        for item in data:
            if item.get("student_type") == "excellent":
                student = ExcellentStudent(
                    item["student_id"], item["name"], item["age"],
                    item["group"], item.get("scholarship", 0),
                    item.get("grades", []), item.get("email", "")
                )
            else:
                student = Student(
                    item["student_id"], item["name"], item["age"],
                    item["group"], item.get("grades", []), item.get("email", "")
                )
            students.append(student)

        print("Данные загружены.")
        return students

    except (json.JSONDecodeError, KeyError, TypeError, ValueError) as error:
        print("Ошибка чтения данных:", error)
        return []
