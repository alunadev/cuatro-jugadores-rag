# Search System — Deep Dive

## Overview
RAG search para:
- Preguntas de usuarios
- Generación de ediciones
- Corrección técnica
- Análisis táctico

---

## 1. Query Pipeline
1. Normalize:
   - lower
   - remove fillers
2. Expand query with synonyms:
   - “bajarlo” → “ralentizar”, “bajar velocidad”
3. embedding(query)
4. ANN search (pgvector)
5. rerank con Gemini-Pro-Reranker
6. entregar chunks + score

---

## 2. Chunking Strategy
- 800 tokens + 150 overlap
- Preserve HTML (mantener imágenes intactas)
- Títulos como anchors

---

## 3. Citation Handling
- Cada chunk tiene:
  - doc_id
  - chunk_index
  - source_path
- LLM genera citas:
  `(ref: doc 03, chunk 12)`

---

## 4. Relevancy Rules
- Penalizar repetición
- Priorizar:
  - coincidencia de golpe (drive, revés…)
  - posición (fondo, red…)
  - intención (defensa, ataque…)

---

## 5. Hybrid Search
Combina:
- Semántica (embeddings)
- Keywords (“bandeja”, “víbora”, “pared”)

Resultado: alta precisión + explicabilidad.
