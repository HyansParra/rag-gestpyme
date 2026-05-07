import requests # necesario para hacer la petición HTTP y descargar el archivo
import os # necesario para manejar rutas de archivos y directorios
from docx import Document # Importamos la librería para Word

def descargar_y_leer_word(url, carpeta_destino="temp_files"):
    try:
        # --- DESCARGA ---
        print(f"Descargando desde: {url}")
        respuesta = requests.get(url)
        respuesta.raise_for_status()
        
        nombre_archivo = url.split("/")[-1]
        ruta_guardado = os.path.join(carpeta_destino, nombre_archivo)
        
        with open(ruta_guardado, 'wb') as f:
            f.write(respuesta.content)
        
        # --- EXTRACCIÓN (Si es .docx) ---
        if ruta_guardado.endswith('.docx'):
            doc = Document(ruta_guardado)
            texto = "\n".join([p.text for p in doc.paragraphs if p.text.strip()])
            print("Texto de Word extraído correctamente.")
            print(f"Primeros 200 caracteres: {texto[:200]}...")
        else:
            print("El archivo descargado no parece ser un Word (.docx)")

        # Limpieza
        os.remove(ruta_guardado)
        
    except Exception as e:
        print(f"Falló el proceso: {e}")

# URL de prueba
url_word = "https://calibre-ebook.com/downloads/demos/demo.docx"
descargar_y_leer_word(url_word)