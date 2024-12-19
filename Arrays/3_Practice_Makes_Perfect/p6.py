def arithmetic_mean(n):
    i = 0
    summer = 0

    while i < len(n):
        summer += n[i]
        i += 1

    mean = summer / len(n)
    return mean


array = [15,8,31,47,2,19]
print(arithmetic_mean(array))