def f(x, y):
    count = 0
    for num in range(x, y + 1):
        if num % 2 == 0 and num < 0:
            count += 1
    return count

if __name__ == "__main__":
    print(f(-7, -2))  # Output: 3
    print(f(-16, 11))  # Output: 0