def analyze_file():
    # Prompt user for the file name
    file_name = input("Enter the name of the file (e.g., books.txt): ")

    try:
        with open(file_name, 'r', encoding='utf-8') as file:
            # Read the content of the file
            lines = file.readlines()

            # Calculate metrics
            line_count = len(lines)
            word_count = sum(len(line.split()) for line in lines)
            char_count = sum(len(line) for line in lines)

            # Print results
            print(f"\nFile name: {file_name}")
            print(f"Number of lines: {line_count}")
            print(f"Number of words: {word_count}")
            print(f"Number of characters: {char_count}")

    except FileNotFoundError:
        print(f"Error: The file '{file_name}' does not exist. Please check the file name and try again.")

# Run the function
if __name__ == "__main__":
    analyze_file()
