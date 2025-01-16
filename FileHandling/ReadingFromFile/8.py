# Prints text and counts words
def print_and_count_words(filename):
    with open(filename, 'r') as file:
        lines = file.readlines()
    word_count = 0
    for line in lines:
        word_count += len(line.split())
    print("".join(lines))
    print(f"Total words: {word_count}")

print_and_count_words('FileHandling\\ReadingFromFile\\pets.txt')