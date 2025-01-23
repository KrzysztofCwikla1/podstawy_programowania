# Price list
prices = {'milk': 1.49, 'butter': 2.09, 'juice': 1.19, 'bread': 1.99}

# Shopping cart with quantities
cart = {'juice': 3, 'bread': 1, 'milk': 2}

# Calculate total cost
total_cost = 0

# Iterate through each item in the cart and calculate the total cost
for item, quantity in cart.items():
    if item in prices:
        total_cost += prices[item] * quantity

# Display the total cost
print(f"Total cost: ${total_cost:.2f}")
