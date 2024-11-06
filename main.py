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