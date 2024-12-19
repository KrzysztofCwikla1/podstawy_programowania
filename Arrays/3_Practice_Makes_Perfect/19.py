def count_greater_than(array, value):
    count = 0
    for x in array:
        if x > value:
            count += 1
    return count

array_real = [1.5, 3.7, 2.8, 9.2, 4.3]
value_to_check = float(input("Enter a value to check: "))
print(f"Count of numbers greater than {value_to_check}: {count_greater_than(array_real, value_to_check)}")