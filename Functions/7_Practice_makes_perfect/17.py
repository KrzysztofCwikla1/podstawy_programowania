def f(palindrome):
    return palindrome==palindrome[::-1] #[::-1] reverses a string
if __name__ == "__main__":
    print(f("radar"))
    print(f("12-11-21"))
    print(f("book"))