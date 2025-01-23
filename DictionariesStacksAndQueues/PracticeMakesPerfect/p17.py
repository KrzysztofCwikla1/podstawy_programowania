import json

# Open the JSON file in read mode
with open('/09-DictionariesStacksAndQueues/cities.json', 'r', encoding='utf-8') as file:
    # Load the data from the JSON file into a variable
    data = json.load(file)

# Print the information about cities
for city in data:
    for key, value in city.items():
        print(f"{key}: {value}")
    print()  # Print a blank line after each city's details
