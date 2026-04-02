from sentence_transformers import SentenceTransformer
import faiss
import numpy as np

model = SentenceTransformer("all-MiniLM-L6-v2")

documents = [
    "Payment failures may take 2-3 business days to refund",
    "Account blocked due to suspicious activity",
    "Recharge issues are resolved within 24 hours",
]

embeddings = model.encode(documents)

index = faiss.IndexFlatL2(len(embeddings[0]))
index.add(np.array(embeddings))


def search_docs(query):
    query_vec = model.encode([query])
    D, I = index.search(np.array(query_vec), k=1)
    return documents[I[0][0]]