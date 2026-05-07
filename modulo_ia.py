import os
import google.generativeai as genai
from dotenv import load_dotenv

load_dotenv()

# Configurar la clave de API de Google
genai.configure(api_key=os.environ.get("GEMINI_API_KEY"))

def generar_embedding(texto):
    """
    Transforma un fragmento de texto en una lista de números (vector) usando Gemini.
    """
    try:
        resultado = genai.embed_content(
            model="models/text-embedding-004",
            content=texto,
            task_type="retrieval_document"
        )
        return resultado['embedding']
    except Exception as e:
        print(f"Error al generar embedding: {e}")
        return None