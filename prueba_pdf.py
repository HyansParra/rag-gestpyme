import fitz  # PyMuPDF librería para manipular archivos PDF

def extraer_texto_pdf(ruta_archivo):
    try:
        # Abre el documento
        documento = fitz.open(ruta_archivo)
        print(f"PDF abierto, Total de páginas: {documento.page_count}")
        
        # Selecciona la primera página (índice 0)
        primera_pagina = documento[0]
        
        # Extraemos el texto
        texto = primera_pagina.get_text()
        
        print("\n--- INICIO DEL TEXTO EXTRAÍDO ---")
        print(texto)
        print("--- FIN DEL TEXTO EXTRAÍDO ---\n")
        
        # Cerramos el documento para liberar recursos
        documento.close()
        
    except Exception as e:
        print(f"Error al intentar leer el PDF: {e}")

# Ejecuta la función apuntando al archivo de prueba
ruta_de_prueba = "temp_files/documento.pdf"
extraer_texto_pdf(ruta_de_prueba)