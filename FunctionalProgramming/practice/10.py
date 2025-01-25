import matplotlib.pyplot as plt

temperatures = {"Krakow": 7, "Warszawa": -2, "Sopot": 4, "Koszalin": -1, "Opole": 3}

# Data for the chart
cities = list(temperatures.keys())
temps = list(temperatures.values())

# Creating the bar chart
plt.bar(cities, temps)
plt.title('Temperatures Recorded in Cities')
plt.xlabel('Cities')
plt.ylabel('Temperature (°C)')

# Display the chart
plt.show()
