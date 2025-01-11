# bank_account.py

class BankAccount:
    def __init__(self, initial_balance=0):
        """Initialize the account with an initial balance."""
        self.account_balance = initial_balance

    def deposit(self, amount):
        """Deposit the specified amount into the account."""
        if amount > 0:
            self.account_balance += amount
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        """Withdraw the specified amount from the account if sufficient funds exist."""
        if amount > 0 and self.account_balance >= amount:
            self.account_balance -= amount
            return True
        elif amount > 0:
            print("Insufficient funds.")
            return False
        else:
            print("Withdrawal amount must be positive.")
            return False

    def display_balance(self):
        """Display the current balance in a user-friendly format."""
        # Corrected output message
        print(f"Current balance: ${self.account_balance:.2f}")
