from typing import List, Dict

def build_rag_prompt(query: str, contexts: List[Dict]) -> str:
    context_texts = []
    for ctx in contexts:
        context_texts.append(
            f"[doc: {ctx['doc_name']} | chunk: {ctx['chunk_index']}]\n{ctx['content']}"
        )
    ctx_block = "\n\n---\n\n".join(context_texts)

    return f"""
Eres el autor de "Cuatro Jugadores de Pádel". 
Responde en tu tono: cercano, didáctico, en segunda persona, priorizando control, punto de impacto, jugar de lado, armado corto.

Pregunta del usuario:
\"\"\"{query}\"\"\"

Contexto relevante (no inventes fuera de esto):
{ctx_block}

Instrucciones:
- Usa el contexto siempre que puedas.
- Si no hay contexto suficiente, dilo claramente.
- Cuando uses información concreta, añade una cita en el formato (ref: {{doc_name}}, chunk {{chunk_index}}).
- Explica con claridad y, cuando tenga sentido, estructura en cuatro puntos.

Respuesta:
""".strip()
