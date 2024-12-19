def compare(array1, array2):
    if array1 == array2:
        return "Comparison: arrays are the same"
    else:
        return "Comparison: arrays are not the same"
    
Array1 = ["water","book","sky"]

Array2 = ["water","book","sky"]

print(f"Array1: "," ".join(Array1))
print(f"Array2: "," ".join(Array2))

print(compare(Array1, Array2))