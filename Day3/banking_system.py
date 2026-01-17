class BankAccount:
    def __init__(self, owner: str, balance: float = 0.0):
        self.owner = owner
        self.balance = balance
    
    def deposit(self, amount: float):
            self.balance += amount
            print(f"Deposited ${amount}. New Balance: ${self.balance}")
    
    def withdraw(self, amount: float):
         self.balance -= amount
         print(f"WithDrew ${amount}. New Balance: ${self.balance}")