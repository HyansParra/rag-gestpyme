import requests # necesario para hacer la petición HTTP y descargar el archivo
import fitz  # PyMuPDF necesario para abrir el PDF y extraer su texto
import os # necesario para manejar rutas de archivos y directorios

def procesar_pdf_desde_url(url, carpeta_destino="temp_files"):
    print(f"Iniciando descarga desde: {url}...")
    
    try:
        # --- ETAPA 1: DESCARGA ---
        respuesta = requests.get(url)
        respuesta.raise_for_status() 
        
        nombre_archivo = url.split("/")[-1]
        ruta_guardado = os.path.join(carpeta_destino, nombre_archivo)
        
        with open(ruta_guardado, 'wb') as archivo:
            archivo.write(respuesta.content) 
            
        print(f"Descarga exitosa. Archivo temporal guardado en: {ruta_guardado}")
        
        # --- ETAPA 2: EXTRACCIÓN DE TEXTO ---
        print("Leyendo el contenido del documento...")
        documento = fitz.open(ruta_guardado) # Abrimos el PDF con PyMuPDF
        texto_completo = "" # Variable para acumular el texto de todas las páginas
        
        # Recorre todas las páginas y une el texto
        for numero_pagina in range(documento.page_count):
            pagina = documento[numero_pagina]
            texto_completo += pagina.get_text() + "\n" # Agrega un salto de línea entre páginas
            
        documento.close()
        print("Texto extraído con éxito")
        
        # --- ETAPA 3: LIMPIEZA (buena práctica) ---
        # Borramos el PDF temporal para no llenar el disco duro
        os.remove(ruta_guardado)
        print("Archivo temporal eliminado")
        
        return texto_completo

    except Exception as e:
        print(f"Ocurrió un error en el proceso: {e}")
        return None

# Probamos el flujo completo
url_de_prueba = "https://www.w3.org/WAI/ER/tests/xhtml/testfiles/resources/pdf/dummy.pdf"
texto_final = procesar_pdf_desde_url(url_de_prueba)

if texto_final:
    print("\n--- INICIO DEL TEXTO DEL SISTEMA ---")
    print(texto_final.strip())
    print("--- FIN DEL TEXTO ---")