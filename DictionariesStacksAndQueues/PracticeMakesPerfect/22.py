import json

# Create an empty dictionary to hold product data
product = {}

# Read product data from the keyboard
product['name'] = input("Enter the product name: ")

# Ensure that the price is a real number with two decimal places
while True:
    try:
        product['price'] = float(input("Enter the product price (real number with two decimal places): "))
        if product['price'] < 0:
            print("Price cannot be negative. Please enter a valid price.")
            continue
        break
    except ValueError:
        print("Invalid input. Please enter a valid number for the price.")

# Read the payment status (yes/no)
while True:
    paid_input = input("Has the product been paid for? (yes/no): ").lower()
    if paid_input == "yes":
        product['paid'] = True
        break
    elif paid_input == "no":
        product['paid'] = False
        break
    else:
        print("Invalid input. Please enter 'yes' or 'no'.")

# Save product data to a json file
with open('product.json', 'w', encoding='utf-8') as file:
    json.dump(product, file, indent=4)

print("Product data has been saved to product.json.")
