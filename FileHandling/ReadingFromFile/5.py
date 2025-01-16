###
# Reads from file, line by line
#
i=0
with open('FileHandling\\ReadingFromFile\\countries.txt', 'rt') as file:
    for line in file:
        print(f"{i}. {line.strip()}")
        i+=1