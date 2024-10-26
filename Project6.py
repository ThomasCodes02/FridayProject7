class BankAccount:
    def __init__(self, account_number, balance=0):
        # Initialize the bank account with an account number and an initial balance
        self.account_number = account_number
        self.balance = balance

    def deposit(self, amount):
        # Deposit the specified amount if it is positive
        if amount > 0:
            self.balance += amount
            print(f"${amount} deposited successfully.")
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        # Withdraw the specified amount if it is positive and within the balance
        if amount > 0:
            if amount <= self.balance:
                self.balance -= amount
                print(f"${amount} withdrawn successfully.")
            else:
                print("Insufficient balance.")
        else:
            print("Withdrawal amount must be positive.")

    def check_balance(self):
        # Display the current balance
        print(f"Current balance: ${self.balance}")

# Create one account with a specific account number and a default balance of 0
account = BankAccount(account_number="0")

# Prompt the user to enter their account number once for verification
entered_account = input("Enter your account number: ")
if entered_account == account.account_number:
    print("Account verified successfully.\n")

    # Indefinite loop to provide account options until the user decides to exit
    while True:
        # Display available options
        print("\nOptions:\n1. Deposit\n2. Withdraw\n3. Check Balance\n4. Exit")
        option = input("Choose an option (1, 2, 3, or 4): ")

        if option == "1":
            # Deposit money if user selects option 1
            try:
                amount = float(input("Enter amount to deposit: "))
                account.deposit(amount)
            except ValueError:
                print("Invalid amount entered. Please enter a valid number.")

        elif option == "2":
            # Withdraw money if user selects option 2
            try:
                amount = float(input("Enter amount to withdraw: "))
                account.withdraw(amount)
            except ValueError:
                print("Invalid amount entered. Please enter a valid number.")

        elif option == "3":
            # Check balance if user selects option 3
            account.check_balance()

        elif option == "4":
            # Exit the loop if user selects option 4
            print("Exiting. Thank you for banking with us.")
            break

        else:
            # Handle invalid option selection
            print("Invalid option selected. Please choose a valid option.")
        
        print()  # Add space between transactions for better readability
else:
    # Display error message if account number is incorrect
    print("Incorrect account number. Access denied.")


