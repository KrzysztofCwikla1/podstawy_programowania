def f(expression):
    result = 0
    current_number = 0
    operator = '+'  # Default operator
    
    for char in expression:
        if char.isdigit():
            current_number = int(char)
        elif char in '+-':
            if operator == '+':
                result += current_number
            elif operator == '-':
                result -= current_number
            operator = char
    # Add the last number
    if operator == '+':
        result += current_number
    elif operator == '-':
        result -= current_number
    
    return result

print(f("2+3"))
print(f("3+8+1"))
print(f("2+3-4+5-0"))

