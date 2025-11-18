import re
from typing import List

def split_markdown_into_chunks(text: str, max_tokens: int = 800, overlap: int = 150) -> List[str]:
    # aproximación simple por párrafos
    paragraphs = re.split(r"\n\s*\n", text.strip())
    chunks = []
    current = []

    def length_tokens(t: str) -> int:
        # aproximación: 1 token ~ 4 caracteres
        return max(1, len(t) // 4)

    for p in paragraphs:
        candidate = ("\n\n".join(current + [p])).strip()
        if not candidate:
            continue
        if length_tokens(candidate) > max_tokens:
            if current:
                chunks.append("\n\n".join(current).strip())
            # si el párrafo ya es muy grande, lo cortamos “a lo bruto”
            if length_tokens(p) > max_tokens:
                chunks.append(p.strip())
                current = []
            else:
                current = [p]
        else:
            current.append(p)

    if current:
        chunks.append("\n\n".join(current).strip())

    # añadir solapamiento simple (reutilizar el final como inicio)
    # para simplificar, dejamos sin overlap duro: suficiente para empezar
    return chunks
