from langchain_text_splitters import RecursiveCharacterTextSplitter

def dividir_texto(texto, tamano_chunk=1000, superposicion=200):
    """
    Toma un texto largo y lo divide en fragmentos más pequeños (chunks).
    - tamano_chunk: Cantidad máxima de caracteres por fragmento.
    - superposicion: Caracteres que se repiten entre un chunk y el siguiente para no perder contexto.
    """
    try:
        text_splitter = RecursiveCharacterTextSplitter(
            chunk_size=tamano_chunk, # Tamaño máximo de cada fragmento en caracteres
            chunk_overlap=superposicion, # Cantidad de caracteres que se superponen entre fragmentos para mantener contexto
            length_function=len, # Función para medir la longitud del texto (en este caso, caracteres)
            # Intenta cortar primero por párrafos, luego por saltos de línea, luego por espacios
            separators=["\n\n", "\n", " ", ""] 
        )
        
        chunks = text_splitter.split_text(texto) # Divide el texto en fragmentos utilizando la configuración definida
        return chunks
        
    except Exception as e:
        print(f"Error al dividir el texto: {e}")
        return []