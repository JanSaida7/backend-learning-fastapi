#day1.py

def calculate_discount(price: float, discount_percent: int) -> float:
    """
    Calculates the final price after discount.
    """
    if discount_percent < 0 or discount_percent > 100:
        raise ValueError("Discount must be between 0 and 100")

    factor = discount_percent / 100
    discount_amount = price * factor
    final_price = price - discount_amount
    return final_price

if __name__ == "__main__":

    try:
        item_price = 100.0
        my_discount = 20

        result = calculate_discount(item_price, my_discount)

        print(f"Original Price: ${item_price}")
        print(f"Discount: {my_discount}%")
        print(f"Final Price: ${result}")

    except ValueError as e:
        print(f"Error: {e}")