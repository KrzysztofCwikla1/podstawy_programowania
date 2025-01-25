employees = [("Smith","Lucy"),("Jones","Janet"),("Lee","Jerry"),
             ("Jackson","Peter"),("Johnson","Rick"),
             ("Lewis","Terry"),("Clarke","Robin")]

# Transform the format to LASTNAME, Firstname
formatted_employees = list(map(lambda x: f"{x[0].upper()}, {x[1]}", employees))
print("\n".join(formatted_employees))
