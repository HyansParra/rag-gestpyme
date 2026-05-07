import pandas as pd # librería para manejar Excel, la usare para leer el archivo y convertirlo a texto

def extraer_datos_excel(ruta_archivo):
    try:
        print(f"Leyendo Excel: {ruta_archivo}...")
        
        # Lee el archivo, si tiene varias hojas, esto lee la primera por defecto
        df = pd.read_excel(ruta_archivo)
        
        # Convierte el contenido de la tabla a una cadena de texto
        # Usamos to_string() para que mantenga una estructura legible
        texto_final = df.to_string(index=False)
        
        print("\n--- CONTENIDO DEL EXCEL ---")
        print(texto_final)
        print("--- FIN DEL CONTENIDO ---\n")
        
        return texto_final
        
    except Exception as e:
        print(f"Error al leer Excel: {e}")
        return None

# Prueba local
ruta_excel = "temp_files/datos_prueba.xlsx"
extraer_datos_excel(ruta_excel)