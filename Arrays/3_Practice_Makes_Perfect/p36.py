def convert_to_1d(array_2d):
    result = []
    for row in array_2d:
        result += row
    return result


array_1 = [
    [2, 3],
    [1, 5]
]

array_2 = [
    [5, 0, 3, 7, 5],
    [9, 0, 9, 1, 2]
]

array_3 = [
    [2, 1],
    [3, 5],
    [7, 4],
    [2, 6]
]


print("1D array for array_1:", convert_to_1d(array_1))
print("1D array for array_2:", convert_to_1d(array_2))
print("1D array for array_3:", convert_to_1d(array_3))
