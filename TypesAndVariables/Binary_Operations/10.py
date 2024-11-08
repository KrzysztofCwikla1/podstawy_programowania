import random

# COMPUTER TURN
computer = random.randint(1, 6)

# YOUR TURN
user = int(input("Guess the dice number (1-6): "))
win = user == computer

print(f"Computer rolled: {computer}")
print(f"You won: {win}")