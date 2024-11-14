# bank_account.py

class BankAccount:
    """A class representing a bank account with deposit, withdrawal, and balance display capabilities."""
    
    def __init__(self, initial_balance=0):
        """Initialize the account with an optional initial balance (defaults to 0)."""
        self.account_balance = initial_balance

    def deposit(self, amount):
        """Deposit the specified amount into the account."""
        if amount > 0:
            self.account_balance += amount
            return True
        return False

    def withdraw(self, amount):
        """Withdraw the specified amount from the account if sufficient funds are available."""
        if amount <= self.account_balance:
            self.account_balance -= amount
            return True
        return False

    def display_balance(self):
        """Display the current balance of the account."""
        print(f"Current balance: ${self.account_balance:.2f}")
