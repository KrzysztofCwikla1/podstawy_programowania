cs = ''

gamer = ''

infl = ''

compsci = input("SURVEY Are you interested in computer scienie? (y/n): ")
if compsci == 'y':
    cs += 'Yes'
elif compsci == 'n':
    cs += 'No'
games = input("Do you like playing computer games? (y/n): ")
if games == 'y':
    gamer += 'Yes'
elif games =='n':
    gamer += 'No'

ig = input("Do you have an instagram account? (y/n): ")
if ig == 'y':
    infl += 'Yes'
elif ig =='n':
    infl += 'No'

print("")

print(f"SURVEY RESULTS Interested in computer science: {cs}")
print(f"Playing computer games: {gamer}")
print(f"Has an instagram account: {infl}")