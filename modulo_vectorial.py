import os
from dotenv import load_dotenv
from supabase import create_client, Client

# Cargar las credenciales del archivo .env
load_dotenv()

def obtener_cliente_supabase() -> Client:
    """
    Inicializa la conexión con Supabase usando las variables de entorno.
    """
    url = os.environ.get("SUPABASE_URL")
    key = os.environ.get("SUPABASE_KEY")
    
    if not url or not key:
        raise ValueError("Error: Faltan las credenciales de Supabase en el archivo .env")
        
    return create_client(url, key)