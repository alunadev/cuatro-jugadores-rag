# CuatroJugadoresAI — System Architecture

## Overview
Sistema basado en RAG + Fine tuning + API de agentes.  
Componentes principales:

User → Frontend (Next.js) → Backend API (FastAPI) → RAG Engine → LLM (Gemini / GPT-finetuned)
↘ Vector DB (Supabase)

---

## 1. Frontend
- Next.js 14
- Interacción vía chat + panel de “Crear edición”
- Editor Markdown en vivo
- Sección de “Buscar consejos” (motor RAG)

---

## 2. Backend (FastAPI)
Endpoints:
- `/rag/query` → Query semántica con citas
- `/editor/generate` → Nueva edición con tu estilo
- `/train/dataset` → Generación de dataset
- `/admin/upload` → Subida de nuevos `.md` para indexación

---

## 3. RAG Layer
Pipeline:
1. Usuario pregunta o solicita edición →  
2. SearchAgent genera embedding de la query  
3. Supabase vector search por similitud  
4. Top-K chunks relevantes  
5. Se ensamblan en el prompt  
6. El modelo responde con citas

---

## 4. Data Model (resumen)
- Tabla `documents`
- Tabla `chunks`
- Tabla `embeddings`
- Tabla `queries_logs`
- Tabla `generated_editions`

---

## 5. Permissions
- Public: consultas RAG  
- Auth: generación de ediciones  
- Admin: subir corpus

---

## 6. Citation Flow
1. LLM recibe chunks con `source_id`  
2. Cuando usa contenido, añade `(ref: doc xx, chunk yy)`  
3. Frontend renderiza clickable references

---

## 7. Scaling
- Embeddings: Gemini, OpenAI o VoyageAI  
- LLM: Gemini 1.5 Pro o GPT-4.1  
- Streaming real-time