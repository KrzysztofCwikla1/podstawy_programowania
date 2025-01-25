grades = [3.0, 5.0, 2.0, 3.5, 4.0, 4.0, 3.5, 2.0, 4.0, 2.0]

# Filter grades above 2.0 and calculate mean
valid_grades = list(filter(lambda grade: grade > 2.0, grades))
mean_grade = sum(valid_grades) / len(valid_grades)

print(f"Arithmetic mean for grades <> 2.0 is {mean_grade}")
