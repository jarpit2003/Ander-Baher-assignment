from rules.order_rules import load_order
from rules.refund_rules import calculate_refund

order = load_order("ORD001")
refund = calculate_refund(order)

print(refund)

