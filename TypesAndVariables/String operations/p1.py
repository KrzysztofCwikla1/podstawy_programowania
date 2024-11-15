###
# A program that calculates the number of characters
# of your name, surname and full name
#
name = 'Domink'   # replace Anna with your name
surname = 'Kawula' # replace May with your surname
characters_in_name = len(name)
characters_in_surname = len(surname)
fullname = len(name+" "+surname)
print(f'Your name has {characters_in_name} characters')
print(f'Your surname has {characters_in_surname} characters')
print(f'Your full name has {fullname} characters') # with a space between name and surname