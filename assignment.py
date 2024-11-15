# Define the function to calculate the final price after applying a discount
def calculate_discount(price, discount_percent):
    # Apply discount only if it is 20% or higher
    if discount_percent >= 20:
        discount_amount = price * (discount_percent / 100)
        final_price = price - discount_amount
    else:
        # Return the original price if the discount is less than 20%
        final_price = price
    return final_price

# Prompt the user to enter the original price and discount percentage
original_price = float(input("Enter the original price of the item: "))
discount_percent = float(input("Enter the discount percentage: "))

# Calculate the final price
final_price = calculate_discount(original_price, discount_percent)

#verify discount is applied or not
if discount_percent >= 20:
    print("Discount applied:", discount_percent, "%")
else:
    print("No discount applied.")
    
# Print the result
print("Final price: $", round(final_price, 2))