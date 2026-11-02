def calculate_discount(price: float, discount: float) -> float:
    """Return the amount of discount for the given price."""
    if price < 0:
        raise ValueError("Price cannot be negative")
    if not 0 <= discount <= 100:
        raise ValueError("Discount must be between 0 and 100")
    return price * discount / 100


def calculate_gst(price: float, gst_rate: float) -> float:
    """Return the GST amount for the given price."""
    if price < 0:
        raise ValueError("Price cannot be negative")
    if not 0 <= gst_rate <= 100:
        raise ValueError("GST rate must be between 0 and 100")
    return price * gst_rate / 100


def calculate_order_total(price: float, discount: float, gst_rate: float) -> float:
    """Calculate the final order total after discount and GST."""
    discount_amount = calculate_discount(price, discount)
    discounted_price = price - discount_amount
    gst_amount = calculate_gst(discounted_price, gst_rate)
    return discounted_price + gst_amount


if __name__ == "__main__":
    total = calculate_order_total(1000, 10, 18)
    print(f"Final order amount: ₹{total:.2f}")
