temperatures = {"Krakow": 7, "Warszawa": -2, "Sopot": 4, "Koszalin": -1, "Opole": 3}

# Use filter to select cities with positive temperatures
positive_temp_cities = list(filter(lambda city: temperatures[city] > 0, temperatures))
print("Cities with positive temperatures:", " ".join(positive_temp_cities))
