import random

dice_roll_1 = random.randint(1, 6)
dice_roll_2 = random.randint(1, 6)
dice_roll_3 = random.randint(1, 6)
total = dice_roll_1 + dice_roll_2 + dice_roll_3

print(f"Dice rolls: {dice_roll_1}, {dice_roll_2}, {dice_roll_3}")
print(f"Sum of dice rolls: {total}")