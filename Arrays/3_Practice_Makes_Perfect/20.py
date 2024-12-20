
arr = [7, 9, 2, 4, 5, 6]

even_numbers = [num for num in arr if num % 2 == 0]
odd_numbers = [num for num in arr if num % 2 != 0]

arr = even_numbers + odd_numbers

print("arr =", arr)
