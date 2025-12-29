import json

def extract_intent(user_query: str) -> dict:
    """
    This function simulates an SLM output.
    In production, this would be replaced with an LLM call.
    """

    query = user_query.lower()

    if "refund" in query:
        return {
            "intent": "REFUND_EXPLANATION",
            "order_id": extract_order_id(user_query)
        }

    if "delivery" in query:
        return {
            "intent": "DELIVERY_ETA",
            "order_id": extract_order_id(user_query)
        }

    if "status" in query:
        return {
            "intent": "ORDER_STATUS",
            "order_id": extract_order_id(user_query)
        }

    return {
        "intent": "FAQ_QUERY",
        "order_id": None
    }


def extract_order_id(text: str):
    for word in text.split():
        if word.startswith("ORD"):
            return word
    return None

