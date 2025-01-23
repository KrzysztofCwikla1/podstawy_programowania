# Saves to a file a list of employees working at a specified position.

# File names
employees_file = 'it_company.csv'
position_file = 'software_engineer.txt'

# Position to filter
job_title = 'Software Engineer'

# Write selected employees to a file
with open(employees_file, 'r') as source_file:
    with open(position_file, 'w') as destination_file:
        for line in source_file:
            if job_title in line:
                destination_file.write(line)

print(f"Employees with the position '{job_title}' have been saved to '{position_file}'.")
