def evaluate_rpn(expression):
    # Stack to hold operands
    stack = []

    # Split the expression by spaces (RPN notation)
    tokens = expression.split()

    for token in tokens:
        if token.isdigit() or (token.replace('.', '', 1).isdigit() and token.count('.') < 2):  # If token is a number (support for floats)
            # Push the number onto the stack
            stack.append(float(token))
        elif token in "+-*/":
            # Pop two operands from the stack
            b = stack.pop()
            a = stack.pop()

            # Perform the operation and push the result back onto the stack
            if token == '+':
                stack.append(a + b)
            elif token == '-':
                stack.append(a - b)
            elif token == '*':
                stack.append(a * b)
            elif token == '/':
                if b == 0:
                    print("Error: Division by zero")
                    return None
                stack.append(a / b)
        elif token == '=':
            # The equal sign indicates we need to print the result
            if len(stack) == 1:
                return stack.pop()
            else:
                print("Error: Invalid RPN expression")
                return None
        else:
            print(f"Error: Invalid token '{token}'")
            return None

# Test cases
expressions = [
    "2 3 + =",                  # 2 + 3 = 5
    "2 4 1 + * =",              # 2 * (4 + 1) = 10
    "2 3 + 4 5 + * =",          # (2 + 3) * (4 + 5) = 45
    "8 3 1 + / 3 2 - 4 + * ="   # 8 / (3 + 1) * (3 - 2 + 4) = 16
]

for expr in expressions:
    result = evaluate_rpn(expr)
    if result is not None:
        print(f"Result of '{expr}': {result}")
