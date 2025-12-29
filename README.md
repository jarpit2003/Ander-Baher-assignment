# Andar-Baher Support Chatbot

A deterministic AI-assisted customer support system with intent-driven routing and rule-based calculations.

## 🚀 Quick Start

### 1. Activate Virtual Environment

```powershell
.\.venv\Scripts\activate
```

You should see `(.venv)` in your terminal prompt.

### 2. Start the FastAPI Server

```powershell
.\.venv\Scripts\python.exe -m uvicorn api:app --reload
```

**Expected Output:**
```
INFO:     Uvicorn running on http://127.0.0.1:8000 (Press CTRL+C to quit)
INFO:     Started reloader process
INFO:     Started server process
INFO:     Waiting for application startup.
INFO:     Application startup complete.
```

### 3. Access the API

**Swagger UI (Interactive Documentation):**
- Open in browser: http://127.0.0.1:8000/docs

**Health Check:**
- Open in browser: http://127.0.0.1:8000/

## 🧪 Testing the API

### Option 1: Using Swagger UI (Easiest)

1. Go to http://127.0.0.1:8000/docs
2. Click on `/query` endpoint
3. Click "Try it out"
4. Enter a query in the request body:
   ```json
   {
     "query": "Why did I get only 25% refund for order ORD001?"
   }
   ```
5. Click "Execute"
6. See the response

### Option 2: Using Test Script

In a **new terminal** (keep server running in first terminal):

```powershell
.\.venv\Scripts\activate
.\.venv\Scripts\python.exe test_api.py
```

### Option 3: Using Python Directly

```powershell
.\.venv\Scripts\activate
.\.venv\Scripts\python.exe test_app.py
```

### Option 4: Using curl (if available)

```powershell
curl -X POST "http://127.0.0.1:8000/query" -H "Content-Type: application/json" -d "{\"query\": \"Why did I get only 25% refund for order ORD001?\"}"
```

## 📝 Example Queries

### Refund Query
```json
{
  "query": "Why did I get only 25% refund for order ORD001?"
}
```
**Expected Response:** Refund amount calculation (57500.0 INR)

### Delivery Query
```json
{
  "query": "delivery ORD002"
}
```
**Expected Response:** Delivery date (2025-01-25)

### Status Query
```json
{
  "query": "What is the status of order ORD002?"
}
```
**Expected Response:** Order status (IN_TRANSIT)

### FAQ Query
```json
{
  "query": "What is your refund policy?"
}
```
**Expected Response:** FAQ fallback message

## 🛠️ Project Structure

```
.
├── api.py                 # FastAPI application
├── app.py                 # Main routing logic
├── data/
│   └── orders.json       # Order data (source of truth)
├── faq/
│   ├── scrape_faq.py    # FAQ scraper
│   ├── chunk_faq.py     # FAQ chunker
│   └── embed_faq.py     # FAQ embedding (Pinecone)
├── rules/
│   ├── order_rules.py   # Order loading
│   ├── refund_rules.py  # Refund calculation
│   └── delivery_rules.py # Delivery ETA
├── slm/
│   └── intent_extractor.py # Intent extraction
└── test_*.py            # Test scripts
```

## 🔧 Troubleshooting

### Server Won't Start

1. **Check if port 8000 is in use:**
   ```powershell
   netstat -ano | findstr :8000
   ```

2. **Use a different port:**
   ```powershell
   .\.venv\Scripts\python.exe -m uvicorn api:app --reload --port 8001
   ```

### Module Not Found Errors

Make sure you're in the project root directory:
```powershell
cd "C:\Users\HP\OneDrive\Desktop\ANDAR-BAHER ASSIGNMENT"
```

### Virtual Environment Issues

If `.venv` doesn't work, recreate it:
```powershell
uv venv
.venv\Scripts\activate
uv sync
```

## 📊 System Architecture

```
User Query
    ↓
FastAPI Endpoint (/query)
    ↓
Intent Extraction (SLM)
    ↓
Router (app.py)
    ↓
Rule Engine (Python)
    ↓
Response
```

## 🎯 Key Features

- ✅ Deterministic refund calculations
- ✅ Intent-driven routing
- ✅ Rule-based order processing
- ✅ FastAPI REST API
- ✅ Clean separation of concerns

## 📚 API Endpoints

- `GET /` - Health check
- `POST /query` - Process user query

## 🔐 Environment Variables

Create `.env` file with:
```
PINECONE_API_KEY=your_actual_api_key_here
PINECONE_ENV=us-east-1
```

## ⚠️ Note on Embeddings

The FAQ embedding step (Phase 3, Step 3.3) requires PyTorch, which may have DLL loading issues on Windows. The core system works without embeddings - FAQ queries will return a fallback message.



