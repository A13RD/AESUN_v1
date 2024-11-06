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

    def reduce_hours_window(self):
        activities = self.activity_manager.view_activities()
        activities_list = [f"{a.id}: {a.name}" for a in activities]

        layout = [
            [sg.Text('Reducir Horas', font=('Helvetica', 14))],
            [sg.Text('Nombre del estudiante:'), sg.Input(key='-STUDENT-')],
            [sg.Text('Seleccionar actividad:')],
            [sg.Listbox(activities_list, size=(40, 6), key='-ACTIVITY-')],
            [sg.Text('Número de horas:'), sg.Input(key='-HOURS-')],
            [sg.Button('Reducir Horas'), sg.Button('Cancelar')]
        ]
        return sg.Window('Reducir Horas', layout, finalize=True)

    def chatbot_window(self):
        layout = [
            [sg.Text('ChatBot', font=('Helvetica', 14))],
            [sg.Text('Nombre del estudiante:'), sg.Input(key='-STUDENT-')],
            [sg.Output(size=(60, 20), key='-OUTPUT-')],
            [sg.Input(key='-INPUT-', size=(45, 1)), sg.Button('Enviar'), sg.Button('Salir')]
        ]
        return sg.Window('ChatBot', layout, finalize=True)

    def run(self):
        main_window = self.create_main_window()
        director_window = None
        student_window = None

        while True:
            window, event, values = sg.read_all_windows()

            if event == sg.WIN_CLOSED or event == 'Salir':
                window.close()
                if window == main_window:
                    break

            if event == 'Director':
                main_window.hide()
                director_window = self.create_director_window()

            if event == 'Estudiante':
                main_window.hide()
                student_window = self.create_student_window()

            if event == 'Volver':
                window.close()
                main_window.un_hide()
                # Director functions
                if event == 'Añadir Actividad':
                    add_window = self.add_activity_window()
                    while True:
                        event2, values2 = add_window.read()
                        if event2 in (sg.WIN_CLOSED, 'Cancelar'):
                            break
                        if event2 == 'Guardar':
                            try:
                                name = values2['-NAME-']
                                date = datetime.strptime(values2['-DATE-'], "%Y-%m-%d")
                                max_students = int(values2['-MAX-'])
                                guide = values2['-GUIDE-']
                                presentation = values2['-PRES-']

                                self.activity_manager.add_activity(name, date, max_students, guide, presentation)
                                sg.popup('Actividad añadida con éxito')
                                break
                            except Exception as e:
                                sg.popup_error(f'Error: {str(e)}')
                    add_window.close()
                    if event == 'Ver Actividades':
                        view_window = self.view_activities_window()
                        while True:
                            event2, values2 = view_window.read()
                            if event2 in (sg.WIN_CLOSED, 'Cerrar'):
                                break
                        view_window.close()

                    if event == 'Preinscribir Estudiante':
                        preinscribe_window = self.preinscribe_student_window()
                        while True:
                            event2, values2 = preinscribe_window.read()
                            if event2 in (sg.WIN_CLOSED, 'Cancelar'):
                                break
                            if event2 == 'Preinscribir':
                                try:
                                    student_name = values2['-STUDENT-']
                                    activity_id = int(values2['-ACTIVITY-'][0].split(':')[0])
                                    student = self.activity_manager.add_student(student_name)
                                    result = self.activity_manager.preinscribe_student(activity_id, student)
                                    if result:
                                        sg.popup_error(result)
                                    else:
                                        sg.popup('Estudiante preinscrito con éxito')
                                        break
                                except Exception as e:
                                    sg.popup_error(f'Error: {str(e)}')
                        preinscribe_window.close()

                    if event == 'Eliminar Estudiante':
                        remove_window = self.remove_student_window()
                        while True:
                            event2, values2 = remove_window.read()
                            if event2 in (sg.WIN_CLOSED, 'Cancelar'):
                                break
                            if event2 == 'Eliminar':
                                try:
                                    student_name = values2['-STUDENT-']
                                    activity_id = int(values2['-ACTIVITY-'][0].split(':')[0])
                                    student = self.activity_manager.get_student_by_name(student_name)
                                    if student:
                                        result = self.activity_manager.remove_student_from_activity(activity_id,
                                                                                                    student)
                                        if result:
                                            sg.popup_error(result)
                                        else:
                                            sg.popup('Estudiante eliminado con éxito')
                                            break
                                    else:
                                        sg.popup_error('Estudiante no encontrado')
                                except Exception as e:
                                    sg.popup_error(f'Error: {str(e)}')
                        remove_window.close()

                if event == 'Agregar Estudiante':
                    add_student_window = self.add_student_window()
                    while True:
                        event2, values2 = add_student_window.read()
                        if event2 in (sg.WIN_CLOSED, 'Cancelar'):
                            break
                        if event2 == 'Agregar':
                            try:
                                student_name = values2['-STUDENT-']
                                student = self.activity_manager.add_student(student_name)
                                sg.popup(f'Estudiante {student.name} agregado con éxito')
                                break
                            except Exception as e:
                                sg.popup_error(f'Error: {str(e)}')
                    add_student_window.close()

                if event == 'Exportar a Excel':
                    try:
                        self.activity_manager.export_activities()
                        sg.popup('Datos exportados a Excel con éxito')
                    except Exception as e:
                        sg.popup_error(f'Error al exportar: {str(e)}')

                    # Student functions
                if event == 'Ver Horas':
                    hours_window = self.student_hours_window()
                    while True:
                        event2, values2 = hours_window.read()
                        if event2 in (sg.WIN_CLOSED, 'Cancelar'):
                            break
                        if event2 == 'Ver Horas':
                            try:
                                student_name = values2['-STUDENT-']
                                student = self.activity_manager.get_student_by_name(student_name)
                                if student:
                                    student.view_hours()
                                else:
                                    sg.popup_error('Estudiante no encontrado')
                            except Exception as e:
                                sg.popup_error(f'Error: {str(e)}')
                    hours_window.close()

                if event == 'Agregar Horas':













