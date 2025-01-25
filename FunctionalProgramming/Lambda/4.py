# Take input from user
ms = float(input("Enter speed in meters per second: "))

# Define anonymous function (lambda) to convert
ms_to_kmh = lambda ms: ms * 3.6

# Calculate speed in km/h and print result
result = ms_to_kmh(ms)
print(f'{ms} m/s = {result} km/h')
