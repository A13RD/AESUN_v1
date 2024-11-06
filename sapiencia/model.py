from dataclasses import dataclass, field
from datetime import datetime
from typing import List, Optional
from sapiencia.emotion_classifier import IA
import uuid
import pandas as pd


@dataclass
class Actividad:
    id: int
    nombre: str
    fecha: datetime
    max_estudiantes: int
    estudiantes_registrados: List['Estudiante'] = field(default_factory=list)
    archivo_guia: Optional[str] = None
    archivo_presentacion: Optional[str] = None

    def registrar_estudiante(self, estudiante: 'Estudiante') -> Optional[str]:
        if len(self.estudiantes_registrados) < self.max_estudiantes:
            self.estudiantes_registrados.append(estudiante)
            estudiante.actividades.append(self)
            return None
        else:
            return "No hay cupos disponibles para esta actividad."

    def eliminar_estudiante(self, estudiante: 'Estudiante') -> Optional[str]:
        if estudiante in self.estudiantes_registrados:
            self.estudiantes_registrados.remove(estudiante)
            estudiante.actividades.remove(self)
            return None
        else:
            return "El estudiante no está registrado en esta actividad."


@dataclass
class GestorDeActividades:
    actividades: List[Actividad] = field(default_factory=list)
    contador_id_actividad: int = 0
    estudiantes: List['Estudiante'] = field(default_factory=list)

    def agregar_actividad(self, nombre: str, fecha: datetime, max_estudiantes: int,
                          guia: Optional[str] = None, presentacion: Optional[str] = None) -> Optional[str]:
        self.contador_id_actividad += 1
        nueva_actividad = Actividad(
            id=self.contador_id_actividad,
            nombre=nombre,
            fecha=fecha,
            max_estudiantes=max_estudiantes,
            archivo_guia=guia,
            archivo_presentacion=presentacion
        )
        self.actividades.append(nueva_actividad)
        return None

    def ver_actividades(self) -> List[Actividad]:
        return self.actividades

    def preinscribir_estudiante(self, id_actividad: int, estudiante: 'Estudiante') -> Optional[str]:
        actividad = self.obtener_actividad_por_id(id_actividad)
        if actividad:
            resultado = actividad.registrar_estudiante(estudiante)
            return resultado
        else:
            return "Actividad no encontrada."

    def eliminar_estudiante_de_actividad(self, id_actividad: int, estudiante: 'Estudiante') -> Optional[str]:
        actividad = self.obtener_actividad_por_id(id_actividad)
        if actividad:
            resultado = actividad.eliminar_estudiante(estudiante)
            return resultado
        else:
            return "Actividad no encontrada."

    def obtener_actividad_por_id(self, id_actividad: int) -> Optional[Actividad]:
        for actividad in self.actividades:
            if actividad.id == id_actividad:
                return actividad
        return None

    def agregar_estudiante(self, nombre_estudiante: str) -> 'Estudiante':
        estudiante = self.obtener_estudiante_por_nombre(nombre_estudiante)
        if not estudiante:
            estudiante = Estudiante(nombre=nombre_estudiante)
            self.estudiantes.append(estudiante)
        return estudiante

    def obtener_estudiante_por_nombre(self, nombre_estudiante: str) -> Optional['Estudiante']:
        for estudiante in self.estudiantes:
            if estudiante.nombre == nombre_estudiante:
                return estudiante
        return None

    def exportar_actividades(self):
        datos = {"nombre": [], "id": [], "fecha": [], "estudiantes_registrados": [], "max_estudiantes": []}
        for actividad in self.actividades:
            nombre = actividad.nombre
            id = actividad.id
            fecha = actividad.fecha
            max_estudiantes = actividad.max_estudiantes
            estudiantes_registrados = len(actividad.estudiantes_registrados)
            datos["nombre"].append(nombre)
            datos["id"].append(id)
            datos["fecha"].append(fecha)
            datos["max_estudiantes"].append(max_estudiantes)
            datos["estudiantes_registrados"].append(estudiantes_registrados)

        df = pd.DataFrame(datos)
        df.to_excel("Actividades_Excel.xlsx", index=False)


class ChatBot:
    @staticmethod
    def escribir_respuesta(self, conversacion: str) -> str:
        asistencia = IA()
        respuesta = asistencia.generar_respuesta_emocional(conversacion)
        return respuesta


@dataclass
class Persona:
    nombre: str
    id: str


@dataclass
class Estudiante(Persona):
    def __init__(self, nombre: str):
        super().__init__(nombre, uuid.uuid4()) #str de números y letras únicos
        self.horas_totales = 0
        self.actividades = []
        self.horas_por_actividad = {}
        self.conversacion = []
        self.chatbot = ChatBot()

    def agregar_horas(self, actividad: Actividad, horas: int) -> Optional[str]:
        if actividad not in self.actividades:
            return "No estás inscrito en esta actividad."
        self.horas_totales += horas
        self.horas_por_actividad[actividad.id] = self.horas_por_actividad.get(actividad.id, 0) + horas
        return None

    def reducir_horas(self, actividad: Actividad, horas: int) -> Optional[str]:
        if actividad not in self.actividades:
            return "No estás inscrito en esta actividad."
        horas_actuales = self.horas_por_actividad.get(actividad.id, 0)
        if horas > horas_actuales:
            return "No puedes reducir más horas de las que tienes asignadas."
        self.horas_totales -= horas
        self.horas_por_actividad[actividad.id] -= horas
        if self.horas_por_actividad[actividad.id] == 0:
            del self.horas_por_actividad[actividad.id]
        return None

    def ver_horas(self):
        print(f"\nHoras totales asignadas: {self.horas_totales}")
        if not self.horas_por_actividad:
            print("No tienes horas asignadas a ninguna actividad.")
            return
        print("Horas por actividad:")
        for id_actividad, horas in self.horas_por_actividad.items():
            print(f"Actividad ID {id_actividad}: {horas} horas")

    def enviar_mensaje(self, mensaje: str) -> List[str]:
        mensaje_formateado = f"Estudiante: {mensaje}"
        self.conversacion.append(mensaje_formateado)
        respuesta = self.chatbot.escribir_respuesta(self.conversacion)
        mensaje_respuesta_formateado = f"ChatBot: {respuesta}"
        self.conversacion.append(mensaje_respuesta_formateado)
        return self.conversacion

    def obtener_conversaciones_previas(self) -> List[str]:
        return self.conversacion
