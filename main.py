import PySimpleGUI as sg
from sapiencia.model import GestorDeActividades, Estudiante, ChatBot
from datetime import datetime

class SapienciaGUI:
    def __init__(self):
        self.activity_manager = GestorDeActividades()
        self.estudiante = None
        self.chatbot = ChatBot()
        sg.theme('LightGrey1')

    def crear_ventana_principal(self):
        layout = [
            [sg.Text('Bienvenido a la Aplicación Estudiantes Sapiencia', font=('Helvetica', 16))],
            [sg.Text('Seleccione su rol:', font=('Helvetica', 12))],
            [sg.Button('Director', size=(20, 2)), sg.Button('Estudiante', size=(20, 2))],
            [sg.Button('Salir', size=(10, 1))]
        ]
        return sg.Window('Sapiencia', layout, finalize=True)

    def crear_ventana_director(self):
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

    def crear_ventana_estudiante(self):
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

    def run(self):
        ventana_principal = self.crear_ventana_principal()

        while True:
            window, event, values = sg.read_all_windows()

            if event == sg.WIN_CLOSED or event == 'Salir':
                window.close()
                if window == ventana_principal:
                    break

            if event == 'Director':
                ventana_principal.hide()
                director_window = self.crear_ventana_director()
                self.manejar_ventana_director(director_window)

            if event == 'Estudiante':
                ventana_principal.hide()
                student_window = self.crear_ventana_estudiante()
                self.manejar_ventana_estudiante(student_window)

            if event == 'Volver':
                window.close()
                ventana_principal.un_hide()

    def manejar_ventana_director(self, window):
        while True:
            event, values = window.read()

            if event == sg.WIN_CLOSED or event == 'Volver':
                window.close()
                return

            if event == 'Añadir Actividad':
                self.agregar_actividad(window)
            elif event == 'Ver Actividades':
                self.ver_actividades(window)
            elif event == 'Preinscribir Estudiante':
                self.preinscribir_estudiante(window)
            elif event == 'Eliminar Estudiante':
                self.eliminar_estudiante(window)
            elif event == 'Agregar Estudiante':
                self.agregar_estudiante(window)
            elif event == 'Exportar a Excel':
                self.exportar_a_excel(window)

    def manejar_ventana_estudiante(self, window):
        while True:
            event, values = window.read()

            if event == sg.WIN_CLOSED or event == 'Volver':
                window.close()
                return

            if event == 'Ver Horas':
                self.ver_horas_estudiante(window)
            elif event == 'Agregar Horas':
                self.agregar_horas_estudiante(window)
            elif event == 'Reducir Horas':
                self.reducir_horas_estudiante(window)
            elif event == 'ChatBot':
                self.abrir_chatbot(window)

    def agregar_actividad(self, window):
        add_window = self.agregar_ventana_actividad()
        while True:
            event, values = add_window.read()
            if event in (sg.WIN_CLOSED, 'Cancelar'):
                break
            if event == 'Guardar':
                try:
                    nombre = values['-NAME-']
                    fecha = datetime.strptime(values['-DATE-'], "%Y-%m-%d")
                    max_estudiantes = int(values['-MAX-'])
                    guia = values['-GUIDE-']
                    presentacion = values['-PRES-']

                    self.activity_manager.agregar_actividad(nombre, fecha, max_estudiantes, guia, presentacion)
                    sg.popup('Actividad añadida con éxito')
                    break
                except Exception as e:
                    sg.popup_error(f'Error: {str(e)}')
        add_window.close()

    def ver_actividades(self, window):
        view_window = self.ver_ventana_actividades()
        while True:
            event, values = view_window.read()
            if event in (sg.WIN_CLOSED, 'Cerrar'):
                break
        view_window.close()

    def preinscribir_estudiante(self, window):
        ventana_preinscribir = self.ventana_preinscribir_estudiante()
        while True:
            event, values = ventana_preinscribir.read()
            if event in (sg.WIN_CLOSED, 'Cancelar'):
                break
            if event == 'Preinscribir':
                try:
                    student_name = values['-STUDENT-']
                    activity_id = int(values['-ACTIVITY-'][0].split(':')[0])
                    student = self.activity_manager.agregar_estudiante(student_name)
                    result = self.activity_manager.preinscribir_estudiante(activity_id, student)
                    if result:
                        sg.popup_error(result)
                    else:
                        sg.popup('Estudiante preinscrito con éxito')
                        break
                except Exception as e:
                    sg.popup_error(f'Error: {str(e)}')
        ventana_preinscribir.close()

    def eliminar_estudiante(self, window):
        ventana_remover = self.remove_student_window()
        while True:
            event, values = ventana_remover.read()
            if event in (sg.WIN_CLOSED, 'Cancelar'):
                break
            if event == 'Eliminar':
                try:
                    student_name = values['-STUDENT-']
                    activity_id = int(values['-ACTIVITY-'][0].split(':')[0])
                    student = self.activity_manager.obtener_estudiante_por_nombre(student_name)
                    if student:
                        result = self.activity_manager.eliminar_estudiante_de_actividad(activity_id, student)
                        if result:
                            sg.popup_error(result)
                        else:
                            sg.popup('Estudiante eliminado con éxito')
                            break
                    else:
                        sg.popup_error('Estudiante no encontrado')
                except Exception as e:
                    sg.popup_error(f'Error: {str(e)}')
        ventana_remover.close()

    def agregar_estudiante(self, window):
        add_student_window = self.ventana_agregar_estudiantes()
        while True:
            event, values = add_student_window.read()
            if event in (sg.WIN_CLOSED, 'Cancelar'):
                break
            if event == 'Agregar':
                try:
                    nombre_estudiante = values['-STUDENT-']
                    student = self.activity_manager.agregar_estudiante(nombre_estudiante)
                    sg.popup(f'Estudiante {student.nombre} agregado con éxito')
                    break
                except Exception as e:
                    sg.popup_error(f'Error: {str(e)}')
        add_student_window.close()

    def exportar_a_excel(self, window):
        try:
            self.activity_manager.exportar_actividades()
            sg.popup('Datos exportados a Excel con éxito')
        except Exception as e:
            sg.popup_error(f'Error al exportar: {str(e)}')

    def ver_horas_estudiante(self, window):
        hours_window = self.ventana_hora_estudiantes()
        while True:
            event, values = hours_window.read()
            if event in (sg.WIN_CLOSED, 'Cancelar'):
                break
            if event == 'Ver Horas':
                try:
                    student_name = values['-STUDENT-']
                    student = self.activity_manager.obtener_estudiante_por_nombre(student_name)
                    if student:
                        student.ver_horas()
                    else:
                        sg.popup_error('Estudiante no encontrado')
                except Exception as e:
                    sg.popup_error(f'Error: {str(e)}')
        hours_window.close()

    def agregar_horas_estudiante(self, window):
        add_hours_window = self.ventana_agregar_horas()
        while True:
            event, values = add_hours_window.read()
            if event in (sg.WIN_CLOSED, 'Cancelar'):
                break
            if event == 'Agregar Horas':
                try:
                    student_name = values['-STUDENT-']
                    activity_id = int(values['-ACTIVITY-'][0].split(':')[0])
                    hours = int(values['-HOURS-'])

                    student = self.activity_manager.obtener_estudiante_por_nombre(student_name)
                    if student:
                        result = self.estudiante.agregar_horas(activity_id, hours)
                        if result:
                            sg.popup_error(result)
                        else:
                            sg.popup(f'{hours} horas añadidas con éxito')
                            break
                    else:
                        sg.popup_error('Estudiante no encontrado')
                except ValueError:
                    sg.popup_error('Por favor ingrese un número válido de horas')
                except Exception as e:
                    sg.popup_error(f'Error: {str(e)}')
        add_hours_window.close()

    def reducir_horas_estudiante(self, window):
        ventana_reducir_horas = self.ventana_reducir_horas()
        while True:
            event, values = ventana_reducir_horas.read()
            if event in (sg.WIN_CLOSED, 'Cancelar'):
                break
            if event == 'Reducir Horas':
                try:
                    student_name = values['-STUDENT-']
                    activity_id = int(values['-ACTIVITY-'][0].split(':')[0])
                    hours = int(values['-HOURS-'])

                    student = self.activity_manager.obtener_estudiante_por_nombre(student_name)
                    if student:
                        result = self.activity_manager.eliminar_estudiante_de_actividad(activity_id, student, hours)
                        if result:
                            sg.popup_error(result)
                        else:
                            sg.popup(f'{hours} horas reducidas con éxito')
                            break
                    else:
                        sg.popup_error('Estudiante no encontrado')
                except ValueError:
                    sg.popup_error('Por favor ingrese un número válido de horas')
                except Exception as e:
                    sg.popup_error(f'Error: {str(e)}')
        ventana_reducir_horas.close()

    def abrir_chatbot(self, window):
        chatbot_window = self.ventana_chatbot()
        while True:
            event, values = chatbot_window.read()
            if event in (sg.WIN_CLOSED, 'Salir'):
                break
            if event == 'Enviar':
                try:
                    student_name = values['-STUDENT-']
                    mensaje = values['-INPUT-']
                    respuesta = self.chatbot.escribir_respuesta(student_name, mensaje)
                    chatbot_window['-OUTPUT-'].print(f"{student_name}: {mensaje}")
                    chatbot_window['-OUTPUT-'].print(f"ChatBot: {respuesta}")
                    chatbot_window['-INPUT-'].update('')
                except Exception as e:
                    sg.popup_error(f'Error: {str(e)}')
        chatbot_window.close()


if __name__ == '__main__':
    app = SapienciaGUI()
    app.run()