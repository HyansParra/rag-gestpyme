import pandas as pd
import google.generativeai as genai
import io
import requests

def analizar_excel_directo(url_excel, pregunta):
    """
    Descarga un Excel, lo convierte a texto usando Pandas y le pide a Gemini que lo analice matemáticamente.
    """
    try:
        # 1. Descargar el archivo
        respuesta = requests.get(url_excel)
        respuesta.raise_for_status()
        
        # 2. Leer con Pandas
        df = pd.read_excel(io.BytesIO(respuesta.content))
        
        # 3. Convertir toda la tabla a formato de texto (CSV)
        datos_texto = df.to_csv(index=False)
        
        # 4. Enviar todo el documento a Gemini para análisis matemático
        modelo = genai.GenerativeModel('gemini-2.5-flash') 
        
        prompt = f"""
        Eres un Analista de Datos para Gestpyme.
        A continuación, te presento el contenido COMPLETO de un documento financiero/facturación:
        
        {datos_texto}
        
        Por favor, actúa como una calculadora y analista. Responde a la siguiente pregunta de forma exacta, realizando las sumas o cálculos que se te pidan.
        
        Pregunta del usuario: {pregunta}
        """
        
        respuesta_ia = modelo.generate_content(prompt)
        return respuesta_ia.text
        
    except Exception as e:
        return f"Error en el análisis de datos estructurados: {e}"