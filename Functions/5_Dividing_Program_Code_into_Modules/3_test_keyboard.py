# employee_data.py
import keyboard  # Importing the keyboard module

# Reads employee's data from keyboard
first_name = keyboard.input_string('Enter first name: ')
last_name = keyboard.input_string('Enter last name: ')
age = keyboard.input_integer('Enter age: ')
salary = keyboard.input_real('Enter salary: ')
is_salary_hidden = keyboard.input_boolean('Hide salary? (y/n): ')

# Prints employee's record
print('DATA RECORD')
print('===========')
print('Name:', first_name, last_name)
print('Age:', age)

# Conditional to print salary based on user's choice
if not is_salary_hidden:
    print('Salary:', salary)
