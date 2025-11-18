# CuatroJugadoresAI — Agents Specification

## Overview
CuatroJugadoresAI es un sistema híbrido: RAG + GPT entrenado con el estilo del autor. 
Opera con tres agentes principales:

1. **EditorAgent**
   - Genera nuevas ediciones siguiendo:
     - estructura obligatoria (intro, puntos 1-4, CTA, footer)
     - tono del autor
     - referencias internas
   - Usa RAG para detectar si un tema está previamente tratado.

2. **CoachAgent**
   - Contesta preguntas de usuarios sobre técnica/táctica de pádel.
   - Usa vector search + citas.
   - Mantiene el enfoque de “enseñanza sencilla en cuatro puntos”.

3. **SearchAgent**
   - Optimiza y ejecuta las queries semánticas.
   - Aplica filtros por edición, concepto técnico, tipo de golpe o nivel.
   - Retorna chunks con “source_id” para cita.

## Document Interaction
El sistema se alimenta de 5 documentos base:

- 01_Fundamentos…
- 02_Paredes…
- 03_Juego_aereo…
- 04_Tactica…
- 05_Mentalidad…

Estos están particionados en chunks y almacenados en Supabase para retrieval.

## Shared Tone Rules
Todos los agentes aplican:
- Cercanía, empatía, lenguaje directo.
- Explicar en cuatro puntos cuando sea aplicable.
- Acción y didáctica sobre teoría.
- Tono positivo, sin tecnicismos innecesarios.
- Segunda persona “tú”.

## Citation System
Cada chunk en Supabase tiene:
- `doc_id`
- `chunk_id`
- `source_path`
- `content`
- `embedding`

Los agentes citan con formato:
> “...texto...” *(ref: doc 02, chunk 14)*

