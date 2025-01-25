test_results = [
    {"name": "Peter", "result": 27},
    {"name": "Anna", "result": 63},
    {"name": "Robert", "result": 92},
    {"name": "Paul", "result": 46},
    {"name": "Barbara", "result": 52}
]

# Filter students whose result is between 50 and 70 points
filtered_students = filter(lambda x: 50 <= x["result"] <= 70, test_results)
for student in filtered_students:
    print(f"{student['name']} - {student['result']} points")
