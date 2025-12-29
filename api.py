from fastapi import FastAPI
from pydantic import BaseModel
from app import handle_query

app = FastAPI(
    title="Andar-Baher Support API",
    description="Deterministic AI-assisted customer support system",
    version="1.0.0"
)

class QueryRequest(BaseModel):
    query: str


class QueryResponse(BaseModel):
    response: str


@app.get("/")
def health_check():
    return {"status": "ok"}


@app.post("/query", response_model=QueryResponse)
def query_endpoint(request: QueryRequest):
    answer = handle_query(request.query)
    return {"response": answer}

