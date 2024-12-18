import random

arr1 = [3, 7, 1, 0, 4]
arr2 = [[2, 3], [7, 1], [0, 4]]

arr3 = []
for _ in range(5):
    arr3.append(7)

arr4 = []
for i in range(1, 10):
    arr4.append(i)

arr5 = []
for i in range(1, 10):
    arr5.append(i * 2)

import random
arr6 = []
for _ in range(10):
    arr6.append(random.randint(1, 20))

arr7 = []
for _ in range(5):
    arr7.append([])

arr8 = []
for _ in range(4):
    row = []
    for _ in range(2):
        row.append(1)
    arr8.append(row)

arr9 = []
for _ in range(5):
    row = []
    for _ in range(3):
        row.append(random.randint(1, 20))
    arr9.append(row)

arr10 = [4, 0, 3]

arr11 = []
for _ in range(15):
    arr11.append(0)

arr12 = []
for i in range(1, 31):
    arr12.append(i)

arr13 = []
for _ in range(20):
    arr13.append(random.randint(0, 1))

arr14 = []
for _ in range(5):
    row = []
    for _ in range(2):
        row.append(False)
    arr14.append(row)

print(f"arr1: {arr1}")
print(f"arr2: {arr2}")
print(f"arr3: {arr3}")
print(f"arr4: {arr4}")
print(f"arr5: {arr5}")
print(f"arr6: {arr6}")
print(f"arr7: {arr7}")
print(f"arr8: {arr8}")
print(f"arr9: {arr9}")
print(f"arr10: {arr10}")
print(f"arr11: {arr11}")
print(f"arr12: {arr12}")
print(f"arr13: {arr13}")
print(f"arr14: {arr14}")
