# Sapiencia - Sistema de Gestión de Estudiantes y Actividades

Sapiencia es una aplicación de gestión de actividades y horas de estudiantes desarrollada en Python. Permite a los directores gestionar actividades y a los estudiantes visualizar y actualizar sus horas. También incluye un chatbot emocional para ofrecer apoyo a los estudiantes.

## Características

- **Gestión de Actividades**: Los directores pueden crear, ver y exportar actividades, así como inscribir o eliminar estudiantes.
- **Registro de Horas**: Los estudiantes pueden ver, agregar o reducir sus horas en actividades específicas.
- **ChatBot Emocional**: Un asistente virtual que ofrece apoyo emocional mediante mensajes empáticos.

## Requisitos del Sistema

- Python 3.7 o superior

## Instalación

1. Clona el repositorio:

   ```bash
   git clone https://github.com/A13RD/AESUN_v1
   cd AESUN_v1
   ```

2. Instala las dependencias:

   ```bash
   pip install -r requirements.txt
   ```

3. Configura tu archivo `.env` con la API Key para el modelo generativo Gemini:

   ```
   API_KEY=la_api_key
   ```

## Uso

Para ejecutar la aplicación:

```bash
python main.py
```

1. **Rol del Director**: Permite gestionar actividades, preinscribir o eliminar estudiantes, y exportar actividades a un archivo Excel.
2. **Rol del Estudiante**: Permite ver, agregar o reducir horas y acceder al chatbot para obtener apoyo emocional.

## Dependencias

Consulta el archivo `requirements.txt` para obtener una lista completa de las dependencias necesarias.

## Estructura del Proyecto

- **main.py**: Archivo principal que ejecuta la interfaz gráfica (GUI) con PySimpleGUI.
- **sapiencia/**: Carpeta que contiene los módulos del proyecto.
  - **model.py**: Define la lógica para la gestión de actividades y estudiantes.
  - **emotion_classifier.py**: Implementa el chatbot emocional.
  - **registro_horas.py**: Maneja el registro de horas y asistencia.


