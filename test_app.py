from app import handle_query

queries = [
    "Why did I get only 25% refund for order ORD001?",
    "When will my order ORD002 be delivered?",
    "What is the status of order ORD002?",
    "What is your refund policy?"
]

for q in queries:
    print("User:", q)
    print("Bot :", handle_query(q))
    print("----")

