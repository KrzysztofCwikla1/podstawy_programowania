# 3x3 Tic-Tac-Toe board
tic_tac_toe_board = [
   ['X', 'O', 'X'],
   [' ', 'X', 'O'],
   ['O', ' ', 'X']
]

# Loop through each row in the board
for row in tic_tac_toe_board:
   for cell in row:
      print(cell, end=" ")  # Print each cell in the row, separated by a space
   print()  # Move to the next line after printing a row
