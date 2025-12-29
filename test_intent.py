from slm.intent_extractor import extract_intent

queries = [
    "Why did I get only 25% refund for order ORD001?",
    "When will my order ORD002 be delivered?",
    "What is the status of order ORD002?",
    "What is your refund policy?"
]

for q in queries:
    print(q)
    print(extract_intent(q))
    print("----")

