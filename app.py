import streamlit as st # Importamos Streamlit para la interfaz web
from ingesta_universal import obtener_texto_universal # Importamos nuestro módulo de extracción universal
from modulo_chunking import dividir_texto  # Importamos nuestro nuevo módulo

# Configuración de la página
st.set_page_config(page_title="Gestpyme - RAG")

st.title("Sistema de Ingesta y Procesamiento RAG")
st.markdown("""
Esta avance representa las Fases 1 y 2 del sistema RAG:
- Fase 1: Ingesta y Extracción: Descarga documentos (PDF, Word, Excel) desde una URL, extrae la información y la segmenta en fragmentos lógicos (Chunking) para la IA.
- Fase 2: Chunking: Aplica técnicas de segmentación utilizando LangChain para dividir el texto extraído en fragmentos manejables (chunks) que mantengan el contexto necesario para la IA. 
""")

# Input de la URL
url_input = st.text_input("Pega aquí la URL del documento:")

if st.button("Procesar Documento"):
    if url_input:
        # FASE 1: EXTRACCIÓN
        with st.spinner("Fase 1: Descargando y extrayendo texto..."):
            texto = obtener_texto_universal(url_input)
            
            if texto:
                st.success("Documento extraído con éxito")
                
                # FASE 2: CHUNKING
                with st.spinner("Fase 2: Aplicando segmentación (Chunking) con LangChain..."):
                    chunks = dividir_texto(texto)
                
                # Mostramos métricas de ambas fases 
                col1, col2, col3 = st.columns(3)
                col1.metric("Caracteres Totales", len(texto))
                col2.metric("Fragmentos Generados", len(chunks))
                col3.metric("Estado", "Listo para Vectorizar")
                
                st.divider()
                
                # Vista previa de los Chunks generados
                st.subheader("Vista previa de los Fragmentos (Chunks)")
                st.write("Así es como la Inteligencia Artificial leerá el documento:")
                
                # Un componente desplegable para no saturar la pantalla
                with st.expander("Ver los primeros 3 fragmentos generados"):
                    for i, chunk in enumerate(chunks[:3]):
                        st.markdown(f"**Fragmento {i+1}** *(Largo: {len(chunk)} caracteres)*")
                        st.info(chunk)
            else:
                st.error("No se pudo procesar el archivo. Revisa que la URL sea válida.")
    else:
        st.warning("Por favor, ingresa una URL.")