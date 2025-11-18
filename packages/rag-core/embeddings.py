import os
from typing import List
import requests

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
EMBEDDING_MODEL = os.getenv("EMBEDDING_MODEL", "embedding-001")

def get_embedding(text: str) -> List[float]:
    url = f"https://generativelanguage.googleapis.com/v1beta/models/{EMBEDDING_MODEL}:embedText"
    headers = {"Content-Type": "application/json"}
    params = {"key": GEMINI_API_KEY}
    payload = {"text": text}

    resp = requests.post(url, headers=headers, params=params, json=payload)
    resp.raise_for_status()
    return resp.json()["embedding"]["value"]
