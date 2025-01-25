# Given data
bottle_capacity = 500  # in ml
tolerance = 2 / 100  # 2% tolerance
filled_bottles = [508, 500, 512, 499, 492, 511, 503, 476, 501, 509]

# Define a function to check whether the bottle is filled incorrectly
def is_incorrectly_filled(volume):
    min_allowed = bottle_capacity - (bottle_capacity * tolerance)
    max_allowed = bottle_capacity + (bottle_capacity * tolerance)
    return not (min_allowed <= volume <= max_allowed)

# Use filter() to find the incorrectly filled bottles
incorrect_bottles = list(filter(is_incorrectly_filled, filled_bottles))

# Calculate the percentage of incorrectly filled bottles
incorrect_percentage = (len(incorrect_bottles) / len(filled_bottles)) * 100

# Display the result
print(f"Bottle capacity:    {bottle_capacity}ml")
print(f"Filling tolerance:  {tolerance * 100}%")
print(f"Filled bottles:     {', '.join(map(str, filled_bottles))}")
print(f"Incorrectly filled: {incorrect_percentage:.0f}%")
