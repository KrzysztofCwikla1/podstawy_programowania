def f(number, even):
    total = 0 
    for digit in str(number):
        if (int(digit)%2 == 0) == even:
            total += int(digit)
    return total

print(f(3124,True)) 
print(f(3124,False))
print(f(20576,False))
print(f(20576,True))
print(f(13115,True))

#output
'''
6
4
12
8
0

'''