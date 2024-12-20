
numbers = [15, 8, 31, 47, 2, 19]

print("existed array:", " ".join(map(str, numbers)))

reversed_numbers = []
for i in range(len(numbers) - 1, -1, -1):  
    reversed_numbers.append(numbers[i])

print("reverse array:", " ".join(map(str, reversed_numbers)))
