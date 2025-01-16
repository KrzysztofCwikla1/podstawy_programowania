basic_data = {
    "name": "Barbara",
    "age": 21
}

advanced_data = {
    "status": "student",
    "married": False,
    "interest": ["reading", "swimming"]
}

# Combine the dictionaries
person = {**basic_data, **advanced_data}

for key, value in person.items():
    print(f"{key} : {value}")