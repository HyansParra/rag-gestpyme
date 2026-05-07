import requests # necesario para hacer la petición HTTP y descargar el archivo
import os # necesario para manejar rutas de archivos y directorios

def descargar_archivo_desde_url(url, carpeta_destino="temp_files"):
    try:
        print(f"Iniciando descarga desde: {url}...")
        
        # Hace la petición a la web
        respuesta = requests.get(url)
        respuesta.raise_for_status()  # Lanza un error si la URL está caída o no existe
        
        # Obtenemos el nombre del archivo desde la misma URL
        nombre_archivo = url.split("/")[-1]
        ruta_guardado = os.path.join(carpeta_destino, nombre_archivo)
        
        # Guarda el contenido binario (wb = write binary) en nuestro disco
        with open(ruta_guardado, 'wb') as archivo:
            archivo.write(respuesta.content)
            
        print(f"Archivo guardado como: {ruta_guardado}")
        return ruta_guardado
        
    except Exception as e:
        print(f"Error al intentar descargar: {e}")
        return None

# Prueba con un PDF público de ejemplo
url_de_prueba = "https://www.w3.org/WAI/ER/tests/xhtml/testfiles/resources/pdf/dummy.pdf"
descargar_archivo_desde_url(url_de_prueba)