# Program to convert 24-hour time to 12-hour time

time_24 = input("Enter time (24-hour format, hh:mm): ")
hours, minutes = map(int, time_24.split(":"))           #changes time_24 to 2 different variables, hours and time

if hours == 0:
    period = "am"
    hours_12 = 12
elif hours == 12:
    period = "pm"
    hours_12 = 12
elif hours > 12:
    period = "pm"
    hours_12 = hours - 12
else:
    period = "am"
    hours_12 = hours

print(f"Time in 12-hour format: {hours_12}:{minutes:02}{period}")