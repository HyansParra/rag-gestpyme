import streamlit as st # libreria para crear interfaces web interactivas con Python
from ingesta_universal import obtener_texto_universal # funcion para extraer texto de diversas fuentes
from modulo_chunking import dividir_texto # funcion para segmentar texto en fragmentos manejables
from modulo_ia import generar_embedding, generar_respuesta # funciones para generar vectores de texto y respuestas inteligentes usando Gemini
from modulo_vectorial import guardar_fragmentos, buscar_similitud # funciones para interactuar con la base de datos vectorial (Supabase)
from modulo_analisis import analizar_excel_directo # funcion para analizar directamente archivos Excel con Gemini

# Configuracion de la interfaz
st.set_page_config(page_title="Gestpyme - Asistente RAG", layout="centered")

st.title("Asistente de Documentacion Inteligente")
st.markdown("Ingrese el enlace de un documento para su procesamiento vectorial o realice consultas sobre la informacion almacenada.")

# Gestion del estado del chat
if "messages" not in st.session_state:
    st.session_state.messages = []

# Despliegue del historial de interaccion en la interfaz
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Captura de entrada del usuario
if prompt := st.chat_input("Ingrese una URL de documento o su consulta..."):
    
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    with st.chat_message("assistant"):
        
        # Modo analisis de datos estructurados (Pandas + Gemini)
        if prompt.lower().startswith("analizar"):
            with st.spinner("Modo Analista: Leyendo documento estructurado y calculando..."):
                # Se espera un formato como: "Analizar http://link_al_excel.xlsx ¿Cuál es el total?"
                partes = prompt.split(" ", 2) 
                if len(partes) >= 3:
                    comando = partes[0]
                    url = partes[1]
                    pregunta_matematica = partes[2]
                    
                    respuesta = analizar_excel_directo(url, pregunta_matematica)
                else:
                    respuesta = "Por favor usa el formato exacto: Analizar [URL_DEL_EXCEL] [Tu pregunta matemática]"
            
            st.markdown(respuesta)
            st.session_state.messages.append({"role": "assistant", "content": respuesta})

        # Logica de procesamiento para entradas de tipo URL (Base de datos vectorial)
        elif prompt.startswith("http"):
            with st.spinner("Ejecutando ciclo de ingesta, fragmentacion y vectorizacion..."):
                texto = obtener_texto_universal(prompt)
                
                if texto:
                    chunks = dividir_texto(texto)
                    embeddings = [generar_embedding(c) for c in chunks]
                    exito = guardar_fragmentos(chunks, embeddings, prompt)
                    
                    if exito:
                        respuesta = f"Procesamiento finalizado. Se han generado y almacenado {len(chunks)} fragmentos vectorizados en la base de datos."
                    else:
                        respuesta = "Error en la fase de persistencia. Los datos no pudieron ser almacenados en Supabase."
                else:
                    respuesta = "Error en la fase de ingesta. No se pudo extraer informacion del enlace proporcionado."
            
            st.markdown(respuesta)
            st.session_state.messages.append({"role": "assistant", "content": respuesta})
            
        # LÓGICA DEL CHATBOT - FASE DE CONSULTA (Respuestas basadas en texto)
        else:
            with st.spinner("Buscando en la base de datos y analizando contexto..."):
                # 1. Convertir la pregunta en un vector
                vector_pregunta = generar_embedding(prompt)
                
                if vector_pregunta:
                    # 2. Buscar similitudes en Supabase
                    resultados = buscar_similitud(vector_pregunta, limite=3)
                    
                    if resultados:
                        # 3. Extraer solo el texto para armar el contexto
                        contexto = "\n\n".join([item['contenido'] for item in resultados])
                        
                        # 4. Generar la respuesta inteligente
                        respuesta = generar_respuesta(prompt, contexto)
                        
                        # Añadir las fuentes al final de la respuesta
                        fuentes = set([item['metadata']['fuente'] for item in resultados])
                        respuesta += f"\n\n---\n*Fuentes consultadas: {', '.join(fuentes)}*"
                        
                    else:
                        respuesta = "No encontré información en la base de datos relacionada con tu pregunta."
                else:
                    respuesta = "Hubo un problema al procesar la pregunta con el modelo de IA."
            
            st.markdown(respuesta)
            st.session_state.messages.append({"role": "assistant", "content": respuesta})