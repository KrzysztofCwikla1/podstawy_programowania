def f(x, y):
    total = 0
    for num in range(x, y + 1):
        if num % 2 == 0 and num % 3 == 0 and num % 4 != 0: #checks if a number is divisible by 2 and 3, while not divisible by 4
            total += num                                   #adds a number meeting the condition to the total
    return total
if __name__ == "__main__":
    print(f(1, 20))  # Output: 24
    print(f(10, 30)) # Output: 48