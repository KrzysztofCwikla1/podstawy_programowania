def f(binary_number):
    for char in binary_number:
        if char not in "01":
            return False
    return True
if __name__ == "__main__":
    print(f("101101"))

    print(f("1311a10100"))