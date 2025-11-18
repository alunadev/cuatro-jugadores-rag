from typing import List, Dict, Any
import psycopg2
import os
from .embeddings import get_embedding

DATABASE_URL = os.getenv("DATABASE_URL")

def get_connection():
    return psycopg2.connect(DATABASE_URL)

def search_chunks(query: str, k: int = 8) -> List[Dict[str, Any]]:
    query_vec = get_embedding(query)
    with get_connection() as conn:
        with conn.cursor() as cur:
            cur.execute(
                """
                select
                  c.id,
                  c.content,
                  c.doc_id,
                  c.chunk_index,
                  d.name,
                  1 - (e.vector <=> %s::vector) as score
                from embeddings e
                join chunks c on c.id = e.chunk_id
                join documents d on d.id = c.doc_id
                order by e.vector <=> %s::vector
                limit %s;
                """,
                (query_vec, query_vec, k),
            )
            rows = cur.fetchall()

    results = []
    for row in rows:
        chunk_id, content, doc_id, chunk_index, doc_name, score = row
        results.append(
            {
                "chunk_id": str(chunk_id),
                "content": content,
                "doc_id": str(doc_id),
                "doc_name": doc_name,
                "chunk_index": chunk_index,
                "score": float(score),
            }
        )
    return results
