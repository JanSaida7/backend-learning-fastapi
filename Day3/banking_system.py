# banking_system.py
import datetime

class BankAccount:
    def __init__(self, owner: str, balance: float = 0.0):
        self.owner = owner
        self.balance = balance
        self.transaction_history = []

    def _log_transaction(self, description: str):
        # Helper method to format time and add to history
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.transaction_history.append(f"{timestamp}: {description}")

    def deposit(self, amount: float):
        if amount <= 0:
            raise ValueError("Deposit amount must be positive")
        self.balance += amount
        self._log_transaction(f"Deposited ${amount}")

    def withdraw(self, amount: float):
        if amount > self.balance:
            raise ValueError("Insufficient funds")
        self.balance -= amount
        self._log_transaction(f"Withdrew ${amount}")

    def print_statement(self):
        print(f"--- Statement for {self.owner} ---")
        for transaction in self.transaction_history:
            print(transaction)
        print(f"Final Balance: ${self.balance}")