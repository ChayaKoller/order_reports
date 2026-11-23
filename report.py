from customers import city_of, vip_customers
from orders import is_free_shipping, last_orders, order_total

ORDERS = [
    {"id": 1, "lines": [{"price": 50.0, "qty": 2}], "discount_percent": 10},
    {"id": 2, "lines": [{"price": 120.0, "qty": 1}, {"price": 40.0, "qty": 2}]},
    {"id": 3, "lines": [{"price": 15.0, "qty": 4}], "discount_percent": 0},
]

CUSTOMERS = [
    {"name": "Avi", "orders": 7, "spent": 1500.0, "address": {"city": "Haifa"}},
    {"name": "Moshe", "orders": 6, "spent": 300.0, "address": None},
    {"name": "Yossi", "orders": 1, "spent": 2000.0, "address": {"city": "Bnei Brak"}},
]


def main() -> None:
    for order in last_orders(ORDERS, 2):
        total = order_total(order)
        print(order["id"], round(total, 2), "free shipping" if is_free_shipping(total) else "")
    print("VIP:", vip_customers(CUSTOMERS))
    for c in CUSTOMERS:
        print(c["name"], city_of(c))


if __name__ == "__main__":
    main()
