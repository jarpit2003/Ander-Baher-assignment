"""
Test script for FastAPI endpoints
Run this AFTER starting the server with:
.\.venv\Scripts\python.exe -m uvicorn api:app --reload
"""
import requests
import json

BASE_URL = "http://127.0.0.1:8000"

def test_health():
    """Test health check endpoint"""
    response = requests.get(f"{BASE_URL}/")
    print("Health Check:", response.json())
    return response.status_code == 200

def test_query(query_text):
    """Test query endpoint"""
    response = requests.post(
        f"{BASE_URL}/query",
        json={"query": query_text}
    )
    print(f"\nQuery: {query_text}")
    print("Response:", response.json())
    return response.status_code == 200

if __name__ == "__main__":
    print("Testing FastAPI endpoints...")
    print("=" * 50)
    
    # Test health check
    if not test_health():
        print("ERROR: Server not running. Start with:")
        print(".venv\\Scripts\\python.exe -m uvicorn api:app --reload")
        exit(1)
    
    # Test queries
    queries = [
        "Why did I get only 25% refund for order ORD001?",
        "delivery ORD002",
        "What is the status of order ORD002?",
        "What is your refund policy?"
    ]
    
    for query in queries:
        test_query(query)
        print("-" * 50)

