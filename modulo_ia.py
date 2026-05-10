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

def generar_respuesta(pregunta, contexto):
    """
    Genera una respuesta utilizando Gemini basada estrictamente en el contexto proporcionado.
    """
    try:
        # Actualizado al modelo actual y estable de Google
        modelo = genai.GenerativeModel('gemini-2.5-flash')
        
        # Creamos el "Prompt" o instrucción estricta
        prompt = f"""
        Eres un asistente corporativo experto para la empresa Gestpyme.
        Tu tarea es responder a la pregunta del usuario utilizando ÚNICAMENTE la información proporcionada en el siguiente Contexto.
        Si la respuesta no se encuentra en el Contexto, debes decir exactamente: "Lo siento, no tengo información sobre eso en los documentos procesados." 
        No inventes información bajo ninguna circunstancia.

        Contexto:
        {contexto}

        Pregunta del usuario: {pregunta}
        """
        
        # Le enviamos el prompt a Gemini
        respuesta = modelo.generate_content(prompt)
        return respuesta.text
        
    except Exception as e:
        print(f"Error al generar respuesta con Gemini: {e}")
        return "Lo siento, ocurrió un error interno de conexión con la inteligencia artificial."