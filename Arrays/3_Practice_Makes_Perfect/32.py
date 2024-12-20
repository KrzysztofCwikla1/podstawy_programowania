# Function to print the 2D array
def print_2d_array(arr):
    for row in arr:
        print(row)

# Create a 3x5 2D array with integer values
array = [
    [1, 2, 3, 4, 5],  # First row
    [6, 7, 8, 9, 10],  # Second row
    [11, 12, 13, 14, 15]  # Third row
]

# Print the original array
print("Original Array:")
print_2d_array(array)

# Swap the first and last rows
array[0], array[2] = array[2], array[0]

# Print the array after swapping
print("\nArray After Swapping First and Last Rows:")
print_2d_array(array)
