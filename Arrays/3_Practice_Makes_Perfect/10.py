arr1 = [4, 36, 12, 28, 9, 44, 5]
arr2 = [5, 1, 36]

unique_values = []
for x in arr1:
    if x not in arr2:
        unique_values.append(x)

print(f"Numbers in arr1 but not in arr2:{unique_values}")