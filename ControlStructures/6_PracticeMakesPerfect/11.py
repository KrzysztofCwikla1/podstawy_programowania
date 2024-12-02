previous_price = float(input('Enter the previous price of the product: '))
current_price =float(input('Enter the current price of the product: '))
discount_percentage=((previous_price-current_price)/previous_price)*100
print(f'Current product price: {current_price}')
print(f'Previos product price: {previous_price}')
if discount_percentage>=10:
    print('Buy the product!!')
    print(f'Product price reduced by {discount_percentage}%')