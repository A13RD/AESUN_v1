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


