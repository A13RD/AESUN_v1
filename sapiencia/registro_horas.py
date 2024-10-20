import pandas as pd


class RegistroHoras:
    def __init__(self):
        self.horas_registradas = []

    def agregar_horas(self):
        try:
            horas = int(input("Introduce las horas a agregar: "))
            info = input("Introduce información adicional (opcional): ")
            self.horas_registradas.append({"Horas": horas, "Info": info})
            print(f"{horas} horas agregadas con éxito.")
        except ValueError:
            print("Por favor, introduce un número válido.")

    def reducir_horas(self):
        try:
            horas = int(input("Introduce las horas a reducir: "))
            if self.total_horas() < horas:
                print("No puedes reducir más horas de las que tienes registradas.")
                return

            self.horas_registradas.append({"Horas": -horas, "Info": "Reducción de horas"})
            print(f"{horas} horas reducidas con éxito.")
        except ValueError:
            print("Por favor, introduce un número válido.")

    def total_horas(self):
        return sum(entry["Horas"] for entry in self.horas_registradas)

    def mostrar_estado(self):
        print("\n--- Estado de Horas ---")
        for entry in self.horas_registradas:
            print(f"Horas: {entry['Horas']}, Info: {entry['Info']}")
        print(f"Total de horas: {self.total_horas()}")


class RegistroAsistencia:
    def __init__(self):
        self.asistencias = []

    def registrar_asistencia(self):
        nombre = input("Introduce el nombre del estudiante: ")
        fecha = input("Introduce la fecha (YYYY-MM-DD): ")
        estado = input("Estado (Presente/Ausente): ").strip().capitalize()

        if estado not in ["Presente", "Ausente"]:
            print("Estado no válido. Debe ser 'Presente' o 'Ausente'.")
            return

        self.asistencias.append({"Nombre": nombre, "Fecha": fecha, "Estado": estado})
        print("Asistencia registrada con éxito.")

    def mostrar_asistencias(self):
        if not self.asistencias:
            print("No hay registros de asistencia.")
            return

        print("\n--- Registro de Asistencia ---")
        for registro in self.asistencias:
            print(f"Nombre: {registro['Nombre']}, Fecha: {registro['Fecha']}, Estado: {registro['Estado']}")

    def exportar_a_excel(self):
        df = pd.DataFrame(self.asistencias)
        archivo = input("Introduce el nombre del archivo (sin .xlsx): ")
        df.to_excel(f"{archivo}.xlsx", index=False)
        print(f"Datos exportados a {archivo}.xlsx con éxito.")
