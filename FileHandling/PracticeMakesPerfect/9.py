# Define the path to the file
file_path = 'it_company.txt'

# Open the file and process the data
try:
    with open(file_path, 'r') as file:
        # Skip the header row
        header = file.readline()

        # Print the title for the output
        print("GRAPHIC DESIGNERS")
        print("=================")

        # Iterate through each line in the file
        for line in file:
            # Split the line into columns based on the tab separator
            columns = line.strip().split('\t')

            # Extract relevant information
            last_name, first_name, job_title, email = columns

            # Check if the job title is "Graphic Designer"
            if job_title == "Graphic Designer":
                # Print the first name, last name, and email
                print(f"{first_name} {last_name},{email}")

except FileNotFoundError:
    print(f"Error: The file '{file_path}' does not exist.")
