price = float(input("Enter price: "))

discount = float(input("Enter discount %: "))

discounted_price = price*((100-discount)*0.01)

print(f"Price with discount: {discounted_price:.2f}")

reduction = price - discounted_price

print(f"Reduction: {reduction:.2f}")