###
# Checks whether at least one number entered
# from the keyboard is not negative
# 
x = int(input('Enter first number: '))
y = int(input('Enter second number: '))

if (x < 0 and y > 0) or (x > 0 and y < 0) or (x > 0 and y > 0):
    print(f'At least one of the numbers {x} and {y} is not negative')
else:
    print("Both numbers are negative")