import os
import google.generativeai as genai
from dotenv import load_dotenv

load_dotenv()

genai.configure(api_key=os.environ.get("GEMINI_API_KEY"))

def generar_embedding(texto):
    """
    Transforma un fragmento de texto en un vector.
    Manejo de errores desactivado temporalmente para depuracion.
    """
    resultado = genai.embed_content(
        model="models/gemini-embedding-001",  # <-- Actualizado al estandar 2026
        content=texto,
        task_type="retrieval_document"
    )
    return resultado['embedding']