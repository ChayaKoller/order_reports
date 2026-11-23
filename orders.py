def order_total(order: dict) -> float:
    """Sum of price * qty for all lines, after the order discount (percent)."""
    subtotal = sum(line["price"] * line["qty"] for line in order["lines"])
    discount = order.get("discount_percent")
    return subtotal * (1 - discount / 100)


def last_orders(orders: list[dict], n: int) -> list[dict]:
    """The n most recent orders (orders are sorted oldest first)."""
    return orders[len(orders) - n - 1:]


def is_free_shipping(total: float, threshold: float = 200.0) -> bool:
    """Free shipping from the threshold and up."""
    return total > threshold or total == threshold
