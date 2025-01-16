import json

# Load the dog data from the file
with open('DictionariesStacksAndQueues\\PracticeMakesPerfect\\dogs.json', 'r', encoding='utf-8') as file:
    dogs_data = json.load(file)

# Print information about dogs younger than 5 years
print("Dogs younger than 5 years:")
for dog in dogs_data:
    if dog['age'] < 5:
        print(f"Name: {dog['name']}")
        print(f"Breed: {dog['breed']}")
        print(f"Age: {dog['age']} years")
        print(f"Weight: {dog['weight_kg']} kg")
        print(f"Owner: {dog['owner']}")
        print(f"Vaccinated: {'Yes' if dog['vaccinated'] else 'No'}")
        print("-" * 30)
