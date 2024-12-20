
def transpose_matrix(m):
   
    return [list(row) for row in zip(*m)]

def print_matrix(m):
    for row in m:
        print(row)


matrix_1 = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

matrix_2 = [
    [1, 2, 3, 4, 5],
    [6, 7, 8, 9, 0]
]

matrix_3 = [
    [5, 6, 7, 8]
]

print("Original Matrix 1:")
print_matrix(matrix_1)
print("Transposed Matrix 1:")
print_matrix(transpose_matrix(matrix_1))

print("\nOriginal Matrix 2:")
print_matrix(matrix_2)
print("Transposed Matrix 2:")
print_matrix(transpose_matrix(matrix_2))

print("\nOriginal Matrix 3:")
print_matrix(matrix_3)
print("Transposed Matrix 3:")
print_matrix(transpose_matrix(matrix_3))
