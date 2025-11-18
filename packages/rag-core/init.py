"""
rag-core package

This module contains the core components for:
- text chunking
- embedding generation
- retrieval over pgvector/Supabase
- prompt construction for RAG and edition generation
"""

from .chunker import split_markdown_into_chunks
from .embeddings import get_embedding
from .retriever import search_chunks
from .prompts import build_rag_prompt

__all__ = [
    "split_markdown_into_chunks",
    "get_embedding",
    "search_chunks",
    "build_rag_prompt",
]
