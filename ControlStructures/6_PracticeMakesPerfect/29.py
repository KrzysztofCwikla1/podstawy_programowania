# Program to print the first N prime numbers

N = int(input("Enter the number of prime numbers to find: "))

count = 0
current_number = 2

while count < N:
    is_prime = True
    for i in range(2,current_number):
        if current_number % i == 0:
            is_prime = False        # checks if the current number is prime
            break
    if is_prime:
        print(current_number, end=" ")
        count += 1                  
    current_number += 1