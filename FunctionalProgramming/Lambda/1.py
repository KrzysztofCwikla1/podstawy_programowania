def mean(x, y):
    return (x + y) / 2

# Take input from user
n1 = int(input("Enter first number: "))
n2 = int(input("Enter second number: "))

# Calculate the mean and print result
result = mean(n1, n2)
print(f'The arithmetic mean of the numbers {n1} and {n2} is {result}')
