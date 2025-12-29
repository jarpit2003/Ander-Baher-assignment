import os
from dotenv import load_dotenv
from sentence_transformers import SentenceTransformer
from pinecone import Pinecone, ServerlessSpec

# Load environment variables
load_dotenv()

PINECONE_API_KEY = os.getenv("PINECONE_API_KEY")
PINECONE_ENV = os.getenv("PINECONE_ENV", "us-east-1")
INDEX_NAME = "anderbaher-faq"

# Initialize Pinecone
pc = Pinecone(api_key=PINECONE_API_KEY)

# Create index if it does not exist
existing_indexes = pc.list_indexes().names()

if INDEX_NAME not in existing_indexes:
    pc.create_index(
        name=INDEX_NAME,
        dimension=384,
        metric="cosine",
        spec=ServerlessSpec(
            cloud="aws",
            region=PINECONE_ENV
        )
    )
    print(f"[OK] Created Pinecone index: {INDEX_NAME}")
else:
    print(f"[OK] Pinecone index already exists: {INDEX_NAME}")

index = pc.Index(INDEX_NAME)

# Load embedding model
model = SentenceTransformer("all-MiniLM-L6-v2")

FILES = ["refund_chunks", "privacy_chunks", "terms_chunks"]

vector_id = 0

for file in FILES:
    with open(f"faq/{file}.txt", "r", encoding="utf-8") as f:
        chunks = f.read().split("\n\n")

    embeddings = model.encode(chunks)

    vectors = []
    for text, embedding in zip(chunks, embeddings):
        vectors.append({
            "id": str(vector_id),
            "values": embedding.tolist(),
            "metadata": {
                "text": text,
                "source": file
            }
        })
        vector_id += 1

    index.upsert(vectors)
    print(f"[OK] Upserted {len(vectors)} vectors from {file}")


