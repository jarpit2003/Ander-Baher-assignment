# Andar-Baher Deterministic Support API

A deterministic, AI-assisted customer support backend built as a take-home assignment.  
The system cleanly separates **AI understanding** from **business logic**, ensuring **correct, explainable, and safe handling of money and dates**.

---

## Objective

Build a customer support system that correctly answers:

### 1. FAQ / Policy Questions
- Refund & returns  
- Privacy policy  
- Terms & conditions  

Handled using **embeddings + vector search** (no hardcoded answers).

### 2. Transactional Questions
- Order status  
- Delivery ETA  
- Refund explanation  

Handled using **SLM-based intent extraction + deterministic backend rule engine**.

---

## Core Design Principles

- ❌ No business logic in AI prompts  
- ❌ No money or date calculations in LLMs  
- ✅ All rules implemented in backend Python code  
- ✅ AI used only for intent identification and parameter extraction  
- ✅ Fully deterministic and testable  

---

## High-Level Architecture

User Query (text)
↓
SLM Intent Extraction OR FAQ Embedding Search
↓
Structured JSON (intent + parameters)
↓
Rule Engine (Python)
↓
Computed Result
↓
Natural-language explanation (no calculations)

yaml
Copy code

---

## Project Structure

.
├── api.py # FastAPI app
├── app.py # Core routing logic
├── data/
│ └── orders.json # Transactional dataset
├── faq/
│ ├── scrape_faq.py # Scrape official FAQ pages
│ ├── chunk_faq.py # Chunk FAQ text
│ ├── embed_faq.py # Generate embeddings
│ └── chunks.txt # Chunked FAQ data
├── rules/
│ ├── order_rules.py # Order loader
│ ├── refund_rules.py # Refund logic
│ └── delivery_rules.py # Delivery ETA logic
├── slm/
│ └── intent_extractor.py # Mock SLM (JSON-only output)
├── test.py # Unit & integration tests
├── pyproject.toml # Dependency definitions
├── uv.lock # Locked dependency versions
├── README.md
└── QUICK_START.md

yaml
Copy code

---

## Data Design

### Transactional Data (`data/orders.json`)
- Multiple users and orders  
- Delivered, in-transit, and cancelled orders  
- Boundary cases (14, 15, 28 days)  

❌ No derived or computed fields stored  
❌ No refund amounts, percentages, or ETAs in data  

All calculations happen **at runtime** via rules.

---

## AI Usage

### FAQ Handling
- Source: Official Andar-Baher policy pages  
- Pipeline: Scrape → Chunk → Embed → Vector DB  
- No hardcoded answers  
- Safe fallback used in demo (no hallucinations)

### Intent Extraction (SLM)
- Keyword-based mock SLM  
- Returns **JSON only**

Example:
```json
{
  "intent": "REFUND_EXPLANATION",
  "order_id": "ORD001"
}
Allowed intents:

ORDER_STATUS

DELIVERY_ETA

REFUND_EXPLANATION

FAQ

The mock SLM can be replaced by Phi-3 / Mistral / Llama without changing backend code.

Setup Instructions (Local)
1. Clone Repository
bash
Copy code
git clone https://github.com/jarpit2003/Ander-Baher-assignment.git
cd Ander-Baher-assignment
2. Create Virtual Environment
bash
Copy code
python -m venv .venv
.\.venv\Scripts\activate
3. Install Dependencies (using uv)
bash
Copy code
pip install uv
uv sync
This project uses pyproject.toml + uv.lock for reproducible builds
(requirements.txt is intentionally not used).

Run the Server
bash
Copy code
python -m uvicorn api:app --reload
Open:

arduino
Copy code
http://127.0.0.1:8000/docs
Demo Queries (MANDATORY)
FAQ Query
json
Copy code
{
  "query": "What is your refund policy?"
}
Expected:

json
Copy code
{
  "response": "Please provide an order ID to explain the refund."
}
Order Status Query
json
Copy code
{
  "query": "What is the status of order ORD002?"
}
Expected:

json
Copy code
{
  "response": "Current status of order ORD002: IN_TRANSIT"
}
Refund Explanation Query
json
Copy code
{
  "query": "Why did I get only 25% refund for order ORD001?"
}
Expected:

json
Copy code
{
  "response": "Your order ORD001 was cancelled. Based on the cancellation policy, your refund amount is 57500.0 INR."
}
