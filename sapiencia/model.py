from dataclasses import dataclass, field
from datetime import datetime
from typing import List, Optional
from sapiencia.emotional_classifier import IA
import uuid
import pandas as pd


@dataclass
class Activity:
    id: int
    name: str
    date: datetime
    max_students: int
    registered_students: List['Student'] = field(default_factory=list)
    guide_file: Optional[str] = None
    presentation_file: Optional[str] = None

    def register_student(self, student: 'Student') -> Optional[str]:
        if len(self.registered_students) < self.max_students:
            self.registered_students.append(student)
            student.activities.append(self)
            return None
        else:
            return "No hay cupos disponibles para esta actividad."

    def remove_student(self, student: 'Student') -> Optional[str]:
        if student in self.registered_students:
            self.registered_students.remove(student)
            student.activities.remove(self)
            return None
        else:
            return "El estudiante no está registrado en esta actividad."


@dataclass
class ActivityManager:
    activities: List[Activity] = field(default_factory=list)
    activity_id_counter: int = 0
    students: List['Student'] = field(default_factory=list)

    def add_activity(self, name: str, date: datetime, max_students: int,
                     guide: Optional[str] = None, presentation: Optional[str] = None) -> Optional[str]:
        self.activity_id_counter += 1
        new_activity = Activity(
            id=self.activity_id_counter,
            name=name,
            date=date,
            max_students=max_students,
            guide_file=guide,
            presentation_file=presentation
        )
        self.activities.append(new_activity)
        return None

    def view_activities(self) -> List[Activity]:
        return self.activities

    def preinscribe_student(self, activity_id: int, student: 'Student') -> Optional[str]:
        activity = self.get_activity_by_id(activity_id)
        if activity:
            result = activity.register_student(student)
            return result
        else:
            return "Actividad no encontrada."

    def remove_student_from_activity(self, activity_id: int, student: 'Student') -> Optional[str]:
        activity = self.get_activity_by_id(activity_id)
        if activity:
            result = activity.remove_student(student)
            return result
        else:
            return "Actividad no encontrada."

    def get_activity_by_id(self, activity_id: int) -> Optional[Activity]:
        for activity in self.activities:
            if activity.id == activity_id:
                return activity
        return None

    def add_student(self, student_name: str) -> 'Student':
        student = self.get_student_by_name(student_name)
        if not student:
            # Pasamos `self` (la instancia de ActivityManager) al crear el estudiante
            student = Student(name=student_name, activity_manager=self)
            self.students.append(student)
        return student

    def get_student_by_name(self, student_name: str) -> Optional['Student']:
        for student in self.students:
            if student.name == student_name:
                return student
        return None

    def export_activities(self):
        data = {"name": [], "id": [], "date": [], "registered_students": [], "max_students": []}
        for activity in self.activities:
            name = activity.name
            id = activity.id
            date = activity.date
            max_students = activity.max_students
            registered_students = len(activity.registered_students)
            data["name"].append(name)
            data["id"].append(id)
            data["date"].append(date)
            data["max_students"].append(max_students)
            data["registered_students"].append(registered_students)

        df = pd.DataFrame(data)
        df.to_excel("Activities_Excel.xlsx", index=False)

# Método para añadir horas a un estudiante
    def add_hours_to_student(self, student_name, hours):
        student = self.get_student_by_name(student_name)
        if student:
            student.total_hours += hours
            print(f"{hours} horas añadidas a {student_name}. Total horas: {student.total_hours}")
        else:
            print("Estudiante no encontrado.")

    # Método para reducir horas a un estudiante
    def reduce_hours_from_student(self, student_name, hours):
        student = self.get_student_by_name(student_name)
        if student:
            student.total_hours = max(0, student.total_hours - hours)  # Evita horas negativas
            print(f"{hours} horas reducidas de {student_name}. Total horas: {student.total_hours}")
        else:
            print("Estudiante no encontrado.")

    def get_chatbox_response(self, user_input: str) -> str:
        # Utiliza IA para generar la respuesta emocional
        assistence = IA()
        response = assistence.generar_respuesta_emocional(user_input)
        return response


class ChatBot:
    def __init__(self, activity_manager: 'ActivityManager'):
        self.activity_manager = activity_manager

    def write_response(self, conversation: str) -> str:
        # Obtiene la respuesta de IA mediante ActivityManager
        response = self.activity_manager.get_chatbox_response(conversation)
        return response


@dataclass
class Person:
    name: str
    id: str


@dataclass
class Student(Person):
    def __init__(self, name: str, activity_manager: ActivityManager):
        super().__init__(name, str(uuid.uuid4()))
        self.total_hours = 0
        self.activities = []
        self.hours_per_activity = {}
        self.conversation = []
        self.chatbot = ChatBot(activity_manager)

    def add_hours(self, activity: Activity, hours: int) -> Optional[str]:
        if activity not in self.activities:
            return "No estás inscrito en esta actividad."
        self.total_hours += hours
        self.hours_per_activity[activity.id] = self.hours_per_activity.get(activity.id, 0) + hours
        return None

    def reduce_hours(self, activity: Activity, hours: int) -> Optional[str]:
        if activity not in self.activities:
            return "No estás inscrito en esta actividad."
        current_hours = self.hours_per_activity.get(activity.id, 0)
        if hours > current_hours:
            return "No puedes reducir más horas de las que tienes asignadas."
        self.total_hours -= hours
        self.hours_per_activity[activity.id] -= hours
        if self.hours_per_activity[activity.id] == 0:
            del self.hours_per_activity[activity.id]
        return None

    def view_hours(self):
        print(f"\nHoras totales asignadas: {self.total_hours}")
        if not self.hours_per_activity:
            print("No tienes horas asignadas a ninguna actividad.")
            return
        print("Horas por actividad:")
        for activity_id, hours in self.hours_per_activity.items():
            print(f"Actividad ID {activity_id}: {hours} horas")

    def send_message(self, message: str) -> List[str]:
        formatted_message = f"Estudiante: {message}"
        self.conversation.append(formatted_message)
        answer = self.chatbot.write_response(self.conversation)
        formatted_answer = f"ChatBot: {answer}"
        self.conversation.append(formatted_answer)
        return self.conversation

    def get_previous_conversations(self) -> List[str]:
        return self.conversation