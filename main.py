
from student_registry import Student, StudentRegistry

def main():
    registry = StudentRegistry()

    while True:
        print("\nStudent Registry")
        print("1. Add student")
        print("2. Remove student")
        print("3. Find student")
        print("4. List students")
        print("5. Exit")

        opcion = input("Elige una opción (1-5): ").strip()

        if opcion == "1":
            student_id = input("ID del estudiante: ")
            name = input("Nombre: ")
            age = input("Edad: ")

            student = Student(student_id, name, age)
            registry.add_student(student)

        elif opcion == "2":
            student_id = input("Ingrese ID del estudiante a eliminar: ")
            registry.remove_student(student_id)

        elif opcion == "3":
            student_id = input("Ingrese ID del estudiante a buscar: ")
            registry.find_student(student_id)

        elif opcion == "4":
            registry.list_students()

        elif opcion == "5":
            print("Saliendo... Hasta luego ❤️")
            break

        else:
            print(" Opción inválida. Por favor elige entre 1 y 5.")


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\nPrograma interrumpido. Adiós.")