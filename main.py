import PySimpleGUI as sg
from sapiencia.model import ActivityManager
from datetime import datetime


class SapienciaGUI:
    def __init__(self):
        self.activity_manager = ActivityManager()
        sg.theme('LightGrey1')

    def create_main_window(self):
        layout = [
            [sg.Text('Bienvenido a la Aplicación Estudiantes Sapiencia', font=('Helvetica', 16))],
            [sg.Text('Seleccione su rol:', font=('Helvetica', 12))],
            [sg.Button('Director', size=(20, 2)), sg.Button('Estudiante', size=(20, 2))],
            [sg.Button('Salir', size=(10, 1))]
        ]
        return sg.Window('Sapiencia', layout, finalize=True)

    def create_director_window(self):
        layout = [
            [sg.Text('Menú Director', font=('Helvetica', 14))],
            [sg.Frame('Gestión de Actividades', [
                [sg.Button('Añadir Actividad', size=(20, 1))],
                [sg.Button('Ver Actividades', size=(20, 1))],
                [sg.Button('Preinscribir Estudiante', size=(20, 1))],
                [sg.Button('Eliminar Estudiante', size=(20, 1))],
                [sg.Button('Agregar Estudiante', size=(20, 1))],
                [sg.Button('Exportar a Excel', size=(20, 1))]
            ])],
            [sg.Button('Volver', size=(10, 1))]
        ]
        return sg.Window('Director', layout, finalize=True)

    def create_student_window(self):
        layout = [
            [sg.Text('Menú Estudiante', font=('Helvetica', 14))],
            [sg.Frame('Gestión de Horas', [
                [sg.Button('Ver Horas', size=(20, 1))],
                [sg.Button('Agregar Horas', size=(20, 1))],
                [sg.Button('Reducir Horas', size=(20, 1))],
                [sg.Button('ChatBot', size=(20, 1))]
            ])],
            [sg.Button('Volver', size=(10, 1))]
        ]
        return sg.Window('Estudiante', layout, finalize=True)

    def add_activity_window(self):
        layout = [
            [sg.Text('Añadir Nueva Actividad', font=('Helvetica', 14))],
            [sg.Text('Nombre:'), sg.Input(key='-NAME-')],
            [sg.Text('Fecha (YYYY-MM-DD):'), sg.Input(key='-DATE-')],
            [sg.Text('Máximo de estudiantes:'), sg.Input(key='-MAX-')],
            [sg.Text('Archivo guía:'), sg.Input(key='-GUIDE-'), sg.FileBrowse()],
            [sg.Text('Presentación:'), sg.Input(key='-PRES-'), sg.FileBrowse()],
            [sg.Button('Guardar'), sg.Button('Cancelar')]
        ]
        return sg.Window('Añadir Actividad', layout, finalize=True)

    def view_activities_window(self):
        activities = self.activity_manager.view_activities()
        headers = ['ID', 'Nombre', 'Fecha', 'Max. Estudiantes', 'Estudiantes Inscritos']
        data = [[a.id, a.name, a.date.strftime("%Y-%m-%d"), a.max_students, len(a.registered_students)] for a in
                activities]

        layout = [
            [sg.Text('Lista de Actividades', font=('Helvetica', 14))],
            [sg.Table(values=data,
                      headings=headers,
                      auto_size_columns=True,
                      justification='center',
                      num_rows=min(25, len(data)))],
            [sg.Button('Cerrar')]
        ]
        return sg.Window('Ver Actividades', layout, finalize=True)

    def preinscribe_student_window(self):
        activities = self.activity_manager.view_activities()
        activities_list = [f"{a.id}: {a.name}" for a in activities]

        layout = [
            [sg.Text('Preinscribir Estudiante', font=('Helvetica', 14))],
            [sg.Text('Nombre del estudiante:'), sg.Input(key='-STUDENT-')],
            [sg.Text('Seleccionar actividad:')],
            [sg.Listbox(activities_list, size=(40, 6), key='-ACTIVITY-')],
            [sg.Button('Preinscribir'), sg.Button('Cancelar')]
        ]
        return sg.Window('Preinscribir Estudiante', layout, finalize=True)

    def remove_student_window(self):
        activities = self.activity_manager.view_activities()
        activities_list = [f"{a.id}: {a.name}" for a in activities]

        layout = [
            [sg.Text('Eliminar Estudiante de Actividad', font=('Helvetica', 14))],
            [sg.Text('Nombre del estudiante:'), sg.Input(key='-STUDENT-')],
            [sg.Text('Seleccionar actividad:')],
            [sg.Listbox(activities_list, size=(40, 6), key='-ACTIVITY-')],
            [sg.Button('Eliminar'), sg.Button('Cancelar')]
        ]
        return sg.Window('Eliminar Estudiante', layout, finalize=True)

    def add_student_window(self):
        layout = [
            [sg.Text('Agregar Nuevo Estudiante', font=('Helvetica', 14))],
            [sg.Text('Nombre del estudiante:'), sg.Input(key='-STUDENT-')],
            [sg.Button('Agregar'), sg.Button('Cancelar')]
        ]
        return sg.Window('Agregar Estudiante', layout, finalize=True)

    def student_hours_window(self):
        layout = [
            [sg.Text('Ver Horas de Estudiante', font=('Helvetica', 14))],
            [sg.Text('Nombre del estudiante:'), sg.Input(key='-STUDENT-')],
            [sg.Button('Ver Horas'), sg.Button('Cancelar')]
        ]
        return sg.Window('Ver Horas', layout, finalize=True)

    def add_hours_window(self):
        activities = self.activity_manager.view_activities()
        activities_list = [f"{a.id}: {a.name}" for a in activities]

        layout = [
            [sg.Text('Agregar Horas', font=('Helvetica', 14))],
            [sg.Text('Nombre del estudiante:'), sg.Input(key='-STUDENT-')],
            [sg.Text('Seleccionar actividad:')],
            [sg.Listbox(activities_list, size=(40, 6), key='-ACTIVITY-')],
            [sg.Text('Número de horas:'), sg.Input(key='-HOURS-')],
            [sg.Button('Agregar Horas'), sg.Button('Cancelar')]
        ]
        return sg.Window('Agregar Horas', layout, finalize=True)





