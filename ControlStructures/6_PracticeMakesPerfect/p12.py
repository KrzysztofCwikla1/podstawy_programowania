num_products = int(input("Number of products purchased: "))
product_price = float(input("Product price: "))

if num_products > 2:
    discounted_products = num_products - 2
    total = (2 * product_price) + (discounted_products * product_price * 0.75)
else:
    total = num_products * product_price
print(f"Amount to pay: {total:.2f}")
