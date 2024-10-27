from abc import ABC, abstractmethod
import pandas as pd
from datetime import datetime


class RegistroError(Exception):
    """Excepción personalizada para errores de registro."""
    pass


class Registro(ABC):
    """Clase base abstracta para manejar registros."""

    @abstractmethod
    def mostrar_estado(self):
        """Método abstracto para mostrar el estado del registro."""
        pass

    @abstractmethod
    def exportar_a_excel(self, nombre_archivo):
        """Método abstracto para exportar registros a Excel."""
        pass


class RegistroHoras(Registro):
    def __init__(self):
        self.horas_registradas = []

    def total_horas(self):
        return sum(entry["Horas"] for entry in self.horas_registradas)

    def agregar_horas(self, horas, info=""):
        if not isinstance(horas, int) or horas <= 0:
            raise RegistroError("Las horas deben ser un número entero positivo.")
        self.horas_registradas.append({"Horas": horas, "Info": info})
        print(f"{horas} horas agregadas con éxito.")

    def reducir_horas(self, horas):
        if not isinstance(horas, int) or horas <= 0:
            raise RegistroError("Las horas a reducir deben ser un número entero positivo.")
        if self.total_horas() < horas:
            raise RegistroError("No puedes reducir más horas de las que tienes registradas.")

        self.horas_registradas.append({"Horas": -horas, "Info": "Reducción de horas"})
        print(f"{horas} horas reducidas con éxito.")

    def mostrar_estado(self):
        if not self.horas_registradas:
            print("No hay horas registradas.")
            return
        print("\n--- Registro de Horas ---")
        for registro in self.horas_registradas:
            print(f"Horas: {registro['Horas']}, Info: {registro['Info']}")

    def exportar_a_excel(self, nombre_archivo):
        df = pd.DataFrame(self.horas_registradas)
        df.to_excel(f"{nombre_archivo}.xlsx", index=False)
        print(f"Datos exportados a {nombre_archivo}.xlsx con éxito.")


class RegistroAsistencia(Registro):
    def __init__(self):
        self.asistencias = []

    def registrar_asistencia(self, nombre, fecha, estado):
        if estado not in ["Presente", "Ausente"]:
            raise RegistroError("Estado no válido. Debe ser 'Presente' o 'Ausente'.")

        try:
            fecha_obj = datetime.strptime(fecha, "%Y-%m-%d")
        except ValueError:
            raise RegistroError("Formato de fecha inválido. Use 'YYYY-MM-DD'.")

        self.asistencias.append({"Nombre": nombre, "Fecha": fecha_obj.strftime("%Y-%m-%d"), "Estado": estado})
        print("Asistencia registrada con éxito.")

    def mostrar_estado(self):
        if not self.asistencias:
            print("No hay registros de asistencia.")
            return

        print("\n--- Registro de Asistencia ---")
        for registro in self.asistencias:
            print(f"Nombre: {registro['Nombre']}, Fecha: {registro['Fecha']}, Estado: {registro['Estado']}")

    def exportar_a_excel(self, nombre_archivo):
        df = pd.DataFrame(self.asistencias)
        df.to_excel(f"{nombre_archivo}.xlsx", index=False)
        print(f"Datos exportados a {nombre_archivo}.xlsx con éxito.")