#Question 1
def calculate_discount(price, discount_percent):
    if discount_percent >= 20:  # Check if discount is 20% or higher
        final_price = price - (price * (discount_percent / 100))
        return final_price
    else:
        return price
    
    
#Question 2
try:
    original_price = float(input("Enter the original price: "))
    discount_percent = float(input("Enter the discount percentage: "))
    
    # Calculate the final price
    final_price = calculate_discount(original_price, discount_percent)
    
    if discount_percent >= 20:
        print(f"The final price after discount is: {final_price}")
    else:
        print(f"No discount applied. The price remains: {original_price}")
except ValueError:
    print("Invalid input! Please enter numeric values.")
