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
