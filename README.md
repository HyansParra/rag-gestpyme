# Sistema RAG y Agente de Análisis de Datos - Gestpyme

Proyecto de práctica profesional desarrollado en **Gestpyme**. 
Este sistema permite la ingesta, procesamiento vectorial y consulta semántica de documentos (PDF, Word), y cuenta con un agente especializado en el análisis de datos estructurados (Excel) utilizando Inteligencia Artificial.

## Características Principales
* **Modo RAG (Documentos):** Segmentación de texto (Chunking) y búsqueda vectorial con Supabase para comprensión lectora de manuales, contratos y normativas.
* **Modo Analista (Datos Estructurados):** Integración con Pandas para procesar archivos Excel completos, permitiendo a la IA realizar cálculos matemáticos complejos, sumas y resúmenes financieros.
* **Ingesta Universal:** Descarga y procesamiento automático desde múltiples tipos de enlaces.
* **Interfaz Interactiva:** Chatbot unificado y moderno construido con Streamlit.

## Stack Tecnológico
* **Lenguaje:** Python 3.10+
* **Datos y Orquestación:** Pandas, LangChain
* **IA / Embeddings:** Google Gemini (gemini-2.5-flash y gemini-embedding-001)
* **Base de Datos:** Supabase (PostgreSQL + extensión pgvector)
* **Frontend:** Streamlit

## Instalación y Configuración Inicial
1. Clonar el repositorio.
2. Crear un entorno virtual: `python -m venv venv`
3. Activar el entorno: `.\venv\Scripts\activate`
4. Instalar las dependencias: `pip install -r requirements.txt`
5. Crear un archivo `.env` en la raíz del proyecto con el siguiente formato:
   ```env
   SUPABASE_URL="tu_url_de_supabase_aqui"
   SUPABASE_KEY="tu_anon_key_aqui"
   GEMINI_API_KEY="tu_api_key_de_google_aqui"

## Instrucciones de Uso
El asistente opera en dos modalidades directamente desde la barra de chat:

### 1. Búsqueda Documental (Texto)
Ideal para extraer reglas o resúmenes de documentos de texto.
- **Para guardar información:** Pega directamente el enlace del documento (ej. `http://ruta/manual.pdf`). El sistema lo fragmentará y guardará en la base de datos.
- **Para consultar:** Escribe tu pregunta de forma natural (ej. *"¿Cuáles son las políticas de la empresa según los documentos?"*).

### 2. Modo Analista (Cálculos en Excel)
Ideal para sumar facturas, buscar totales o cruzar datos en tablas. No usa la base de datos, lee el archivo en tiempo real.
- Usa la palabra clave **Analizar**, seguida del link del Excel y tu pregunta matemática.
- **Ejemplo de uso:** `Analizar http://ruta/facturas.xlsx ¿Cuál es la suma total de las ganancias del mes de enero?`