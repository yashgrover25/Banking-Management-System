class BankAccount:
    def __init__(self):
        self.balance = 0.0

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"₹{amount} deposited successfully.")
        else:
            print("Invalid deposit amount.")

    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            print(f"₹{amount} withdrawn successfully.")
        else:
            print("Insufficient balance or invalid amount.")

    def display_balance(self):
        print(f"Current Balance: ₹{self.balance}")


class BankingSystem:
    def __init__(self):
        self.account = BankAccount()

    def menu(self):
        while True:
            print("\n--- Banking Menu ---")
            print("1. Deposit")
            print("2. Withdraw")
            print("3. Display Balance")
            print("4. Exit")

            choice = input("Enter your choice (1-4): ")

            if choice == '1':
                amount = float(input("Enter amount to deposit: ₹"))
                self.account.deposit(amount)

            elif choice == '2':
                amount = float(input("Enter amount to withdraw: ₹"))
                self.account.withdraw(amount)

            elif choice == '3':
                self.account.display_balance()

            elif choice == '4':
                print("Thank you for using the banking system. Goodbye!")
                break

            else:
                print("Invalid choice. Please select between 1 and 4.")

banking = BankingSystem()
banking.menu()
