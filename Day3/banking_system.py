# banking_system.py
import datetime

class BankAccount:
    def __init__(self, owner: str, balance: float = 0.0):
        self.owner: str = owner
        self.balance: float = balance
        self.transaction_history: list[str] = []

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


class SavingsAccount(BankAccount):
    def __init__(self, owner: str, balance: float = 0.0, interest_rate: float = 0.05):
        # Call the parent constructor
        super().__init__(owner, balance)
        self.interest_rate: float = interest_rate

    def apply_interest(self):
        interest = self.balance * self.interest_rate
        self.deposit(interest)
        self._log_transaction(f"Interest appiled (${interest})")
        print(f"Interest appiled: ${interest}")