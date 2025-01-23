# class definition
class Student():
    def __init__(self):
        self.name = ""
        self.age = 0
        self.grade = ""  # Third attribute added for grade

def main():
    # object creation based on the class
    student1 = Student()
    student2 = Student()
    student3 = Student()  # Third student added

    # Assigning values to student attributes
    student1.name = "Dominic"
    student1.age = 19
    student1.grade = "A"

    student2.name = "Olivia"
    student2.age = 21
    student2.grade = "B+"

    student3.name = "Sophia"
    student3.age = 20
    student3.grade = "A-"

    # Printing student information
    print('LIST OF STUDENTS')
    print('================')
    print(f'{student1.name}, {student1.age} years old, Grade: {student1.grade}')
    print(f'{student2.name}, {student2.age} years old, Grade: {student2.grade}')
    print(f'{student3.name}, {student3.age} years old, Grade: {student3.grade}')

if __name__ == "__main__":
    main()
