###
# Program for testing built-in functions
#

# Largest number from the given list
max_number = max(7, 5, 6, 3, 8, 2)
print('Max number of 7, 5, 6, 3, 8, 2 is', max_number)

# Smallest number from the given list
min_number = min(4, 7, 2, 3, 9, 8)
print('Min number of 4, 7, 2, 3, 9, 8 is', min_number)

# Length of the phrase "computer science"
str_length = len("computer science")
print('The number of characters in "computer science" is', str_length)

# Letter read from the keyboard
letter = input('Enter a letter: ')
print('The letter entered is', letter)

# Number representing the string "20303"
number_from_string = int("20303")
print('The number representing the string "20303" is', number_from_string)

# Binary string representing decimal number 304
binary_string = bin(304)
print('The binary string representing decimal number 304 is', binary_string)

# Hexadecimal string representing decimal number 304
hex_string = hex(304)
print('The hexadecimal string representing decimal number 304 is', hex_string)

# Integer representing the Unicode code of the € sign
unicode_code = ord('€')
print('The integer representing the Unicode code of the € sign is', unicode_code)

# Absolute value of -17
absolute_value = abs(-17)
print('The absolute value of -17 is', absolute_value)
