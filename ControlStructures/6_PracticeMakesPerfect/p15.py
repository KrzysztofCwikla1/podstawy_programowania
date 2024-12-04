enter = input("Enter EAN-13 article number: ")

if len(enter) == 13:
    print("Article number is correct")
    if enter[0:3] == '590':
        print("Article manufactured in Poland")
    else:
        print("Article manufactured in other country")
else:
    print("Article number is not correct")
    
