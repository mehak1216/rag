# src/chunker.py
import re

class TextChunker:
    def __init__(self, chunk_size=200, overlap=50):
        self.chunk_size = chunk_size
        self.overlap = overlap

    def clean_text(self, text):
        text = text.replace("\n", " ")
        text = re.sub(r"\s+", " ", text)
        return text.strip()

    def chunk_text(self, text):
        text = self.clean_text(text)
        if not text :
            return []   # FIX: avoid empty chunks

        words = text.split()
        chunks = []

        start = 0
        while start < len(words):
            end = start + self.chunk_size
            chunks.append(" ".join(words[start:end]))
            start += self.chunk_size - self.overlap

        return chunks
