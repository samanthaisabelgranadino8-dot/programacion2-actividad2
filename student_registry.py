class Student:
    def __init__(self, student_id, name, age):
        self.student_id = str(student_id)
        self.name = name
        self.age = int(age)

    def __str__(self):
        return f"ID: {self.student_id} - Name: {self.name} - Age: {self.age}"


class StudentRegistry:
    def __init__(self):
        self.students = []

    def add_student(self, student):
        if any(s.student_id == student.student_id for s in self.students):
            print(" El estudiante ya está registrado.")
        else:
            self.students.append(student)
            print(" Estudiante agregado correctamente.")

    def remove_student(self, student_id):
        for student in self.students:
            if student.student_id == student_id:
                self.students.remove(student)
                print(" Estudiante eliminado.")
                return
        print(" Estudiante no encontrado.")

    def find_student(self, student_id):
        for student in self.students:
            if student.student_id == student_id:
                print(" Estudiante encontrado:")
                print(student)
                return
        print(" Estudiante no encontrado.")

    def list_students(self):
        if not self.students:
            print(" No hay estudiantes registrados.")
        else:
            print(" Lista de estudiantes:")
            for student in self.students:
                print(student)