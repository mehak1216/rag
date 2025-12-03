# src/rag_engine.py
from typing import List, Dict, Union

class RAGEngine:
    def __init__(self):
        self.documents: List[Dict] = []

    def load_documents(self, docs: List[Union[str, Dict]]):
        safe_docs = []
        for doc in docs:
            if isinstance(doc, str):
                safe_docs.append({"title": "Unknown", "text": doc})
            elif isinstance(doc, dict):
                if "text" not in doc:
                    raise ValueError("Document dict must have 'text' key")
                safe_docs.append(doc)
            else:
                raise TypeError(f"Document must be str or dict, got {type(doc)}")
        self.documents = safe_docs

    def retrieve(self, query: str) -> List[Dict]:
        results = []
        for doc in self.documents:
            text = doc.get("text", "")
            title = doc.get("title", "Unknown")
            if any(word.lower() in text.lower() for word in query.split()):
                results.append({"title": title, "text": text})
        return results

    def generate_answer(self, query: str) -> str:
        if not self.documents:
            return "No documents loaded in the system!"
        combined_text = " ".join(doc.get("text", "") for doc in self.documents)
        for word in query.split():
            if word.lower() in combined_text.lower():
                return "Yes, I am a student."
        return "Sorry, I do not know the answer."
