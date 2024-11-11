decimal_num = int(input("Enter number: "))

#converting decimal to binary using python function
binary_number = bin(decimal_num)[2:]

print(f"Binary number: {binary_number}")

#converting decimal to hexadecimal using python function
hexadecimal = hex(decimal_num)[2:]

print(f"Hexadecimal number: {hexadecimal}")