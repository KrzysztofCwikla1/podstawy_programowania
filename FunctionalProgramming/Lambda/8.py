# Define anonymous function to return initials
initials = lambda name, surname: name[0] + surname[0]

# Test the function
name = input("Enter first name: ")
surname = input("Enter surname: ")

print(f"Initials: {initials(name, surname)}")
