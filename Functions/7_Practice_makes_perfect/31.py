def f(x, n):
    if n == 0:          #this function counts x to the n power
        return 1
    return x * f(x, n - 1)  #x^n = x * x^(n-1)

if __name__ == "__main__":
    print(f(5, 3))