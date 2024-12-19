def compare(arr1, arr2):
    return bool([x for x in arr1 if x in arr2])

array1 = [1,2,3]
array2 = [0,1,2,3,4]

print(compare(array1, array2))