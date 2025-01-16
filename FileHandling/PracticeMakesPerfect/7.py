import re

# Count vowels in user input
def count_vowels():
    text = input("Enter text: ")
    vowels = re.findall(r'[aeiouAEIOU]', text) #zwraca wszystkie samogloski w tekscie
    print(f"Number of vowels: {len(vowels)}")

count_vowels()