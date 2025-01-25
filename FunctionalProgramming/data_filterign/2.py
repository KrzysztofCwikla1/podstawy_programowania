speeds = [48, 47, 54, 50, 42, 68, 39, 46]

# Filter speeds above 50 km/h
too_high = list(filter(lambda speed: speed > 50, speeds))

# Print result
print(f"Recorded values: {speeds}")
print(f"Speed too high: {too_high}")
