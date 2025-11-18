# cuatro-jugadores-rag

Sistema RAG + redactor entrenado con las ediciones de **Cuatro Jugadores de Pádel**.

## Qué hace

- RAG (búsqueda semántica con citas) sobre tus 5 volúmenes `.md`.
- API para:
  - `/rag/query`: preguntas tipo “cómo mejorar mi bandeja”.
  - `/editor/generate`: generar nuevas ediciones con tu tono.
- Frontend Next.js:
  - Chat RAG.
  - Pantalla “Crear edición”.

## Stack

- Backend: FastAPI + Supabase (PostgreSQL + pgvector)
- Frontend: Next.js 14 (app router)
- RAG engine: Python (packages/rag-core)
- Embeddings / LLM: Gemini (o compatible)

## Setup rápido

1. Clona el repo
2. Copia tus `.md` a `data/corpus/`
3. Configura `.env` desde `.env.example`
4. Crea BD y aplica `supabase/schema.sql`
5. Instala backend:

   ```bash
   cd apps/api
   pip install -r requirements.txt
