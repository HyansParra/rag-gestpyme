import streamlit as st # libreria para crear interfaces web interactivas con Python
from ingesta_universal import obtener_texto_universal # funcion para extraer texto de diversas fuentes
from modulo_chunking import dividir_texto # funcion para segmentar texto en fragmentos manejables
from modulo_ia import generar_embedding # funcion para convertir texto en vectores usando Gemini
from modulo_vectorial import guardar_fragmentos # funcion para almacenar fragmentos y vectores en Supabase

# Configuracion de la interfaz
st.set_page_config(page_title="Gestpyme - Asistente RAG", layout="centered")

st.title("Asistente de Documentacion Inteligente")
st.markdown("Ingrese el enlace de un documento para su procesamiento vectorial o realice consultas sobre la informacion almacenada.")

# Gestion del estado del chat
if "messages" not in st.session_state:
    st.session_state.messages = []

# Despliegue del historial de interaccion
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Captura de entrada del usuario
if prompt := st.chat_input("Ingrese una URL de documento o su consulta..."):
    
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    with st.chat_message("assistant"):
        # Logica de procesamiento para entradas de tipo URL
        if prompt.startswith("http"):
            with st.spinner("Ejecutando ciclo de ingesta, fragmentacion y vectorizacion..."):
                # Fase 1: Extraccion de contenido
                texto = obtener_texto_universal(prompt)
                
                if texto:
                    # Fase 2: Segmentacion de texto (Chunking)
                    chunks = dividir_texto(texto)
                    
                    # Fase 3: Generacion de representaciones vectoriales (Embeddings)
                    embeddings = [generar_embedding(c) for c in chunks]
                    
                    # Fase 4: Persistencia en base de datos vectorial (Supabase)
                    exito = guardar_fragmentos(chunks, embeddings, prompt)
                    
                    if exito:
                        respuesta = f"Procesamiento finalizado. Se han generado y almacenado {len(chunks)} fragmentos vectorizados en la base de datos."
                    else:
                        respuesta = "Error en la fase de persistencia. Los datos no pudieron ser almacenados en Supabase."
                else:
                    respuesta = "Error en la fase de ingesta. No se pudo extraer informacion del enlace proporcionado."
        
        # Logica para consultas de lenguaje natural sobre los datos almacenados con IA
        else:
            respuesta = "Consultas sobre datos no implementadas actualmente"
        
        st.markdown(respuesta)
        st.session_state.messages.append({"role": "assistant", "content": respuesta})