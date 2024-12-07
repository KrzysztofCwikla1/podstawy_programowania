def f(n):
    count = 0
    current_number = 2

    while count < n:
        is_prime = True
        for i in range(2, current_number):
            if current_number % i == 0:
                is_prime = False
                break
        if is_prime:
            count += 1
        current_number += 1
    
    return current_number-1

if __name__ == "__main__":
    print(f(1))
    print(f(5))
    print(f(10))