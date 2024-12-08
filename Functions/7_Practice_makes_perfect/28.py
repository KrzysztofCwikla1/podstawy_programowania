def f(dice):
    max_streak = 0
    current_streak = 1
    most_rolled = None

    for i in range(1, len(dice)):
        if dice[i] == dice[i - 1]:      #checks if the current dice roll is equal to the last, if it is increment the streak
            current_streak += 1
        else:
            if current_streak > max_streak:     #check if its the biggest streak after it ends
                max_streak = current_streak
                most_rolled = dice[i - 1]       #assigns the dice number to the most_rolled variable
            current_streak = 1

    # Final check after the loop
    if current_streak > max_streak:
        max_streak = current_streak
        most_rolled = dice[-1]

    return int(most_rolled)
if __name__ == "__main__":
    print(f("5233165554211"))  # Output: 5
    print(f("2133"))          # Output: 3