import random
def rand_elem(array):
    return random.choice(array)

array_elements = [10, 20, 30, 40, 50]
for i in range(5):
    print(f"Randomly selected element: {rand_elem(array_elements)}")