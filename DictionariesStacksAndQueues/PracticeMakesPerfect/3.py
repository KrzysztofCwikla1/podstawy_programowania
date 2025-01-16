translations = {
    'computer': 'komputer',
    'mouse': 'myszka',
    'keyboard': 'klawiatura',
    'printer': 'drukarka'
}

word = input("Enter a word in English: ").lower()
if word in translations:
    print(f"The Polish translation of '{word}' is '{translations[word]}'.")
else:
    print(f"Sorry, the translation for '{word}' is unavailable.")
