def f(product_code):
    first_digit = int(product_code[0])
    second_digit = int(product_code[1])
    third_digit = int(product_code[2])

    control_digit = int(product_code[3])

    
    remainder = (first_digit + second_digit + third_digit) % 7

    return remainder == control_digit

print(f("1082"))  
print(f("2035"))  
print(f("1114"))  
print(f("7071"))