
def print_unique_elements(arr):
    unique_elements = []
    index = 0

    while index < len(arr):
        if arr.count(arr[index]) == 1:  
            unique_elements.append(arr[index])
        index += 1

    
    print("Unique elements:", unique_elements)


arr = [2,3,2,5,8,1,9,8]

print_unique_elements(arr)
