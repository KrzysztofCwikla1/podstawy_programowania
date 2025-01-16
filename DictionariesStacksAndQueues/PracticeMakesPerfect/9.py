import csv

# Step 1: Read the provinces data from the CSV file
province_dict = {}

with open('DictionariesStacksAndQueues\\PracticeMakesPerfect\\province.csv', 'r', encoding='utf-8') as file:
    reader = csv.reader(file)
    next(reader)  # Skip the header row
    for row in reader:
        letter = row[0]  # First letter
        province_name = row[1]  # Province name
        province_dict[letter] = province_name

# Step 2: Initialize a dictionary to store the vehicle counts for each province
vehicle_counts = {province: 0 for province in province_dict.values()}

# Step 3: Read the vehicle registration numbers from the text file
with open('DictionariesStacksAndQueues\\PracticeMakesPerfect\\vehicle.txt', 'r', encoding='utf-8') as file:
    vehicles = file.readlines()

# Step 4: Count vehicles per province based on the first letter of the registration number
for vehicle in vehicles:
    vehicle = vehicle.strip()  # Remove any extra whitespace or newline
    first_letter = vehicle[0]  # Get the first letter of the registration number
    if first_letter in province_dict:
        province_name = province_dict[first_letter]
        vehicle_counts[province_name] += 1

# Step 5: Print the results
print("Number of vehicles registered in each province:")
print("="*50)

for province, count in vehicle_counts.items():
    print(f"{province}: {count} vehicles")
