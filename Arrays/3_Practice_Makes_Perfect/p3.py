def power(n):
    return [i**2 for i in n if i in n]

array = [8,2,5,1,9]
print(power(array))