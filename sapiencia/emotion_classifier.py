import os
from dotenv import load_dotenv
import google.generativeai as genai
load_dotenv('../.env')
api_key = os.getenv("API_KEY")
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




