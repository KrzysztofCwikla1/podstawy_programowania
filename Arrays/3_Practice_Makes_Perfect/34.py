def identity_matrix(n): #identity matrix diagonal is filled with 1s, rest with 0s
    matrix = []
    for i in range(n):
        # Create a row with zeros
        row = [0] * n
        # Set the diagonal element to 1
        row[i] = 1
        matrix.append(row)
    return matrix

# Function to print a 2D array (matrix)
def print_matrix(matrix):
    for row in matrix:
        print(" ".join(map(str, row))) #it will print each row below another
sizes = [3, 5, 8]
for size in sizes:
    print(f"Identity matrix of size {size}:")
    matrix = identity_matrix(size)
    print_matrix(matrix)
    print()