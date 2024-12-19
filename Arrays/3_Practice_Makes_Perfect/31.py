array = [[-38, 19], [5, 40], [-7, 11], [29, 16]]

min_value = array[0][0]  
max_value = array[0][0]  
min_position = (0, 0)     # The first value position is (0, 0)
max_position = (0, 0)     

for row_index, row in enumerate(array): #enumerate adds an index to the iterated value, row_index for the row index, and col_index for the column index
    for col_index, value in enumerate(row):
        if value < min_value:
            min_value = value
            min_position = (row_index, col_index)
        if value > max_value:
            max_value = value
            max_position = (row_index, col_index)

# Print the results
print(f"Smallest value: {min_value} at position (row {min_position[0]}, column {min_position[1]})")
print(f"Largest value: {max_value} at position (row {max_position[0]}, column {max_position[1]})")