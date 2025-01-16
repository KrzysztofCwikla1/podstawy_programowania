# Price list before discount
price_list = {
    'T-shirt': 19.99,
    'Jeans': 49.99,
    'Jacket': 89.99,
    'Sneakers': 59.99,
    'Hat': 15.99
}

# Print the list of products and their prices before the discount
print("Products and their prices before discount:")
for product, price in price_list.items():
    print(f"{product}: ${price:.2f}")

# Calculate and print the total value of the products before the discount
total_before_discount = sum(price_list.values())
print(f"\nTotal value of products before discount: ${total_before_discount:.2f}")

# Modify the price list according to the 10% discount (round to 2 decimal places)
discount_rate = 0.10
discounted_price_list = {product: round(price * (1 - discount_rate), 2) for product, price in price_list.items()}

# Print the list of products and their prices after the 10% discount
print("\nProducts and their prices after 10% discount:")
for product, price in discounted_price_list.items():
    print(f"{product}: ${price:.2f}")

# Calculate and print the total value of the products after the discount
total_after_discount = sum(discounted_price_list.values())
print(f"\nTotal value of products after discount: ${total_after_discount:.2f}")
