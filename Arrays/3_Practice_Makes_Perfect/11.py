def bubblesort(array):
    n = len(array)
    for i in range(n):
        for j in range(0, n - i - 1):
            if array[j] > array[j + 1]:  
                array[j], array[j + 1] = array[j + 1], array[j]
    return array

arrays = [
    [4, 36, 12, 28, 9, 44, 5],
    [5, 1, 36],
    [7, 3, 11, 19, 5]
]

for i, arr in enumerate(arrays):
    sorted_array = bubblesort(arr[:]) 
    print(f"Original array {i + 1}: {arr}")
    print(f"Sorted array {i + 1}: {sorted_array}\n")
