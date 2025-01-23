import queue

def decimal_to_binary(n):
    """
    Converts a natural number to its binary representation using a stack.
    :param n: Natural number to convert
    :return: Binary representation as a string
    """
    if n == 0:
        return "0"

    stack = queue.LifoQueue()
    
    print("Division\tRemainder")

    # Perform division and store remainders in the stack
    while n > 0:
        remainder = n % 2
        stack.put(remainder)
        print(f"{n} / 2 = {n // 2}\t{remainder}")
        n //= 2

    # Construct the binary number by popping from the stack
    binary_number = ""
    while not stack.empty():
        binary_number += str(stack.get())

    return binary_number

# Example usage
natural_number = 18
binary_result = decimal_to_binary(natural_number)
print(f"\nNatural number: {natural_number}")
print(f"Binary number: {binary_result}")
