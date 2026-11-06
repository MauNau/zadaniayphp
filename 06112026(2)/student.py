import re


class Student:
    def __init__(self, student_id, name, age, group, grades=None, email=""):
        if int(age) < 16:
            raise ValueError("Возраст студента должен быть не меньше 16 лет.")

        self.student_id = int(student_id)
        self.name = str(name)
        self.age = int(age)
        self.group = str(group)
        self.grades = list(grades) if grades is not None else []
        self.email = email

        for grade in self.grades:
            if not isinstance(grade, int) or grade < 2 or grade > 5:
                raise ValueError("Оценки должны быть целыми числами от 2 до 5.")

        if self.email and not self.check_email(self.email):
            raise ValueError("Неправильный формат электронной почты.")

    @staticmethod
    def check_email(email):
        pattern = r"^[\w.-]+@[\w.-]+\.[A-Za-z]{2,}$"
        return re.match(pattern, email) is not None

    def show_info(self):
        print(self)

    def add_grade(self, grade):
        grade = int(grade)
        if grade < 2 or grade > 5:
            raise ValueError("Оценка должна быть от 2 до 5.")
        self.grades.append(grade)

    def delete_last_grade(self):
        if self.grades:
            return self.grades.pop()
        return None

    def get_average_grade(self):
        if len(self.grades) == 0:
            return 0
        return sum(self.grades) / len(self.grades)

    def get_max_grade(self):
        return max(self.grades) if self.grades else None

    def get_min_grade(self):
        return min(self.grades) if self.grades else None

    def get_unique_grades(self):
        return set(self.grades)

    def is_successful(self):
        return self.get_average_grade() >= 3

    def get_status(self):
        average = self.get_average_grade()
        if average >= 4.5:
            return "Отличник"
        elif average >= 3:
            return "Успевающий"
        else:
            return "Неуспевающий"

    def to_dict(self):
        return {
            "student_id": self.student_id,
            "name": self.name,
            "age": self.age,
            "group": self.group,
            "grades": self.grades,
            "email": self.email,
            "student_type": "excellent" if isinstance(self, ExcellentStudent) else " обычный"
        }

    def __str__(self):
        return (
            f"ID: {self.student_id} | Студент: {self.name} | Возраст: {self.age}\n"
            f"Группа: {self.group} | Оценки: {self.grades}\n"
            f"Средний балл: {self.get_average_grade():.2f} | "
            f"Статус: {self.get_status()} | Email: {self.email or 'не указан'}"
        )


class ExcellentStudent(Student):
    def __init__(self, student_id, name, age, group, scholarship, grades=None, email=""):
        super().__init__(student_id, name, age, group, grades, email)
        self.scholarship = float(scholarship)

    def show_info(self):
        super().show_info()
        print("Стипендия:", self.get_scholarship())

    def get_scholarship(self):
        return self.scholarship

    def to_dict(self):
        data = super().to_dict()
        data["student_type"] = "excellent"
        data["scholarship"] = self.scholarship
        return data


class Group:
    def __init__(self, name):
        self.name = name
        self.students = []

    def add_student(self, student):
        self.students.append(student)

    def delete_student(self, student_id):
        for student in self.students:
            if student.student_id == student_id:
                self.students.remove(student)
                return True
        return False

    def show_students(self):
        for student in self.students:
            student.show_info()

    def get_average_grade(self):
        if not self.students:
            return 0
        return sum(s.get_average_grade() for s in self.students) / len(self.students)
