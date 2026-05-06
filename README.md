# Sistema RAG - Consulta de Documentos Inteligente

Proyecto de práctica profesional desarrollado en **Gestpyme**. 
Este sistema permite la ingesta, procesamiento y consulta semántica de documentos multiformato (PDF, Word, Excel) mediante Inteligencia Artificial.

## Características Principales
* **Multiformato:** Extracción de texto desde múltiples tipos de archivos.
* **Procesamiento Inteligente:** Segmentación de texto (Chunking) para optimizar el contexto.
* **Búsqueda Vectorial:** Almacenamiento y consulta de embeddings utilizando Supabase (pgvector).
* **Interfaz de Usuario:** Chatbot interactivo construido con Streamlit.

## Stack Tecnológico
* **Lenguaje:** Python 3.10+
* **Orquestador:** LangChain
* **IA / Embeddings:** Google Gemini
* **Base de Datos:** Supabase
* **Frontend:** Streamlit

## Instalación y Configuración Inicial
1. Clonar el repositorio.
2. Crear un entorno virtual: `python -m venv venv`
3. Activar el entorno: `.\venv\Scripts\activate`
4. Instalar las dependencias: pip install -r requirements.txt