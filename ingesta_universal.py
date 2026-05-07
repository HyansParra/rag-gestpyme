import requests # necesario para hacer la petición HTTP y descargar el archivo
import os # necesario para manejar rutas de archivos y directorios
import fitz  # PyMuPDF para PDF
from docx import Document  # para Word
import pandas as pd  # para Excel

def obtener_texto_universal(url):
    """
    Descarga un archivo desde una URL, detecta su tipo y extrae el texto.
    Soporta PDF, DOCX y XLSX.
    """
    try:
        # Crear carpeta temporal si no existe
        if not os.path.exists("temp_files"):
            os.makedirs("temp_files")

        print(f"Procesando: {url}")
        
        # 1. Ingesta (Descarga)
        respuesta = requests.get(url, timeout=10) # Agregamos un timeout para evitar bloqueos largos
        respuesta.raise_for_status() # Verifica que la descarga fue exitosa
        
        nombre_archivo = url.split("/")[-1] # Extraemos el nombre del archivo de la URL
        ruta_temporal = os.path.join("temp_files", nombre_archivo)
        
        with open(ruta_temporal, 'wb') as f:
            f.write(respuesta.content)
        
        # 2. Extracción (Parsing) según extensión del archivo
        extension = nombre_archivo.lower() # Convertimos a minúsculas para evitar problemas con mayúsculas
        texto_extraido = "" # Variable para almacenar el texto extraído

        if extension.endswith(".pdf"):
            doc = fitz.open(ruta_temporal) # Abrimos el PDF con PyMuPDF
            for pagina in doc:
                texto_extraido += pagina.get_text() + "\n" # Agrega un salto de línea entre páginas
            doc.close()
            
        elif extension.endswith(".docx"):
            doc = Document(ruta_temporal) # Abrimos el Word con python-docx
            texto_extraido = "\n".join([p.text for p in doc.paragraphs if p.text.strip()]) # Une los párrafos con saltos de línea, solo si tienen texto
            
        elif extension.endswith((".xlsx", ".xls")):
            # Openpyxl es necesario para archivos .xlsx
            df = pd.read_excel(ruta_temporal) # Lee el Excel con pandas
            texto_extraido = df.to_string(index=False)
        
        else:
            print(f"Formato '{extension}' no soportado actualmente.") 
            return None

        # 3. Limpieza de archivos temporales
        if os.path.exists(ruta_temporal):
            os.remove(ruta_temporal) # Elimina el archivo temporal para no llenar el disco duro
            
        print(f"Procesado con éxito. Caracteres extraídos: {len(texto_extraido)}")
        return texto_extraido

    except Exception as e:
        print(f"Error en el orquestador: {e}")
        return None

# --- Bloque de ejecución para pruebas ---
if __name__ == "__main__":
    # Insertar URL de prueba (puede ser PDF, DOCX o XLSX)
    url_prueba = "https://calibre-ebook.com/downloads/demos/demo.docx"
    resultado = obtener_texto_universal(url_prueba)
    
    if resultado:
        print("\n--- VISTA PREVIA DEL RESULTADO ---")
        print(resultado[:300] + "...") # Mostrar solo los primeros 300 caracteres para no saturar la consola
        print("--- FIN DE LA VISTA PREVIA ---")