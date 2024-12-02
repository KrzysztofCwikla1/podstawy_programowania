# Program to convert a decimal number to binary

decimal_number = int(input("Enter decimal number: "))
binary_number = ""

original_number = decimal_number

while decimal_number > 0:
    remainder = decimal_number % 2  # find the remainder
    binary_number = str(remainder) + binary_number  # add remainder to the left of the binary string
    decimal_number //= 2  # update the number by dividing it by 2

# Display the result
print(f"{original_number}(10) = {binary_number}(2)")