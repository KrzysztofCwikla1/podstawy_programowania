# Takes a number from the user and counts down to zero.
# The last five seconds of the counter are displayed in words.

import time

# Dictionary to map numbers to words for the last five seconds
number_words = {
    5: "five",
    4: "four",
    3: "three",
    2: "two",
    1: "one"
}

countdown = int(input("Enter the number of seconds to count down: "))

while countdown > 0:
    if countdown in number_words:  # Check if the number is in the dictionary
        print(number_words[countdown])
    else:
        print(countdown)  # Print the number normally if not in the dictionary
    countdown -= 1
    time.sleep(1)  # Wait for 1 second

print("Time's up!")
