# 🚀 QUICK START GUIDE

## Method 1: Double-Click to Run (Easiest!)

1. **Double-click** `RUN_ME.bat` file
2. Wait for server to start (you'll see "Uvicorn running on http://127.0.0.1:8000")
3. **Open your browser** and go to: http://127.0.0.1:8000/docs
4. Test the API using Swagger UI!

## Method 2: Manual Start (PowerShell)

### Step 1: Open PowerShell in Project Folder
- Right-click in the project folder
- Select "Open in Terminal" or "Open PowerShell window here"

### Step 2: Activate Virtual Environment
```powershell
.\.venv\Scripts\activate
```

You should see `(.venv)` appear in your prompt.

### Step 3: Start the Server
```powershell
python -m uvicorn api:app --reload
```

**Expected Output:**
```
INFO:     Uvicorn running on http://127.0.0.1:8000 (Press CTRL+C to quit)
INFO:     Started reloader process
INFO:     Started server process
INFO:     Waiting for application startup.
INFO:     Application startup complete.
```

### Step 4: Test the API

**Option A: Use Swagger UI (Recommended)**
1. Open browser: http://127.0.0.1:8000/docs
2. Click on `/query` endpoint
3. Click "Try it out"
4. Enter this in the request body:
   ```json
   {
     "query": "Why did I get only 25% refund for order ORD001?"
   }
   ```
5. Click "Execute"
6. See the response!

**Option B: Test with Python Script**
Open a **NEW** terminal window (keep server running):
```powershell
.\.venv\Scripts\activate
python test_app.py
```

## 🧪 Test Queries

Try these queries in Swagger UI:

1. **Refund Query:**
   ```json
   {
     "query": "Why did I get only 25% refund for order ORD001?"
   }
   ```
   Expected: Refund amount 57500.0 INR

2. **Delivery Query:**
   ```json
   {
     "query": "delivery ORD002"
   }
   ```
   Expected: Delivery date 2025-01-25

3. **Status Query:**
   ```json
   {
     "query": "What is the status of order ORD002?"
   }
   ```
   Expected: Status IN_TRANSIT

4. **FAQ Query:**
   ```json
   {
     "query": "What is your refund policy?"
   }
   ```
   Expected: FAQ fallback message

## ✅ Verification Checklist

- [ ] Server starts without errors
- [ ] Browser can access http://127.0.0.1:8000/docs
- [ ] Swagger UI loads
- [ ] `/query` endpoint works
- [ ] Refund query returns correct amount (57500.0 INR)

## 🛑 Stopping the Server

Press `CTRL+C` in the terminal where the server is running.

## ❌ Troubleshooting

### Port Already in Use
If port 8000 is busy, use a different port:
```powershell
python -m uvicorn api:app --reload --port 8001
```

### Module Not Found
Make sure you're in the project root directory:
```powershell
cd "C:\Users\HP\OneDrive\Desktop\ANDAR-BAHER ASSIGNMENT"
```

### Virtual Environment Not Activated
Always activate before running:
```powershell
.\.venv\Scripts\activate
```

## 📊 What You'll See

When you test a query, you'll get responses like:

- **Refund:** "Your order ORD001 was cancelled. Based on the cancellation policy, your refund amount is 57500.0 INR."
- **Delivery:** "Expected delivery status for order ORD002: 2025-01-25"
- **Status:** "Current status of order ORD002: IN_TRANSIT"

## 🎉 Success!

If you see the Swagger UI and can execute queries, you're all set!


