price = int(input("Enter the amount in PLN: "))

nl = '\n'

five = price // 5
remainder = price % 5

two = remainder // 2
remainder = remainder % 2

one = remainder // 1


print(f"The amount of PLN {price} in coins:{nl}5 PLN coins: {five}{nl}2 PLN coins: {two}{nl}1 PLN coins: {one}")
