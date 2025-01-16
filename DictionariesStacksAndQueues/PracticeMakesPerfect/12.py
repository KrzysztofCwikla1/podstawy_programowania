def reverse_string(text):
    stack = list(text)
    reversed_text = ""
    while stack:
        reversed_text += stack.pop() #funkcja odwraca string wypychając elementy stosu, (last in first out)
    return reversed_text

text = input("Enter text to reverse: ")
print(f"Reversed text: {reverse_string(text)}")