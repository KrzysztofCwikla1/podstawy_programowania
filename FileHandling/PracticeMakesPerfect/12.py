import csv

# Function to write books to the corresponding genre file
def write_to_file(genre, book_data):
    # Mapping genres to filenames
    genre_to_file = {
        'Fiction': 'books_fiction.txt',
        'Dystopian': 'books_dystopian.txt',
        'Classic': 'books_classic.txt',
        'Romance': 'books_romance.txt',
        'Adventure': 'books_adventure.txt',
        'Historical': 'books_historical.txt',
        'Modernist': 'books_modernist.txt',
        'Epic': 'books_epic.txt',
        'Gothic': 'books_gothic.txt',
        'Psychological': 'books_psychological.txt',
        'Fantasy': 'books_fantasy.txt',
        'Philosophical': 'books_philosophical.txt',
        'Southern Gothic': 'books_southern_gothic.txt',
        'Literary': 'books_literary.txt',
        'Magic Realism': 'books_magic_realism.txt',
        'Gothic Horror': 'books_gothic_horror.txt',
        'Novella': 'books_novella.txt',
        'Satire': 'books_satire.txt',
        'Science Fiction': 'books_science_fiction.txt',
        'Post-apocalyptic': 'books_post_apocalyptic.txt',
        'Horror': 'books_horror.txt'
    }
    
    # Get the corresponding file for the genre
    if genre in genre_to_file:
        filename = genre_to_file[genre]
        with open(filename, 'a', encoding='utf-8') as file:
            file.write(f"{book_data}\n")

# Function to process the CSV file and categorize books by genre
def process_books_file(csv_filename):
    with open(csv_filename, newline='', encoding='utf-8') as csvfile:
        # Create a CSV reader to read the CSV file
        reader = csv.reader(csvfile)
        
        # Skip the header row
        next(reader)
        
        # Process each row in the CSV file
        for row in reader:
            # Assuming the CSV columns are: Title, Author, Genre, Year
            title, author, genre, year = row
            book_data = f"{title} by {author} ({year})"
            
            # Call function to write the book to the appropriate file based on the genre
            write_to_file(genre, book_data)

# Main function to execute the program
def main():
    # Path to the CSV file
    csv_filename = 'books.csv'
    
    # Process the CSV file and categorize books
    process_books_file(csv_filename)
    print("Books have been categorized and saved in the corresponding files.")

if __name__ == "__main__":
    main()
