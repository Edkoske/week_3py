def calculate_discount(price, discount_percent):
    """
    Calculate the final price after applying a discount.
    
    Parameters:
        price (float): Original price of the item.
        discount_percent (float): Discount percentage.
    
    Returns:
        float: Final price after applying discount if it's 20% or higher,
               otherwise returns the original price.
    """
    if discount_percent >= 20:
        discount_amount = (discount_percent / 100) * price
        final_price = price - discount_amount
        return final_price
    else:
        return price


# Prompt user for input
try:
    original_price = float(input("Enter the original price of the item: "))
    discount = float(input("Enter the discount percentage: "))

    # Calculate final price
    final_price = calculate_discount(original_price, discount)

    # Print result
    if discount >= 20:
        print(f"Final price after {discount}% discount: {final_price:.2f}")
    else:
        print(f"No discount applied. Original price: {final_price:.2f}")

except ValueError:
    print("Invalid input. Please enter numeric values for price and discount.")
