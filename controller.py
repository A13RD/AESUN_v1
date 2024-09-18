from model import ActivityManager, Student
from datetime import datetime


def director_menu(activity_manager: ActivityManager):
    while True:
        print("\n--- Menú Director ---")
        print("1. Añadir actividad")
        print("2. Ver actividades")
        print("3. Preinscribir estudiante")
        print("4. Eliminar estudiante de actividad")
        print("5. Volver al menú principal")

        choice = input("Ingrese una opción: ")

        if choice == '1':
            name = input("Nombre de la actividad: ")
            date_str = input("Fecha de la actividad (YYYY-MM-DD): ")
            date = datetime.strptime(date_str, "%Y-%m-%d")
            max_students = int(input("Número máximo de estudiantes: "))
            guide = input("Archivo guía (opcional): ")
            presentation = input("Archivo presentación (opcional): ")
            activity_manager.add_activity(name, date, max_students, guide, presentation)
            print("Actividad añadida con éxito.")

        elif choice == '2':
            activities = activity_manager.view_activities()
            for activity in activities:
                print(
                    f"ID: {activity.id}, Nombre: {activity.name}, Fecha: {activity.date}, Máx. Estudiantes: {activity.max_students}")

        elif choice == '3':
            activity_id = int(input("ID de la actividad: "))
            student_name = input("Nombre del estudiante: ")
            student = activity_manager.add_student(student_name)
            result = activity_manager.preinscribe_student(activity_id, student)
            if result:
                print(result)
            else:
                print("Estudiante preinscrito con éxito.")

        elif choice == '4':
            activity_id = int(input("ID de la actividad: "))
            student_name = input("Nombre del estudiante: ")
            student = activity_manager.get_student_by_name(student_name)
            if student:
                result = activity_manager.remove_student_from_activity(activity_id, student)
                if result:
                    print(result)
                else:
                    print("Estudiante eliminado de la actividad con éxito.")
            else:
                print("Estudiante no encontrado.")

        elif choice == '5':
            break
        else:
            print("Opción inválida. Intente de nuevo.")


def student_menu(activity_manager: ActivityManager):
    while True:
        print("\n--- Menú Estudiante ---")
        print("1. Ver horas")
        print("2. Agregar horas")
        print("3. Reducir horas")
        print("4. Volver al menú principal")

        choice = input("Ingrese una opción: ")

        if choice == '1':
            student_name = input("Nombre del estudiante: ")
            student = activity_manager.get_student_by_name(student_name)
            if student:
                student.view_hours()
            else:
                print("Estudiante no encontrado.")

        elif choice == '2':
            student_name = input("Nombre del estudiante: ")
            activity_id = int(input("ID de la actividad: "))
            hours = int(input("Número de horas: "))
            student = activity_manager.get_student_by_name(student_name)
            activity = activity_manager.get_activity_by_id(activity_id)
            if student and activity:
                result = student.add_hours(activity, hours)
                if result:
                    print(result)
                else:
                    print("Horas añadidas con éxito.")
            else:
                print("Estudiante o actividad no encontrados.")

        elif choice == '3':
            student_name = input("Nombre del estudiante: ")
            activity_id = int(input("ID de la actividad: "))
            hours = int(input("Número de horas: "))
            student = activity_manager.get_student_by_name(student_name)
            activity = activity_manager.get_activity_by_id(activity_id)
            if student and activity:
                result = student.reduce_hours(activity, hours)
                if result:
                    print(result)
                else:
                    print("Horas reducidas con éxito.")
            else:
                print("Estudiante o actividad no encontrados.")

        elif choice == '5':
            student_name = input("Ingrese el nombre del estudiante a agregar: ")
            student = activity_manager.add_student(student_name)
            print(f"Estudiante '{student.name}' agregado con éxito.")

        elif choice == '6':

            break
        else:
            print("Opción inválida. Intente de nuevo.")
