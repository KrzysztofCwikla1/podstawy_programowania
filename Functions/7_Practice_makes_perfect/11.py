def f(n1,n2,n3):
    for num in [n1,n2,n3]:
        if num <=0:
            return False
    return True
if __name__ == "__main__":
    print(f(11, 6, -4))