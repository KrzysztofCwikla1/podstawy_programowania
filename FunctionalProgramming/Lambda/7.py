# Define anonymous function to check if number is even
is_even = lambda number: number % 2 == 0

# Test the function
number = int(input("Enter a number: "))
print("Even" if is_even(number) else "Odd")
