# User Flows Documentation

## 1. Crear nueva edición
1. Usuario entra en “Crear edición”
2. Indica:
   - Tema
   - Enfoque (técnico / táctico / mental)
   - Aspectos clave
3. EditorAgent:
   - Consulta RAG
   - Genera borrador completo
4. Usuario edita en Markdown
5. Guarda y exporta a ZIP/Substack

## 2. Buscar un consejo
1. Usuario escribe: “cómo defender globos”
2. SearchAgent:
   - Embedding → retrieval → citas
3. Respuesta con 4 puntos + referencias

## 3. Añadir nuevo documento
1. Admin sube `.md`
2. Backend particiona en chunks
3. Genera embeddings
4. Inserta en Supabase

## 4. Entrenar el modelo
1. Admin selecciona ediciones
2. Backend genera dataset JSONL
3. Lanza fine-tuning (Gemini o GPT)
4. Nuevo modelo se asigna a EditorAgent
