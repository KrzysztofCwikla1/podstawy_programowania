# Take input from user
n1 = int(input("Enter first number: "))
n2 = int(input("Enter second number: "))

# Define an anonymous function (lambda)
mean = lambda x, y: (x + y) / 2

# Calculate the mean and print result
result = mean(n1, n2)
print(f"The arithmetic mean of {n1} and {n2} is {result}")
