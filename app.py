from slm.intent_extractor import extract_intent
from rules.order_rules import load_order
from rules.refund_rules import calculate_refund
from rules.delivery_rules import delivery_eta


def handle_query(user_query: str) -> str:
    intent_data = extract_intent(user_query)
    intent = intent_data["intent"]
    order_id = intent_data["order_id"]

    if intent == "REFUND_EXPLANATION":
        if not order_id:
            return "Please provide an order ID to explain the refund."

        order = load_order(order_id.rstrip("?.!,"))
        refund = calculate_refund(order)

        return (
            f"Your order {order_id} was cancelled. "
            f"Based on the cancellation policy, "
            f"your refund amount is {refund} {order['currency']}."
        )

    if intent == "DELIVERY_ETA":
        if not order_id:
            return "Please provide an order ID to check delivery."

        order = load_order(order_id.rstrip("?.!,"))
        eta = delivery_eta(order)

        return f"Expected delivery status for order {order_id}: {eta}"

    if intent == "ORDER_STATUS":
        if not order_id:
            return "Please provide an order ID to check status."

        order = load_order(order_id.rstrip("?.!,"))
        return f"Current status of order {order_id}: {order['order_status']}"

    # FAQ fallback
    return (
        "This is a general policy-related question. "
        "In production, it would be answered using FAQ semantic search."
    )

