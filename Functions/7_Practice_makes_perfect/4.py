def f(text, letter):
    return text.count(letter) #count returns the number of given elements in a string
if __name__ == "__main__":
    text = "You never get a second chance to make a first impression"
    letter = 'e'
    print(f"The number of letter '{letter}': {f(text, letter)}")
