from datetime import datetime

def calculate_refund(order: dict) -> float:
    if order["order_status"] != "CANCELLED":
        return 0.0

    booking_date = datetime.fromisoformat(order["booking_date"])
    cancellation_date = datetime.fromisoformat(order["cancellation_date"])

    days_difference = (cancellation_date - booking_date).days
    amount = order["booking_amount"]

    if days_difference <= 14:
        return amount * 0.5
    elif days_difference <= 28:
        return amount * 0.25
    else:
        return 0.0

