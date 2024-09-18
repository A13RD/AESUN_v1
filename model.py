from dataclasses import dataclass, field
from datetime import datetime
from typing import List, Optional

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
            student = Student(name=student_name)
            self.students.append(student)
        return student

    def get_student_by_name(self, student_name: str) -> Optional['Student']:
        for student in self.students:
            if student.name == student_name:
                return student
        return None

@dataclass
class Student:
    def __init__(self, name: str):
        self.name = name
        self.total_hours = 0
        self.activities = []
        self.hours_per_activity = {}

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
