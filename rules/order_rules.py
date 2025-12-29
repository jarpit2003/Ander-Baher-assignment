import json

def load_order(order_id: str) -> dict:
    with open("data/orders.json", "r", encoding="utf-8") as f:
        orders = json.load(f)

    for order in orders:
        if order["order_id"] == order_id:
            return order

    raise ValueError(f"Order {order_id} not found")

