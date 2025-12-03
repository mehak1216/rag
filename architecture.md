# Mini RAG Architecture

## 1. Architecture Diagram
[Client] → [Query] → [Embed Query] → [Vector DB Search] → [Top Chunks] →  
→ [Prompt Construction] → [LLM] → [Answer]

## 2. Text Extraction + Chunking
- Clean text: remove extra spaces.
- Chunk size: 300 words
- Overlap: 50 words
- Why: reduces context fragmentation.

## 3. Embedding Model
Model: `all-MiniLM-L6-v2`  
Reasons:
- Lightweight  
- Fast  
- High accuracy for semantic search

## 4. Vector DB
FAISS FlatL2
- Fast  
- Reliable  
- Works locally  

## 5. Retrieval Strategy
- Embed query
- KNN search (top_k=3)
- Return most relevant chunks

## 6. Prompt Template
