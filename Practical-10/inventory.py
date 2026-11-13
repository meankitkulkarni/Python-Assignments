import logging

logging.basicConfig(
    filename="inventory.log",
    level=logging.DEBUG,
    format="%(asctime)s - %(levelname)s - %(message)s",
)

logger = logging.getLogger(__name__)


def calculate_total_price(price, quantity):
    logger.debug("Calculating total price: price=%s, quantity=%s", price, quantity)
    if price < 0:
        logger.error("Invalid price provided: %s", price)
        raise ValueError("Price cannot be negative")
    if quantity <= 0:
        logger.error("Invalid quantity provided: %s", quantity)
        raise ValueError("Quantity must be greater than zero")

    total = price * quantity
    logger.info("Calculated total price: %.2f", total)
    return total


def apply_discount(total, discount_percent):
    logger.debug(
        "Applying discount: total=%s, discount_percent=%s", total, discount_percent
    )
    if total < 0:
        logger.error("Invalid total amount: %s", total)
        raise ValueError("Total cannot be negative")
    if not 0 <= discount_percent <= 100:
        logger.error("Invalid discount percentage: %s", discount_percent)
        raise ValueError("Discount percent must be between 0 and 100")

    discounted_total = total - (total * discount_percent / 100)
    logger.info(
        "Discounted amount after %s%% discount: %.2f",
        discount_percent,
        discounted_total,
    )
    return discounted_total


def check_stock(available_stock, requested_quantity):
    logger.info(
        "Checking stock: available=%s, requested=%s",
        available_stock,
        requested_quantity,
    )
    if available_stock < 0:
        logger.error("Invalid available stock: %s", available_stock)
        raise ValueError("Available stock cannot be negative")
    if requested_quantity <= 0:
        logger.error("Invalid requested quantity: %s", requested_quantity)
        raise ValueError("Requested quantity must be greater than zero")

    if requested_quantity <= available_stock:
        logger.info("Stock check passed: %s units available", available_stock)
        return True

    logger.warning(
        "Insufficient stock: requested %s, but only %s available",
        requested_quantity,
        available_stock,
    )
    return False


if __name__ == "__main__":
    if check_stock(50, 5):
        subtotal = calculate_total_price(200, 5)
        final_price = apply_discount(subtotal, 10)
        print(f"Order fulfilled! Final discounted price: ₹{final_price:.2f}")
