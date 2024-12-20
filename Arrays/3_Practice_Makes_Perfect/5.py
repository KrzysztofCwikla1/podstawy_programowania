
numbers = [15, 8, 31, 47, 2, 19]


total_sum = 0
for number in numbers:
    total_sum += number

arithmetic_mean = total_sum / len(numbers)

print("Array:", " ".join(map(str, numbers)))
print("Arithmetic mean:", arithmetic_mean)
