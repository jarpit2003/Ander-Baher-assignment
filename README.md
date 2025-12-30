# Ander–Baher Deterministic Support API

A deterministic, AI-assisted customer support backend built as a take-home assignment.

The system strictly separates **AI understanding** from **business logic**, ensuring:
- Correct handling of money and dates
- No hallucinations
- Fully testable and explainable behavior

---
Live Demo:-
https://drive.google.com/file/d/1xSfBLF9iU7PaTWCiERfrrHgO1RypfgkB/view?usp=sharing
(Use Headphones  for better voice quality)

## 1. Objective

Build a customer support system that correctly answers:

### A. FAQ / Policy Questions
- Refund & returns  
- Privacy policy  
- Terms & conditions  

Handled using **embeddings + vector search** (no hardcoded answers).

### B. Transactional Questions
- Order status  
- Delivery ETA  
- Refund explanation  

Handled using **SLM-based intent extraction** + **deterministic backend rules**.

---

## 2. Core Design Principles

- ❌ No business logic in AI prompts  
- ❌ No money or date calculations in LLMs  
- ✅ All rules implemented in backend Python code  
- ✅ AI used only for intent identification & parameter extraction  
- ✅ Fully deterministic and testable  

---

## 3. Architecture (High Level)

User Query (text)  
↓  
FAQ Vector Search **OR** SLM Intent Extraction  
↓  
Structured JSON (intent + parameters)  
↓  
Python Rule Engine  
↓  
Computed Result  
↓  
Natural-language explanation (no calculations)

---

## 4. Data Guarantees

- Multiple users and orders
- Delivered, in-transit, and cancelled orders
- Boundary cases (14, 15, 28 days)

❌ No derived or computed fields stored  
❌ No refund amounts, percentages, or ETAs in data  

✅ All calculations happen **at runtime** via backend rules

---

## 5. AI Usage

### FAQ Handling
- Source: Official Ander–Baher policy pages
- Pipeline: **Scrape → Chunk → Embed → Vector DB**
- No hardcoded FAQ answers
- Safe fallback used in demo (no hallucinations)

### Intent Extraction (SLM)
- Keyword-based mock SLM
- Returns **JSON only**
- No calculations
- No business logic



Example output:

```json
{
  "intent": "REFUND_EXPLANATION",
  "order_id": "ORD001"
}
```
6. Tech Stack

Python 3.11+

FastAPI

Uvicorn

uv (dependency management)

7. Setup Instructions (Local Demo)
Step 1: Clone Repository
```
git clone https://github.com/jarpit2003/Ander-Baher-assignment
cd Ander-Baher-assignment
```
Step 2: Create Virtual Environment
```
python -m venv .venv
.\.venv\Scripts\activate
```
Step 3: Install Dependencies
```
pip install uv
uv sync
```
8. Run the Server
   ```
   python -m uvicorn api:app --reload
   ```
9.Open Swagger UI:
```
http://127.0.0.1:8000/docs
```
9. Mandatory Demo Queries

These must be executed during the demo
A. FAQ Query

Request:
```
{
  "query": "What is your refund policy?"
}
```
Expected response:
```
{
  "response": "Please provide an order ID to explain the refund."
}
```
B. Order Status Query

Request:
```
{
  "query": "What is the status of order ORD002?"
}
```
Expected response:
```
{
  "response": "Current status of order ORD002: IN_TRANSIT"
}
```
C. Refund Explanation Query

Request:
```
{
  "query": "Why did I get only 25% refund for order ORD001?"
}
```
Expected response:
```
{
  "response": "Your order ORD001 was cancelled after the 14-day window. As per policy, only a partial refund applies."
}
```
<img width="1143" height="870" alt="image" src="https://github.com/user-attachments/assets/3e67d5f4-10c1-429d-95d7-afbb6ac24ff0" />
<img width="1477" height="869" alt="image" src="https://github.com/user-attachments/assets/37572dce-dab2-474b-9509-de41564f32e5" />
<img width="1675" height="746" alt="image" src="https://github.com/user-attachments/assets/74f70885-681c-4759-83c6-1887c934916c" />
<img width="1229" height="814" alt="image" src="https://github.com/user-attachments/assets/f217a699-9add-457a-a6d7-74a0d6a32836" />





