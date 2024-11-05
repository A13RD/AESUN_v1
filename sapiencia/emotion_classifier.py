import os
from dotenv import load_dotenv
import google.generativeai as genai
load_dotenv('../.env')
api_key = os.getenv("API_KEY")
genai.configure(api_key=api_key)
class IA:
    @staticmethod
    def generar_respuesta_emocional(input_text):
        """
        Genera una respuesta emocional usando Gemini, actuando como un asistente de apoyo.
         Parámetros:
        - input_text (str): el texto de entrada que describe el estado emocional o la consulta del usuario.
         Retorna:
        - str: respuesta generada por Gemini.
        """
        # Define el prompt para asistencia emocional
        prompt = f"Actúa como un asistente emocional. Alguien te dice: '{input_text}'. Responde con empatía y apoyo emocional."



# Ejemplo de uso
input_text = "Me siento un poco triste y solo últimamente. ¿Qué me aconsejas?"
respuesta = generar_respuesta_emocional(input_text)
print(respuesta)





