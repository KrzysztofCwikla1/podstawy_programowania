# Define function to convert speed from meters per second to kilometers per hour
def ms_to_kmh(ms):
    return ms * 3.6

# Take input from user
ms = float(input("Enter speed in meters per second: "))

# Calculate speed in km/h and print result
result = ms_to_kmh(ms)
print(f'{ms} m/s = {result} km/h')
