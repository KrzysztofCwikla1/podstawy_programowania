def f(number, x, y):
    return x <= number <= y

def main():
    number = 7
    x, y = 2, 15
    print(f"Number {number} in the range <{x},{y}>: {'yes' if f(number, x, y) else 'no'}")
if __name__ == "__main__":
    main()