# Calculates the sum of even numbers from 1 to a given number N

N = 10
sum_even = 0

# Calculate the sum of even numbers
for i in range(2, N + 1, 2):  
    sum_even += i

print(f"The sum of even numbers from 1 to {N} is: {sum_even}")
