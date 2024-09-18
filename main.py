from model import ActivityManager
from controller import director_menu, student_menu

def main():
    activity_manager = ActivityManager()

    while True:
        print("Bienvenido a la Aplicación Estudiantes Sapiencia")
        print("Seleccione su rol:")
        print("1. Director")
        print("2. Estudiante")
        print("3. Salir")

        choice = input("Ingrese una opción: ")

        if choice == '1':
            director_menu(activity_manager)
        elif choice == '2':
            student_menu(activity_manager)
        elif choice == '3':
            print("Gracias por usar la aplicación.")
            break
        else:
            print("Opción inválida. Por favor, intente de nuevo.")

if __name__ == "__main__":
    main()
