array_2d = [
    [1, 2, 3, 4, 5],
    [6, 7, 8, 9, 10],
    [11, 12, 13, 14, 15]
]


print("Before swapping:")
for row in array_2d:
    print(row)


for row in array_2d:
    row[0], row[-1] = row[-1], row[0]


print("\nAfter swapping:")
for row in array_2d:
    print(row)
