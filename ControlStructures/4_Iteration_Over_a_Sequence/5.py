# Encrypts text using Caesar Code, shifting each letter in the alphabet right one position
plain_text = 'The early bird catches the worm'
encrypted_text = ''

for char in plain_text:
    if char.isalpha():
        if char == 'z':
            new_char = 'a'
        elif char == 'Z': 
            new_char = 'A'
        else:
            new_char = chr(ord(char) + 1)
    else:
        new_char = char
    encrypted_text += new_char
print(plain_text)
print(encrypted_text)