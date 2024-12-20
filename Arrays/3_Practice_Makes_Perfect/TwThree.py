
def count_words(text):
    words = text.split()  
    return len(words)

def words_longest_first(text):
    words = text.split()
    return sorted(words, key=lambda word: len(word), reverse=True)

def words_alphabetically(text):
    words = text.split()
    return sorted(words)
