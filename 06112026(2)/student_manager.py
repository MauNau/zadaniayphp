class StudentManager:
    def __init__(self):
        self.students = []

    def add_student(self, student):
        if self.find_student(student.student_id) is not None:
            print("Студент с таким ID уже существует.")
            return False
        self.students.append(student)
        print("Студент добавлен.")
        return True

    def show_students(self):
        if not self.students:
            print("Список студентов пуст.")
            return
        for student in self.students:
            student.show_info()
            print("-" * 45)

    def find_student(self, student_id):
        for student in self.students:
            if student.student_id == student_id:
                return student
        return None

    def find_by_name(self, name):
        result = []
        for student in self.students:
            if name.lower() in student.name.lower():
                result.append(student)
        return result

    def delete_student(self, student_id):
        student = self.find_student(student_id)
        if student is None:
            print("Студент не найден.")
            return False
        self.students.remove(student)
        print("Студент удален.")
        return True

    def update_student(self, student_id):
        student = self.find_student(student_id)
        if student is None:
            print("Студент не найден.")
            return False

        print("Оставьте поле пустым, если не хотите его менять.")
        name = input("Новое ФИО: ").strip()
        age_text = input("Новый возраст: ").strip()
        group = input("Новая группа: ").strip()
        email = input("Новый email: ").strip()

        try:
            if name:
                student.name = name
            if age_text:
                age = int(age_text)
                if age < 16:
                    raise ValueError("Возраст должен быть не меньше 16 лет.")
                student.age = age
            if group:
                student.group = group
            if email:
                from student import Student
                if not Student.check_email(email):
                    raise ValueError("Неправильный формат email.")
                student.email = email
            print("Данные изменены.")
            return True
        except ValueError as error:
            print("Ошибка:", error)
            return False

    def find_by_group(self, group):
        return [student for student in self.students if student.group.lower() == group.lower()]

    def count_students(self):
        return len(self.students)
