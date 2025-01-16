###
# Reads from file, line by line
#
with open('FileHandling\\ReadingFromFile\\countries.txt', 'rt') as file:
    for line in file:
        print(line, end="")