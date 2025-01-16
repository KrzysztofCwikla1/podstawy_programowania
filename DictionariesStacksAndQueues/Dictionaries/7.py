# Data containing information about the number of products
store_inventory = {
    'Laptop': 15,
    'Desktop PC': 10,
    'Monitor': 25,
    'Keyboard': 50,
    'Mouse': 60,
    'External Hard Drive': 30,
    'Printer': 12,
    'Router': 20,
    'USB Flash Drive': 100,
    'Graphics Card': 8
}

# Print the list of products and their quantities
print("Products and their quantities in the store:")
for product, quantity in store_inventory.items():
    print(f"{product}: {quantity}")

# Calculate and print the total number of products in the store
total_products = sum(store_inventory.values())
print(f"\nTotal number of products in the store: {total_products}")
