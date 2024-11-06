import os
from dotenv import load_dotenv
import google.generativeai as genai
from typing import Optional


class IA:
    def __init__(self):
        load_dotenv()
        api_key = os.getenv("API_KEY")
        if not api_key:
            raise ValueError ("API_KEY no encontrada en el archivo .env")
        genai.configure(api_key=api_key)
        self.model = genai.GenerativeModel("gemini-1.5-flash")

    def generar_respuesta_emocional(self, input_text: str) -> Optional[str]:
        """
        Genera una respuesta emocional usando Gemini, actuando como un asistente de apoyo.
         Parámetros:
        - input_text (str): el texto de entrada que describe el estado emocional o la consulta del usuario.
         Retorna:
        - str: respuesta generada por Gemini.
        """
        try:
            prompt = f"Actúa como un asistente emocional. Alguien te dice: '{input_text}'. Responde con empatía y apoyo emocional."
            response = self.model.generate_content(prompt)
            return response.text

        except Exception as e:
            print(f"Error al generar respuesta: {str(e)}")
            return None

