person = {
    "name": "Marek",
    "surname": "Banach",
    "age": 25,
    "hobby": ["swimming", "excursions"],
    "married": True,
    "phone": {"landline": "123444321", "mobile": "777888999"}
}

# Display specific values
print(f"Name: {person['name']}")
print(f"Hobbies: {person['hobby']}")
print('\n')
for key, value in person.items():
    print(f"{key} : {value}")
print('\n')
person["surname"] = "Nowak"
person["married"] = not person["married"]
person["gender"] = "male"
person["hobby"].append("bicycle")
person["phone"]["work"] = "313131444"
print('\n')
# Display updated dictionary
for key, value in person.items():
    print(f"{key} : {value}")