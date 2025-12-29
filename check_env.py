from dotenv import load_dotenv
import os

load_dotenv()

print("API KEY FOUND:", bool(os.getenv("PINECONE_API_KEY")))
print("PINECONE_ENV:", os.getenv("PINECONE_ENV"))

