import os

class BankAccount:
    def __init__(self, initial_balance=0, file_path="balance.txt"):
        """Initialize the account balance from file or set to initial balance."""
        self.file_path = file_path
        if os.path.exists(self.file_path):
            with open(self.file_path, "r") as f:
                self.__account_balance = float(f.read().strip() or 0)
        else:
            self.__account_balance = initial_balance
            self._save_balance()

    def _save_balance(self):
        """Save the current balance to the file."""
        with open(self.file_path, "w") as f:
            f.write(str(self.__account_balance))

    def deposit(self, amount):
        """Deposit a positive amount."""
        if amount > 0:
            self.__account_balance += amount
            self._save_balance()
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        """Withdraw if sufficient funds exist."""
        if amount <= 0:
            print("Withdrawal amount must be positive.")
            return False
        if self.__account_balance >= amount:
            self.__account_balance -= amount
            self._save_balance()
            return True
        return False

    def display_balance(self):
        """Show the current account balance."""
        print(f"Current Balance: ${self.__account_balance:.2f}")
