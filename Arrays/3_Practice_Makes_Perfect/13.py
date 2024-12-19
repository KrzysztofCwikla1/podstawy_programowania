def occurs(number, array):
    for num in array:
        if num == number:
            return True
    return False

arr = [15, 38, 7, 23, 14]
number_to_check = int(input("Enter a number to check: "))
if occurs(number_to_check, arr)==True:
    print(f"Number {number_to_check} appears in the array {arr}" )
else: 
    print(f"Number {number_to_check} does not appear in the array {arr}")