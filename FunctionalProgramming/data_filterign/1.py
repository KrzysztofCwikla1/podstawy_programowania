employees = ["SMITH Lucy", "JONES Janet", "LEE Jerry", "JACKSON Peter", "JOHNSON Rick", "LEWIS Terry", "CLARKE Robin"]

# Filter employees with surname starting with 'J'
emp_J = list(filter(lambda e: e.split()[0][0] == 'J', employees))

# Print the result
for emp in emp_J:
    print(emp)
