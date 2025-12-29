def delivery_eta(order: dict):
    if order["shipping"]["actual_delivery_date"]:
        return "DELIVERED"
    return order["shipping"]["expected_delivery_date"]

