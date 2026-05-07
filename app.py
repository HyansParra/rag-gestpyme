import streamlit as st # Interfaz de usuario
from ingesta_universal import obtener_texto_universal # Función para descargar y extraer texto de documentos
from modulo_chunking import dividir_texto # Función para dividir texto en fragmentos (chunks)

# Configuración inicial de la página
st.set_page_config(page_title="Gestpyme - Asistente RAG", layout="centered")

st.title("Asistente de Documentación Inteligente")
st.markdown("Ingrese el enlace de un documento para procesarlo o realice consultas sobre la información ya almacenada.")

# Inicializar historial de chat si no existe
if "messages" not in st.session_state:
    st.session_state.messages = []

# Mostrar historial de mensajes
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Barra de entrada de chat para el usuario
if prompt := st.chat_input("Pegue un enlace o realice una pregunta..."):
    
    # Agregar mensaje del usuario al historial
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    # Lógica de respuesta
    with st.chat_message("assistant"):
        # Detectar si el input es una URL
        if prompt.startswith("http"):
            with st.spinner("Procesando documento..."):
                texto = obtener_texto_universal(prompt)
                if texto:
                    chunks = dividir_texto(texto)
                    respuesta = f"Documento procesado correctamente. Se han generado {len(chunks)} fragmentos y están listos para ser almacenados en la base de datos."
                else:
                    respuesta = "No se pudo extraer información del enlace proporcionado. Verifique que el archivo sea un PDF, Word o Excel válido."
        else:
            # Lógica de chat futura
            respuesta = "Funcionalidad de chat aún no implementada. Por ahora, solo se pueden procesar documentos a través de enlaces."
        
        st.markdown(respuesta)
        st.session_state.messages.append({"role": "assistant", "content": respuesta})