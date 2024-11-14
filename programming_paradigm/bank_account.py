class BankAccount:
    def __init__(self, initial_balance=0):
#Initialize the bank account with an optional initial balance (default is 0)."""
        self.account_balance = initial_balance

    def deposit(self, amount):
#Deposit the given amount into the account."""
        if amount > 0:
            self.account_balance += amount
            print(f"Deposited {amount}. Current balance: {self.account_balance}")
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
    #Withdraw the given amount from the account if funds are sufficient."""
        if amount > 0 and amount <= self.account_balance:
            self.account_balance -= amount
            print(f"Withdrew {amount}. Current balance: {self.account_balance}")
            return True
        else:
            print("Insufficient funds or invalid amount.")
            return False

    def display_balance(self):
    #Displays the current balance.
        print(f"Current balance: {self.account_balance}")


