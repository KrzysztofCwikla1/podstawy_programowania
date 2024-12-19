array_2d = [
    [7, 3, 7, 9, 0],
    [2, 9, 0, 1, 5],
    [3, 8, 6, 4, 7],
    [8, 7, 1, 1, 5]
]
last_column_sum = 0

for row in array_2d:
    last_column_sum += row[-1] #adds the value of the element with the last index

print(f"Sum of values in the last column:{last_column_sum}")