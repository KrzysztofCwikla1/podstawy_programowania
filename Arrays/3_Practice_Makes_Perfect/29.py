
def create_2d_arr(x, y):

    return [[0 for _ in range(y)] for _ in range(x)]

array = create_2d_arr(3, 5)

for row in array:
    print(row)
