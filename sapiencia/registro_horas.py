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
