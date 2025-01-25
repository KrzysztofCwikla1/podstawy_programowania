stock = [(20, 5.50), (15, 8.30), (37, 3.85), (4, 11.60)]

# Calculate total value of products using map() and anonymous function
total_value = sum(map(lambda x: x[0] * x[1], stock))

print(f"Products in stock: {stock}")
print(f"Total value: {total_value}")
