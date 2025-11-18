# Database Schema — Supabase (PostgreSQL)

## Tables Overview

### 1. documents
| column       | type        | desc |
|--------------|-------------|------|
| id           | uuid PK     | unique doc |
| name         | text        | file name |
| category     | text        | fundamentals / paredes / tactica / etc |
| created_at   | timestamptz | |

### 2. chunks
| column      | type        | desc |
|-------------|-------------|------|
| id          | uuid PK     | |
| doc_id      | uuid FK     | maps to documents |
| chunk_index | int         | ordering |
| content     | text        | text block |
| token_count | int         | size |

### 3. embeddings
| column      | type        | desc |
|-------------|-------------|------|
| chunk_id    | uuid FK     | |
| vector      | vector(1536) | embedding |
| created_at  | timestamptz | |

### 4. generated_editions
| id          | uuid PK |
| title       | text |
| body        | text |
| user_id     | uuid |
| sources     | jsonb |

### 5. queries_logs
| id          | uuid PK |
| query       | text |
| results     | jsonb |
| created_at  | timestamptz |

## Indexes
- `embeddings.vector` → ANN index (pgvector)
- `chunks.doc_id`
- `generated_editions.user_id`

## RAG Query Procedure
1. embed(query)  
2. SELECT chunk_id FROM embeddings ORDER BY vector <-> query LIMIT K  
3. JOIN chunks → get text  
4. LLM receives: query + context + citations  
