numbers = list(range(1, 21))
divisible_by_2_and_3 = list(filter(lambda x: x % 2 == 0 and x % 3 == 0, numbers))
print(divisible_by_2_and_3)
