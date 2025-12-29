from rules.order_rules import load_order
from rules.delivery_rules import delivery_eta

order = load_order("ORD002")
print(delivery_eta(order))

