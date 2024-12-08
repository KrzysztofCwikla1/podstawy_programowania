def f(detector):
    count = 0
    max_count = 0
    for i in detector:
        if i == "+":
            count += 1
        elif i == "-":
            count -=1
        
        max_count = max(count, max_count)

    return max_count >= 3 

print(f("+-+++-+---")) 
print(f("+-+-+-+-"))
print(f("+-++-+--"))
print(f("+-++-++-+---"))