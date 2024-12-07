# ATM (cash machine) simulator with PIN functionality

balance = 1000  # Initial balance
pin = '1111'  # Initial 4-digit PIN code

# Function to check the current PIN
def check_pin():
    entered_pin = input("Enter your 4-digit PIN: ")
    if entered_pin == pin:
        print("PIN is correct.")
        return True
    else:
        print("Incorrect PIN. Access denied.")
        return False

# Function to change the PIN
def change_pin():
    global pin  # Modify the global pin variable
    current_pin = input("Enter your current 4-digit PIN: ")
    if current_pin == pin:
        new_pin = input("Enter your new 4-digit PIN: ")
        if len(new_pin) == 4 and new_pin.isdigit():
            pin = new_pin
            print("PIN has been successfully changed.")
        else:
            print("Invalid PIN. It must be exactly 4 digits.")
    else:
        print("Incorrect current PIN. PIN change failed.")

# Main program loop
while True:
    print()
    print("ATM Menu:")
    print("1. Check balance")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Check PIN")
    print("5. Change PIN")
    print("6. Exit")

    choice = input("Choose an option (1-6): ")
    print()

    if choice == '1':
        if check_pin():
            print(f"Your current balance is: €{balance}")
    elif choice == '2':
        if check_pin():
            try:
                amount = float(input("Enter the amount to deposit: "))
                if amount > 0:
                    balance += amount
                    print(f"€{amount} has been deposited. New balance: €{balance}")
                else:
                    print("Deposit amount must be greater than zero.")
            except ValueError:
                print("Invalid input. Please enter a valid amount.")
    elif choice == '3':
        if check_pin():
            try:
                amount = float(input("Enter the amount to withdraw: "))
                if amount > 0:
                    if amount <= balance:
                        balance -= amount
                        print(f"€{amount} has been withdrawn. New balance: €{balance}")
                    else:
                        print("Insufficient balance.")
                else:
                    print("Withdrawal amount must be greater than zero.")
            except ValueError:
                print("Invalid input. Please enter a valid amount.")
    elif choice == '4':
        check_pin()
    elif choice == '5':
        change_pin()
    elif choice == '6':
        print("Exiting... Thank you for using the ATM!")
        break  # Exit the loop
    else:
        print("Invalid option. Please try again.")
