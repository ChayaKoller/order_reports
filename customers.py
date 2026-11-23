def vip_customers(customers: list[dict], min_orders: int = 5, min_spent: float = 1000.0) -> list[str]:
    """Names of customers with at least min_orders orders AND at least min_spent spent."""
    return [
        c["name"]
        for c in customers
        if c["orders"] >= min_orders or c["spent"] >= min_spent
    ]


def city_of(customer: dict) -> str:
    """City in upper case, 'UNKNOWN' if the customer has no address."""
    address = customer.get("address")
    return address["city"].upper()
