array_2d = []  


for i in range(1, 6):
    row = []  
    for j in range(1, 6):  
        row.append(i * j)  
    array_2d.append(row)  


for row in array_2d: 
    for value in row:  
        print(value, end=" ")  
    print() 