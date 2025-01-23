# Makes a copy of a text file

# File names
original_file = 'healthy_lifestyle.txt'
target_file = 'copy_healthy_lifestyle.txt'

# Read the content of the original file
with open(original_file, 'r') as source_file:
    content = source_file.read()

# Write the content to the target file (copy)
with open(target_file, 'w') as destination_file:
    destination_file.write(content)

print(f"Contents of '{original_file}' have been copied to '{target_file}'.")
