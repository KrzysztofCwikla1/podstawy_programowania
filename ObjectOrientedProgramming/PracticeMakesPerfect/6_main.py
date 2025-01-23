class BankAccount:
    def __init__(self, account_number):
        self.account_number = account_number
        self.balance = 0.0

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient funds on the account")
        else:
            self.balance -= amount

    def show_details(self):
        print(f"Bank Account No: {self.account_number}")
        print(f"Balance: PLN {self.balance:.2f}")
        
def main():
    account = BankAccount("12 3456 5555 9090 1111 0000 7722")

    print("Account details:")
    account.show_details()

    print("\nDeposit PLN 25.30:")
    account.deposit(25.30)
    account.show_details()

    print("\nWithdraw PLN 31.70:")
    account.withdraw(31.70)
    account.show_details()

    print("\nWithdraw PLN 14:")
    account.withdraw(14.00)
    account.show_details()

if __name__ == "__main__":
    main()
