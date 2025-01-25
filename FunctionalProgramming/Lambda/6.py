# Take input from user
distance = float(input("Enter distance in km: "))
hours = int(input("Enter number of travel hours: "))
minutes = int(input("Enter number of travel minutes: "))

# Define anonymous function (lambda) to calculate average speed
avg_speed = lambda distance, hours, minutes: distance / (hours + minutes / 60)

# Calculate average speed and print result
result = avg_speed(distance, hours, minutes)
print(f'Average speed: {result:.2f} km/h')
