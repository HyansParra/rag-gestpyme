import os
from dotenv import load_dotenv
from supabase import create_client, Client

# Cargar las credenciales del archivo .env
load_dotenv()

def obtener_cliente_supabase() -> Client:
    """
    Inicializa la conexion con Supabase usando las variables de entorno.
    """
    url = os.environ.get("SUPABASE_URL")
    key = os.environ.get("SUPABASE_KEY")
    
    if not url or not key:
        raise ValueError("Error: Faltan las credenciales de Supabase en el archivo .env")
        
    return create_client(url, key)

def guardar_fragmentos(chunks, embeddings, url_origen):
    """
    Toma la lista de fragmentos y sus vectores para guardarlos en Supabase.
    """
    try:
        # Aqui llamamos a la funcion que obtiene el cliente de Supabase
        supabase = obtener_cliente_supabase()
        
        datos_a_insertar = []
        for i in range(len(chunks)):
            registro = {
                "contenido": chunks[i],
                "embedding": embeddings[i],
                "metadata": {"fuente": url_origen, "indice": i}
            }
            datos_a_insertar.append(registro)
        
        # Realizamos la insercion masiva en la tabla
        supabase.table("documentos_gestpyme").insert(datos_a_insertar).execute()
        return True
    except Exception as e:
        print(f"Error al guardar en Supabase: {e}")
        return False