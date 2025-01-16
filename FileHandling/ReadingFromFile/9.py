# Filter employees by job title
def filter_employees_by_position(filename, position):
    with open(filename, 'r') as file:
        employees = file.readlines()
    for i, line in enumerate(employees, 1): #pętla iteruje przez ponumerowaną listę pracowników, zwracających tych z zgadzającym się argumentem position
        if position in line:
            print(f"{i}. {line.strip()}") 

filter_employees_by_position('FileHandling\\ReadingFromFile\\it_company.csv', 'Software Engineer')