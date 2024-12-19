def second_largest(arr):
    if len(arr) < 2:
        raise ValueError("Array must contain at least two elements.")
    
    largest = second = arr[0]
    for num in arr:
        if num > largest:
            second = largest
            largest = num
        elif num > second and num != largest:
            second = num
    return second

def difference_between_extremes(arr):
    min_val = max_val = arr[0]
    for num in arr:
        if num < min_val:
            min_val = num
        if num > max_val:
            max_val = num
    return max_val - min_val

def median(arr):
    # Implement sorting manually
    sorted_arr = arr[:]  # Make a copy of the array
    for i in range(len(sorted_arr)):
        for j in range(0, len(sorted_arr) - i - 1):
            if sorted_arr[j] > sorted_arr[j + 1]:
                sorted_arr[j], sorted_arr[j + 1] = sorted_arr[j + 1], sorted_arr[j]
    n = len(sorted_arr)
    if n % 2 == 1:
        return sorted_arr[n // 2]
    else:
        return (sorted_arr[n // 2 - 1] + sorted_arr[n // 2]) / 2

def smallest_and_largest(arr):
    min_val = max_val = arr[0]
    for num in arr:
        if num < min_val:
            min_val = num
        if num > max_val:
            max_val = num
    return [min_val, max_val]

def to_string(arr):
    result = ""
    for i, num in enumerate(arr):
        result += str(num)
        if i < len(arr) - 1:
            result += "-"
    return result

# Testowe dane
numbers = [7, 3, 8, 5, 2]

# Wyświetlanie wyników
print(f"Numbers: {','.join(map(str, numbers))}")
print(f"Second largest number: {second_largest(numbers)}")
print(f"Median: {median(numbers)}")
smallest_largest = smallest_and_largest(numbers)
print(f"Smallest and largest number: {smallest_largest[0]},{smallest_largest[1]}")
print(f"Numbers as a string: {to_string(numbers)}")
