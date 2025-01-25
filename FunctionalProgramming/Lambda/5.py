def avg_speed(distance, hours, minutes):
    total_time = hours + minutes / 60  # Convert minutes to hours
    return distance / total_time

# Take input from user
distance = float(input("Enter distance in km: "))
hours = int(input("Enter number of travel hours: "))
minutes = int(input("Enter number of travel minutes: "))

# Calculate average speed and print result
result = avg_speed(distance, hours, minutes)
print(f'Average speed: {result:.2f} km/h')
