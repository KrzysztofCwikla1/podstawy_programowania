from functools import reduce

numbers = [2, 4, 6, 3, 7, 5]

# Filter even numbers and sum using reduce
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
even_sum = reduce(lambda x, y: x + y, even_numbers)

print(f"Sum of even numbers: {even_sum}")

