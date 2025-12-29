from rules.order_rules import load_order

order = load_order("ORD001")
print(order["order_status"])
print(order["booking_amount"])

