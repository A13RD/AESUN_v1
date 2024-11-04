import os
from dotenv import load_dotenv
import google.generativeai as genai

# Cargar las variables de entorno desde el archivo .env
# Especifica la ruta completa del archivo si está fuera de la carpeta del código
load_dotenv('../.env')  # Asegúrate de ajustar el camino si es necesario

# Obtener la API_KEY desde el archivo .env
api_key = os.getenv("API_KEY")

# Configuración de la API de Gemini
genai.configure(api_key=api_key)
class IA:
def generar_respuesta_emocional(input_text):
    """
    Genera una respuesta emocional usando Gemini, actuando como un asistente de apoyo.
     Parámetros:
    - input_text (str): el texto de entrada que describe el estado emocional o la consulta del usuario.

    Retorna:
    - str: respuesta generada por Gemini.
    """


