class C:
    def __init__(self, name, surname, age, seniority):
        self.name = name
        self.surname = surname
        self.age = age
        self.seniority = seniority

    def __str__(self):
        name_rep = f"{self.surname.upper()}{self.name[0].upper()}{self.seniority}" if self.age >= 18 else f"{self.surname.lower()}{self.name[0].lower()}{self.seniority}"
        return name_rep
def main():
    emp1 = C("Anna", "May", 17, 7)
    emp2 = C("George", "Brown", 21, 4)

    print(emp1)  # Output: maya7
    print(emp2)  # Output: BROWNG4

if __name__ == "__main__":
    main()